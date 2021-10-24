"""Latin scansion app."""

import functools

import flask
import wtforms  # type: ignore
import yaml

import latin_scansion
import pynini


CONFIG = "config.yaml"


## Startup.


# Creates app object.
app = flask.Flask(__name__)


# Loads configs.
with open(CONFIG, "r") as source:
    app.config.update(yaml.safe_load(source))


## Forms.


class ScansionForm(wtforms.Form):

    string = wtforms.StringField(
        "string", [wtforms.validators.Length(min=1, max=32768)]
    )
    show_text = wtforms.BooleanField("show_text")
    show_norm = wtforms.BooleanField("show_norm")
    show_raw_pron = wtforms.BooleanField("show_raw_pron")
    show_var_pron = wtforms.BooleanField("show_var_pron")
    show_feet = wtforms.BooleanField("show_feet")
    show_syllables = wtforms.BooleanField("show_syllables")


## Curries functions.


with pynini.Far(app.config["far_path"], "r") as far:
    scan_document = functools.partial(
        latin_scansion.scan_document,
        far["NORMALIZE"],
        far["PRONOUNCE"],
        far["VARIABLE"],
        far["SYLLABLE"],
        far["WEIGHT"],
        far["HEXAMETER"],
    )


## Routes.


@app.route("/")
def index() -> str:
    form = ScansionForm()
    return flask.render_template("index.html")


@app.route("/result.html", methods=["POST"])
def result() -> str:
    form = ScansionForm(flask.request.form)
    if form.validate():
        lines = form.string.data.splitlines()
        return flask.render_template(
            "result.html",
            document=scan_document(lines, "<webapp input>"),
            show_text=bool(form.show_text.data),
            show_norm=bool(form.show_norm.data),
            show_raw_pron=bool(form.show_raw_pron.data),
            show_var_pron=bool(form.show_var_pron.data),
            show_feet=bool(form.show_feet.data),
            show_syllables=bool(form.show_syllables.data),
        )
    return "<p>Form validation failed.</p>"


if __name__ == "__main__":
    app.run()

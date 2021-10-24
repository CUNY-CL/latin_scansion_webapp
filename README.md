# 🏛️ Latin scansion webapp 🏛️

This is a webapp wrapper for the [Latin scansion engine](https://github.com/CUNY-CL/latin_scansion).

## License

The engine is released under an Apache 2.0 license. Please see
[LICENSE.txt](LICENSE.txt) for details.

## Installation 

Install requirements:

    pip install -r requirements.txt

Then, copy the grammar FAR `all.far` into the working directory.

## Launch for prod

    gunicorn --workers 1 --log-file - app:app

## Authors

-   [Jillian Chang](jillianchang15@gmail.com)
-   [Kyle Gorman](kgorman@gc.cuny.edu)

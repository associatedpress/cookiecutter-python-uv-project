# AP Python UV Cookiecutter

This is a project template powered by [Cookiecutter](https://github.com/cookiecutter/cookiecutter) for use with [datakit-project](https://github.com/associatedpress/datakit-project/).

## Structure

```
.
├── .gitignore
├── README.md
├── analysis
│   └── archive
├── data
│   ├── documentation
│   ├── handmade
│   ├── html_reports
│   ├── processed
│   ├── public
│   └── source
├── etl
├── publish
├── scratch
├── viz
```

- `.gitignore`
  - Ignores a few typical temporary/unnecessary files common to most data projects.
- `README.md`
  - Project-specific readme with boilerplate for data projects.
  - Includes sourcing details and places to explain how to replicate/remake the project.
- `analysis`
  - Code that involves analysis on already-cleaned data. Code for cleaning data should go in `etl`.
  - Multiple analysis files are numbered sequentially.
  - If we are sharing the data, last analysis script is called make_dw_files.[R,py] to write_csv to public folder.
  - `analysis/archive`
    - Any analyses for story threads that are no longer being investigated are placed here for reference.
- `data`
  - This is the directory used with our `datakit-data` plugin.
  - `data/documentation`
    - Documentation on data files should go here - data dictionaries, manuals, interview notes.
  - `data/handmade`
    - Manually created data sets by reporters go here.
  - `data/html_reports`
    - Any HTML reports or pages generated by code should go here.
  - `data/processed`
    - Data that has been processed by scripts in this project and is clean and ready for analysis goes here.
  - `data/public`
    - Public-facing data files (i.e., final datasets we share with reporters/make accessible) go here - data files which are 'live'.
  - `data/source`
    - Original data from sources goes here.
- `etl`
  - ETL (extract, transform, load) scripts for reading in source data and cleaning and standardizing it to prepare for analysis go here.
    - Multiple etl files are numbered.
    - Joins are included in etl process.
    - Last step of ETL process is to output an [RDS,Pickle] file to data/processed.
      - naming convention: etl_WHATEVERNAME.[rds,pkl]
- `publish`
  - This directory holds all documents in the project that will be public facing (e.g. data.world documents).
- `scratch`
  - This directory contains scratch materials that will not be used in the project at the end.
  - Common cases are filtered tables or quick visualizations for reporters.
  - This directory is not tracked in git.
- `viz`
  - Graphics and visualization development specific work such as web interactive code should go here.

## Usage

You will need to clone this repository to `~/.cookiecutters/` (make the directory if it doesn't exist):

```
cd path/to/.cookiecutters
git clone git@github.com:associatedpress/cookiecutter-generic-project
```

Then, use `datakit project`:

```
datakit project create --template cookiecutter-generic-project
```

If you'd like to avoid specifying the template each time, you can edit `~/.datakit/plugins/datakit-project/config.json` to use this template by default:

```
{"default_template": "/Users/lfenn/.cookiecutters/cookiecutter-generic-project"}
```

## UV project and package management

Dependencies:

- UV: `curl -LsSf https://astral.sh/uv/install.sh | sh`

## Configuration

You can set the default name, email, etc. for a project in the `cookiecutter.json` file.

## Notes

When cloning a Datakit project that someone else created, you will need to create a virtual environment and install the dependencies. You can do this by running the following from the termminal.

```
uv venv
uv sync
```

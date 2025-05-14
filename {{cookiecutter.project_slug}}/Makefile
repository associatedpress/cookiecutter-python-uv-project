# datakit tasks
dkgo:
	datakit data init
	datakit data push
	datakit gitlab integrate

dkglb:
	datakit gitlab integrate

dkdata:
	datakit data init

dkpush:
	datakit data push

dkpush_delete:
	datakit data push delete

dkpull:
	datakit data pull

# administrative tasks
run_notebook:
	uv run jupyter lab --no-browser

analysis_files:
	uv run quarto render analysis/*.ipynb --to html --execute

rmd_to_notebook:
	uv run jupytext --set-formats Rmd,ipynb analysis/*.Rmd

notebook_to_rmd:
	uv run jupytext --set-formats ipynb,Rmd analysis/*.ipynb

# define the source file
SOURCE_FILE = readme.ipynb

# define the destination directory
DEST_DIR = analysis/readme.ipynb

# define the target to move the file
readme:
	@echo "Moving $(SOURCE_FILE) to $(DEST_DIR)"
	mv $(SOURCE_FILE) $(DEST_DIR)

# package management tasks
sync:
	uv sync

install:
	uv add jupyterlab==3.6.3 itables jupyterlab-templates jupytext notebook pandas

install_linting:
	uv add black flake8 jupyterlab-code-formatter jupyterlab_flake8

install_multitask:
	uv add p_tqdm

install_tools:
	uv add rich retry pyjanitor arrow python-slugify cleantext

install_ai:
	uv add openai tiktoken scikit-learn

install_gfx:
	uv add plotnine

install_altair:
	uv add altair ap-altair-theme

install_web_scrape:
	uv add requests beautifulsoup4

install_gis:
	uv add geopandas

# etl tasks

# audit tasks

# export tasks

# data tasks
check_s3:
	aws s3 ls --recursive "s3://data.ap.org/projects/2025/template-for-counting-and-tracking/data" --profile default

# data distribution tasks
copy_distributed_data:
	cp <PATH_TO_LOCAL_FILE> data/public

create_distribution:
	datakit dworld create --slug template-for-counting-and-tracking

upload_distribution:
	datakit dworld push

update_documentation:
	datakit dworld summary

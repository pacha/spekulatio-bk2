
project_dir := justfile_directory()

export PYTHONPATH := project_dir

@help:
  just --list

@test-all:
  pytest --capture=no -o log_cli=false tests/

@test *params:
  pytest -x --capture=no -o log_cli=true {{ params }}

@format:
  black {{ project_dir }}

@type-check:
  mypy {{ project_dir }}/spekulatio/

@cli:
  ipython

run *params:
  #!/usr/bin/env python3
  from spekulatio.cli import spekulatio
  params = "{{ params }}".split()
  spekulatio(params)


import click

from .version import spekulatio_version
from .build import spekulatio_build


@click.group(context_settings={"show_default": True})
def spekulatio():
    pass


spekulatio.add_command(spekulatio_version)  # type: ignore
spekulatio.add_command(spekulatio_build)  # type: ignore

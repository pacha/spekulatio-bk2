import click

from spekulatio.logs import log


@click.command(name="build")
def spekulatio_build():
    """Build output."""

    # setup logging
    log.setLevel("DEBUG")

    log.info("Spekulatio build")

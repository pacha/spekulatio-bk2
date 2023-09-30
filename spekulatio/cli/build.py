
import click

from spekulatio.logs import log
from spekulatio.services import build


@click.command(name="build")
@click.option(
    "-v",
    "--verbose",
    is_flag=True,
    default=False,
    help="Show debug information.",
)
def spekulatio_build(
    verbose,
):
    """Build output."""

    # setup logging
    log.setLevel("DEBUG" if verbose else "WARN")

    foo = build(bar="hello world!")
    print(foo)

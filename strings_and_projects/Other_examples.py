from dynaconf import Dynaconf
settings = Dynaconf(settings_file=["settings.toml"])
# setttings.as_dict() -> dict, then pass to something
db_config = DatabaseConfig(**settings.as_dict()["database"])

import click
@click.command()
@click.option("--host", default="localhost")
@click.option("--port", default=8000)
@click.argument("extra", nargs=-1, type=click.UNPROCESSED)
def run(host, port, extra):
    # extra are unparsed key=value pairs
    extra_dict = dict(arg.split('=') for arg in extra)
    config = {**{"host": host, "port": port}, **extra_dict}
    start_server(**config)
    
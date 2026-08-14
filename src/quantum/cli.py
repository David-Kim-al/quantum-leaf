"""Command line interface for quantum-leaf."""
import click


@click.group()
def main():
    """quantum circuit simulation playground"""


@main.command()
def version():
    """Print version."""
    click.echo("quantum-leaf 0.4.1")


if __name__ == "__main__":
    main()

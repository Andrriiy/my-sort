import click

def _try_float(s):
    try:
        return float(s)
    except Exception:
        return s

@click.command(context_settings=dict(help_option_names=["-h", "--help"]))
@click.argument("filename", required=True, type=click.Path(exists=True))
@click.option("-r", "--reverse", is_flag=True, help="Reverse sort order")
@click.option("-n", "--numeric", is_flag=True, help="Numeric sort")
def cli(filename, reverse, numeric):
    """my-sort: простий аналог UNIX sort."""
    with open(filename, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f]

    keyfunc = _try_float if numeric else None
    lines.sort(key=keyfunc, reverse=reverse)

    for line in lines:
        print(line)

if __name__ == "__main__":
    cli()

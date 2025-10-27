from setuptools import setup, find_packages
import pathlib

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text(encoding="utf-8")

setup(
    name="my-sort",
    version="0.1.0",
    description="Simple CLI sort utility",
    long_description=README,
    long_description_content_type="text/markdown",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["click"],
    entry_points={
        "console_scripts": [
            "my-sort = my_sort.cli:cli",
        ],
    },
    python_requires=">=3.8",
)

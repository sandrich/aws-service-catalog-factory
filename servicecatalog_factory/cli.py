# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

from servicecatalog_factory import core
import logging
import click

logger = logging.getLogger()
logger.setLevel(logging.INFO)


@click.group()
@click.option('--info/--no-info', default=False)
@click.option('--info-line-numbers/--no-info-line-numbers', default=False)
def cli(info, info_line_numbers):
    """cli for pipeline tools"""
    if info:
        logging.basicConfig(
            format='%(levelname)s %(threadName)s %(message)s', level=logging.INFO
        )
    if info_line_numbers:
        logging.basicConfig(
            format='%(levelname)s %(threadName)s [%(filename)s:%(lineno)d] %(message)s',
            datefmt='%Y-%m-%d:%H:%M:%S',
            level=logging.INFO
        )


@cli.command()
@click.argument('p', type=click.Path(exists=True))
def validate(p):
    core.validate(p)


@cli.command()
@click.argument('p', type=click.Path(exists=True))
def generate_via_luigi(p):
    core.generate_via_luigi(p)


@cli.command()
@click.argument('p', type=click.Path(exists=True))
def show_pipelines(p):
    core.show_pipelines(p)


@cli.command()
@click.argument('p', type=click.Path(exists=True))
def deploy(p):
    core.deploy(p)


@cli.command()
@click.argument('portfolio-name')
@click.argument('product')
@click.argument('version')
def nuke_product_version(portfolio_name, product, version):
    core.nuke_product_version(portfolio_name, product, version)


@cli.command()
@click.argument('branch-name')
def bootstrap_branch(branch_name):
    core.bootstrap_branch(branch_name)


@cli.command()
def bootstrap():
    core.bootstrap()


@cli.command()
@click.argument('complexity', default='simple')
@click.argument('p', type=click.Path(exists=True))
def seed(complexity, p):
    core.seed(complexity, p)


@cli.command()
def version():
    core.version()


@cli.command()
@click.argument('p', type=click.Path(exists=True))
def upload_config(p):
    core.upload_config(p)


@cli.command()
@click.argument('p', type=click.Path(exists=True))
def fix_issues(p):
    core.fix_issues(p)


@cli.command()
@click.argument('stack-name')
def delete_stack_from_all_regions(stack_name):
    core.delete_stack_from_all_regions(stack_name)


@cli.command()
def list_resources():
    core.list_resources()


@cli.command()
@click.argument('f', type=click.File())
@click.argument('name')
@click.argument('portfolio_name', default=None)
def import_product_set(f, name, portfolio_name):
    core.import_product_set(f, name, portfolio_name)


if __name__ == "__main__":
    cli()

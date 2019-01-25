import requests
from bs4 import BeautifulSoup
import click

url = "https://public.dhe.ibm.com/software/products/UrbanCode/plugins/ibmucd/"

@click.group()
def cli():
    pass

@cli.command()
def listallplugins():
    req = requests.get(url)
    list_plugins = []
    soup = BeautifulSoup(req.text, 'html.parser')
    for link in soup.find_all('a'):
        list_plugins.append(link.get('href'))
        matchers = ['/']
        matching = [s for s in list_plugins if any(xs in s for xs in matchers)]
    click.echo(matching)

@cli.command()
@click.option('--name', help="Enter the name of the plugin - Please run listallplugins command to get correct naming convention")
def getpluginversions(name):
    downloadurl = url + name
    list_versions = []
    req = requests.get(downloadurl)
    soup = BeautifulSoup(req.text, 'html.parser')
    for link in soup.find_all('a'):
        list_versions.append(link.get('href'))
        matchers = ['.zip']
        matching = [s for s in list_versions if any(xs in s for xs in matchers)]
    click.echo(matching)

@cli.command()
@click.option('--name', help="Enter the name of the plugin - Please run listallplugins command to get correct naming convention")
@click.option('--version', prompt="Enter plugin version you want to download")
def downloadplugin(name, version):
    downloadurl = url + name + '/' + version
    req = requests.get(downloadurl)
    with open(version, "wb") as f:
        f.write(req.content)
    if req.status_code == 200:
        click.echo("Download Successful")

if __name__ == '__main__':
    cli()


from setuptools import setup
import re

def get_property(prop, project):
    """Gets the given property by name in the project's first init file."""
    result = re.search(
        r'{}\s*=\s*[\'"]([^\'"]*)[\'"]'.format(prop),
        open(project + '/__init__.py').read()
    )
    return result.group(1)

long_description = ''
with open('README.md', 'r') as f:
    long_description = f.read()

project_name = 'certainty'

install_requires = ''
with open(f'requirements/{project_name}.txt', 'r') as f:
    install_requires = f.read()

setup(
    name=project_name,
    version=get_property('__version__', project_name),
    author='Derek S. Prijatelj',
    author_email='dprijate@nd.edu',
    packages=[
        project_name,
        #f'{project_name}.dir',
    ],
    #scripts
    description=' '.join(
        'Probablistic models of certainty.',
    ),
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=f'https://github.com/prijatelj/{project_name}',
    install_requires=install_requires,
    python_requires='>=3.8',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    #tests_require=['pytest'],
    #setup_requires=['pylint', 'pytest-runner'],
    # Add the Script Interfce that provides `packagename submodule` similar to
    # `git pull` or `git push` commands for git and unify them under one alias
)

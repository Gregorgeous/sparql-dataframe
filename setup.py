from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='sparql_dataframe',
    version='0.4-fork',
    description='Convert SPARQL results to Pandas dataframes',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/Gregorgeous/sparql-dataframe',
    author='Ted Lawless',
    author_email='lawlesst@gmail.com',
    license='MIT',
    packages=['sparql_dataframe_fork'],
    install_requires=[
    'pandas>=0.22.0',
    'SPARQLWrapper>=1.8.1'
    ],
    test_suite="tests",
    zip_safe=False
)

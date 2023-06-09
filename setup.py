from setuptools import setup, find_packages

setup(
    name='jupyter_run_code',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'IPython',
    ],
    author='Omar Faruk',
    author_email='omarfaruk20@iut-dhaka.edu',
    description='This package addes a Jupyter magic command to write code \
        and run it.',
    url='https://github.com/omarfarukof/jupyter-run-code',
)

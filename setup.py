from setuptools import setup


def _get_requirements():
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()
    return requirements


setup(
    name='sentiment-analysis',
    version='1.0',
    install_requires=_get_requirements(),
)

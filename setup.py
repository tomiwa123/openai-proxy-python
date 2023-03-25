from setuptools import setup, find_packages

VERSION = '0.2.2'
DESCRIPTION = 'A price proxy for the OpenAI API'
LONG_DESCRIPTION = 'This proxy enables better budgeting and cost management for making OpenAI API calls ' \
                   'including more transparency into pricing. Github repo here: ' \
                   'https://github.com/tomiwa123/openai-proxy-python'

# Setting up
setup(
    # the name must match the folder name 'openai_proxy'
    name="openai_proxy",
    version=VERSION,
    author="Ayotomiwa Akinyele",
    author_email="<ayotomiwa.akinyele@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['openai', 'tiktoken'],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'

    keywords=['python', 'openai', 'proxy', 'api', 'wrapper'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
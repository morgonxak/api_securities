import setuptools

name = "api_securities"
python_minimal = "3.8"
version = "0.0.0"

with open("README.rst") as file:
    long_description = file.read()

setuptools.setup(
    name=name,
    version=version,
    description="Получает данные об фьючерсе для нейронной сети",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    author="Shumelev D.I.",
    author_email="cmit.dima@gmail.com",
    license="MIT",
    classifiers=[
        "Natural Language :: Russian",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    keywords="moex iss investing futures",
    install_requires=[
          'markdown',
      ]
)
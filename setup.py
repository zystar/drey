from setuptools import setup, find_packages
setup(
      name="drey",
      version="0.0.1",
      description="A blog base on tornado.",
      author="wanghongxu",
      url="https://github.com/wang19930902/drey",
      license="Apache License",
      packages=find_packages('drey'),
      scripts=["drey/app.py"],
      )

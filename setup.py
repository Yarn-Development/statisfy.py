from setuptools import setup,find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setup(
  name="statisfy",
  version="0.0.2",
  author="Aspekts",
  author_email="aspektshelp@gmail.com",
  description="Get statistics from your favourite social media sites, games and more!",
  long_description_content_type="text/markdown",
  long_description=long_description,
  packages=find_packages(),
  url="https://github.com/aspekts/statisfy.py",
  download_url="https://github.com/aspekts/statisfy/archive/v_002.tar.gz",
  project_urls={
        "Bug Tracker": "https://github.com/aspekts/statisfy.py/issues",
  },
  keywords=[
    'python',
    'stats',
    'statisfy',
    'statistics',
    'api wrapper',
    'analytics'
  ],
  classifiers=[
    "Development Status :: 2 - Pre-Alpha",
    "Intended Audience :: Developers",
    "Programming Language :: Python :: 3",
    "Operating System :: Unix",
    "Operating System :: MacOS :: MacOS X",
    "Operating System :: Microsoft :: Windows",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English"
  ]
)
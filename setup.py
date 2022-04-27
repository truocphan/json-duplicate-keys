# python setup.py bdist_wheel sdist
# twine upload --skip-existing dist/*
import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="json_duplicate_keys",
	version="22.4.28",
	author="Truoc Phan",
	license="MIT",
	author_email="truocphan112017@gmail.com",
	description="Flatten / Unflatten and Loads / Dumps JSON object with Duplicate Keys",
	long_description=long_description,
	long_description_content_type="text/markdown",
	install_requires=[],
	url="https://github.com/truocphan/json_duplicate_keys",
	classifiers=[
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 2",
		"Programming Language :: Python :: Implementation :: Jython"
	],
	keywords=["json", "duplicate keys", "json duplicate keys", "flatten", "unflatten"],
	packages=["json_duplicate_keys"],
)
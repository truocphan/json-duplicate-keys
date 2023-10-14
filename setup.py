import setuptools
import datetime

setuptools.setup(
	name="json-duplicate-keys",
	version=datetime.datetime.now().strftime("%Y.%m.%d"),
	author="Truoc Phan",
	license="MIT",
	author_email="truocphan112017@gmail.com",
	description="Flatten/ Unflatten and Load(s)/ Dump(s) JSON File/ Object with Duplicate Keys",
	long_description=open("README.md").read(),
	long_description_content_type="text/markdown",
	install_requires=open("requirements.txt").read().split(),
	url="https://github.com/truocphan/json-duplicate-keys",
	classifiers=[
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 2",
		"Programming Language :: Python :: Implementation :: Jython"
	],
	keywords=["json", "duplicate keys", "json duplicate keys", "flatten", "unflatten"],
	packages=["json_duplicate_keys"],
)
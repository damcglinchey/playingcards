import setuptools

PROJECT_NAME = 'playingcards'

version = {}
with open(PROJECT_NAME + '/version.py', 'r') as fp:
	exec(fp.read(), version)

setuptools.setup(
	name=PROJECT_NAME,
	version=version['__version__'],
	author='D. McGlinchey',
	author_email='damcglinchey@gmail.com',
	description='Tools for playing cards',
	packages=setuptools.find_packages(),
	scripts=['scripts/play_war.py'],
	classifiers=[
		"Programming Language :: Python :: 3",
		"Operating System :: OS Independent"],
	python_requires='>=3.6')
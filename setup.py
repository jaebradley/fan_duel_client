from setuptools import setup, find_packages
setup(
  name='fan-duel-client',
  packages=find_packages(exclude=['tests*']),
  install_requires=['requests', 'enum34', 'pytz'],
  version='0.3',
  description='A FanDuel client',
  author='Jae Bradley',
  author_email='jae.b.bradley@gmail.com',
  url='https://github.com/jaebradley/fan_duel_client',
  download_url='https://github.com/jaebradley/fan_duel_client/tarball/0.3',
  keywords=['sports', 'dfs', 'fanduel'],
  classifiers=[],
)
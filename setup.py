'''
  Copyright (C) 2025  Linked Ideal LLC.[https://linked-ideal.com/]
 
  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU Affero General Public License as
  published by the Free Software Foundation, version 3.
 
  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU Affero General Public License for more details.
 
  You should have received a copy of the GNU Affero General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

from setuptools import setup, find_packages

setup(
    name='ToposoidCommon',
    version="0.6.0",
    description="",
    author='Makoto Kubodera',
    packages=find_packages(),
    license='',
    package_data={'ToposoidCommon': ['logging.yml']},    
    include_package_data=True,
    install_requires=[
        "PyYAML",
        "pydantic",
        "regex",
        "langdetect"        
    ]
)
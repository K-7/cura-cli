# cli tool written in Python
Custom k2a CLI

### Usage 
- Install cli in any machine using root permission \
`$ sudo pip install git+https://github.com/K-7/k2a-cli`\
OR\
`sudo pip install --upgrade git+https://github.com/K-7/k2a-cli`

- If you've cloned this project, and Want to install the library (and all development dependencies) \
 `$ pip install -e .[test]`
 
- If you'd like to run all tests for this project. This will trigger py.test, along with its popular coverage plugin\
`$ python setup.py test`
        
- if you'd like to cut a new release of this CLI tool, and publish it to the Python Package Index (PyPI), you can do so by running:\
`$ python setup.py sdist bdist_wheel`\
`$ twine upload dist/*`        

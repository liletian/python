1. install python in windows or linux
   Download Python Executable Installer
2. Type sysdm.cpl and click OK. This opens the System Properties window and the python path to the system path.
3. python get-pip.py
4. python -m pip install --upgrade pip
5. python -m pip install --upgrade pip
6. pip install pytest
7. pip install requests
8. pip install --user pipx
9. help(object)
10. python -m pip install jupyter
11. pip install jupyter_contrib_nbextensions && jupyter contrib nbextension install
12. gist.github.com
14. pip install matplotlib
15. pip install pandas
16. pip install seaborn
17. pipenv shell
18. jupyter notebook
19. ptpython
20. pipenv lock
21. pipenv graph
22. pipenv graph --reverse
23. pipenv open flask
24. pipenv check
25. pipenv --venv
26. pipenv --where
27. pipenv install numpy
28. pyqt 
29. pip install pypiwin32
30. pip install --upgrade ipykernel
31. python manage.py runserver
32. django-admin startproject django_project
33. django-admin
34. manage.py startapp blog
35. DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
36. def save(self, **kwargs):

https://github.com/Tebs-Lab/intro-to-deep-learning


https://github.com/GoogleCloudPlatform/keras-idiomatic-programmer/tree/master/books/deep-learning-design-patterns/Workshops/Novice

python source code
https://github.com/python/cpython
https://realpython.com/cpython-source-code-guide/#what-does-a-compiler-do



dir(object)


python on mac tips

1. tensor flow mac need a plug-in
   https://developer.apple.com/metal/tensorflow-plugin/
2. mac os python direct installation
   https://www.python.org/downloads/macos/
3. jupyter notebook installation
   https://jupyter.org/install
4. python install with version specified
   pip install -Iv tensorflow==1.5
   pip install -Iv numpy==1.13
5. which -a jupyter
6. open jupyter notebook with specific python version
   /usr/local/opt/python@3.8/bin/python3 -m notebook
   python3 -m notebook

7. If you're using macOS go to Macintosh HD > Applications > Python3.6 folder (or whatever version of python you're using) > double click on "Install Certificates.command" file. 
   
For many objects, you can use this code, replacing 'object' with the object you're interested in: object_methods = [method_name for method_name in dir(object)if callable(getattr(object, method_name))]
gist.github.com
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem (registry editor) LongPathsEnabled

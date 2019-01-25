# ucdutils
Installation:
  First please install pipenv https://pipenv.readthedocs.io/en/latest/
  Then after you clone the project, goto the directory from the command line and type
  pipenv install 
  Then pipenv shell  (To activate this project's virtualenv, )
  then python UcdUtil.py
  
  
Usage:
  python Ucdtil.py
  1) List all plugins avaliable for UCD -> python Ucdtil.py listallplugins
  2) Get avaliable plugin versions -> python Ucdtil.py getpluginversions --name
  3) Download a pluginn version -> python Ucdtil.py downloadplugin --name 
  
	
Help:
 python Ucdtil.py commandname --help
 
Example:

 python Ucdtil.py listallplugins
 ['/software/products/UrbanCode/plugins/', 'AccuRevSourceConfig/', 'AgentPropertiesCollector/']
 
 
 python Ucdtil.py getpluginversions --name AccuRevSourceConfig
 ['AccuRevSourceConfig-4.973889.zip', 'AccuRevSourceConfig-6.1003936.zip', 'AccuRevSourceConfig-7.1007947.zip']
 
 
 python Ucdtil.py downloadplugin --name AccuRevSourceConfig
 Enter plugin version you want to download: AccuRevSourceConfig-6.1003936.zip
 

1.  we are utilizing 'rest_framework' to set up our rest api.

	a. add rest_framework to our settings apps
	b. create an api folder to making managing api easier
		1. create 3 files
			=> serialize.py: this will convert our homecook model to json and validate 	the data
			=> ulrs.py: we will set the routes || url|| path.
				routers from rest_framework will make our url naming easy.
				ex. http://localhost:8001/kitchens/ 
			=> views.py: API endpoint that allows our data models to be viewed or 	      edited.

*** make sure to link or reference api.url  from the main url in the settings ***
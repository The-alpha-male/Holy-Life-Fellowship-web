all: 
	@echo "Hello $(LOGNAME), nothing to do by default"
	@echo "Try 'make help'"

help:
	@echo ""
	@echo "dbUpdate - 'Making migrations and updating the database'"
	@echo "run - 'Running the server on the specified Port default is 9062'"
	@echo "pull - 'Get Changes from github MUST HAVE github Personal Token'"
	@echo ""

dbUpdate:
	python3 manage.py makemigrations
	python3 manage.py migrate

run:
	python3 manage.py runserver 

pull:
	@echo "You should have your Github Personal Token"
	git pull origin master
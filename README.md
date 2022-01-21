## Raspi_monitoring

## Technology used: 
- Python 
- Docker
- FastAPI
- PonyORM
- MySQL


# Assumptions: 

Small project to get familiar with PonyORM and FastAPI but more importantly with deployment on linux.
I will use raspberry pi, docker and python to get it running. 
Application will run on the RPI, monitor the temperature and perhaps a few other statistics. 
It will then use PonyORM to store them in MySQL database. 
There will also be FastAPI app, that will expose this data via RESTful API. 

I will consider it a success, when running a docker container I can get the data via postman from another machine in the network. 


Plan:
Step 1:  
 - Build a simple app that measures the temperature of the rpi - DONE
 - Writes this data to the DB model - datestamp, value, perhaps a simple func to include some text - - DONE
 - Deploy with Docker somehow. - DONE

Step 2: 
 - Expose the DB to be accessed outside of the docker container
 - you need to run this command: docker run -v /your/local/directory:/code/db
 - Deploy with mysql db as another docker service 
 - Once a day/ once a week some statistics are produced - mean, max, min etc. - this could use some design pattern - TO DO  
 - Save the resuls in a separate table in the DB - TO DO 

Step 3: 
 - Setup FastAPI app that will retrieve the data from MySQL and expose this to the outside. 

Step 4: 
 - Set alerts for when the threshold is exceeded. 
 - Deliver email notification in such case. 

Step 5: 
- Expand the monitoring to other sensors - humidity for example. 
 
# Future enhancements


 




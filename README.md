## pony_orm_connector

# Assumptions: 

Small project to get more familiar with ServiceNow and Observer pattern. 
Could be later used to become a Strategy Pattern for generating reports. 
Main point here is to be able to take data from A, put it in a model, and 
store it in the DB for further use. 

- query service now in a loop 
- perform action when a new record is detected 
- for now focusing on the incidents 
- I want to calculate the total downtime of outages
- I want to save these findings to the DB 
- I want to query the DB to check how much $$ is lost for each outage 

# Future enhancements

- deploy with two settings Test - sqlite in memory for testing and 
PROD with mysql
- no clue how to deploy with docker so gotta learn this 
- probably deploy on raspberry pi



## pony_orm_connector

# Assumptions: 

Small project to get familiar with Pony orm but more importantly with deployment on linux.
I will use raspberry pi, docker and python to get it running. 

Plan:
Step 1:  
 - Build a simple app that measures the temperature of the rpi 
 - Writes this data to the DB model - datestamp, value, perhaps a simple func to include some text
 - Deploy with Docker somehow.  

# Future enhancements

Step 2: 
 - Once a day/ once a week some statistics are produced - mean, max, min etc. - this could use some design pattern - Strategy 
 - They are send via email - this will require using .env and be careful with these

Step 3: 
 - If the temperature is above the treshold - event is triggered - another pattern could be applied here - Observer
 - Another email is triggered but with different warning. 

Step 4: 
 - use this setup to include more measurements - either fake values, or actual sensors plugged in to the rpi. 


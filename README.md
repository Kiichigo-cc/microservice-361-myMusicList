# microservice-361-myMusicList

Users request data from the client side by calling on the export server js. The export server js must constantly be running in the background and listening 
for requests, and once it recieves one from the client, it will run the code necessary. In this example code I have, simply running export_service.js with 
node export_service.js then running client.js will make it make its call. Since the export_service.js is listening on port 3000, seeing the client.js run on port 
3000 causes it to trigger. Right now, it is currently written so that it will search for pOg in the database, but this can be changed with a variable. 

Recieving data requires only to have a blank output.txt file. After export.py is run, output.txt will be filled with the names of every album name that had 
the searched for string within it. Using that output.txt file, it should be possible to use those names to sort the database.json for the applicable albums. 

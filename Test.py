import json


with open('Vaudeville_Tour_Listings.txt', 'r') as input_file:
    data = input_file.read()
    org_dict = json.loads(data)
    x = org_dict.keys()
    output_list = []
    flat_dictionary_list = []
    for date in x:
        calendar_date = date
        date_list =[date,[]]
        cities  = org_dict[date]
        y = cities.keys()
        for city in y:
            city_name = city
            venue_output_list = [city,[]]
            #print("The City Is " + city)                                                                                                                                                   
            venues = cities[city]
            venue_list = venues.keys()
            #print(venue_list)                                                                                                                                                              
            for venue in venue_list:
                venue_name = venue
                #print("The Venue Is " + venue)                                                                                                                                             
                performers = venues[venue]
                venue_and_performer_list = [venue, performers]
                #print(venue_and_performer_list)                                                                                                                                                            venue_output_list[1].append(venue_and_performer_list)
                for performer in performers:
                    performer  = { "date" : date, "city_name" : city, "venue_name" : venue, "performer" : performer}
                    flat_dictionary_list.append(performer)
            date_list[1].append(venue_output_list)
            #print(venue_output_list[0])                                                                                                                                                            #print(date_list)                                                                                                                                                                   
        output_list.append(date_list)
    #print(date_list)                                                                                                                                                                       
print(flat_dictionary_list)

with open ('Vaudeville_Flat_List.txt', 'w') as out_file:
    for x in flat_dictionary_list:
        out_file.write(json.dumps(x))

import json

def format(json_data):

    out_list = []
    d = json.loads(json_data)
    for key, value in d.items():
        if value["names"] != []:
            out_str = "📅"+key+"📅\n"
            for theatre in value["names"]:

                out_str += "\n🎭"+theatre["name"]+"\n"

                if theatre["description"] != None:
                    out_str += theatre["description"]+"\n"
                
                if theatre["place&time"] != None:
                    out_str += theatre["place&time"]+"\n"
            
            out_list.append(out_str)

    #Такое невозможно, но мало ли
    if out_list == []:
        out_list.append("Спектакли за указанный месяц не найдены!")
    
    return out_list
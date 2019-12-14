import json

def format(json_data):
    
    out_list = []
    d = json.loads(json_data)
    
    for key, value in d.items():
        out_str = "📅 "+key

        for name in value:
            out_str += "\n"+name
        out_list.append(out_str+"\n")

    return out_list
    
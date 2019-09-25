{"filter":false,"title":"run.py","tooltip":"/run.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":9,"column":34},"end":{"row":9,"column":35},"action":"remove","lines":["<"],"id":43}],[{"start":{"row":9,"column":34},"end":{"row":9,"column":35},"action":"insert","lines":["/"],"id":44},{"start":{"row":9,"column":35},"end":{"row":9,"column":36},"action":"insert","lines":["U"]}],[{"start":{"row":9,"column":36},"end":{"row":9,"column":37},"action":"insert","lines":["S"],"id":45},{"start":{"row":9,"column":37},"end":{"row":9,"column":38},"action":"insert","lines":["E"]},{"start":{"row":9,"column":38},"end":{"row":9,"column":39},"action":"insert","lines":["R"]},{"start":{"row":9,"column":39},"end":{"row":9,"column":40},"action":"insert","lines":["N"]},{"start":{"row":9,"column":40},"end":{"row":9,"column":41},"action":"insert","lines":["A"]},{"start":{"row":9,"column":41},"end":{"row":9,"column":42},"action":"insert","lines":["M"]}],[{"start":{"row":9,"column":42},"end":{"row":9,"column":43},"action":"insert","lines":["E"],"id":46}],[{"start":{"row":9,"column":43},"end":{"row":9,"column":44},"action":"insert","lines":["/"],"id":47},{"start":{"row":9,"column":44},"end":{"row":9,"column":45},"action":"insert","lines":["M"]},{"start":{"row":9,"column":45},"end":{"row":9,"column":46},"action":"insert","lines":["E"]},{"start":{"row":9,"column":46},"end":{"row":9,"column":47},"action":"insert","lines":["S"]},{"start":{"row":9,"column":47},"end":{"row":9,"column":48},"action":"insert","lines":["S"]},{"start":{"row":9,"column":48},"end":{"row":9,"column":49},"action":"insert","lines":["A"]}],[{"start":{"row":9,"column":49},"end":{"row":9,"column":50},"action":"insert","lines":["G"],"id":48},{"start":{"row":9,"column":50},"end":{"row":9,"column":51},"action":"insert","lines":["E"]}],[{"start":{"row":9,"column":68},"end":{"row":9,"column":69},"action":"remove","lines":[">"],"id":49},{"start":{"row":9,"column":67},"end":{"row":9,"column":68},"action":"remove","lines":["e"]},{"start":{"row":9,"column":66},"end":{"row":9,"column":67},"action":"remove","lines":["g"]},{"start":{"row":9,"column":65},"end":{"row":9,"column":66},"action":"remove","lines":["a"]},{"start":{"row":9,"column":64},"end":{"row":9,"column":65},"action":"remove","lines":["s"]},{"start":{"row":9,"column":63},"end":{"row":9,"column":64},"action":"remove","lines":["s"]},{"start":{"row":9,"column":62},"end":{"row":9,"column":63},"action":"remove","lines":["e"]},{"start":{"row":9,"column":61},"end":{"row":9,"column":62},"action":"remove","lines":["m"]},{"start":{"row":9,"column":60},"end":{"row":9,"column":61},"action":"remove","lines":["<"]},{"start":{"row":9,"column":59},"end":{"row":9,"column":60},"action":"remove","lines":[">"]},{"start":{"row":9,"column":58},"end":{"row":9,"column":59},"action":"remove","lines":["e"]},{"start":{"row":9,"column":57},"end":{"row":9,"column":58},"action":"remove","lines":["m"]},{"start":{"row":9,"column":56},"end":{"row":9,"column":57},"action":"remove","lines":["a"]},{"start":{"row":9,"column":55},"end":{"row":9,"column":56},"action":"remove","lines":["n"]},{"start":{"row":9,"column":54},"end":{"row":9,"column":55},"action":"remove","lines":["r"]},{"start":{"row":9,"column":53},"end":{"row":9,"column":54},"action":"remove","lines":["e"]},{"start":{"row":9,"column":52},"end":{"row":9,"column":53},"action":"remove","lines":["s"]},{"start":{"row":9,"column":51},"end":{"row":9,"column":52},"action":"remove","lines":["u"]}],[{"start":{"row":4,"column":0},"end":{"row":4,"column":13},"action":"insert","lines":["messages = []"],"id":50}],[{"start":{"row":5,"column":0},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":51},{"start":{"row":6,"column":0},"end":{"row":7,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":7,"column":0},"end":{"row":8,"column":0},"action":"insert","lines":["",""],"id":52}],[{"start":{"row":7,"column":0},"end":{"row":8,"column":55},"action":"insert","lines":["def add_messages(username, message):","    messages.append(\"{}: {}\".format(username, message))"],"id":53}],[{"start":{"row":16,"column":0},"end":{"row":18,"column":27},"action":"remove","lines":["@app.route('/<username>')","def user(username):","    return \"Hi \" + username"],"id":54},{"start":{"row":16,"column":0},"end":{"row":18,"column":41},"action":"insert","lines":["@app.route(\"/<username>\")","def user(username):","    return \"Welcome {0}\".format(username)"]}],[{"start":{"row":16,"column":11},"end":{"row":16,"column":12},"action":"remove","lines":["\""],"id":55}],[{"start":{"row":16,"column":11},"end":{"row":16,"column":12},"action":"insert","lines":["'"],"id":56}],[{"start":{"row":16,"column":23},"end":{"row":16,"column":24},"action":"remove","lines":["\""],"id":57}],[{"start":{"row":16,"column":23},"end":{"row":16,"column":24},"action":"insert","lines":["'"],"id":58}],[{"start":{"row":0,"column":0},"end":{"row":26,"column":70},"action":"remove","lines":["import os","from flask import Flask","","app = Flask(__name__)","messages = []","","","def add_messages(username, message):","    messages.append(\"{}: {}\".format(username, message))","","@app.route(\"/\")","def index():","    \"\"\"Main page with instructions\"\"\"","    return \"To send a message use /USERNAME/MESSAGE\"","","","@app.route('/<username>')","def user(username):","    return \"Welcome {0}\".format(username)","","","@app.route('/<username>/<message>')","def send_message(username, message):","    return \"{0}: {1}\".format(username, message)","","","app.run(host=os.getenv(\"IP\"), port=int(os.getenv(\"PORT\")), debug=True)"],"id":59},{"start":{"row":0,"column":0},"end":{"row":27,"column":70},"action":"insert","lines":["import os","from flask import Flask","","app = Flask(__name__)","messages = []","","","def add_messages(username, message):","    messages.append(\"{}: {}\".format(username, message))","","","@app.route(\"/\")","def index():","    \"\"\" Main page with instructions \"\"\"","    return \"To send a message use: /USERNAME/MESSAGE\"","","","@app.route(\"/<username>\")","def user(username):","    return \"Welcome {0}\".format(username)","","","@app.route(\"/<username>/<message>\")","def send_message(username, message):","    return \"{0}: {1}\".format(username, message)","","","app.run(host=os.getenv(\"IP\"), port=int(os.getenv(\"PORT\")), debug=True)"]}],[{"start":{"row":11,"column":11},"end":{"row":11,"column":12},"action":"remove","lines":["\""],"id":60}],[{"start":{"row":11,"column":11},"end":{"row":11,"column":12},"action":"insert","lines":["'"],"id":61}],[{"start":{"row":11,"column":13},"end":{"row":11,"column":14},"action":"remove","lines":["\""],"id":62}],[{"start":{"row":11,"column":13},"end":{"row":11,"column":14},"action":"insert","lines":["'"],"id":63}],[{"start":{"row":17,"column":11},"end":{"row":17,"column":12},"action":"remove","lines":["\""],"id":64}],[{"start":{"row":17,"column":11},"end":{"row":17,"column":12},"action":"insert","lines":["/"],"id":65}],[{"start":{"row":17,"column":11},"end":{"row":17,"column":12},"action":"remove","lines":["/"],"id":66}],[{"start":{"row":17,"column":11},"end":{"row":17,"column":12},"action":"insert","lines":[","],"id":67}],[{"start":{"row":17,"column":11},"end":{"row":17,"column":12},"action":"remove","lines":[","],"id":68}],[{"start":{"row":17,"column":11},"end":{"row":17,"column":12},"action":"insert","lines":["'"],"id":69}],[{"start":{"row":17,"column":23},"end":{"row":17,"column":24},"action":"remove","lines":["\""],"id":70}],[{"start":{"row":17,"column":23},"end":{"row":17,"column":24},"action":"insert","lines":["'"],"id":71}],[{"start":{"row":22,"column":11},"end":{"row":22,"column":12},"action":"remove","lines":["\""],"id":72}],[{"start":{"row":22,"column":11},"end":{"row":22,"column":12},"action":"insert","lines":["'"],"id":73}],[{"start":{"row":22,"column":33},"end":{"row":22,"column":34},"action":"remove","lines":["\""],"id":74}],[{"start":{"row":22,"column":33},"end":{"row":22,"column":34},"action":"insert","lines":["'"],"id":75}],[{"start":{"row":14,"column":33},"end":{"row":14,"column":34},"action":"remove","lines":[":"],"id":76}],[{"start":{"row":19,"column":40},"end":{"row":19,"column":41},"action":"insert","lines":[","],"id":77}],[{"start":{"row":19,"column":41},"end":{"row":19,"column":42},"action":"insert","lines":[" "],"id":78},{"start":{"row":19,"column":42},"end":{"row":19,"column":43},"action":"insert","lines":["m"]},{"start":{"row":19,"column":43},"end":{"row":19,"column":44},"action":"insert","lines":["e"]},{"start":{"row":19,"column":44},"end":{"row":19,"column":45},"action":"insert","lines":["s"]},{"start":{"row":19,"column":45},"end":{"row":19,"column":46},"action":"insert","lines":["s"]},{"start":{"row":19,"column":46},"end":{"row":19,"column":47},"action":"insert","lines":["a"]}],[{"start":{"row":19,"column":47},"end":{"row":19,"column":48},"action":"insert","lines":["g"],"id":79},{"start":{"row":19,"column":48},"end":{"row":19,"column":49},"action":"insert","lines":["e"]}],[{"start":{"row":27,"column":23},"end":{"row":27,"column":24},"action":"remove","lines":["\""],"id":80}],[{"start":{"row":27,"column":23},"end":{"row":27,"column":24},"action":"insert","lines":["'"],"id":81}],[{"start":{"row":27,"column":26},"end":{"row":27,"column":27},"action":"remove","lines":["\""],"id":82}],[{"start":{"row":27,"column":26},"end":{"row":27,"column":27},"action":"insert","lines":["'"],"id":83}],[{"start":{"row":27,"column":49},"end":{"row":27,"column":50},"action":"remove","lines":["\""],"id":84}],[{"start":{"row":27,"column":49},"end":{"row":27,"column":50},"action":"insert","lines":["'"],"id":85}],[{"start":{"row":27,"column":54},"end":{"row":27,"column":55},"action":"remove","lines":["\""],"id":86}],[{"start":{"row":27,"column":54},"end":{"row":27,"column":55},"action":"insert","lines":["'"],"id":87}],[{"start":{"row":19,"column":48},"end":{"row":19,"column":49},"action":"remove","lines":["e"],"id":88},{"start":{"row":19,"column":47},"end":{"row":19,"column":48},"action":"remove","lines":["g"]},{"start":{"row":19,"column":46},"end":{"row":19,"column":47},"action":"remove","lines":["a"]},{"start":{"row":19,"column":45},"end":{"row":19,"column":46},"action":"remove","lines":["s"]},{"start":{"row":19,"column":44},"end":{"row":19,"column":45},"action":"remove","lines":["s"]},{"start":{"row":19,"column":43},"end":{"row":19,"column":44},"action":"remove","lines":["e"]},{"start":{"row":19,"column":42},"end":{"row":19,"column":43},"action":"remove","lines":["m"]},{"start":{"row":19,"column":41},"end":{"row":19,"column":42},"action":"remove","lines":[" "]},{"start":{"row":19,"column":40},"end":{"row":19,"column":41},"action":"remove","lines":[","]}],[{"start":{"row":23,"column":36},"end":{"row":24,"column":0},"action":"insert","lines":["",""],"id":89},{"start":{"row":24,"column":0},"end":{"row":24,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":24,"column":4},"end":{"row":24,"column":6},"action":"insert","lines":["\"\""],"id":90}],[{"start":{"row":24,"column":6},"end":{"row":24,"column":7},"action":"insert","lines":["\""],"id":91}],[{"start":{"row":24,"column":7},"end":{"row":24,"column":8},"action":"insert","lines":["C"],"id":92},{"start":{"row":24,"column":8},"end":{"row":24,"column":9},"action":"insert","lines":["r"]},{"start":{"row":24,"column":9},"end":{"row":24,"column":10},"action":"insert","lines":["e"]},{"start":{"row":24,"column":10},"end":{"row":24,"column":11},"action":"insert","lines":["a"]},{"start":{"row":24,"column":11},"end":{"row":24,"column":12},"action":"insert","lines":["t"]},{"start":{"row":24,"column":12},"end":{"row":24,"column":13},"action":"insert","lines":["e"]}],[{"start":{"row":24,"column":13},"end":{"row":24,"column":14},"action":"insert","lines":[" "],"id":93},{"start":{"row":24,"column":14},"end":{"row":24,"column":15},"action":"insert","lines":["a"]}],[{"start":{"row":24,"column":15},"end":{"row":24,"column":16},"action":"insert","lines":[" "],"id":94},{"start":{"row":24,"column":16},"end":{"row":24,"column":17},"action":"insert","lines":["n"]},{"start":{"row":24,"column":17},"end":{"row":24,"column":18},"action":"insert","lines":["e"]},{"start":{"row":24,"column":18},"end":{"row":24,"column":19},"action":"insert","lines":["w"]}],[{"start":{"row":24,"column":19},"end":{"row":24,"column":20},"action":"insert","lines":[" "],"id":95},{"start":{"row":24,"column":20},"end":{"row":24,"column":21},"action":"insert","lines":["m"]},{"start":{"row":24,"column":21},"end":{"row":24,"column":22},"action":"insert","lines":["e"]},{"start":{"row":24,"column":22},"end":{"row":24,"column":23},"action":"insert","lines":["s"]},{"start":{"row":24,"column":23},"end":{"row":24,"column":24},"action":"insert","lines":["s"]},{"start":{"row":24,"column":24},"end":{"row":24,"column":25},"action":"insert","lines":["a"]},{"start":{"row":24,"column":25},"end":{"row":24,"column":26},"action":"insert","lines":["g"]},{"start":{"row":24,"column":26},"end":{"row":24,"column":27},"action":"insert","lines":["e"]}],[{"start":{"row":24,"column":27},"end":{"row":24,"column":28},"action":"insert","lines":[" "],"id":96},{"start":{"row":24,"column":28},"end":{"row":24,"column":29},"action":"insert","lines":["a"]},{"start":{"row":24,"column":29},"end":{"row":24,"column":30},"action":"insert","lines":["n"]},{"start":{"row":24,"column":30},"end":{"row":24,"column":31},"action":"insert","lines":["d"]}],[{"start":{"row":24,"column":31},"end":{"row":24,"column":32},"action":"insert","lines":[" "],"id":97},{"start":{"row":24,"column":32},"end":{"row":24,"column":33},"action":"insert","lines":["t"]},{"start":{"row":24,"column":33},"end":{"row":24,"column":34},"action":"insert","lines":["h"]},{"start":{"row":24,"column":34},"end":{"row":24,"column":35},"action":"insert","lines":["e"]},{"start":{"row":24,"column":35},"end":{"row":24,"column":36},"action":"insert","lines":["n"]}],[{"start":{"row":24,"column":36},"end":{"row":24,"column":37},"action":"insert","lines":[" "],"id":98},{"start":{"row":24,"column":37},"end":{"row":24,"column":38},"action":"insert","lines":["r"]},{"start":{"row":24,"column":38},"end":{"row":24,"column":39},"action":"insert","lines":["e"]},{"start":{"row":24,"column":39},"end":{"row":24,"column":40},"action":"insert","lines":["d"]},{"start":{"row":24,"column":40},"end":{"row":24,"column":41},"action":"insert","lines":["i"]},{"start":{"row":24,"column":41},"end":{"row":24,"column":42},"action":"insert","lines":["r"]},{"start":{"row":24,"column":42},"end":{"row":24,"column":43},"action":"insert","lines":["e"]},{"start":{"row":24,"column":43},"end":{"row":24,"column":44},"action":"insert","lines":["c"]}],[{"start":{"row":24,"column":44},"end":{"row":24,"column":45},"action":"insert","lines":["t"],"id":99}],[{"start":{"row":24,"column":45},"end":{"row":24,"column":46},"action":"insert","lines":[" "],"id":100},{"start":{"row":24,"column":46},"end":{"row":24,"column":47},"action":"insert","lines":["t"]},{"start":{"row":24,"column":47},"end":{"row":24,"column":48},"action":"insert","lines":["o"]}],[{"start":{"row":24,"column":48},"end":{"row":24,"column":49},"action":"insert","lines":[" "],"id":101},{"start":{"row":24,"column":49},"end":{"row":24,"column":50},"action":"insert","lines":["c"]},{"start":{"row":24,"column":50},"end":{"row":24,"column":51},"action":"insert","lines":["h"]},{"start":{"row":24,"column":51},"end":{"row":24,"column":52},"action":"insert","lines":["a"]}],[{"start":{"row":24,"column":52},"end":{"row":24,"column":53},"action":"insert","lines":["t"],"id":102}],[{"start":{"row":24,"column":53},"end":{"row":24,"column":54},"action":"insert","lines":[" "],"id":103},{"start":{"row":24,"column":54},"end":{"row":24,"column":55},"action":"insert","lines":["p"]},{"start":{"row":24,"column":55},"end":{"row":24,"column":56},"action":"insert","lines":["a"]},{"start":{"row":24,"column":56},"end":{"row":24,"column":57},"action":"insert","lines":["g"]},{"start":{"row":24,"column":57},"end":{"row":24,"column":58},"action":"insert","lines":["e"]},{"start":{"row":24,"column":58},"end":{"row":24,"column":59},"action":"insert","lines":["\""]}],[{"start":{"row":24,"column":59},"end":{"row":24,"column":60},"action":"insert","lines":["\""],"id":104},{"start":{"row":24,"column":60},"end":{"row":24,"column":61},"action":"insert","lines":["\""]}],[{"start":{"row":18,"column":19},"end":{"row":19,"column":0},"action":"insert","lines":["",""],"id":105},{"start":{"row":19,"column":0},"end":{"row":19,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":19,"column":4},"end":{"row":19,"column":6},"action":"insert","lines":["\"\""],"id":106}],[{"start":{"row":19,"column":6},"end":{"row":19,"column":7},"action":"insert","lines":["\""],"id":107}],[{"start":{"row":19,"column":7},"end":{"row":19,"column":8},"action":"insert","lines":["D"],"id":108},{"start":{"row":19,"column":8},"end":{"row":19,"column":9},"action":"insert","lines":["i"]},{"start":{"row":19,"column":9},"end":{"row":19,"column":10},"action":"insert","lines":["s"]},{"start":{"row":19,"column":10},"end":{"row":19,"column":11},"action":"insert","lines":["p"]},{"start":{"row":19,"column":11},"end":{"row":19,"column":12},"action":"insert","lines":["l"]},{"start":{"row":19,"column":12},"end":{"row":19,"column":13},"action":"insert","lines":["a"]},{"start":{"row":19,"column":13},"end":{"row":19,"column":14},"action":"insert","lines":["y"]}],[{"start":{"row":19,"column":14},"end":{"row":19,"column":15},"action":"insert","lines":[" "],"id":109},{"start":{"row":19,"column":15},"end":{"row":19,"column":16},"action":"insert","lines":["m"]},{"start":{"row":19,"column":16},"end":{"row":19,"column":17},"action":"insert","lines":["e"]},{"start":{"row":19,"column":17},"end":{"row":19,"column":18},"action":"insert","lines":["s"]},{"start":{"row":19,"column":18},"end":{"row":19,"column":19},"action":"insert","lines":["s"]},{"start":{"row":19,"column":19},"end":{"row":19,"column":20},"action":"insert","lines":["a"]},{"start":{"row":19,"column":20},"end":{"row":19,"column":21},"action":"insert","lines":["g"]},{"start":{"row":19,"column":21},"end":{"row":19,"column":22},"action":"insert","lines":["e"]},{"start":{"row":19,"column":22},"end":{"row":19,"column":23},"action":"insert","lines":["s"]}],[{"start":{"row":19,"column":23},"end":{"row":19,"column":24},"action":"insert","lines":["\""],"id":110},{"start":{"row":19,"column":24},"end":{"row":19,"column":25},"action":"insert","lines":["\""]},{"start":{"row":19,"column":25},"end":{"row":19,"column":26},"action":"insert","lines":["\""]}],[{"start":{"row":4,"column":13},"end":{"row":5,"column":0},"action":"insert","lines":["",""],"id":111},{"start":{"row":5,"column":0},"end":{"row":6,"column":0},"action":"insert","lines":["",""]},{"start":{"row":6,"column":0},"end":{"row":6,"column":1},"action":"insert","lines":["d"]},{"start":{"row":6,"column":1},"end":{"row":6,"column":2},"action":"insert","lines":["e"]},{"start":{"row":6,"column":2},"end":{"row":6,"column":3},"action":"insert","lines":["f"]}],[{"start":{"row":6,"column":3},"end":{"row":6,"column":4},"action":"insert","lines":[" "],"id":112},{"start":{"row":6,"column":4},"end":{"row":6,"column":5},"action":"insert","lines":["a"]},{"start":{"row":6,"column":5},"end":{"row":6,"column":6},"action":"insert","lines":["d"]},{"start":{"row":6,"column":6},"end":{"row":6,"column":7},"action":"insert","lines":["d"]},{"start":{"row":6,"column":7},"end":{"row":6,"column":8},"action":"insert","lines":["_"]},{"start":{"row":6,"column":8},"end":{"row":6,"column":9},"action":"insert","lines":["m"]},{"start":{"row":6,"column":9},"end":{"row":6,"column":10},"action":"insert","lines":["e"]}],[{"start":{"row":6,"column":10},"end":{"row":6,"column":11},"action":"insert","lines":["s"],"id":113},{"start":{"row":6,"column":11},"end":{"row":6,"column":12},"action":"insert","lines":["s"]},{"start":{"row":6,"column":12},"end":{"row":6,"column":13},"action":"insert","lines":["a"]},{"start":{"row":6,"column":13},"end":{"row":6,"column":14},"action":"insert","lines":["g"]},{"start":{"row":6,"column":14},"end":{"row":6,"column":15},"action":"insert","lines":["e"]},{"start":{"row":6,"column":15},"end":{"row":6,"column":16},"action":"insert","lines":["s"]}],[{"start":{"row":6,"column":16},"end":{"row":6,"column":18},"action":"insert","lines":["()"],"id":114}],[{"start":{"row":6,"column":17},"end":{"row":6,"column":18},"action":"insert","lines":["u"],"id":115},{"start":{"row":6,"column":18},"end":{"row":6,"column":19},"action":"insert","lines":["s"]},{"start":{"row":6,"column":19},"end":{"row":6,"column":20},"action":"insert","lines":["e"]},{"start":{"row":6,"column":20},"end":{"row":6,"column":21},"action":"insert","lines":["r"]}],[{"start":{"row":6,"column":21},"end":{"row":6,"column":22},"action":"insert","lines":["n"],"id":116},{"start":{"row":6,"column":22},"end":{"row":6,"column":23},"action":"insert","lines":["a"]},{"start":{"row":6,"column":23},"end":{"row":6,"column":24},"action":"insert","lines":["m"]}],[{"start":{"row":6,"column":17},"end":{"row":6,"column":24},"action":"remove","lines":["usernam"],"id":117},{"start":{"row":6,"column":17},"end":{"row":6,"column":25},"action":"insert","lines":["username"]}],[{"start":{"row":6,"column":25},"end":{"row":6,"column":26},"action":"insert","lines":[","],"id":118}],[{"start":{"row":6,"column":26},"end":{"row":6,"column":27},"action":"insert","lines":[" "],"id":119},{"start":{"row":6,"column":27},"end":{"row":6,"column":28},"action":"insert","lines":["m"]},{"start":{"row":6,"column":28},"end":{"row":6,"column":29},"action":"insert","lines":["e"]}],[{"start":{"row":6,"column":27},"end":{"row":6,"column":29},"action":"remove","lines":["me"],"id":120},{"start":{"row":6,"column":27},"end":{"row":6,"column":35},"action":"insert","lines":["messages"]}],[{"start":{"row":6,"column":34},"end":{"row":6,"column":35},"action":"remove","lines":["s"],"id":121}],[{"start":{"row":6,"column":34},"end":{"row":6,"column":35},"action":"remove","lines":[")"],"id":122}],[{"start":{"row":6,"column":34},"end":{"row":6,"column":35},"action":"insert","lines":[")"],"id":123},{"start":{"row":6,"column":35},"end":{"row":6,"column":36},"action":"insert","lines":[":"]}],[{"start":{"row":6,"column":36},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":124},{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"insert","lines":["    "]},{"start":{"row":7,"column":4},"end":{"row":7,"column":5},"action":"insert","lines":["m"]},{"start":{"row":7,"column":5},"end":{"row":7,"column":6},"action":"insert","lines":["e"]},{"start":{"row":7,"column":6},"end":{"row":7,"column":7},"action":"insert","lines":["s"]},{"start":{"row":7,"column":7},"end":{"row":7,"column":8},"action":"insert","lines":["s"]},{"start":{"row":7,"column":8},"end":{"row":7,"column":9},"action":"insert","lines":["a"]},{"start":{"row":7,"column":9},"end":{"row":7,"column":10},"action":"insert","lines":["g"]}],[{"start":{"row":7,"column":10},"end":{"row":7,"column":11},"action":"insert","lines":["e"],"id":125},{"start":{"row":7,"column":11},"end":{"row":7,"column":12},"action":"insert","lines":["."]}],[{"start":{"row":7,"column":12},"end":{"row":7,"column":13},"action":"insert","lines":["a"],"id":126},{"start":{"row":7,"column":13},"end":{"row":7,"column":14},"action":"insert","lines":["p"]},{"start":{"row":7,"column":14},"end":{"row":7,"column":15},"action":"insert","lines":["p"]},{"start":{"row":7,"column":15},"end":{"row":7,"column":16},"action":"insert","lines":["e"]},{"start":{"row":7,"column":16},"end":{"row":7,"column":17},"action":"insert","lines":["n"]},{"start":{"row":7,"column":17},"end":{"row":7,"column":18},"action":"insert","lines":["d"]}],[{"start":{"row":7,"column":18},"end":{"row":7,"column":20},"action":"insert","lines":["()"],"id":127}],[{"start":{"row":7,"column":19},"end":{"row":7,"column":21},"action":"insert","lines":["\"\""],"id":128}],[{"start":{"row":7,"column":20},"end":{"row":7,"column":21},"action":"insert","lines":["{"],"id":129},{"start":{"row":7,"column":21},"end":{"row":7,"column":22},"action":"insert","lines":["}"]}],[{"start":{"row":7,"column":22},"end":{"row":7,"column":23},"action":"insert","lines":[","],"id":130}],[{"start":{"row":7,"column":23},"end":{"row":7,"column":24},"action":"insert","lines":[" "],"id":131},{"start":{"row":7,"column":24},"end":{"row":7,"column":25},"action":"insert","lines":["{"]},{"start":{"row":7,"column":25},"end":{"row":7,"column":26},"action":"insert","lines":["}"]}],[{"start":{"row":7,"column":26},"end":{"row":7,"column":27},"action":"insert","lines":[","],"id":132}],[{"start":{"row":7,"column":26},"end":{"row":7,"column":27},"action":"remove","lines":[","],"id":133}],[{"start":{"row":7,"column":27},"end":{"row":7,"column":28},"action":"insert","lines":["."],"id":134},{"start":{"row":7,"column":28},"end":{"row":7,"column":29},"action":"insert","lines":["f"]},{"start":{"row":7,"column":29},"end":{"row":7,"column":30},"action":"insert","lines":["o"]},{"start":{"row":7,"column":30},"end":{"row":7,"column":31},"action":"insert","lines":["r"]},{"start":{"row":7,"column":31},"end":{"row":7,"column":32},"action":"insert","lines":["m"]},{"start":{"row":7,"column":32},"end":{"row":7,"column":33},"action":"insert","lines":["a"]},{"start":{"row":7,"column":33},"end":{"row":7,"column":34},"action":"insert","lines":["t"]}],[{"start":{"row":7,"column":34},"end":{"row":7,"column":36},"action":"insert","lines":["()"],"id":135}],[{"start":{"row":7,"column":35},"end":{"row":7,"column":36},"action":"insert","lines":["u"],"id":136},{"start":{"row":7,"column":36},"end":{"row":7,"column":37},"action":"insert","lines":["s"]},{"start":{"row":7,"column":37},"end":{"row":7,"column":38},"action":"insert","lines":["e"]}],[{"start":{"row":7,"column":35},"end":{"row":7,"column":38},"action":"remove","lines":["use"],"id":137},{"start":{"row":7,"column":35},"end":{"row":7,"column":43},"action":"insert","lines":["username"]}],[{"start":{"row":7,"column":43},"end":{"row":7,"column":44},"action":"insert","lines":[","],"id":138}],[{"start":{"row":7,"column":44},"end":{"row":7,"column":45},"action":"insert","lines":[" "],"id":139},{"start":{"row":7,"column":45},"end":{"row":7,"column":46},"action":"insert","lines":["m"]},{"start":{"row":7,"column":46},"end":{"row":7,"column":47},"action":"insert","lines":["e"]}],[{"start":{"row":7,"column":45},"end":{"row":7,"column":47},"action":"remove","lines":["me"],"id":140},{"start":{"row":7,"column":45},"end":{"row":7,"column":52},"action":"insert","lines":["message"]}],[{"start":{"row":10,"column":0},"end":{"row":11,"column":55},"action":"remove","lines":["def add_messages(username, message):","    messages.append(\"{}: {}\".format(username, message))"],"id":141},{"start":{"row":9,"column":0},"end":{"row":10,"column":0},"action":"remove","lines":["",""]},{"start":{"row":8,"column":0},"end":{"row":9,"column":0},"action":"remove","lines":["",""]},{"start":{"row":7,"column":54},"end":{"row":8,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":0,"column":0},"end":{"row":28,"column":70},"action":"remove","lines":["import os","from flask import Flask","","app = Flask(__name__)","messages = []","","def add_messages(username, message):","    message.append(\"{}, {}\".format(username, message))","","","@app.route('/')","def index():","    \"\"\" Main page with instructions \"\"\"","    return \"To send a message use /USERNAME/MESSAGE\"","","","@app.route('/<username>')","def user(username):","    \"\"\"Display messages\"\"\"","    return \"Welcome {0}\".format(username)","","","@app.route('/<username>/<message>')","def send_message(username, message):","    \"\"\"Create a new message and then redirect to chat page\"\"\"","    return \"{0}: {1}\".format(username, message)","","","app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)"],"id":142},{"start":{"row":0,"column":0},"end":{"row":36,"column":70},"action":"insert","lines":["import os","from flask import Flask, redirect","","app = Flask(__name__)","messages = []","","","def add_messages(username, message):","    \"\"\"Add messages to the `messages` list\"\"\"","    messages.append(\"{}: {}\".format(username, message))","","","def get_all_messages():","    \"\"\"Get all of the messages and separate them with a `br`\"\"\"","    return \"<br>\".join(messages)","","","@app.route(\"/\")","def index():","    \"\"\"Main page with instructions\"\"\"","    return \"To send a message use: /USERNAME/MESSAGE\"","","","@app.route(\"/<username>\")","def user(username):","    \"\"\"Display chat messages\"\"\"","    return \"<h1>Welcome, {0}</h1>{1}\".format(username, get_all_messages())","","","@app.route(\"/<username>/<message>\")","def send_message(username, message):","    \"\"\"Create a new message and redirect back to the chat page\"\"\"","    add_messages(username, message)","    return redirect(\"/\" + username)","","","app.run(host=os.getenv(\"IP\"), port=int(os.getenv(\"PORT\")), debug=True)"]}],[{"start":{"row":0,"column":0},"end":{"row":36,"column":70},"action":"remove","lines":["import os","from flask import Flask, redirect","","app = Flask(__name__)","messages = []","","","def add_messages(username, message):","    \"\"\"Add messages to the `messages` list\"\"\"","    messages.append(\"{}: {}\".format(username, message))","","","def get_all_messages():","    \"\"\"Get all of the messages and separate them with a `br`\"\"\"","    return \"<br>\".join(messages)","","","@app.route(\"/\")","def index():","    \"\"\"Main page with instructions\"\"\"","    return \"To send a message use: /USERNAME/MESSAGE\"","","","@app.route(\"/<username>\")","def user(username):","    \"\"\"Display chat messages\"\"\"","    return \"<h1>Welcome, {0}</h1>{1}\".format(username, get_all_messages())","","","@app.route(\"/<username>/<message>\")","def send_message(username, message):","    \"\"\"Create a new message and redirect back to the chat page\"\"\"","    add_messages(username, message)","    return redirect(\"/\" + username)","","","app.run(host=os.getenv(\"IP\"), port=int(os.getenv(\"PORT\")), debug=True)"],"id":143},{"start":{"row":0,"column":0},"end":{"row":38,"column":70},"action":"insert","lines":["import os","from datetime import datetime","from flask import Flask, redirect","","app = Flask(__name__)","messages = []","","","def add_messages(username, message):","    \"\"\"Add messages to the `messages` list\"\"\"","    now = datetime.now().strftime(\"%H:%M:%S\")","    messages.append(\"({}) {}: {}\".format(now, username, message))","","","def get_all_messages():","    \"\"\"Get all of the messages and separate them with a `br`\"\"\"","    return \"<br>\".join(messages)","","","@app.route(\"/\")","def index():","    \"\"\"Main page with instructions\"\"\"","    return \"To send a message use: /USERNAME/MESSAGE\"","","","@app.route(\"/<username>\")","def user(username):","    \"\"\"Display chat messages\"\"\"","    return \"<h1>Welcome, {0}</h1>{1}\".format(username, get_all_messages())","","","@app.route(\"/<username>/<message>\")","def send_message(username, message):","    \"\"\"Create a new message and redirect back to the chat page\"\"\"","    add_messages(username, message)","    return redirect(\"/\" + username)","","","app.run(host=os.getenv(\"IP\"), port=int(os.getenv(\"PORT\")), debug=True)"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":14,"column":23},"end":{"row":14,"column":23},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1569422417574,"hash":"9d87726d51b39cb8e54071407e5017b6414be66f"}
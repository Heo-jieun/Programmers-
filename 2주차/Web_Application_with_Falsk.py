from flask import Flask, jsonify, request

app = Flask(__name__)

menus = [
    {"id" : 1, "name" : "Espresso", "price" : 3800},
    {"id" : 2, "name" : "Americano", "price" : 4100},
    {"id" : 3, "name" : "CfeLatte", "price" : 4600},
]


@app.route('/')
def hello_flask():
    return "Helow World!"

count = 3
# GET / menus -> 자료를 가지고 온다.
@app.route('/menus') # menus라는 자료에 접근하는 주소 / methods = ['GET']이 디폴트
def get_menus() :


    # 딕셔너리는 json으로 바꿔줄 수 없어서 menus를 value로 하는 새로운 딕셔너리를 만들어줌
    return jsonify({"menus" : menus}) # jsonify : json화 해서 바꿔줌

# POST /menus -> 자료를 자원에 추가한다.
@app.route('/menus', methods = ['POST'])
def create_menu() :
    # 전달받은 자료를 menus 자원에 추가
    # request가 JSON이라고 가정
    request_data = request.get_json()
    global count
    count += 1
    new_menu = {
        "id" : count,
        "name" : request_data['name'],
        "price" : request_data['price']
    }
    menus.append(new_menu)
    return jsonify(new_menu)

# PUT / menu에서 id에 해당하는 자료를 update해준다.
@app.route('/PUT/menu/<int:id>', methods = ["PUT"])
def update_menu(id) :
    update_data = request.get_json()

    menus[id-1].update( name = update_data["name"])
    menus[id-1].update( price = update_data["price"])

    return jsonify(menus[id-1])

# DELETE / menu에서 id에 해당하는 데이터를 삭제한다.
@app.route('/DELETE/menu/<int:id>', methods = ["DELETE"] )
def delete_menu(id) :
    del menus[id-1]
    return jsonify(menus)

if __name__ == '__main__':
    app.run()

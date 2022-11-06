from flask import Flask, render_template, request, redirect, url_for, flash, make_response, session, abort
import json
import os.path
from werkzeug.utils import secure_filename
app = Flask(__name__)
app.secret_key = "|\|||<|-|||_"

@app.route('/', methods=['GET', 'POST'])
def home():
    if session:
        with open('json/poll/users.json') as file:
            dict1 = json.load(file)
            img = dict1[session['uname']]['gender-img']
            return redirect(url_for('home_template'))
    else:
        return render_template('sign.html', msg='')


@app.route('/sign', methods=['POST'])
def sign():
    if request.method == 'POST':
        #return request.form['file']
        #render_template('loading.html')
        uname = request.form['uname']
        psw = request.form['psw']
        gender = 'default'
        full_name = ''
        level = request.form['level']

        session.clear()
        session['uname'] = uname
        session['psw'] = psw

        file = request.files['file']
        file_name = request.form['full_name']

	
        if file_name == 'fish':
            full_name = 'File=none.png'
        else:
            full_name = file_name + secure_filename(file.filename)
            file.save('static/chat/user_files/{}'.format(full_name))

#poll+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        c = ''
        if os.path.exists('json/poll/users.json'):
            user_dict1 = {}
            with open('json/poll/users.json') as user_file1:
                user_dict1 = json.load(user_file1)
                if uname in user_dict1.keys():
                    msg = 'That username already exists. Please use another username'
                    return render_template('sign.html', msg=msg)
                else:
                    if gender == 'male':
                        c = 'File=/Static/poll/male.jpg'
                    elif gender == 'female':
                        c = 'File=/Static/poll/female.png'
                    else:
                        c = 'File=/Static/poll/none.png'
                    user_dict1[uname] = {
                        'password' : psw,
                        'gender-img' : c,
                        'polls' : [],
                        'gender-img': full_name,
                        'rewards': 1,
                        'money': 0
                    }
                with open('json/poll/users.json', 'w') as hih:
                    json.dump(user_dict1, hih)
        else:
            user_dict2 = {}
            gender = gender
            if gender == 'male':
                c = 'File=/Static/poll/male.jpg'
            elif gender == 'female':
                c = 'File=/Static/poll/female.png'
            else:
                c = 'File=/Static/poll/none.png'
            user_dict2[uname] = {
                'password' : psw,
                'gender-img' : c,
                'polls' : [],
                'gender-img': full_name,
                'rewards': 1,
                'money': 0
            }
            with open("json/poll/users.json", "w") as hib:
                json.dump(user_dict2, hib)

    #chat+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        if os.path.exists('json/chat/users.json'):
            with open('json/chat/users.json') as file:
                user_dict = json.load(file)
                if uname in user_dict.keys():
                    msg = 'That Username already exists'
                    return render_template('sign.html', msg=msg)
                else:
                    user_dict[uname] = {
                        'password' : psw,
                        'img' : '/Static/chat/none.PNG',
                        'groups' : [],
                        'gender-img': full_name,
                        'rewards': 1,
                        'money': 0
                    }
                    with open('json/chat/users.json', 'w') as file2:
                        json.dump(user_dict, file2)
                        if os.path.exists('json/chat/chat.json'):
                            with open('json/chat/chat.json') as file102:
                                dict102 = json.load(file102)
                                dict102['World Chat']['people'].append(session['uname'])
                                with open('json/chat/chat.json', 'w') as file103:
                                    json.dump(dict102, file103)
                        else:
                            dict104 = {}
                            dict104['World Chat'] = {
                            'people': [],
                            'chat': [],
                            'gender-img': full_name,
                            'rewards': 1,
                            'money': 0
                            }
                            dict104['World Chat']['people'].append(session['uname'])
                            with open('json/chat/chat.json', 'w') as file105:
                                json.dump(dict104, file105)
        else:
            user_dict3 = {}
            user_dict3[uname] = {
                'password' : psw,
                'img' : '/Static/chat/none.PNG',
                'groups' : [],
                'gender-img': full_name,
                'rewards': 1,
                'money': 0
            }
            with open('json/chat/users.json', 'w') as file4:
                json.dump(user_dict3, file4)
    #spell+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        if os.path.exists('json/spell/users.json'):
            with open('json/spell/users.json') as file:
                user_dict = json.load(file)
                if uname in user_dict.keys():
                    msg = 'That Username already exists'
                    return render_template('sign.html', msg=msg)
                else:
                    user_dict[uname] = {
                        'password' : psw,
                        'gender-img' : '/Static/spell/none.PNG',
                        'level' : int(level),
                        'avg-percent' : 100,
                        'wrong' : [],
                        'custom' : [],
                        'gender-img': full_name,
                        'rewards': 1,
                        'money': 0
                    }
                    with open('json/spell/users.json', 'w') as file2:
                        json.dump(user_dict, file2)
                return redirect(url_for('home'))
        else:
            user_dict3 = {}
            user_dict3[uname] = {
                'password' : psw,
                'gender-img' : '/Static/spell/none.PNG',
                'level' : int(level),
                'avg-percent' : 100,
                'wrong' : [],
                'custom' : [],
                'gender-img': full_name,
                'money': 0,
                'rewards': 1
            }
            #return user_dict3
            with open('json/spell/users.json', 'w') as file4:
                json.dump(user_dict3, file4)
        return redirect(url_for('home'))

@app.route('/log_page', methods=['GET'])
def log_page():
    return render_template('log.html', msg=" ")

@app.route('/login', methods=['POST'])
def login():
    uname = request.form['uname']
    psw = request.form['psw']
    if os.path.exists('json/poll/users.json'):
        with open('json/poll/users.json') as target:
            file = json.load(target)
            if uname in file.keys():
                if psw == file[uname]['password']:
                    session.clear()
                    session['uname'] = uname
                    session['psw'] = psw
                    return redirect(url_for('home'))
                else:
                    msg = 'Wrong'
                    return render_template('log.html', msg=msg)
            msg = 'Wrong'
            return render_template('log.html', msg=msg)
    else:
        return redirect(url_for('home'))

@app.route('/HOME')
def home_template():
    if session:
        with open('json/poll/users.json') as fish:
            fishy = json.load(fish)
            img = fishy[session['uname']]['gender-img']
            fishy[session['uname']]['rewards'] += 1
            points = fishy[session['uname']]['rewards']
            with open('json/poll/users.json', 'w') as fillet:
                json.dump(fishy, fillet)
                return render_template('home.html', img='chat/user_files/{}'.format(img), name=session['uname'], points=points)
    else:
        return redirect(url_for('home'))

@app.route('/sign_out')
def sign_out():
    session.clear()
    return redirect(url_for('home'))

@app.route('/user')
def users():
    if session:
        listy = 25
        with open('json/poll/users.json') as fish:
            fishy = json.load(fish)
            img = fishy[session['uname']]['gender-img']
            points = fishy[session['uname']]['rewards']
            money = fishy[session['uname']]['money']
            psw = fishy[session['uname']]['password']
            if points >= listy:
                money += 10
                points -= 25
                fishy[session['uname']]['rewards'] -= 25
                fishy[session['uname']]['money'] += 10
            with open('json/shop.json') as shop_file:
                shop = json.load(shop_file)
                owned = []
                unowned = []
                colors = []
                #return shop
                for elm in shop['Shop']:
                    for key in elm.keys():
                        if session['uname'] in elm[key]:
                            owned.append(key)
                        else:
                            unowned.append(key)
                for elm in unowned:
                    dh0d = elm.split(' ')
                    colors.append(dh0d[0])
                #return  {'dict': colors}
                if len(unowned) == 0:
                    owned = ['ALL of the Badges']
                    fishy[session['uname']]['money'] += 280
                    with open('json/poll/users.json', 'w') as guddi:
                        json.dump(fishy, guddi)
                    return render_template('user.html', img='chat/user_files/{}'.format(img), name=session['uname'], points=points, money=money, psw=psw, owned=owned, unowned=unowned, colors=colors, r='reward')
                else:
                    return render_template('user.html', img='chat/user_files/{}'.format(img), name=session['uname'], points=points, money=money, psw=psw, owned=owned, unowned=unowned, colors=colors, r='nope')
    else:
        return redirect(url_for('home'))

@app.route('/purchase', methods=['POST'])
def purchase():
    color = request.form['color']
    with open('json/shop.json') as shop_file:
        shopa = json.load(shop_file)
        #return {'dict': shopa['Shop'][0]['{} Badge'.format(color)]}

        with open('json/poll/users.json') as jkj:
            usersk = json.load(jkj)
            hi = []
            if usersk[session['uname']]['money'] >= 10:
                num = 0
                for elm in shopa['Shop']:
                    #hi.append(elm)
                    for key in elm.keys():
                        #hi.append(elm[key])
                        if key == '{} Badge'.format(color):
                            shopa['Shop'][num][key].append(session['uname'])

                    num += 1
                #return {'djkict': hi}
                #return '{} Badge'.format(color)
                usersk[session['uname']]['money'] = usersk[session['uname']]['money'] - 10
                #return usersk
                with open('json/poll/users.json', 'w') as lkjkl:
                    #return shopa
                    json.dump(usersk, lkjkl)
                with open('json/shop.json', 'w') as asdsa:
                    json.dump(shopa, asdsa)
                return redirect(url_for('users'))
            else:
                return redirect(url_for('users'))

@app.route('/leaders')
def leaders():
    if session:
        users = []
        with open('json/poll/users.json') as file:
            user_dict = json.load(file)
            for elm in user_dict.keys():
                users.append({int(user_dict[elm]['money']): elm})
            #return {'dict':users}
            num = 0
            big = {}
            massive = []
            numbers = []
            for counter in range(0, len(users)):
                for elm in users:
                    for key in elm.keys():
                        if num == 0:
                            big = {str(key): elm[key]}
                        else:
                            a = big.keys()
                            return {'a': a}
                            if int(users[elm][key]) > int(a[0]):
                                big = {str(key): elm[key]}
                    num += 1
                b = ''
                for keys in big.keys():
                    b = str(keys)
                    #users.remove(b)
                    massive.append(str(big[b]))
                    numbers.append(b)
                #return big
            return render_template('leader.html', top=massive, numbers=numbers, name=session['uname'])

#CHAT###########################################################################C####################################################################################################################################################################
#CHAT###########################################################################H####################################################################################################################################################################
#CHAT###########################################################################A####################################################################################################################################################################
#CHAT###########################################################################T####################################################################################################################################################################

@app.route('/chat', methods=['GET', 'POST'])
def chat__home():
    if session:
        return redirect(url_for('chat__chat_cookies'))
    return render_template('/chat/home.html', show='false')

@app.route('/chat/true', methods=['GET', 'POST'])
def chat__home2():
    return render_template('/chat/home2.html', show='true')

@app.route('/chat/create_account')
def chat__sign_page():
    return render_template('/chat/sign.html')


@app.route('/chat/chat')
def chat__chat_cookies():
    if session:
        if os.path.exists('json/chat/chat.json'):
            with open('json/chat/chat.json') as file:
                chat_dict = json.load(file)
                user_list = []
                big_list = {}
                counter = 0
                people = []
                text = []
                for groups in chat_dict.keys():
                    if session['uname'] in chat_dict[groups]['people']:
                        people.append({groups : chat_dict[groups]['people']})
                        string = 'message{}'.format(counter)
                        big_list.update({"text{}".format(counter + 1) : chat_dict[groups]['chat']})
                        user_list.append(groups)
                        text.append("text{}".format(counter + 1))
                    counter += 1
                stream=big_list
                #return stream
                ping = []
                for elm in user_list:
                    ping.append(elm.replace(' ', '_'))
                #return {'dict': ping}
                return render_template('/chat/chat.html', name=session['uname'], chats_encode=ping, chats=user_list, stream=stream, length=len(user_list), people=people, text=text, show="img", dh0d='b')
        else:
            return redirect(url_for('chat__chat_empty'))
    else:
        return redirect(url_for('chat__home'))

@app.route('/chat/create', methods=['POST', 'GET'])
def chat__create():
    if request.method == "POST":
        with open('json/chat/users.json') as file:
            dict1 = json.load(file)
            return render_template('/chat/color.html', name=session['uname'], users=dict1.keys())
    else:
        if session:
            return redirect(url_for('chat__chat_cookies'))
        else:
            return redirect(url_for('chat__home'))

@app.route('/chat/create_chat', methods=['GET', 'POST'])
def chat__new_chat():
    if request.method == 'POST':

        group_name = request.form['group']
        people_list = request.form['people'].split(', ')
        people_list.remove(people_list[-1])
        with open('json/chat/users.json') as user_file:
            user_dict = json.load(user_file)
            bad = 0
            for elm in people_list:
                if elm in user_dict.keys():
                    user_dict[elm]['groups'].append(group_name)
                else:
                    bad += 1
            with open('json/chat/users.json', 'w') as rfile:
                json.dump(user_dict, rfile)
            if bad > 0:
                flash('some of the users you chose do not exist')
                return redirect(url_for('chat__create'))
        if os.path.exists('json/chat/chat.json'):
            with open('json/chat/chat.json') as chat_file:
                chat_dict = json.load(chat_file)
                chat_dict[group_name] = {
                    'people' : people_list,
                    'chat' : []
                }
                with open('json/chat/chat.json', 'w') as chat_file2:
                    json.dump(chat_dict, chat_file2)
        else:
            chat_dict2 = {}
            chat_dict2[group_name] = {
                'people' : people_list,
                'chat' : []
            }
            chat_dict2['World Chat'] = {
            'people': [],
            'chat': []
            }
            with open('json/chat/chat.json', 'w') as chat_file2:
                json.dump(chat_dict2, chat_file2)
        return redirect(url_for('chat__chat_cookies'))
    else:
        if session:
            return redirect(url_for('chat__chat_cookies'))
        else:
            return redirect(url_for('chat__home'))

@app.route('/chat/304923082475783948575392847205347584025982307324983409586304852794873928472985349')
def chat__chat_empty():
    if session:
        return render_template('/chat/empty.html', name=session['uname'])
    else:
        return redirect(url_for('chat__home'))

@app.route('/chat/post', methods=['GET', 'POST'])
def chat__post():
    if request.method == 'POST':
        posts = request.form['message']
        wheres = request.form['from']
        with open('json/chat/chat.json') as file:
            chat_dict = json.load(file)
            chat_dict[wheres]['chat'].append({"from": session['uname'], "text": posts})
            with open('json/chat/chat.json', 'w') as bob:
                json.dump(chat_dict, bob)
            return render_template('/chat/blank.html', show=wheres)


@app.route('/chat/kick', methods=['POST', 'GET'])
def chat__kick():
    if request.method == 'POST':
        if request.form['from'] == 'chat':
            with open('json/chat/chat.json') as file:
                dict1 = json.load(file)
            return render_template('/chat/kick.html', people=dict1[request.form['chat']]['people'], chat=request.form['chat'])
        else:
            people = request.form['words'].split(', ')
            people.remove(people[-1])
            with open('json/chat/chat.json') as file:
                dict1 = json.load(file)
                list1 = []
                list1.append(request.form['chat'])
                for counter in range(0, int(request.form['num'])):
                    for elm in list1:
                        dict1[elm]['people'].remove(people[counter])
                with open('json/chat/chat.json', 'w') as file999:
                    json.dump(dict1, file999)
                return redirect(url_for('chat__chat_cookies'))
    else:
        if session:
            return redirect(url_for('chat__chat_cookies'))
        else:
            return redirect(url_for('chat__home'))


@app.route('/chat/join', methods=['GET', 'POST'])
def chat__join():
    if request.method == 'POST':
        if request.form['from'] == 'chat':
            with open('json/chat/users.json') as file:
                dict1 = json.load(file)
            return render_template('/chat/join.html', users=dict1.keys(), chat=request.form['chat'], name=session['uname'])
        else:
            #return {'dict': [request.form['chat'], request.form['people'], request.form['num']]}
            people= request.form['people'].split(', ')
            people.remove(people[0])
            with open('json/chat/chat.json') as file:
                dict1 = json.load(file)
                for counter in range(0, int(request.form['num'])):
                    dict1[request.form['chat']]['people'].append(people[counter])
                with open('json/chat/chat.json', 'w') as file888:
                    json.dump(dict1, file888)
                return redirect(url_for('chat__chat_cookies'))
    else:
        if session:
            return redirect(url_for('chat__chat_cookies'))
        else:
            return redirect(url_for('chat__home'))

@app.route('/chat/Chat', methods=['GET', 'POST'])
def chat__chat_post():
    if request.method == 'POST':
        show = request.form['show']
        if session:
            if os.path.exists('json/chat/chat.json'):
                with open('json/chat/chat.json') as file:
                    chat_dict = json.load(file)
                    user_list = []
                    big_list = {}
                    counter = 0
                    people = []
                    text = []
                    for groups in chat_dict.keys():
                        if session['uname'] in chat_dict[groups]['people']:
                            people.append({groups : chat_dict[groups]['people']})
                            string = 'message{}'.format(counter)
                            big_list.update({"text{}".format(counter + 1) : chat_dict[groups]['chat']})
                            user_list.append(groups)
                            text.append("text{}".format(counter + 1))
                        counter += 1
                    stream=big_list
                    #return stream
                    ping = []

                    for elm in user_list:
                        ping.append(elm.replace(' ', '_'))
                        show2 = show.replace(' ', '_')
                    return render_template('/chat/chat.html', name=session['uname'], chats_encode=ping, chats=user_list, stream=stream, length=len(user_list), people=people, text=text, show=show2, dh0d='a')

#POLL###########################################################################P####################################################################################################################################################################P
#POLL###########################################################################O####################################################################################################################################################################O
#POLL###########################################################################L####################################################################################################################################################################L
#POLL###########################################################################L####################################################################################################################################################################L

@app.route('/poll')
def poll__log():
    if session:
        return redirect(url_for('poll__home_cookies'))
    else:
        return render_template('/poll/home5.html', color='#34c5f7', color2='#0011FF')


#sends you to the create page where you can create a poll
@app.route('/poll/create', methods=['GET', 'POST'])
def poll__create():
    #return session
    if request.method == 'POST':
        return render_template('/poll/create.html', creator=session['uname'], color='#34c5f7', color2='#0011FF')
    else:
        return render_template('/poll/create.html', creator=session['uname'], color='#34c5f7', color2='#0011FF')

#gets all the information from the create page and makes a website for the user to access
@app.route('/poll/done', methods=['GET', 'POST'])
def poll__done():
    if request.method == 'POST':
        if len(request.form['please'].split(' ')) > 1:
            flash('poll code has an extra space')
            return redirect(url_for('poll__create'))
        if os.path.exists('json/poll/passwords.json'):
            with open('json/poll/passwords.json') as psw:
                psws = json.load(psw)
                if request.form['title'] in psws.keys():
                    flash('That Poll Title was already used')
                    return redirect(url_for('poll__create'))
        poll_dict = {}
        if os.path.exists('json/poll/stats.json'):
            with open('json/poll/stats.json') as pollsss:
                poll_dict = json.load(pollsss)
                title = request.form['title']
                a_dict = {}
                for counter in range(0, int(request.form['q_num'])):
                    inner_dict = {}
                    for questions in range(0, int(request.form['num{}'.format(counter + 1)])):
                        inner_dict.update({request.form['o{}q{}'.format(questions + 1, counter + 1)] : 0})
                    a_dict.update({'Question_{}'.format(counter + 1) : inner_dict})
                poll_dict[title] = a_dict
                with open('json/poll/stats.json', 'w') as poll_json:
                    json.dump(poll_dict, poll_json)
        else:
            poll_dict = {}
            title = request.form['title']
            a_dict = {}
            for counter in range(0, int(request.form['q_num'])):
                inner_dict = {}
                for questions in range(0, int(request.form['num{}'.format(counter + 1)])):
                    inner_dict.update({request.form['o{}q{}'.format(questions + 1, counter + 1)] : 0})
                a_dict.update({'Question_{}'.format(counter + 1) : inner_dict})
            poll_dict[title] = a_dict
            with open('json/poll/stats.json', 'w') as poll_json:
                json.dump(poll_dict, poll_json)
        #psw
        if os.path.exists('json/poll/passwords.json'):
            passwords_dict = {}
            with open('json/poll/passwords.json') as passwords_json:
                passwords_dict = json.load(passwords_json)
                listy = []
                for counter in range(0, int(request.form['q_num'])):
                    listy.append(request.form['question{}'.format(counter + 1 )])
                passwords_dict[request.form['title']] = {
                    'password' : request.form['please'],
                    request.form['please'] : request.form['title'],
                    'type' : 'private',
                    'creator' : request.form['ucreater'],
                    'visits' : 0,
                    'question' : listy,
                    'takers' : []
                }
            with open('json/poll/passwords.json', 'w') as password_json:
                json.dump(passwords_dict, password_json)
        else:
            password_dict = {}
            listy = []
            for counter in range(0, int(request.form['q_num'])):
                listy.append(request.form['question{}'.format(counter + 1 )])
            password_dict[request.form['title']] = {
                'password' : request.form['please'],
                request.form['please'] : request.form['title'],
                'type' : 'private',
                'creator' : request.form['ucreater'],
                'visits' : 0,
                'question' : listy,
                'takers' : []
            }
            with open('json/poll/passwords.json', 'w') as psw:
                json.dump(password_dict, psw)

        users = {}
        with open('json/poll/users.json') as user:
            users = json.load(user)
            creeter = request.form['ucreater']
            users[creeter]['polls'].append(request.form['title'])
            with open('json/poll/users.json', 'w') as userspa:
                json.dump(users, userspa)

        #radio
        q_html = ''
        inner_html = ''
        for counter in range(0, int(request.form['q_num'])):
            for question in range(0, int(request.form['num{}'.format(counter + 1)])):
                inner_html = inner_html + "<label class='container'>" + request.form['o{}q{}'.format(question + 1, counter + 1)] + "<input type='radio' name='" + 'radio{}'.format(counter + 1) + "' value='" + request.form['o{}q{}'.format(question + 1, counter + 1)]  + "' required><span class='checkmark'></span></label><br>"
            q_html = q_html + "<br><input style='display:none' name='shub' value='" + request.form['q_num'] + "'><div class='question'<br><label for='" + 'radio{}'.format(counter + 1) + "'><h2>" + request.form['question{}'.format(counter + 1)] + "</h2></label><br>" + inner_html + "</div>"
            inner_html = ''
        pre_html = "<!DOCTYPE html><html lang='en' dir='ltr'><head><meta charset='utf-8'><link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css'><title>" + request.form['title'] + "</title><style>.container {display: block;position: relative;padding-left: 35px;margin-bottom: 12px;cursor: pointer;font-size: 22px;-webkit-user-select: none;-moz-user-select: none;-ms-user-select: none;user-select: none;}.container input {position: absolute;opacity: 0;cursor: pointer;}.checkmark {position: absolute;top: 0;left: 0;height: 25px;width: 25px;background-color: #eee;border-radius: 50%;}.container:hover input ~ .checkmark {background-color: #ccc;}.container input:checked ~ .checkmark {background-color: #2196F3;}.checkmark:after {content: "";position: absolute;display: none;}.container input:checked ~ .checkmark:after {display: block;}.container .checkmark:after {top: 9px;left: 9px;width: 8px;height: 8px;border-radius: 50%;background: white;} body {background: #34c5f7;font-family: sans-serif;}.question {border-radius: 8px;background: white;padding-left: 25%;padding-right: 25%;padding:3%;} .bob, input[type='radio'] {font-size:30px} body {background:{{ color }}}</style></head><body><br><a style='background:{{ color2 }};padding-top:35px;padding-left: 7px;padding-right: 7px;padding-bottom:7px;border-radius:20px;border: 2px solid black' id='home' href='{{ url_for('poll__home_cookies') }}'><i class='fa fa-home' style='color:white;font-size:50px' style='color:black;font-size:30px'></i></a><br><br><br><div class='question'><br><h4>Share this link with your friends : <a href='http://nikhilodeon.live/poll/poll/" + request.form['please'] + "'>http://nikhilodeon.live/poll/poll/" + request.form['please'] + "</a></h4><br><h4>Poll Title : " + request.form['title'] +"</h4><br><h4>Poll Password : " + request.form['please'] + "</h4><br></div><br><h1>This is how your Poll will look:</h1><br><div class='question'><form action='{{ url_for('poll__done') }}' method='post'><br><h1>" + request.form['title'] + "</h1><br></div><br><div class='question'><br><label for='name'>Your Name:</label><br><input style='font-size:20px' type='text' name='name' placeholder='Name'><br></div><br>" + q_html + "<br></div><br><div class='question'><br><input style='display:none' value='" + request.form['title'] + "' name='code'><button type=\"button\" style='padding:3px;background:#0011FF;border: 2px solid black;color: white'>Submit</button><br></div></form></body></html>"

        html = "<!DOCTYPE html><html lang='en' dir='ltr'><head><meta charset='utf-8'><link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css'><title>" + request.form['title'] + "</title><link rel='shortcut icon' href='{{url_for('static', filename='sike.ico')}}'><style>.container {display: block;position: relative;padding-left: 35px;margin-bottom: 12px;cursor: pointer;font-size: 22px;-webkit-user-select: none;-moz-user-select: none;-ms-user-select: none;user-select: none;}.container input {position: absolute;opacity: 0;cursor: pointer;}.checkmark {position: absolute;top: 0;left: 0;height: 25px;width: 25px;background-color: #eee;border-radius: 50%;}.container:hover input ~ .checkmark {background-color: #ccc;}.container input:checked ~ .checkmark {background-color: #2196F3;}.checkmark:after {content: "";position: absolute;display: none;}.container input:checked ~ .checkmark:after {display: block;}.container .checkmark:after {top: 9px;left: 9px;width: 8px;height: 8px;border-radius: 50%;background: white;} body {background: #34c5f7;font-family: sans-serif;}.question {border-radius: 8px;background: white;padding-left: 25%;padding-right: 25%;padding:3%;} .bob, input[type='radio'] {font-size:30px} body {background:{{ color }}}</style></head><body><form action='{{ url_for('poll__thanks') }}' method='post'><br><a style='background:{{ color2 }};padding-top:35px;padding-left: 7px;padding-right: 7px;padding-bottom:7px;border-radius:20px;border: 2px solid black' id='home' href='{{ url_for('poll__home_cookies') }}'><i class='fa fa-home' style='color:white;font-size:50px' style='color:black;font-size:30px'></i></a><br><div class='question'><br><h1>" + request.form['title'] + "</h1><br></div><br><input style='display:none' name='name' value='{{ cookie }}'>" + q_html + "<br></div><br><div class='question'><br><input style='display:none' value='" + request.form['title'] + "' name='code'><button type=\"submit\" style='padding:3px;background:#0011FF;border: 2px solid black;color: white'>Submit</button><br></div></form></body></html>"
        html2 = "<!DOCTYPE html><html lang='en' dir='ltr'><head><meta charset='utf-8'><link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css'><title>" + request.form['title'] + "</title><link rel='shortcut icon' href='{{url_for('static', filename='sike.ico')}}'><style>.container {display: block;position: relative;padding-left: 35px;margin-bottom: 12px;cursor: pointer;font-size: 22px;-webkit-user-select: none;-moz-user-select: none;-ms-user-select: none;user-select: none;}.container input {position: absolute;opacity: 0;cursor: pointer;}.checkmark {position: absolute;top: 0;left: 0;height: 25px;width: 25px;background-color: #eee;border-radius: 50%;}.container:hover input ~ .checkmark {background-color: #ccc;}.container input:checked ~ .checkmark {background-color: #2196F3;}.checkmark:after {content: "";position: absolute;display: none;}.container input:checked ~ .checkmark:after {display: block;}.container .checkmark:after {top: 9px;left: 9px;width: 8px;height: 8px;border-radius: 50%;background: white;} body {background: #34c5f7;font-family: sans-serif;}.question {border-radius: 8px;background: white;padding-left: 25%;padding-right: 25%;padding:3%;} .bob, input[type='radio'] {font-size:30px} body {background:{{ color }}}</style></head><body><br><br><div class='question'><form action='{{ url_for('poll_thanks') }}' method='post'><br><a style='background:{{ color2 }};padding-top:35px;padding-left: 7px;padding-right: 7px;padding-bottom:7px;border-radius:20px;border: 2px solid black' id='home' href='{{ url_for('poll__home_cookies') }}'><i class='fa fa-home' style='color:white;font-size:50px' style='color:black;font-size:30px'></i></a><br><h1>" + request.form['title'] + "</h1><br></div><br><div class='question'><br><label for='name'>Your Name:</label><br><input style='font-size:20px' type='text' name='name' placeholder='Name'><br></div><br>" + q_html + "<br></div><br><div class='question'><br><input style='display:none' value='" + request.form['title'] + "' name='code'><button type=\"submit\" style='padding:3px;background:#0011FF;border: 2px solid black;color: white'>Submit</button><br></div></form></body></html>"
        with open("Templates/poll/user/{}.html".format(request.form['please']), "w") as poll_web:
            poll_web.write(html)
        with open("Templates/poll/done/{}.html".format(request.form['please']), 'w') as pre_poll_web:
            pre_poll_web.write(pre_html)
        with open("Templates/poll/done/{}2.html".format(request.form['please']), 'w') as poll_web2:
            poll_web2.write(html2)

        return render_template('/poll/done/' + request.form['please'] + '.html', color='#34c5f7', color2='#0011FF')
    else:
        return redirect(url_for('poll__home_cookies'))
#if the string after '/poll/' is in the json-file passwords.json it will give the page with coensides with the password
@app.route('/poll/poll/<string:code>')
def poll__dopoll(code):
    if os.path.exists('json/poll/passwords.json'):
        passwords = {}
        with open('json/poll/passwords.json') as password:
            passwords = json.load(password)
            for key in passwords.keys():
                if passwords[key]['password'] == code:
                    if session:
                        return render_template('/poll/user/' + code + '.html', code=code, color='#34c5f7', color2='#0011FF', cookie=session['uname'])
                    else:
                        return render_template('/poll/done/' + code + '2.html', code=code, color='#34c5f7', color2='#0011FF')
            flash('Poll not found')
            return redirect(url_for('poll__home'))

@app.route('/poll/thanks', methods=['GET', 'POST'])
def poll__thanks():
    if request.method == 'POST':

        with open('json/poll/passwords.json') as psw_file:
            psw_dict = json.load(psw_file)
            if request.form['name'] in psw_dict[request.form['code']]['takers']:
                flash('Input Not Submitted! You Already Did the poll')
                return render_template('/poll/thanks.html', uname=request.form['name'], psw=request.form['code'], color='#34c5f7', color2='#0011FF')
            else:
                code = request.form['code']
                name = request.form['name']
                count = request.form['shub']

                with open('json/poll/passwords.json') as psw_file:
                    psw_dict = json.load(psw_file)
                    psw_dict[code]['takers'].append(name)
                    psw_dict[code]['visits'] = len(psw_dict[code]['takers'])
                    with open('json/poll/passwords.json', 'w') as psw_file2:
                        json.dump(psw_dict, psw_file2)
                #stat.json update stats
                listA = []
                for counter in range(0, int(count)):
                    listA.append(request.form['radio{}'.format(counter + 1)])
                with open('json/poll/stats.json') as stat_file:
                    stat_dict = json.load(stat_file)
                    a = 0
                    for elm in listA:
                        stat_dict[code]['Question_{}'.format(a + 1)][elm] += 1
                        a += 1
                    with open('json/poll/stats.json', 'w') as stat_file2:
                        json.dump(stat_dict, stat_file2)
                #render_template
                return render_template('/poll/thanks.html', uname=name, psw=code, color='#34c5f7', color2='#0011FF')
    else:
        return redirect(url_for('poll__home_cookies'))


@app.route('/poll/stats_from_poll', methods=['POST', 'GET'])
def poll__stats_from_poll():
    if request.method == 'POST':
        poll_name = request.form['psw']
        stats_dict = {}
        with open('json/poll/stats.json') as stat:
            stats_dict = json.load(stat)
            poll_dict = stats_dict[poll_name]
            if request.form['stat_type'] == 'column':
                with open('json/poll/passwords.json') as psw_file:
                    psw_dict = json.load(psw_file)
                    q_list = psw_dict[poll_name]['question']
                    psw = psw_dict[poll_name]['password']
                    listA = []
                    for counter in range(0, len(q_list)):
                        listA.append(counter)
                        return render_template('/poll/column2.html', result_dict=poll_dict, q_list=q_list, color='#34c5f7', color2='#0011FF', num_list=listA, clap=poll_name, psw=psw)
            else:
                with open('json/poll/passwords.json') as psw_file:
                    psw_dict = json.load(psw_file)
                    q_list = psw_dict[poll_name]['question']
                    psw = psw_dict[poll_name]['password']
                    listA = []
                    for counter in range(0, len(q_list)):
                        listA.append(counter)
                    return render_template('/poll/pie2.html', result_dict=poll_dict, q_list=q_list, color='#34c5f7', color2='#0011FF', num_list=listA, clap=poll_name, psw=psw)
    else:
        return redirect(url_for('poll__home_cookies'))

@app.route('/poll/stats_from_home', methods=['GET', 'POST'])
def poll__stats_from_home():
    if request.method == 'POST':
        poll_name = request.form['poll_name']
        stat_dict = {}
        with open('json/poll/stats.json') as stat:
            stat_dict = json.load(stat)
            if poll_name in stat_dict.keys():
                poll_dict = stat_dict[poll_name]
                if request.form['type'] == 'pie':
                    with open('json/poll/passwords.json') as psw_file:
                        psw_dict = json.load(psw_file)
                        q_list = psw_dict[poll_name]['question']
                        psw = psw_dict[poll_name]['password']
                        listA = []
                        for counter in range(0, len(q_list)):
                            listA.append(counter)
                        return render_template('/poll/pie.html', result_dict=poll_dict, q_list=q_list, color='#34c5f7', color2='#0011FF', num_list=listA, clap=poll_name, psw=psw, name=poll_name)
                else:
                    with open('json/poll/passwords.json') as psw_file:
                        psw_dict = json.load(psw_file)
                        q_list = psw_dict[poll_name]['question']
                        listA = []
                        psw = psw_dict[poll_name]['password']
                        for counter in range(0, len(q_list)):
                            listA.append(counter)
                        return render_template('/poll/column.html', result_dict=poll_dict, q_list=q_list, color='#34c5f7', color2='#0011FF', num_list=listA, clap=poll_name, psw=psw)
            else:
                return redirect(url_for('poll__home_cookies'))

@app.route('/poll/home-cookies')
def poll__home_cookies():
    #return render_template('/poll/home2.html', username=uname, img=c, poll_list=poll_list)
    #return session
    if session:
        uname = session['uname']
        psw = session['psw']
        user_dict = {}
        if os.path.exists('json/poll/users.json'):
            with open('json/poll/users.json') as user_file:
                user_dict = json.load(user_file)
                image = user_dict[uname]['gender-img']
                poll_list = user_dict[uname]['polls']
                images = image.split('=')
                if len(poll_list) > 0:
                    return render_template('/poll/home2.html', username=uname, poll_list=poll_list, img=images[0], color='#34c5f7', color2='#0011FF')
                else:
                    try:
                        return render_template('/poll/home.html', username=uname, img=images[0], color='#34c5f7', color2='#0011FF')
                    except:
                        return render_template('/poll/home.html', username=uname, img=images[0], color='#34c5f7', color2='#0011FF')

        else:
            session.clear()
            return redirect(url_for('poll__log'))
    else:
            return redirect(url_for('poll__log'))


@app.route('/poll/poll_code', methods=['GET', 'POST'])
def poll__poll_code():
    if request.method == 'POST':
        poll_name = request.form['name'].casefold()
        poll_psw = request.form['code'].casefold()
        psw_dict = {}
        with open('json/poll/passwords.json') as psw_file:
            psw_dict = json.load(psw_file)
            if poll_name in psw_dict.keys():
                if psw_dict[poll_name]["password"] == poll_psw:
                    return render_template('/poll/user/' + poll_psw + '.html', color='#34c5f7', color2='#0011FF', cookie=session['uname'])
                else:
                    flash('Poll Password is Incorrect')
                    return redirect(url_for('poll__home_cookies'))
            else:
                flash('Poll Name is Incorrect')
                return redirect(url_for('poll__home_cookies'))

@app.route('/poll/sign-out', methods=['GET', 'POST'])
def poll__sign_out():
    if request.method == 'POST':
        session.clear()
        return redirect(url_for('poll__log'))


@app.route('/poll/public-polls', methods=['GET', 'POST'])
def poll__public():
    if os.path.exists('json/poll/passwords.json'):
        with open('json/poll/passwords.json') as psw_file:
            psw_dict = json.load(psw_file)
            num_list = []
            random_list = []
            for poll in psw_dict.keys():
                if psw_dict[poll]['type'] == 'public':
                    poll_views = psw_dict[poll]['visits']
                    num_list.append({'number' : poll_views, 'name' : poll})
                    random_list.append(poll)
            for O_index in range(0, len(num_list) - 1):
                for I_index in range(O_index + 1, len(num_list)):
                    if num_list[O_index]['number'] > num_list[I_index]['number']:
                        swap = num_list[I_index]
                        num_list[I_index] = num_list[O_index]
                        num_list[O_index] = swap
            new_list = []
            new_psw_list = []
            try:
                for counter in range(0, 15):
                    elm = num_list[counter]['name']
                    new_list.append(elm)
                    elm2 = psw_dict[elm]['password']
                    new_psw_list.append(elm2)

                    return render_template('/poll/public.html', polls=new_list, psws=new_psw_list, color='#34c5f7', color2='#0011FF')
            except:
                lisd = []
                for counter in psw_dict.keys():
                    lisd.append(psw_dict[counter]['password'])

                    return render_template('/poll/public.html', polls=random_list, psws=lisd, color='#34c5f7', color2='#0011FF')
    else:
        if session:
            return render_template('/poll/public.html', color='#34c5f7', color2='#0011FF')
        else:
            flash('No Polls Yet')
            return render_template('/poll/public.html', color='#34c5f7', color2='#0011FF')

@app.route('/poll/search', methods=['GET', 'POST'])
def poll__search():
    if request.method == 'POST':
        search = request.form['search']
        if os.path.exists('json/poll/passwords.json'):
            psw_dict = {}
            with open('json/poll/passwords.json') as psw_file:
                psw_dict = json.load(psw_file)
                query_list = []
                query_psw_list = []
                for key in psw_dict.keys():
                    if psw_dict[key]['type'] == 'public':
                        key_list = key.split(' ')
                        search_list = search.split(' ')
                        for search_elm in search_list:
                            for key_elm in key_list:
                                if search_elm.casefold() == key_elm.casefold():
                                    query_list.append(key)
                                    query_psw_list.append(psw_dict[key]['password'])
                if len(query_list) > 0:
                    return render_template('/poll/search.html', pws=query_psw_list, names=query_list, search=search, color='#34c5f7', color2='#0011FF')
                else:
                    flash('No results')
                    return redirect(url_for('poll__public'))
        else:
            flash('No results')
            return redirect(url_for('poll__public'))
    else:
        return redirect(url_for('poll__home_cookies'))




@app.route('/poll/active', methods=['POST'])
def poll__active():
    if request.method == 'POST':
        poll = request.form['ekam']
        with open('json/poll/users.json') as target2:
            json_file2 = json.load(target2)
            json_file2[session['uname']]['polls'].remove(poll)
            with open('json/poll/users.json', 'w') as guddi2:
                json.dump(json_file2, guddi2)


        with open('json/poll/passwords.json') as target:
            json_file = json.load(target)
            json_file[poll]['type'] = "public"
            json_file[poll]['creator'] = 'imagine_imagine_imagine_imagine_imagine_imagine'
            with open('json/poll/passwords.json', 'w') as guddi:
                json.dump(json_file, guddi)
                ################################################################
                if session:
                    uname = session['uname']
                    psw = session['psw']
                    user_dict = {}
                    if os.path.exists('json/poll/users.json'):
                        with open('json/poll/users.json') as user_file:
                            user_dict = json.load(user_file)
                            image = user_dict[uname]['gender-img']
                            poll_list = user_dict[uname]['polls']
                            images = image.split('=')
                            if len(poll_list) > 0:
                                return render_template('/poll/home2.html', username=uname, poll_list=poll_list, img=images[0], color='#34c5f7', color2='#0011FF')
                            else:
                                return render_template('/poll/home.html', username=uname, img=images[0], color='#34c5f7', color2='#0011FF')



@app.route('/poll/deactive', methods=['POST'])
def poll__deactive():
    if request.method == 'POST':
        poll = request.form['ekam']
        with open('json/poll/passwords.json') as target:
            json_file = json.load(target)
            json_file[poll]['type'] == 'private'
            json_file[poll]['creator'] = session['uname']
            with open('json/poll/passwords.json', 'w') as guddi:
                json.dump(json_file, guddi)
                ################################################################
                with open('json/poll/stats.json') as stats:
                    stats_json = json.load(stats)
                    for elm in stats_json[poll].keys():
                        for elm2 in stats_json[poll][elm]:
                            stats_json[poll][elm][elm2] = 0
                ################################################################
                poll_name = poll
                stat_dict = json_file
                if poll_name in stat_dict.keys():
                    poll_dict = stat_dict[poll_name]
                    with open('json/poll/passwords.json') as psw_ffile:
                        psw2_dict = json.load(psw_ffile)
                        q_list = psw2_dict[poll_name]['question']
                        listA = []
                        for counter in range(0, len(q_list)):
                            listA.append(counter)
                        return render_template('/poll/pie.html', result_dict=poll_dict, q_list=q_list, color='#34c5f7', color2='#0011FF', num_list=listA, clap=poll_name)

#SPELL###########################################################################S####################################################################################################################################################################S
#SPELL###########################################################################P####################################################################################################################################################################P
#SPELL###########################################################################E####################################################################################################################################################################E
#SPELL###########################################################################L####################################################################################################################################################################L
#SPELL###########################################################################L####################################################################################################################################################################L

@app.route('/spell')
def spell__home():
    if session:
        with open('json/spell/users.json') as file:
            dict1 = json.load(file)
            level = dict1[session['uname']]['level']
            img = dict1[session['uname']]['gender-img']
            percent = dict1[session['uname']]['avg-percent']
            if len(dict1[session['uname']]['wrong']) > 1:
                a = 'show'
                return render_template('/spell/home_cookies.html', level=level, name=session['uname'], img=img, p=round(percent), a=a, twenty=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
            else:
                a = 'hide'
                return render_template('/spell/home_cookies.html', level=level, name=session['uname'], img=img, p=round(percent), a=a, twenty=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    else:
        return render_template('/spell/home_anticookies.html', a='false', message="")



@app.route('/spell/quiz', methods=['POST', 'GET'])
def spell__quiz():
    if request.method == 'POST':
        if request.form['title'] == 'General Test':
            with open('json/spell/words.json') as file:
                words = json.load(file)
                list1 = []
                list2 = []
                num = 0
                for elm in words['word list']:
                    for key in elm.keys():
                        if words['word list'][num][key] == 0.5:
                            list1.append(key)
                    num += 1
                if len(list1) < 1:
                    with open('json/spell/users.json') as file2:
                        users = json.load(file2)
                        num2 = 0
                        for elm2 in words['word list']:
                            for key2 in elm2.keys():
                                if words['word list'][num2][key2] == users[session['uname']]['level']:
                                    list2.append(key2)
                            num2 += 1
                    real2 = []
                    try:
                        for counter2 in range(0, 10):
                            real2.append(list2[counter2])
                    except:
                        for elm4 in list2:
                            real2.append(elm4)
                    return render_template('/spell/spell2.html', words=real2, end_num=len(real2), froms="normal", title='The Spelling Test')
                else:
                    real1 = []
                    try:
                        for counter in range(0, 10):
                            real1.append(list1[counter])
                    except:
                        for elm3 in list1:
                            real1.append(elm3)
                            return render_template('/spell/spell2.html', words=real1, end_num=len(real1), froms="normal", title='The Spelling Test')
        else:
            #MHMS-7: Unit 3
            split = request.form['title'].split(': Unit ')
            unit = split[1]
            with open('json/spell/mhms-7.json') as json_file:
                word_dict = json.load(json_file)
                da_words = word_dict['Unit_{}'.format(unit)]
                return render_template('/spell/spell2.html', words=da_words, end_num=len(da_words), froms="mhms", title='MHMS-7: Unit ' + unit + ' Spelling Test')

    else:
        return redirect(url_for('spell__home'))


@app.route('/spell/done', methods=['GET', 'POST'])
def spell__done():
    if request.method == "POST":
        correct = []
        wrong = []
        for counter in range(0, int(request.form['correct_num'])):
            correct.append(request.form['c{}'.format(counter + 1)])
        for counter2 in range(0, int(request.form['wrong_num'])):
            wrong.append(request.form['i{}'.format(counter2 + 1)])
        with open('json/spell/words.json') as file:
            words = json.load(file)
            if request.form['from'] == "normal":
                for elm in correct:
                    for counter in range(0, 500):
                        for key in words['word list'][counter].keys():
                            if key == elm:
                                if words['word list'][counter][key] != 0:
                                    if words['word list'][counter][key] == 0.5:
                                        words['word list'][counter][key] -= 0.5
                                    else:
                                        words['word list'][counter][key] -= 1
            elif request.form['from'] == "impove":
                slist = []
                for counter66 in range(0, 500):
                    for keys66 in words['word list'][counter66].keys():
                        slist.append(keys66)
                for elm77 in correct:
                    with open('json/spell/users.json') as file99:
                        dict99 = json.load(file99)
                        dict99[session['uname']]['wrong'].remove(elm77)
                        with open('json/spell/users.json', 'w') as file111:
                            json.dump(dict99, file111 )

            if request.form['from'] == "normal" or request.form['from'] == "improve":
                for elm2 in wrong:
                    for counter2 in range(0, 500):
                        for key2 in words['word list'][counter2].keys():
                            if key2 == elm2:
                                if words['word list'][counter2][key2] != 12:
                                    if words['word list'][counter2][key2] == 0.5:
                                        words['word list'][counter2][key2] += 0.5
                                    else:
                                        words['word list'][counter2][key2] += 1


            with open('json/spell/words.json', 'w') as file2:
                json.dump(words, file2)
        with open('json/spell/users.json') as file3:
            dict1 = json.load(file3)
            img = dict1[session['uname']]['gender-img']
            percent = (len(correct) / (len(correct) + len(wrong))) * 100
            c_percent = dict1[session['uname']]['avg-percent']
            avg_percent = (percent + c_percent) / 2
            dict1[session['uname']]['avg-percent'] = avg_percent
            num = int(request.form['correct_num']) + int(request.form['wrong_num'])
            for elm2 in wrong:
                dict1[session['uname']]['wrong'].append(elm2)
            if avg_percent <= 50:
                dict1[session['uname']]['level'] -= 1
                levelz = dict1[session['uname']]['level']
                with open('json/spell/users.json', 'w') as file444:
                    json.dump(dict1, file444)
                if len(wrong) == 0:
                    return render_template('/spell/results.html', correct=len(correct), old_percent=round(c_percent), new_percent=round(avg_percent), currant_percent=round(percent), wrong=wrong, q_num=num, name=session['uname'], level=levelz, passs="fail", r_len=len(wrong), jk='yes', img=img)
                else:
                    return render_template('/spell/results.html', correct=len(correct), old_percent=round(c_percent), new_percent=round(avg_percent), currant_percent=round(percent), wrong=wrong, q_num=num, name=session['uname'], level=levelz, passs="fail", r_len=len(wrong), jk='no', img=img)
            with open('json/spell/users.json', 'w') as file4444:
                json.dump(dict1, file4444)
                if len(wrong) == 0:
                    return render_template('/spell/results.html', correct=len(correct), old_percent=round(c_percent), new_percent=round(avg_percent), currant_percent=round(percent), wrong=wrong, q_num=num, name=session['uname'], level=dict1[session['uname']]['level'], passs="good", r_len=len(wrong), jk='yes', img=img)
                else:
                    return render_template('/spell/results.html', correct=len(correct), old_percent=round(c_percent), new_percent=round(avg_percent), currant_percent=round(percent), wrong=wrong, q_num=num, name=session['uname'], level=dict1[session['uname']]['level'], passs="good", r_len=len(wrong), jk='no', img=img)

    else:
        return redirect(url_for('spell__home'))

@app.route('/spell/iquiz', methods=['GET', 'POST'])
def spell__iquiz():
    if request.method == 'POST':
        with open('json/spell/users.json') as file:
            dict1 = json.load(file)
            list1 = dict1[session['uname']]['wrong']
            return render_template('/spell/spell2.html', words=list1, end_num=len(list1), froms="improve", title="Improvement Test")
    else:
        return redirect(url_for('spell__home'))

@app.route('/spell/delete', methods=['GET', 'POST'])
def spell__delete():
    if request.method == 'POST':
        with open('json/spell/users.json') as file:
            users = json.load(file)
            list2 = request.form['input'].split(', ')
            list2.remove(list2[-1])
            for elm in list2:
                users[session['uname']]['custom'].remove(elm)
            with open('json/spell/users.json', 'w') as file2:
                json.dump(users, file2)
                return redirect(url_for('spell__custom'))

@app.route('/spell/add_custom', methods=['GET', 'POST'])
def spell__add():
    if request.method == 'POST':
        with open('json/spell/users.json') as file:
            users = json.load(file)
            users[session['uname']]['custom'].append(request.form['word'])
            with open('json/spell/users.json', 'w') as file2:
                json.dump(users, file2)
                return redirect(url_for('spell__custom'))

@app.route('/spell/custom', methods=['GET', 'POST'])
def spell__custom():
    with open('json/spell/users.json') as file:
        users = json.load(file)
        return render_template('/spell/custom.html', words=users[session['uname']]['custom'], len=len(users[session['uname']]['custom']))

@app.route('/spell/cquiz', methods=['POST', 'GET'])
def spell__cquiz():
    if request.method == 'POST':
        with open('json/spell/users.json') as file:
            dict1 = json.load(file)
            list1 = dict1[session['uname']]['custom']
            return render_template('/spell/spell2.html', words=list1, end_num=len(list1), froms="custom", title="Your Custom Test")
    else:
        return redirect(url_for('spell__home'))



@app.route('/fb')
def fb():
    return render_template('fb.html')

@app.route('/feedback', methods=['POST'])
def feedback():
    if request.method == 'POST':
        fb = request.form['fb']
        with open('json/spell/feedback.json') as target:
            dict = json.load(target)
            dict['Feedback'].append(fb)
            with open('json/spell/feedback.json', 'w') as target2:
                json.dump(dict, target2)
            return render_template('fb2.html')

@app.route('/spell/lub')
def spell__lub():
    return "<h1 style='color:blue; font-family:monospace; font-size:100px;'>air bnb 808 guddy gladdy gloogi glug bob glub niyaw lub<br>By: Nihar</h1>"

@app.errorhandler(404)
def spell__page_not_found(error):

    if os.path.exists('json/spell/user.json'):
        if session:
            return render_template('/spell/error.html', error="Page Not Found", error_type="Error 404", issue="The page you are looking for does not exist", ttd="Make sure the URL for this page is correct", name=session['uname']), 404
        else:
            return render_template("error.html", error="Page Not Found", error_type="Error 404", issue="The page you are looking for does not exist", ttd="Make sure the URL for this page is correct", name="User"), 404
    else:
        return render_template('/spell/error.html', error="Page Not Found", error_type="Error 404", issue="The page you are looking for does not exist", ttd="Make sure the URL for this page is correct", name='User'), 404


@app.errorhandler(405)
def spell__method_not_allowed(error):
    if os.path.exists('json/spell/user.json'):
        if session:
            return render_template('/spell/error.html', error="That Method is not alowed", error_type="Error 405", issue="You tried to come to the webpage using the wrong way", ttd="Try coming from the home page instead of typing the URL"), 405
        else:
            return render_template('/spell/error.html', error="That Method is not alowed", error_type="Error 405", issue="You tried to come to the webpage using the wrong way", ttd="Try coming from the home page instead of typing the URL"), 405
    else:
        return render_template('/spell/error.html', error="That Method is not allowed", error_type="Error 405", issue="You tried to come to the webpage using the wrong way", ttd="Try coming from the home page instead of typing the URL"), 405

@app.errorhandler(500)
def spell__internal_server_error(error):
    if os.path.exists('json/spell/user.json'):
        if session:
            return render_template('/spell/error.html', error="There was an error on our side", error_type="Error 500", issue="There was an error on our side, We appologize", ttd="Going back to the home page and clear your chat_cookies", name=session['uname']), 500
        else:
            return render_template('/spell/error.html', error="There was an error on our side", error_type="Error 500", issue="There was an error on our side, We appologize", ttd="Going back to the home page and clear your chat_cookies", name=User), 500
    else:
        return render_template('/spell/error.html', error="There was an error on our side", error_type="Error 500", issue="There was an error on our side, We appologize", ttd="Going back to the home page and clear your chat_cookies", name=User), 500

#-*- coding:utf-8 -*-
from flask import Flask

app = Flask(__name__)

##############
#Flask 라우팅#
##############

# @app.route()를 통해 URL패턴과 POST Method를 정의하고
# 바로 하단의 함수에서 URL 패턴 매칭되는 Action을 처리

# app.debug는 개발의 편의를 위해 존재하며, True값일 경우 코드를 변경하면
# 자동으로 서버가 재실행된다.
# 웹상에서 파이썬 코드를 수행할 수 있게 되므로, 운영환경에서는 주의해야함

# 외부에서도 접근을 가능하게 하려면 app.run(host='0.0.0.0')로
# 서버 실행부를 변경해야 한다.

@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/main')
def main():
    return 'Main Page'

# <>로 URL패턴을 변수로 처리 가능
# <자료형: 변수명>형식으로 URL패턴 검증 가능 int:는 정수만 입력가능을 의미

@app.route('/routing/<username>')
def showUserProfile(username):
    return 'USER : %s' % username

@app.route('/routing/id<int:userId>')
def showUserProfileById(userId):
    return 'USER ID : %d' % userId

############
#Flask 로깅#
############


# Flask자체 app.logger 항목을 통해 로깅이 가능하다

@app.route('/logging/<username>')
def LoggingUserProfile(username):
    app.logger.debug('RETRIEVE DATA - USER ID : %s' % username)
    app.logger.debug('RETRIEVE DATA - Check Complete')
    app.logger.warn('RETRIEVE DATA - Warning... User Not Found.')
    app.logger.error('RETRIEVE DATA - ERR! User unauthenification.')
    return 'USER : %s' % username


##########################
#Flask 로그인 및 세션 생성#
##########################

@app.route('/account/login', methods=['POST'])
def login():
    if request.method == 'POST':
        userId = request.form['id']
        wp = request.form['wp']

        if len(userId) == 0 or len(wp) == 0:
            return userId+', '+wp+'로그인 정보를 제대로 입력하지 않았습니다.'

            session['logFlag'] = True
            session['userId'] = userId
            return session['userId'] + ' 님 환영합니다.'
        else:
            return '잘못된 접근입니다.'
app.secret_key = 'sample_secret_key'

#@app.rout('/account/login', methods=['POST]) 내부에 methods 항목을 통해 받을 REST Action Type을 지정
# 지정 이외의 Action Type을 사용하면 Flask가 405에러를 출력

#request 모듈에서 POST한 파라미터 값ㅇ르 가져오기 위해서는 request.form['id']와 같이 사용
# request.form['id']로 사용시 id파라미터가 없으면 Flask가 400 에러를 출력

#app.secret_key는 세션 키를 생성하며, 로그인과 같이 세션을 맺는 경우 필수적으로 넣어야 한다.
# 세션 생성시, app.secret_key로 키를 생성하지 않으면 Flask가 500 에러를 출력



##########################
#Flask 로그인 정보 가져오기#
##########################

@app.route('/user', methods=['GET'])
def getUser():

    if session.get('logFlag') != True:
        return '잘못된 접근입니다.'
    
    userId = session ['userId']
    return '[GET][USER] USER ID : {0}'.format(userId)

##########
#로그 아웃#
##########

#예제를 하기 앞서 상단 import을 아래와 같이 추가/수정한다.
# from flask import Flask, request, session, render_template, redirect, url_for

# @app.route('/account/logout', methods=['POST','GET']) 
# def logout(): 
#     session['logFlag'] = False session.pop('userId', None) 
#     return redirect(url_for('main'))

# redirect()를 활용하면, 사용자의 조회 위치를 변경할 수 있다.
# url_for()는 route주소로 이동하는 것이 아닌 정의된 함수를 호출한다. 위 예제에서 main을 호출하는 대상은 main()인 함수이다.
# session.clear()를 사용하면 따로 설정 필요없이 session을 비울 수 있다.

#######################################


##################
#Flask Error 처리#
##################

@app.errorhandler(400)
def uncaughtError(error):
    return '잘못된 사용입니다.'

#app.errorhandler()를 통해 에럴르 Catch 및 처리 할 수 있다.
# abort()를 사용하면 특정 error를 발생 시킬 수 있다. 
# ex) abort(401)은 몰론 abort모듈을 import해야 한다.

#abort 예시

# @app.route('/user', methods=['GET']) 
# def getUser(): 
#     if 'userId' in session: 
#         return '[GET][USER] USER ID : {0}'.format(session['userId']) 
#     else: 
#         abort(400)

#session안에 userId 항목이 없다면, abort를 통해 400에러가 출력되게 한다.

#Flask 응답 처리
@app.errorhandler(404) 
def not_found(error): 
    resp = make_response(render_template('error.html'), 404)
    resp.headers['X-Something'] = 'A value' 
    return resp
#make_response() 함수를 통해 반환되는 Object를 만들고, 이를 처리 가능할 수 있게 된다.

#Flask Redirect처리
#특정 URL Alias 등 Redirect가 필요한데, Post 데이터를 같이 보내어서 Redirect를 하려면,
#url_for() 함수를 사용 시, 상태 코드 값을 같이 보내어야 한다.

@app.route('/login', methods=['POST','GET']) 
def login_direct(): 
    if request.method == 'POST': 
        return redirect(url_for('login'), code=307) 
    else: 
        return redirect(url_for('login'))

#######################################################

if __name__ == '__main__':
    app.run(debug = True)
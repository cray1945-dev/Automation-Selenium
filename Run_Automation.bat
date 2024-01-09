@echo off
pytest --alluredir="C:\MyRobin\Python\app\Assertion\reports" login.py
pytest --alluredir="C:\MyRobin\Python\app\Assertion\reports" registrasi.py
pytest --alluredir="C:\MyRobin\Python\app\Assertion\reports" discussion_post_img.py
pytest --alluredir="C:\MyRobin\Python\app\Assertion\reports" comment.py
pytest --alluredir="C:\MyRobin\Python\app\Assertion\reports" absen.py
pytest --alluredir="C:\MyRobin\Python\app\Assertion\reports" leave_request.py
pytest --alluredir="C:\MyRobin\Python\app\Assertion\reports" leave_double.py
pytest --alluredir="C:\MyRobin\Python\app\Assertion\reports" attendance_request.py

allure serve reports
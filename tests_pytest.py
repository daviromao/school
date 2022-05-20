import os
from dotenv import load_dotenv

import requests

load_dotenv()

class TestCourses:
  headers = {'Authorization': f'Token {os.environ.get("TOKEN_TEST")}'}
  url_base_courses = 'http://localhost:8000/api/v2/courses/'

  def test_get_courses(self):
    response = requests.get(url=self.url_base_courses, headers=self.headers)

    assert response.status_code == 200
  
  def test_get_course(self):
    url = self.url_base_courses + '3/'
    response = requests.get(url=url, headers=self.headers)

    assert response.status_code == 200

  def test_post_course(self):
    new_course = {
      "title": "ruby course 3",
      "url": "http://www.udemy.com/ruby3"
    }

    response = requests.post(url=self.url_base_courses, headers=self.headers, data=new_course)

    assert response.status_code == 201
    assert response.json()['title'] == new_course['title']
  
  def test_put_course(self):
    updated_course = {
      "title": "new ruby course",
      "url": "http://www.udemy.com/newruby"
    }

    url= self.url_base_courses + '2/'

    response = requests.put(url=url, headers=self.headers, data=updated_course)

    assert response.status_code == 200
    assert response.json()['title'] == updated_course['title']

  def test_delete_curse(self):
    url = self.url_base_courses + '8/'
    response = requests.delete(url=url, headers=self.headers)

    assert response.status_code == 204 and len(response.text) == 0

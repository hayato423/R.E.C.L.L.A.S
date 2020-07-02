"""
designer:中村友哉
date:2020.07.02
purpose:授業詳細画面表示
"""

import PySimpleGUI as sg
import sqlite3
class Lecture:

  def __init__(self,lecture_name,teacher_name):
    self.lecture_name = lecture_name
    self.teacher_name = teacher_name
    self.fetch_zoom_url(self.lecture_name)


  def fetch_zoom_url(self,lecture_name):
    try:
      conn = sqlite3.connect('reclass.db')
      cur = conn.cursor()
      SQL = 'select url from zoomURL where lecture_name=?'
      cur.execute(SQL,(lecture_name,))
      execute_resut = cur.fetchone()
      if execute_resut != None:
        self.zoom_url = execute_resut[0]
      else:
        self.zoom_url = ''
    except sqlite3.Error as e:
      sg.popup(e)
    finally:
      conn.close()


  def open(self):
    layout = [
      [sg.Text(self.lecture_name)],
      [sg.Text('担当講師'),sg.Text(self.teacher_name)],
      [sg.Text('zoomURL'),sg.InputText(key = 'zoom_url',default_text=self.zoom_url)],
      #[sg.Text('休講'),sg.Text(self.no_class_days)],
      [sg.Button('OK')],
      [sg.Button('キャンセル')]
    ]
    window = sg.Window(self.lecture_name,layout=layout,size=(200,200))

    while True:
      event ,value = window.read()

      if event == 'OK':
        if len(value['zoom_url']) > 80:
          show_message = 'zoomURLは80字以下にしてください'
          sg.popup(show_message)
        else:
          try:
            conn = sqlite3.connect('reclass.db')
            cur = conn.cursor()
            SQL = 'replace into zoomURL values(?,?)'
            cur.execute(SQL,(self.lecture_name,value['zoom_url']))
            conn.commit()
          except sqlite3.Error:
            sg.popup('データベース保存中にエラーが発生しました')
          finally:
            conn.close()
            self.fetch_zoom_url(self.lecture_name)
            window.close()

      if event == 'キャンセル':
        window.close()

      if event is None:
        break
    window.close()
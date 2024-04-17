import os
import psycopg2

def init_dba():
    conn = psycopg2.connect(
            host="database",
            database="postgres",
            user="postgres",
            password="admin")
            
    cur = conn.cursor()

    cur.execute('DROP TABLE IF EXISTS public.fio;')
    cur.execute('CREATE TABLE public.fio (id serial PRIMARY KEY,'
                                            'name varchar (50) NOT NULL,'
                                            'date varchar (50) NOT NULL,'
                                            'spec varchar (50) NOT NULL);'
                                            )
                                            
    cur.execute('DROP TABLE IF EXISTS public.user;')
    cur.execute('CREATE TABLE public.user (id serial PRIMARY KEY,'
                                            'login varchar (90) NOT NULL,,'
                                            'sms integer NOT NULL,'
                                            'id1 integer NOT NULL,'
                                            'date varchar (50) NOT NULL);'
                                            )
                                            
    cur.execute('INSERT INTO public.fio (name, date, spec) VALUES (%s, %s, %s)',
                ('Ходяков Иван Валерьевич',
                '08:00-15:00',
                'Стоматолог')
                )
    cur.execute('INSERT INTO public.fio (name, date, spec) VALUES (%s, %s, %s)',
                ('Чечевский Андрей Сергеевич',
                '09:00-18:00',
                'Участковый врач')
                )
    cur.execute('INSERT INTO public.fio (name, date, spec) VALUES (%s, %s, %s)',
                ('Ерулина Жанна Аркадьевна',
                '12:00-16:00',
                'Психолог')
                )
    cur.execute('INSERT INTO public.fio (name, date, spec) VALUES (%s, %s, %s)',
                ('Пастух Ольга Михайловна',
                '07:00-10:00',
                'Лаборант')
                )    
                           
    cur.execute('INSERT INTO public.user (login, sms, id1, date) VALUES (%s, %s, %s, %s)',
                ('+78986664502',
                5500,
                2,
                '12:15')
                )
    cur.execute('INSERT INTO public.user (login, sms, id1, date) VALUES (%s, %s, %s, %s)',
                ('+79196663409',
                0208,
                1,
                '13:00')
                )
    cur.execute('INSERT INTO public.user (login, sms, id1, date) VALUES (%s, %s, %s, %s)',
                ('+79265340071',
                3648,
                4,
                '07:25')
                )

    conn.commit()
    cur.close()
    conn.close()
init_dba()

import os
import psycopg2

def init_dba():
    conn = psycopg2.connect(
            host="database",
            database="postgres",
            user="postgres",
            password="admin")
            
    cur = conn.cursor()

    cur.execute('DROP TABLE IF EXISTS public.namep;')
    cur.execute('CREATE TABLE public.fio (id serial PRIMARY KEY,'
                                            'name-o varchar (50) NOT NULL,'
                                            'name-p varchar (50) NOT NULL,'
                                            'date-o varchar (50) NOT NULL,'
                                            'date-p varchar (50) NOT NULL);'
                                            )
                                            
    cur.execute('DROP TABLE IF EXISTS public.user;')
    cur.execute('CREATE TABLE public.user (id serial PRIMARY KEY,'
                                            'login varchar (90) NOT NULL,'
                                            'sms varchar (90) NOT NULL,'
                                            'id1 integer NOT NULL,'
                                            'chair integer NOT NULL,'
                                            'vagon integer NOT NULL,'
                                            )
                                            
    cur.execute('INSERT INTO public.fio (name-o, name-p, date-o, date-p) VALUES (%s, %s, %s, %s)',
                ('Москва Ярославская',
                'Петушки',
                '15:17',
                '18:22')
                )
    cur.execute('INSERT INTO public.fio (name-o, name-p, date-o, date-p) VALUES (%s, %s, %s, %s)',
                ('Москва Ленинградская',
                'Санкт-Петербург',
                '15:30',
                '20:15')
                )
    cur.execute('INSERT INTO public.fio (name-o, name-p, date-o, date-p) VALUES (%s, %s, %s, %s)',
                ('Ярославль',
                'Москва Ярославская',
                '16:10',
                '20:10')
                )
    cur.execute('INSERT INTO public.fio (name-o, name-p, date-o, date-p) VALUES (%s, %s, %s, %s)',
                ('Подольск',
                'Нахабино',
                '19:02',
                '21:12')
                )    
                           
    cur.execute('INSERT INTO public.user (login, sms, id1, chair, vagon) VALUES (%s, %s, %s, %s, %s)',
                ('Сложнов Егор Алексеевич',
                '4518',
                2,
                '15',
                6)
                )
    cur.execute('INSERT INTO public.user (login, sms, id1, chair, vagon) VALUES (%s, %s, %s, %s, %s)',
                ('Панченков Илья Сергеевич',
                '3917',
                1,
                '13',
                7)
                )
    cur.execute('INSERT INTO public.user (login, sms, id1, chair, vagon) VALUES (%s, %s, %s, %s, %s)',
               ('Венедикт Васильевич Ерофеев',
                '3879',
                1,
                '11',
                7)
                )

    conn.commit()
    cur.close()
    conn.close()
init_dba()

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from posts.models import Posts
from categorias.models import Categoria
from comentarios.models import Comentarios
from random import choice, randint


class Command(BaseCommand):

    def handle(self, *args, **options):

        Posts.objects.all().delete()
        Categoria.objects.all().delete()
        Comentarios.objects.all().delete()

        lista_comentarios = [
            ['Liberty Mcbride', 'Liberty@email.com', 'Liberty'],
            ['Macaulay Donovan', 'Macaulay@gmail.com', 'Macaulay'],
            ['Dione Hilton', 'Dione@hotmail.com', 'Dione'],
            ['Jorge Alston', 'Jorge@uol.com', 'Jorge'],
            ['Darin Brock', 'Darin@yahoo.com', 'Darin'],
            ['Patryk Watkins', 'Patryk@email.com', 'Patryk'],
            ['Kalem O-Brien', 'Kalem@gmail.com', 'Kalem'],
            ['Markus Sumner', 'Markus@hotmail.com', 'Markus'],
            ['Eilidh Schofield', 'Eilidh@uol.com', 'Eilidh'],
            ['Lillian Sullivan', 'Lillian@yahoo.com', 'Lillian'],
            ['Remy Kirkpatrick', 'Remy@email.com', 'Remy'],
            ['Nella Albert', 'Nella@gmail.com', 'Nella'],
            ['Finnian Downs', 'Finnian@hotmail.com', 'Finnian'],
            ['Sultan Galvan', 'Sultan@uol.com', 'Sultan'],
            ['Jimi Weaver', 'Jimi@yahoo.com', 'Jimi'],
            ['Aarush Wheatley', 'Aarush@email.com', 'Aarush'],
            ['Conner Beard', 'Conner@gmail.com', 'Conner'],
            ['Cameron Ferry', 'Cameron@hotmail.com', 'Cameron'],
            ['Niko Bright', 'Niko@uol.com', 'Niko'],
            ['Shawn Armitage', 'Shawn@yahoo.com', 'Shawn'],
            ['Franklin Cruz', 'Franklin@email.com', 'Franklin'],
            ['Rhianna Gray', 'Rhianna@gmail.com', 'Rhianna'],
            ['Willa Jensen', 'Willa@hotmail.com', 'Willa'],
            ['Vicki Winters', 'Vicki@uol.com', 'Vicki'],
            ['Caitlin Jimenez', 'Caitlin@yahoo.com', 'Caitlin'],
            ['Zachariah Ortiz', 'Zachariah@email.com', 'Zachariah'],
            ['Tevin Andrade', 'Tevin@gmail.com', 'Tevin'],
            ['Khalid Martinez', 'Khalid@hotmail.com', 'Khalid'],
            ['Micah Melendez', 'Micah@uol.com', 'Micah'],
            ['Safia Cortes', 'Safia@yahoo.com', 'Safia'],
            ['Korban Chandler', 'Korban@email.com', 'Korban'],
            ['Kerri Ramirez', 'Kerri@gmail.com', 'Kerri'],
            ['Aarav Allan', 'Aarav@hotmail.com', 'Aarav'],
            ['Rhodri Ray', 'Rhodri@uol.com', 'Rhodri'],
            ['Laaibah Werner', 'Laaibah@yahoo.com', 'Laaibah'],
            ['Ellisha Phelps', 'Ellisha@email.com', 'Ellisha'],
            ['Emilee Moreno', 'Emilee@gmail.com', 'Emilee'],
            ['Aiesha Snow', 'Aiesha@hotmail.com', 'Aiesha'],
            ['Ptolemy Walls', 'Ptolemy@uol.com', 'Ptolemy'],
            ['Kwame Hernandez', 'Kwame@yahoo.com', 'Kwame'],
            ['Annabell Head', 'Annabell@email.com', 'Annabell'],
            ['Nyah Melia', 'Nyah@gmail.com', 'Nyah'],
            ['Susannah Gillespie', 'Susannah@hotmail.com', 'Susannah'],
            ['Rosina Hardy', 'Rosina@uol.com', 'Rosina'],
            ['Gracey Burn', 'Gracey@yahoo.com', 'Gracey'],
            ['Saffa Campos', 'Saffa@email.com', 'Saffa'],
            ['Edgar Horner', 'Edgar@gmail.com', 'Edgar'],
            ['Harriette Pittman', 'Harriette@hotmail.com', 'Harriette'],
            ['Bayley Young', 'Bayley@uol.com', 'Bayley'],
            ['Haydon Conley', 'Haydon@yahoo.com', 'Haydon'],
            ['Mairead Benjamin', 'Mairead@email.com', 'Mairead'],
            ['Caiden Melton', 'Caiden@gmail.com', 'Caiden'],
            ['Emillie Brennan', 'Emillie@hotmail.com', 'Emillie'],
            ['Abdi Ingram', 'Abdi@uol.com', 'Abdi'],
            ['Ian Briggs', 'Ian@yahoo.com', 'Ian'],
            ['Haris Jenkins', 'Haris@email.com', 'Haris'],
            ['Yasser Ramsay', 'Yasser@gmail.com', 'Yasser'],
            ['Fern Hope', 'Fern@hotmail.com', 'Fern'],
            ['Manal Richardson', 'Manal@uol.com', 'Manal'],
            ['Mali Witt', 'Mali@yahoo.com', 'Mali'],
            ['Jarvis Cook', 'Jarvis@email.com', 'Jarvis'],
            ['Enrique Edwards', 'Enrique@gmail.com', 'Enrique'],
            ['Viaan Turner', 'Viaan@hotmail.com', 'Viaan'],
            ['Malachi Solis', 'Malachi@uol.com', 'Malachi'],
            ['Finley Castro', 'Finley@yahoo.com', 'Finley'],
            ['Summer - Louise Blair', 'Summer@email.com', 'Summer'],
            ['Haaris Crouch', 'Haaris@gmail.com', 'Haaris'],
            ['Alasdair Knott', 'Alasdair@hotmail.com', 'Alasdair'],
            ['Che Donaldson', 'Che@uol.com', 'Che'],
            ['Floyd Mayer', 'Floyd@yahoo.com', 'Floyd'],
            ['Ayaz Monroe', 'Ayaz@email.com', 'Ayaz'],
            ['Aryan Stanton', 'Aryan@gmail.com', 'Aryan'],
            ['Nansi Barrow', 'Nansi@hotmail.com', 'Nansi'],
            ['Emerson Delgado', 'Emerson@uol.com', 'Emerson'],
            ['Libbie Langley', 'Libbie@yahoo.com', 'Libbie'],
            ['Jamila Rivers', 'Jamila@email.com', 'Jamila'],
            ['Beulah Bishop', 'Beulah@gmail.com', 'Beulah'],
            ['Vishal Hines', 'Vishal@hotmail.com', 'Vishal'],
            ['Woody Donald', 'Woody@uol.com', 'Woody'],
            ['Kavan Sheridan', 'Kavan@yahoo.com', 'Kavan'],
            ['Brendon Neal', 'Brendon@email.com', 'Brendon'],
            ['Betsy Morse', 'Betsy@gmail.com', 'Betsy'],
            ['Alanna Clemons', 'Alanna@hotmail.com', 'Alanna'],
            ['Anna Ruiz', 'Anna@uol.com', 'Anna'],
            ['Ishan Phillips', 'Ishan@yahoo.com', 'Ishan'],
            ['Effie Peacock', 'Effie@email.com', 'Effie'],
            ['Jaspal Perez', 'Jaspal@gmail.com', 'Jaspal'],
            ['Kayan Webber', 'Kayan@hotmail.com', 'Kayan'],
            ['Kaycee Peters', 'Kaycee@uol.com', 'Kaycee'],
            ['Kaydee Talbot', 'Kaydee@yahoo.com', 'Kaydee'],
            ['Chloe Ann Collins', 'Chloe@email.com', 'Chloe'],
            ['Eadie Duarte', 'Eadie@gmail.com', 'Eadie'],
            ['Jeevan Bowes', 'Jeevan@hotmail.com', 'Jeevan'],
            ['Kaiya Crossley', 'Kaiya@uol.com', 'Kaiya'],
            ['Kaan Noble', 'Kaan@yahoo.com', 'Kaan'],
            ['Uzair Hatfield', 'Uzair@email.com', 'Uzair'],
            ['Darren Kearns', 'Darren@gmail.com', 'Darren'],
            ['Lennon Parra', 'Lennon@hotmail.com', 'Lennon'],
            ['Beverly Saunders', 'Beverly@uol.com', 'Beverly'],
            ['Fionnuala Southern', 'Fionnuala@yahoo.com', 'Fionnuala'],
        ]

        lista_categorias = [
            'Python',
            'Django',
            'Tecnologia',
            'Sistemas',
        ]

        for c in lista_categorias:
            Categoria.objects.create(
                nome=c
            )

        details = [
            ['Lorem Ipsum', 'Latin in programming'],
            ['Your Title', 'Enter description here'],
            ['Resources to Learn Python', 'Top resources to learn Python in 2021'],
            ['Django Rest Framework', 'How Django Rest Framework compares to others'],
            ['Lion King', 'Review of the Lion King movie'],
            ['Mechanical Keyboards', 'What to look for when buying a mechanincal keyboard'],
        ]

        for i in range(1, 21):
            x = bool(choice([0, 1]))
            y = choice(lista_categorias)
            z = choice(details)
            Posts.objects.create(
                titulo=f'{z[0]} | {i}',
                autor=User.objects.get(username='bruno'),
                conteudo=f'testando{i}',
                excerto=f'{z[1]}',
                categoria_id=Categoria.objects.get(nome=y).id,
                publicado_post=x,
            )

        posts_ids = Posts.objects.all()[5:].values_list('id', flat=True)

        user_comentario = User.objects.get(
            username='Comentador',
        )

        print(user_comentario)

        for v in lista_comentarios:
            post_id = choice(posts_ids)
            publicado = bool(choice([0, 1]))
            Comentarios.objects.create(
                nome=v[0],
                email=v[1],
                comentario=v[2],
                post_id=post_id,
                usuario_id=user_comentario.id,
                publicado_comentario=publicado,
            )

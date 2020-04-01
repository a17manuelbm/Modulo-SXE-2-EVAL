# -*- coding: utf-8 -*-
{
    'name': "My VideoClub",  # Module title
    'summary': "Manejo de alquiler de peliculas",  # Module subtitle phrase
    'description': """Video club para el álquiler de películas""",  # You can also rst format
    'author': "A17ManuelBM",
    'website': "http://www.videoclubmanuel.com",
    'category': 'Ocio',
    'version': '2.1',
    'depends': ['base'],
    # This data files will be loaded at the installation (commented becaues file is not added in this example)
    'data': [
        'security/ir.model.access.csv',
        'views/pelicula.xml',
        'views/directores.xml',
        'views/alquiler.xml',
    ],
    # This demo data files will be loaded if db initialize with demo data (commented becaues file is not added in this example)
    # 'demo': [
    #     'demo.xml'
    # ],
}

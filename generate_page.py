"""Generate an HTML page"""

import dominate
import dominate.tags as tags

doc = dominate.document(title='Dominate your HTML')

with doc.head:
    tags.link(rel='stylesheet', href='style.css')
    tags.script(type='text/javascript', src='script.js')

with doc:
    with tags.div(id='header').add(ol()):
        for i in ['home', 'about', 'contact']:
            tags.li(tags.a(i.title(), href=f'/{i}.html'))

    with div():
        tags.attr(cls='body')
        tags.p('Lorem ipsum..')

print(doc)

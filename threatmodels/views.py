from flask import render_template

from app import app, pages

taxonomy = [ 'Application', 'Trusted Parties', 'Untrusted Parties', 'Key Storage', 'Convenience',
'Authentication', 'Architecture', 'tags' ]

@app.route('/')
def home():
    posts = [page for page in pages if 'date' in page.meta]
    # Sort pages by date
    sorted_posts = sorted(posts, reverse=True,
        key=lambda page: page.meta['date'])
    table = {}
    table['header'] = [taxonomy, ""]
    for post in sorted_posts:
        metas = []
        for col in taxonomy:
            if col in page.meta:
                metas.append(post.meta[col])
        if len(metas) == len(taxonomy):
            table[post.meta['Application']] = [metas,post]
    return render_template('index.html', pages=sorted_posts, table=table)

@app.route('/about/')
def about():
    page = pages.get_or_404('about')
    return render_template('page.html', page=page)

@app.route('/<path:path>/')
def page(path):
    # Path is the filename of a page, without the file extension
    # e.g. "first-post"
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)

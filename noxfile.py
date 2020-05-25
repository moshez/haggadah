import nox

nox.options.envdir = "build/nox"

@nox.session
def build_haggadah(session):
    session.install('.')
    session.run('python', '-m', 'haggadah.install_font')
    tmpdir = session.create_tmp()
    session.run('python', '-m', 'haggadah', f"{tmpdir}/haggadah.pdf")

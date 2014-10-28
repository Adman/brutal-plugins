import imhdsk
from brutal.core.plugin import match, cmd, threaded
import codecs
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


def rootify(word):
    """Return probable root of the word."""

    if len(word) <= 5:
        return word

    w = word[::-1]
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    for x in range(len(word)):
        if w[x] in vowels and x != 0:
            return word[:-x-1]


@threaded
@match(regex='.*bus (?:z|zo) (.*?) (:?do|na) (.+?)(?:\s|$)')
def mhd_match(event, f, t, *args, **kwargs):
    f = f
    t = args[0]

    if f == t:
        return "Not in this universe."

    time = ''
    date = ''
    if len(args) >= 3:
        time = args[2]
    if len(args) >= 4:
        date = args[3]

    probable_r = []
    probable_r.append(imhdsk.routes(f, t, time=time, date=date))
    if len(probable_r[0]) == 0:
        updated_f = rootify(f)
        probable_r.append(imhdsk.routes(updated_f, t, time=time, date=date))
        updated_t = rootify(t)
        probable_r.append(imhdsk.routes(f, updated_t, time=time, date=date))
        probable_r.append(imhdsk.routes(updated_f, updated_t,
                                        time=time, date=date))

    r = probable_r[0]
    for results in probable_r:
        if len(results) > len(r):
            r = results

    out = r[0].__repr__()
    out = unicode(out.strip(codecs.BOM_UTF8), 'utf-8')
    return out.encode('utf-8')


@threaded
@cmd
def mhd(event):
    args = event.args

    if len(args) < 2:
        return

    f = args[0]
    t = args[1]

    if f == t:
        return "Not in this universe."

    time = ''
    date = ''
    if len(args) >= 3:
        time = args[2]
    if len(args) >= 4:
        date = args[3]

    r = imhdsk.routes(f, t, time=time, date=date)
    if len(r) == 0:
        return

    out = r[0].__repr__()
    out = unicode(out.strip(codecs.BOM_UTF8), 'utf-8')
    return out.encode('utf-8')
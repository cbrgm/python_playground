def format_duration(n):
    if n == 0:
        return 'now'
    ms = 60
    hs = ms * 60
    ds = hs * 24
    ys = ds * 365

    y, x = divmod(n, ys)
    d, x = divmod(x, ds)
    h, x = divmod(x, hs)
    m, s = divmod(x, ms)

    y_str = (str(y) + " years" if y!=1 else '1 year') if y!=0 else ''
    d_str = (str(d) + " days" if d!=1 else '1 day') if d!=0 else ''
    h_str = (str(h) + " hours" if h!=1 else '1 hour') if h!=0 else ''
    m_str = (str(m) + " minutes" if m!=1 else '1 minute') if m!=0 else ''
    s_str = (str(s) + " seconds" if s!=1 else '1 second') if s!=0 else ''

    r = [y_str, d_str, h_str, m_str, s_str]
    r = [i for i in r if i!='']
    if len(r) >= 2:
        res = r[:-2] + [' and '.join(r[-2:])]
    else:
        res = r
    return ', '.join(res)
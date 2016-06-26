# -*- coding:utf-8 -*-
import graphviz as gv
import pydotplus
import shutil


def draw(alfabeto, estados, inicio, trans, final, nro_vuelta):
    g = gv.Digraph(format='dot')
    g.graph_attr['rankdir'] = 'LR'
    g.node('ini', shape="point")
    for e in estados:
        try:
            current = e[1]
            e = e[0]
        except:
            current = False
            e = e
        if e in final:
            if current is True:
                g.node(e, shape="doublecircle", color='blue')
            else:
                g.node(e, shape="doublecircle")
        else:
            if current is True:
                g.node(e, shape="circle", color='blue')
            else:
                g.node(e, shape="circle")
        if e in inicio:
            if nro_vuelta == 0:
                g.edge('ini', e, color='blue', weight='2')
            else:
                g.edge('ini', e)

    for t in trans:
        if t[2] not in alfabeto:
            return 0
        try:
            if t[3] is True:
                g.edge(t[0], t[1], label=str(t[2]), color='blue', weight='2')
            else:
                g.edge(t[0], t[1], label=str(t[2]))
        except:
            g.edge(t[0], t[1], label=str(t[2]))
    g.render(filename="temp/dot/temp", view=False)
    graph = pydotplus.graph_from_dot_file('temp/dot/temp.dot')
    graph.write_jpg('temp/dot/Digraph_'+str(nro_vuelta)+'.png')
    from PIL import Image
    im = Image.open('temp/dot/Digraph_'+str(nro_vuelta)+'.png')
    bg = Image.new("RGB", im.size, (255,255,255))
    bg.paste(im)
    if bg.size[0] >= 410:
        basewidth = 410
        wpercent = (basewidth/float(bg.size[0]))
        hsize = int((float(bg.size[1])*float(wpercent)))
        bg = bg.resize((basewidth,hsize), Image.ANTIALIAS)
    bg.save('temp/Digraph_'+str(nro_vuelta)+'.gif')
    shutil.rmtree('temp/dot')

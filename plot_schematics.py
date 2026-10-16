"""Vector drawing primitives; copied into each independent project generator."""
import argparse
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon, Circle, FancyArrowPatch

plt.rcParams.update({'font.family':'STIXGeneral', 'mathtext.fontset':'stix',
                     'font.size':9, 'pdf.fonttype':42, 'ps.fonttype':42,
                     'text.usetex':False, 'axes.unicode_minus':False})
CM = 1 / 2.54

class Drawing:
    def __init__(self, bounds):
        x0,y0,x1,y1 = bounds
        self.fig = plt.figure(figsize=((x1-x0)*CM,(y1-y0)*CM))
        self.ax = self.fig.add_axes([0,0,1,1], xlim=(x0,x1), ylim=(y0,y1))
        self.ax.set_aspect('equal'); self.ax.axis('off')
        self.nodes = {}
        self.labels = []

    def text(self,x,y,label,size=9,ha='center',va='center'):
        artist=self.ax.text(x,y,label,fontsize=size,ha=ha,va=va,
                            linespacing=1.15,clip_on=False,zorder=4)
        self.labels.append([artist,None])
        return artist

    def box(self,name,x,y,w,h,label,dashed=False,shape='rect',size=9):
        style = {'edgecolor':'black','facecolor':'white','linewidth':.55,
                 'linestyle':(0,(4,3)) if dashed else 'solid', 'zorder':2}
        if shape == 'diamond':
            obj = Polygon([(x-w/2,y),(x,y+h/2),(x+w/2,y),(x,y-h/2)],**style)
        elif shape == 'circle': obj = Circle((x,y),w/2,**style)
        else: obj = Rectangle((x-w/2,y-h/2),w,h,**style)
        self.ax.add_patch(obj); self.text(x,y,label,size)
        self.labels[-1][1]=(x-w/2,y-h/2,x+w/2,y+h/2)
        self.nodes[name] = (x,y,w,h,shape)

    def point(self,name,side):
        x,y,w,h,_ = self.nodes[name]
        return {'n':(x,y+h/2),'s':(x,y-h/2),'e':(x+w/2,y),
                'w':(x-w/2,y),'nw':(x-w/2,y+h/2),
                'ne':(x+w/2,y+h/2),'c':(x,y)}[side]

    def line(self,points,dashed=False):
        xs,ys=zip(*points)
        self.ax.plot(xs,ys,color='black',linewidth=.55,
                     linestyle=(0,(4,3)) if dashed else 'solid',zorder=1)

    def arrow(self,p,q,dashed=False,via=()):
        points=[p,*via,q]
        if via:self.line(points[:-1],dashed)
        self.ax.add_patch(FancyArrowPatch(points[-2],points[-1],
                         arrowstyle='-|>',mutation_scale=7.5,linewidth=.55,
                         color='black',shrinkA=0,shrinkB=0,
                         linestyle=(0,(4,3)) if dashed else 'solid',zorder=1))

    def edge(self,a,b,sa='s',sb='n',**kwargs):
        self.arrow(self.point(a,sa),self.point(b,sb),**kwargs)

    def frame(self,x,y,w,h):
        self.ax.add_patch(Rectangle((x,y),w,h,fill=False,edgecolor='black',
                                   linewidth=.55,linestyle=(0,(4,3)),zorder=0))

    def save(self,out,name):
        # Fixed physical canvas: do not enlarge or rasterize the scientific figure.
        self.fig.canvas.draw()
        renderer=self.fig.canvas.get_renderer()
        x0,x1=self.ax.get_xlim();y0,y1=self.ax.get_ylim()
        for artist,node in self.labels:
            b=artist.get_window_extent(renderer).transformed(self.ax.transData.inverted())
            if b.x0<x0-.02 or b.x1>x1+.02 or b.y0<y0-.02 or b.y1>y1+.02:
                raise ValueError(name+': clipped label '+repr(artist.get_text()))
            if node and (b.x0<node[0]-.02 or b.x1>node[2]+.02 or b.y0<node[1]-.02 or b.y1>node[3]+.02):
                raise ValueError(name+': label exceeds node '+repr(artist.get_text()))
        self.fig.savefig(out/(name+'.pdf'),format='pdf',
                         metadata={'Creator':'Python Matplotlib','Producer':None,
                                   'CreationDate':None,'ModDate':None})
        plt.close(self.fig)


def shifted_reservations(out):
    d=Drawing((0,0,14.3,5.4))
    d.arrow((.35,1.0),(13.7,1.0))
    for x,label in [(1.4,r'$(i-1)I$'),(7.0,r'$iI$'),(12.5,r'$(i+1)I$')]:
        d.line([(x,.87),(x,1.13)]);d.text(x,.45,label)
    d.line([(7.0,1.15),(7.0,4.85)],dashed=True)
    d.box('u',2.5,4.1,3.8,1.0,'$u_i$: offset $0$\n$p_i=\\mathrm{true}$',size=9)
    d.box('v',2.5,2.45,3.8,1.0,'$v_{i-1}$: offset $I$\n$p_{i-1}=\\mathrm{false}$',size=9)
    d.arrow(d.point('u','e'),(6.8,4.1));d.arrow(d.point('v','e'),(6.8,2.45))
    d.ax.plot([7],[4.1],marker='o',markersize=3,color='black')
    d.ax.plot([7],[2.45],marker='s',markersize=4,color='black',markerfacecolor='white')
    d.text(10.5,3.65,'Two records at one clock.\nDifferent stages observe\ndifferent iterations.',8.5)
    d.save(out,'shifted-reservations')

def ticket_retirement(out):
    d=Drawing((0,0,14.5,7.0))
    d.frame(.3,.45,4.15,6.15);d.frame(4.9,.45,9.3,6.15)
    d.box('fast',2.35,5.25,3.55,1.25,'Guessed replica\nStart at $0$',size=9)
    d.box('slow',2.35,2.9,3.55,1.45,'Actual replay\nStart at $R$\nActive $\\neg M$',size=9)
    d.box('select',7.05,4.1,3.2,1.3,'Choose ticket\nfor each $v$',size=9)
    d.box('retire',11.65,4.1,4.25,1.6,'Visit $v_1,\\ldots,v_m$\nUpdate; emit or fault',size=9)
    d.edge('fast','select','e','nw')
    x,y,w,h,_=d.nodes['select']
    d.arrow(d.point('slow','e'),(x-w/2,y-h/2))
    d.text(5.2,5.3,r'$M$',8.5);d.text(5.2,2.9,r'$\neg M$',8.5)
    d.edge('select','retire','e','w')
    d.text(2.35,1.3,'Private values\nor faults',8.5)
    d.text(9.5,1.3,r'Source-ordered retirement at $iI+C$',8.5)
    d.save(out,'ticket-retirement')

def main():
    import argparse
    parser=argparse.ArgumentParser();parser.add_argument('--outdir',type=Path,required=True)
    args=parser.parse_args();args.outdir.mkdir(parents=True,exist_ok=True)
    shifted_reservations(args.outdir);ticket_retirement(args.outdir)
if __name__=='__main__':main()

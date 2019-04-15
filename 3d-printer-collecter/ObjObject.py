import urllib.request
import urllib.error
import numpy as np


class ObjObject:

    def __init__(self, resource):
        self.resource = resource

        # Check if the first 4 characters of the resource is 'http' to see if the
        # obj coordinates file is a url or not. (Could be local file)
        if resource[:4] == "http":
            self.isResourceURL = True
        else:
            self.isResourceURL = False

        self.vertices = []
        self.faces = []

        if self.isResourceURL:
            try:
                response = urllib.request.urlopen(self.resource)
                self.obj_data = response.read().decode('utf-8')
            except urllib.error.URLError as e:
                print(e.reason)
                return

            lines = self.obj_data.splitlines()

        else:
            try:
                lines = open(self.resource, "r")
            except FileNotFoundError as e:
                print(e)
                return

        for line in lines:
            slist = line.split()
            if slist:
                if slist[0] == 'v':
                    vertex = list(map(float, slist[1:]))
                    self.vertices.append(vertex)
                elif slist[0] == 'f':
                    face = []
                    for k in range(1, len(slist)):
                        face.append([int(s) for s in slist[k].replace('//', '/').split('/')])

                    if len(face) > 3:  # triangulate the n-polygonal face, n>3
                        self.faces.extend(
                            [[face[0][0] - 1, face[k][0] - 1, face[k + 1][0] - 1] for k in range(1, len(face) - 1)])
                    else:
                        self.faces.append([face[j][0] - 1 for j in range(len(face))])
                else:
                    pass

        self.vertices = np.array(self.vertices)
        self.faces = np.array(self.faces)

        x, y, z = self.vertices[:, :3].T
        I, J, K = self.faces.T

        self.mesh = dict(type='mesh3d',
                         x=x,
                         y=y,
                         z=z,
                         # IMPORTANT! the color codes must be triplets of floats  in [0,1]!!
                         # Plotly docs do not mention this requirement
                         # https://github.com/plotly/plotly.js/blob/master/src/traces/mesh3d/attributes.js#L150
                         i=I,
                         j=J,
                         k=K,
                         name='',
                         showscale=False,
                         hoverinfo="none"
                         )


# Creating an obj of a teapot with a URL as the resource
# obj = ObjObject("https://people.sc.fsu.edu/~jburkardt/data/obj/teapot.obj")


# Creating an obj of a cube with a local file as the resource
# obj2 = ObjObject("cube.obj")

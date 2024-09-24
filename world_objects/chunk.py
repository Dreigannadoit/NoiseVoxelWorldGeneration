from settings import *
from meshes.chunk_mesh import ChunkMesh

class Chunk:
    def __init__(self, app):
        self.app = app
        self.voxels: np.array = self.generate_voxels()
        self.mesh: ChunkMesh = None
        self.create_mesh() # create mesh - shocker

    def create_mesh(self):
        self.mesh = ChunkMesh(self)

    def render(self):
        self.mesh.render()

    def generate_voxels(self):
        # empty chunk
        voxels = np.zeros(CHUNK_VOL, dtype='unit8')

        # fill chunk
        for x in range( CHUNK_SIZE ):
            for z in range( CHUNK_SIZE ):
                for y in range( CHUNK_SIZE ):
                    voxels[x + CHUNK_SIZE * z + CHUNK_AREA * y] = 1

        return voxels
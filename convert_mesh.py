import os
import open3d as o3d
import numpy as np

## change the vertex x to -x

data_dir = 'output/refined_mesh'
dst_dir = 'output/refined_mesh_flip'

obj_name = 'sugarfine_3Dgs7000_sdfestim02_sdfnorm02_level03_decim1000000_normalconsistency01_gaussperface1.obj'

for seq in os.listdir(data_dir):
    if os.path.exists(os.path.join(dst_dir, seq, obj_name)):
        continue
    
    seq_dir = os.path.join(data_dir, seq)
    dst_seq_dir = os.path.join(dst_dir, seq)
    if not os.path.exists(dst_seq_dir):
        os.makedirs(dst_seq_dir)
    obj_path = os.path.join(seq_dir, obj_name)
    mesh = o3d.io.read_triangle_mesh(obj_path)
    new_vertices = np.array(mesh.vertices)
    # import pdb; pdb.set_trace()
    new_vertices[:, 0] = -new_vertices[:, 0]
    mesh.vertices = o3d.utility.Vector3dVector(new_vertices)
    o3d.io.write_triangle_mesh(os.path.join(dst_seq_dir, obj_name), mesh)
    
    print('flip %s'%obj_path)
import pybullet as p

def start_simulation():
    physics_client = p.connect(p.GUI)
    p.setGravity(0, 0, -9.8)
    plane_id = p.loadURDF("plane.urdf")
    print("Simulação iniciada!")

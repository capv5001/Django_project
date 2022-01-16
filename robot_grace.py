from controller import Robot
TIME_STEP = 32
MAX_VEL = 6.28

# Prender ambos motores a la mitad de la velocidad máxima.

robot = Robot()

wheel_right=robot.getDevice('wheel Left')

# Avanzar una distancia determinada y luego volver a la posición inicial.
# Girar 90 grados en sentido horario y luego frenar.
# Girar 180 grados en sentido antihorario y luego frenar.
# Trazar un círculo con el movimiento del robot. IMPORTANTE: Usar el mundo "mapa_circulito.wbt"
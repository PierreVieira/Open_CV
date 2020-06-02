AZUL, VERDE, VERMELHO = (255, 0, 0), (0, 255, 0), (0, 0, 255)  # No OPEN CV é BGR em vez de RGB
CIANO, AMARELO = (255, 255, 0), (0, 255, 255)
opening_iterations = 15
dilatation_iterations = 20
closing_iterations = 5
largura_video = 400
altura_video = int((largura_video*720)/1280)
pos_line, offset = 150, 30
xy1, xy2 = (20, pos_line), (300, pos_line)
area_ret_min = 200
cache_detects = []
total = up = down = 0
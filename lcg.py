def getrandomnumber(m, a, c, z_0):
  random_numbers = []

  gen_z = []

  for i in range(m):
    z_i = ((a*z_0)+c) % m
    gen_z.append(z_0)
    u_0 = z_0/m
    z_0 = z_i
    random_numbers.append(u_0)
  return random_numbers, gen_z

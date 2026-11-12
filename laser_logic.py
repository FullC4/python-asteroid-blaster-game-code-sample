for i in lasers:
  if not app.charged:
      tr = Rect(500,500,10,10,fill='red')
      ofc = 10
      cdx = random.choice([-i.dx*ofc,i.dx*ofc])
      cdy = random.choice([-i.dy*ofc,i.dy*ofc])
      tr.centerX,tr.centerY = i.centerX+cdx,i.centerY+cdy
      tr.time = 10
      laserstrail.add(tr)
  else:
      tr = Rect(500,500,10,10,fill=gradient('red','orange'))
      ofc = 10
      cdx = random.choice([-i.dx*ofc,i.dx*ofc])
      cdy = random.choice([-i.dy*ofc,i.dy*ofc])
      tr.centerX,tr.centerY = i.centerX+cdx,i.centerY+cdy
      tr.time = 10
      laserstrail.add(tr)

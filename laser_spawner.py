def firelaser(x,y):
    if not app.charged:
        las = Rect(800, 800, 20, 10,fill='red')
        las.centerX,las.centerY = starship.centerX, starship.centerY
        lasers.add(las)
        las.rotateAngle = angleTo(las.centerX, las.centerY,x,y)-90
        las.shot=True
        las.dx=cos(radians(las.rotateAngle))
        las.dy=sin(radians(las.rotateAngle))
        las.time=50
    else:
        las = Rect(800, 800, 20, 10,fill=gradient('red','orange',start='left'))
        las.centerX,las.centerY = starship.centerX, starship.centerY
        lasers.add(las)
        las.rotateAngle = angleTo(las.centerX, las.centerY,x,y)-90
        las.shot=True
        las.dx=cos(radians(las.rotateAngle))*1.25
        las.dy=sin(radians(las.rotateAngle))*1.25
        las.time=50

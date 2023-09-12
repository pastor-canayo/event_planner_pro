from PIL import Image
img = Image.open('images/ticketing.jpg')
img.save('optimize-ticketing.jpg', optimize = True, quality = 50)

img = Image.open('images/attendee.jpg')
img.save('optimize-attendee.jpg', optimize = True, quality = 30)

img = Image.open('images/event.jpg')
img.save('optimize-event.jpg', optimize = True, quality = 50)

img = Image.open('images/postAnalysis.jpg')
img.save('optimize-postAnalysis.jpg', optimize = True, quality = 30)

img = Image.open('images/registration.jpg')
img.save('optimize-registration.jpg', optimize = True, quality = 30)
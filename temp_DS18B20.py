#/home/pi/temperature.py
# open the ds18b20file.
tfile =open("/sys/bus/w1/devices/28-01201cd1596c/w1_slave")
# Read all of thetext in the file.
text =tfile.read()
# close the file
tfile.close()
# Split the textwith new lines (\n) and select the second line.
secondline =text.split("\n")[1]
# Split the lineinto words, referring to the spaces, and select the 10th word (counting from0).
temperaturedata =secondline.split(" ")[9]
# The first twocharacters are "t=", so get rid of those and convert the temperaturefrom a string to a number.
temperature =float(temperaturedata[2:])
# Put the decimalpoint in the right place and display it.
temperature =temperature / 1000
print (temperature)


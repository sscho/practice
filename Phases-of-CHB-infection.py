
#ALT levels are normal (<19 U/L for females and <30 U/L for males)
#HBV DNA levels, ALT levels, and HBeAg status are among the most important determinants risk of progression to cirrhosis
#HBV DNA levels (>2,000 IU/mL), HBeAg status, and cirrhosis are key predictors of HCC risk
#Higher HBV DNA level is associated with progressively higher rates of cirrhosis and HCC.

from sys import argv

script, first, third = argv

print "Script:", script
print "First:", first
print "Your third:", third


Gender = raw_input ("Is your patient male or female?")
ALT = raw_input ("What is your patient's ALT levels?")
HBV_DNA = raw_input ("What is your HBV DNA levels (IU/ml)?")
HBeAg = raw_input ("Is your patient HBeAg positive or negative?")

print "So, your patient's gender, ALT levels, HBV DNA viral load values, and HBeAg status is as follows: \n* %r,\n* %r levels of ALT,\n* %r IU/ml,\n* HBeAg-%r." % (Gender, ALT, HBV_DNA, HBeAg)

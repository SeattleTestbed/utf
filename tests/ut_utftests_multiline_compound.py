# This test makes sure that multiline pragmas can contain wildcards anywhere

#pragma out
#pragma out Test message one
#pragma out Test message two
#pragma out 
#pragma out Test message three
#pragma out
print "Test message one"
print "Test message two"
print "Ignore this message"
print "Test message three"
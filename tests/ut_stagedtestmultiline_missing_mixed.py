# This test should fail since the 'one' messages are not printed out.

#pragma out message one
#pragma out message two
print "Test message two"

#pragma error message one
#pragma error message two
print "Error message two"

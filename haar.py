import numpy as np 
from matplotlib import pyplot as plt

data_len = 400
HAAR_COEFF = 8 

signal = np.sin(4*np.pi*np.linspace(0,1,data_len)) + 0.0*np.random.randn(data_len)

def haar(signal,sig_digits):
	new_signal = np.zeros(len(signal))
	# print int(np.log2(len(signal)))
	for level in xrange(int(np.log2(len(signal)))):
		new_signal_len = len(signal)/2
		new_signal = np.zeros(new_signal_len)
		for j in xrange(new_signal_len):
			new_signal[j]=signal[2*j]+signal[2*j+1]

		if new_signal_len==sig_digits:
			break;
		signal = new_signal

	return new_signal

def interprolate(signal, desired_len):
	scale=len(signal)*1.0/desired_len
	print "scale", scale
	new_signal = np.zeros(desired_len)
	for index in xrange(desired_len):
		new_index = scale*index
		down = int(new_index)
		up = np.ceil(new_index)

		if (up==len(signal)):
			up -= 1

		new_signal[index] = (up-new_index)*signal[up]+(new_index-down)*signal[down]

	return new_signal

def round_power_two(x):
	return 1<<(x-1).bit_length()

def interprolate(signal, desired_len):
	return np.interp(np.linspace(0,1,desired_len),np.linspace(0,1,len(signal)),signal)

def haar_transform(signal):
	new_data = haar(interprolate(signal,round_power_two(len(signal))),HAAR_COEFF)
	dmax=np.amax(new_data)
	dmin=np.amin(new_data)
	if (dmax==dmin):
		return np.zeros(len(new_data))
 	return 2*((new_data - dmin)*1.0/(dmax - dmin))-1
	
# plt.plot(haar_transform(signal))
# plt.show()


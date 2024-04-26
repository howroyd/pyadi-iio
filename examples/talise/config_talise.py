talise_address = "ip:192.168.2.1"  
lo_freq = 700000000#int(4.1e9)
tx_sine_baseband_freq = 20000000# 245760  # 245.760 kHz
amplitude_discrete = 2**14
sample_rate = 245760000 # Hz
num_samps = int((20*sample_rate)/tx_sine_baseband_freq) #int((20*sample_rate)/tx_sine_baseband_freq) # number of samples per call to rx()

rx_channels_used = [0, 1, 2, 3]
tx_channels_used = [0]

rx_gain_control_mode = "manual"
rx_gain = 60#10
tx_gain = 0#-10
tx_unused_channel_gain = -80

rx_buffer_size = num_samps
tx_buffer_size = num_samps
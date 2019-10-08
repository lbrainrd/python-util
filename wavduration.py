import scipy.io.wavfile as wav
import os, glob

file_path = "c:\eprime\projects\RSPIN_Signal_Noise_LS"

for f_name in glob.glob(os.path.join(file_path, '*.wav')):
    (s_rate, s_sig) = wav.read(f_name)
    dur_secs = len(s_sig) / float(s_rate)
    # output string to a file
    print("%s,%.2f" % (os.path.basename(f_name), dur_secs))

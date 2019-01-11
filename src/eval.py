import sys
import mir_eval
clean = mir_eval.io.load_wav(sys.argv[1])[0]
noisy = mir_eval.io.load_wav(sys.argv[2])[0]


[sdr, isr, sir, sar, perm] = mir_eval.separation.bss_eval_images(clean, noisy)
print("{} {} {} {}".format(sdr[0], isr[0], sir[0], sar[0]))


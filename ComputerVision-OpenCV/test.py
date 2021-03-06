## import Numpy
import numpy as np

# Import Matplotlib
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkCairo')

gray_histogram = [[0.000e+00],
                  [2.000e+00],
                  [1.000e+00],
                  [7.000e+00],
                  [1.300e+01],
                  [1.200e+01],
                  [1.800e+01],
                  [3.600e+01],
                  [2.900e+01],
                  [3.500e+01],
                  [3.400e+01],
                  [4.300e+01],
                  [3.300e+01],
                  [4.700e+01],
                  [4.100e+01],
                  [4.800e+01],
                  [4.100e+01],
                  [5.100e+01],
                  [5.400e+01],
                  [5.600e+01],
                  [4.900e+01],
                  [7.500e+01],
                  [7.700e+01],
                  [6.600e+01],
                  [8.400e+01],
                  [8.000e+01],
                  [8.400e+01],
                  [9.800e+01],
                  [1.150e+02],
                  [1.110e+02],
                  [1.200e+02],
                  [1.230e+02],
                  [9.600e+01],
                  [1.320e+02],
                  [1.100e+02],
                  [1.170e+02],
                  [1.490e+02],
                  [1.510e+02],
                  [1.320e+02],
                  [1.520e+02],
                  [1.740e+02],
                  [1.680e+02],
                  [1.740e+02],
                  [1.670e+02],
                  [1.970e+02],
                  [2.040e+02],
                  [2.130e+02],
                  [1.840e+02],
                  [2.120e+02],
                  [2.200e+02],
                  [2.590e+02],
                  [1.860e+02],
                  [2.510e+02],
                  [2.330e+02],
                  [3.170e+02],
                  [3.110e+02],
                  [4.070e+02],
                  [4.740e+02],
                  [5.520e+02],
                  [7.040e+02],
                  [8.390e+02],
                  [9.750e+02],
                  [1.312e+03],
                  [1.423e+03],
                  [1.620e+03],
                  [1.802e+03],
                  [2.015e+03],
                  [2.246e+03],
                  [2.293e+03],
                  [2.384e+03],
                  [2.552e+03],
                  [2.666e+03],
                  [2.930e+03],
                  [2.784e+03],
                  [2.716e+03],
                  [2.841e+03],
                  [2.564e+03],
                  [2.564e+03],
                  [2.287e+03],
                  [2.041e+03],
                  [1.882e+03],
                  [1.683e+03],
                  [1.466e+03],
                  [1.249e+03],
                  [1.164e+03],
                  [1.088e+03],
                  [9.770e+02],
                  [8.520e+02],
                  [7.950e+02],
                  [7.280e+02],
                  [6.900e+02],
                  [7.030e+02],
                  [6.910e+02],
                  [6.390e+02],
                  [5.900e+02],
                  [5.340e+02],
                  [4.920e+02],
                  [4.610e+02],
                  [4.370e+02],
                  [4.230e+02],
                  [3.870e+02],
                  [4.090e+02],
                  [3.450e+02],
                  [3.430e+02],
                  [3.310e+02],
                  [3.120e+02],
                  [3.060e+02],
                  [3.070e+02],
                  [2.680e+02],
                  [2.550e+02],
                  [2.660e+02],
                  [2.420e+02],
                  [2.170e+02],
                  [2.340e+02],
                  [1.960e+02],
                  [2.300e+02],
                  [2.140e+02],
                  [2.010e+02],
                  [2.020e+02],
                  [1.740e+02],
                  [2.020e+02],
                  [1.790e+02],
                  [2.020e+02],
                  [1.840e+02],
                  [2.020e+02],
                  [2.010e+02],
                  [1.600e+02],
                  [1.510e+02],
                  [1.760e+02],
                  [1.850e+02],
                  [1.770e+02],
                  [1.720e+02],
                  [1.990e+02],
                  [1.770e+02],
                  [1.800e+02],
                  [1.630e+02],
                  [1.670e+02],
                  [1.600e+02],
                  [1.860e+02],
                  [1.990e+02],
                  [1.960e+02],
                  [1.910e+02],
                  [1.950e+02],
                  [1.830e+02],
                  [1.770e+02],
                  [1.960e+02],
                  [1.550e+02],
                  [1.970e+02],
                  [1.960e+02],
                  [1.850e+02],
                  [1.770e+02],
                  [1.960e+02],
                  [1.720e+02],
                  [2.080e+02],
                  [1.910e+02],
                  [1.640e+02],
                  [1.840e+02],
                  [1.510e+02],
                  [1.900e+02],
                  [2.010e+02],
                  [1.890e+02],
                  [1.770e+02],
                  [1.900e+02],
                  [1.770e+02],
                  [1.940e+02],
                  [1.920e+02],
                  [1.920e+02],
                  [1.870e+02],
                  [1.710e+02],
                  [1.830e+02],
                  [1.780e+02],
                  [1.950e+02],
                  [1.900e+02],
                  [1.790e+02],
                  [1.720e+02],
                  [1.840e+02],
                  [1.940e+02],
                  [1.710e+02],
                  [1.860e+02],
                  [1.740e+02],
                  [1.900e+02],
                  [1.930e+02],
                  [1.710e+02],
                  [1.850e+02],
                  [1.880e+02],
                  [1.950e+02],
                  [1.590e+02],
                  [1.750e+02],
                  [2.000e+02],
                  [1.900e+02],
                  [1.770e+02],
                  [1.890e+02],
                  [1.820e+02],
                  [2.120e+02],
                  [2.230e+02],
                  [1.860e+02],
                  [2.140e+02],
                  [2.000e+02],
                  [2.190e+02],
                  [2.120e+02],
                  [1.950e+02],
                  [2.040e+02],
                  [2.300e+02],
                  [2.210e+02],
                  [2.080e+02],
                  [2.080e+02],
                  [2.030e+02],
                  [2.150e+02],
                  [1.940e+02],
                  [1.860e+02],
                  [1.770e+02],
                  [1.860e+02],
                  [1.750e+02],
                  [1.670e+02],
                  [1.700e+02],
                  [1.480e+02],
                  [1.740e+02],
                  [1.620e+02],
                  [1.410e+02],
                  [1.450e+02],
                  [1.410e+02],
                  [1.730e+02],
                  [1.650e+02],
                  [1.690e+02],
                  [1.740e+02],
                  [1.830e+02],
                  [1.900e+02],
                  [2.050e+02],
                  [1.810e+02],
                  [1.820e+02],
                  [1.600e+02],
                  [1.630e+02],
                  [1.760e+02],
                  [1.900e+02],
                  [1.670e+02],
                  [1.580e+02],
                  [1.400e+02],
                  [1.140e+02],
                  [9.600e+01],
                  [9.600e+01],
                  [1.020e+02],
                  [1.010e+02],
                  [7.900e+01],
                  [4.300e+01],
                  [1.100e+01],
                  [4.000e+00],
                  [0.000e+00],
                  [0.000e+00],
                  [0.000e+00],
                  [0.000e+00],
                  [0.000e+00],
                  [0.000e+00],
                  [0.000e+00],
                  [0.000e+00],
                  [0.000e+00],
                  [0.000e+00]]

plt.figure()
plt.title('Histogram of GrayScale image')
plt.xlabel('Bins')
plt.ylabel('# of Pixels')
plt.plot(gray_histogram)
plt.xlim([0, 256])
plt.show()

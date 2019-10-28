import tensorflow as tf
import tensorflow.contrib as tc
import tensorflow.contrib.layers as tcl

def leaky_relu(x, alpha=0.2):
	return tf.maximum(tf.minimum(0.0, alpha * x), x
)

def lrelu(x, leak=0.2, name="lrelu"):
	with tf.variable_scope(name):
		f1 = 0.5 * (1 + leak)
		f2 = 0.5 * (1 - leak)
		return f1 * x + f2 * abs(x)


class D_conv_mnist(object):
	def __init__(self):
		self.name = 'D_conv_mnist'

	def __call__(self, x, reuse=False):
		with tf.variable_scope(self.name) as scope:
			if reuse:
				scope.reuse_variables()
			size = 64
			shared = tcl.conv2d(x, num_outputs=size, kernel_size=4, # bzx28x28x1 -> bzx14x14x64
						stride=2, activation_fn=lrelu)
			shared = tcl.conv2d(shared, num_outputs=size * 2, kernel_size=4, # 7x7x128
						stride=2, activation_fn=lrelu, normalizer_fn=tcl.batch_norm)
			shared = tcl.flatten(shared)
			
			d = tcl.fully_connected(shared, 1, activation_fn=None, weights_initializer=tf.random_normal_initializer(0, 0.02))
			q = tcl.fully_connected(shared, 128, activation_fn=lrelu, normalizer_fn=tcl.batch_norm)
			q = tcl.fully_connected(q, 10, activation_fn=None) # 10 classes
			return d, q
	@property
	def vars(self):
		return tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, scope=self.name)


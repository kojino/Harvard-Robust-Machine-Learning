hidden = tf.layers.dense(noises, gen_hidden_dim, tf.nn.relu, name="g_hidden")
out_images = tf.layers.dense(hidden, image_dim, tf.nn.sigmoid, name="g_out")

hidden = tf.layers.dense(images, disc_hidden_dim, tf.nn.relu, name="d_hidden")
out_prob = tf.layers.dense(hidden, 1, tf.nn.sigmoid, name="d_out")

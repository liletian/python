num = [1]
denum = [1, 103, 302,200]
GH = transfer_function(num, denum)

# create a list of evenly spaced gains
gains = np.linspace(0.0, 1e5, num=500)

# compute and plot root-locus
roots = compute_roots(GH, gains)
fig, ax = plot_root_locus(gains, roots)
plt.show()

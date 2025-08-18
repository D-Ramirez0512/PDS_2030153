import matplotlib.pyplot as plt

def signal_graphs(t_continue, t_discrete, x_continue, x_discrete, title):
    plt.figure(figsize=(8, 8))
    plt.suptitle(title)

    # Continue signal
    plt.subplot(3, 1, 1)
    plt.plot(t_continue, x_continue, 'r')
    plt.title('Continue signal')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.grid()

    # Discrete signal
    plt.subplot(3, 1, 2)
    plt.stem(t_discrete, x_discrete, basefmt='k-')
    plt.title('Discrete signal')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.grid()

    # Overlaid signals
    plt.subplot(3, 1, 3)
    plt.plot(t_continue, x_continue, 'r', label='Continue')
    plt.stem(t_discrete, x_discrete, basefmt='k-', label='Discrete')
    plt.title('Overlapping signals')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.grid()

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()


def dac_graphs(d_in, a_out, voltage, levels, bits):
    plt.figure(figsize=(8, 6))
    plt.suptitle(f'DAC {bits} bits')
    
    plt.step(d_in, a_out, where='post', color='r')
    plt.xlabel('Digital input level')
    plt.ylabel('Analog voltage')
    plt.grid()
    plt.ylim(-0.1, voltage + 0.1)
    plt.xlim(-1, levels)
    plt.show()

import matplotlib.pyplot as plt


def generate_circle_plot(df, path):
    # create data
    names = df["Ticker"] + (df['Peso'] * 100).apply(lambda x: " " + str(round(x, 2)) + "%")
    size = df['Peso']

    plt.clf()
    plt.cla()
    plt.close()

    # Create a circle for the center of the plot
    my_circle = plt.Circle((0, 0), 0.7, color='white')

    plt.pie(size, labels=names)
    p = plt.gcf()

    p.gca().add_artist(my_circle)
    # plt.show()
    p.savefig(path)
    return p

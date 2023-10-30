import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['A', 'B', 'C']
    values = [200, 40, 500]

    ax = plt.subplot()
    ax.pie(values, labels=labels)
    plt.savefig('pie.png')
    plt.close()
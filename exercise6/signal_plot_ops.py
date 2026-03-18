import matplotlib.pyplot as plt

#smazat toml, readme, venv - vsude, kde to jde, pokud se neco vytvori v nejake slozce vyse, taky smazat (vsechno z pycharmu)

def load_signal_from_txt(path):
    with open(path, "r", encoding="utf-8") as file:
        list = []
        for line in file:
            list.append(line)
    return list

def signal_min(values):
    return min(values)

def signal_max(values):
    return values.max()

def signal_avg(values):
    return sum(values)/len(values)

def plot_signal(values):
    plt.plot(values)
    plt.show()


if __name__ == "__main__":
    values = load_signal_from_txt("ekg_signal.txt")
    print(signal_min(values))
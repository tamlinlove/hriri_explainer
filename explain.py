import pandas as pd
# Hide that one annoying pandas warning
pd.options.mode.chained_assignment = None 

class Explainer:
    csv_dir = "~/catkin_ws/src/hriri/logging/decision_csvs/"

    def __init__(self,csv_file):
        print(csv_file)

if __name__ == "__main__":
    filename = Explainer.csv_dir + "decision_test.csv"
    exp = Explainer(filename)

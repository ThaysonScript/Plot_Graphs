import matplotlib.pyplot as plt

class Graph:
    def __init__(self, df_plot) -> None:
        self.df_plot = df_plot
    
    def title(self, title):
        self.df_plot.set_title(f'{title}')
        
    def xlabel(self, title): 
        self.df_plot.set_xlabel(f'{title}')
        
    def ylabel(self, title):
        self.df_plot.set_ylabel(f'{title}')
        
    def grid_grade(self, title: bool):
        self.df_plot.grid(f'{title}')
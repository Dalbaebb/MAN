import matplotlib.pyplot as plt
from scipy.integrate import odeint, solve_ivp
import sys
sys.path.insert(1,"../Libraries")
from colors import COLORS
from DeletionLibrary import delete 

FILENAME = "SIR phase portrets.pdf"

def SIR_deriv(t,y,beta,gamma):
    S,I,R = y
    dSdt = -beta * S * I
    dIdt = beta * S * I - gamma * I
    dRdt = gamma * I
    return dSdt,dIdt,dRdt

S_0 = 1
I_0 = 0.0001
R_0 = 0

y_0 = (S_0,I_0,R_0)

R0 = 10 # - к-сть можливих заражень, що утворяться завдяки одній зараженій людині
tau = 8 # - інфекційний період
gamma = 1/tau # - темпи виздоровлення
beta = R0 * gamma # - ймовірність зараження

res = solve_ivp(fun=SIR_deriv, t_span=(0,100), y0=y_0, args=(beta,gamma), max_step=1)

S,I,R = res.y
time = res.t

figure = plt.figure(facecolor="w",figsize=(10,6),dpi=600)
diagram = figure.add_subplot(111,axisbelow=True) # - утворює одну діаграму, що займає 1 - рядок, 1 - стовбець, і знаходиться в 1 позиції

diagram.plot(time,S,color=COLORS["S"],alpha=0.5,lw=2,label="Suspectible") # - .plot(x,y,linewidth,label...), alpha - насиченість кольору, linestyle - стиль ліній
diagram.plot(time,I,color=COLORS["I"],alpha=0.5,lw=2,label="Infectious")
diagram.plot(time,R,color=COLORS["R"],alpha=0.5,lw=2,label="Removed")

diagram.fill_between(time, 0, S, color=COLORS["S"], alpha=0.15) # - Заповнює кольором площу між двома кривими: .fill_between(x,y1,y2...), де y1 - координата початку площі, y2 - кінця
diagram.fill_between(time, 0, I, color=COLORS["I"], alpha=0.15)
diagram.fill_between(time, 0, R, color=COLORS["R"], alpha=0.15)

diagram.set_xlabel("Time (days)")
diagram.set_ylabel("Fraction of population in compartment")
diagram.set_ylim(0, 1.0) # - Створює межі вертикальної осі у

diagram.grid(visible=True, which='major', axis = "both", c='w', lw=2, ls='-') # - Створює сітку 

diagram.spines["right"].set_visible(False) # - Ховає якусь з осей діаграми
diagram.spines["top"].set_visible(False)

legend = diagram.legend()
legend.get_frame().set_alpha(0.5)
plt.legend(title='', bbox_to_anchor=(0.5, -0.33), loc="lower center", ncol=3, frameon=False) # - Створює легедну діаграми, bbox_to_anchor() вівдповідає за її позицію
figure.subplots_adjust(bottom=0.25)

delete(FILENAME)
plt.savefig(FILENAME)

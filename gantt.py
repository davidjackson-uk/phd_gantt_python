import plotly.express as px
import pandas as pd
from datetime import date
from datetime import timedelta 

today = date.today()
tomorrow = today + timedelta(days=1)

df = pd.DataFrame([
    dict(Task="Today", Start=(today), Finish=(tomorrow), Workstream="You are Here", value_bf_vat=1),
    dict(Task="Hinds/MFT", Start='2024-05-10', Finish='2024-05-15', Workstream="Investigation", value_bf_vat=75),
    dict(Task="Inquiry/CCCU", Start='2024-04-23', Finish='2024-04-30', Workstream="Review", value_bf_vat=30),
    dict(Task="Urology", Start='2024-05-01', Finish='2024-05-02', Workstream="Coaching", value_bf_vat=20),
    dict(Task="Urology", Start='2024-05-23', Finish='2024-07-30', Workstream="Coaching", value_bf_vat=10),
    dict(Task="Jones/BVUK", Start='2024-04-25', Finish='2024-05-25', Workstream="Investigation", value_bf_vat=15),
    dict(Task="Evans/BVUK", Start='2024-04-23', Finish='2024-05-17', Workstream="Investigation", value_bf_vat=15),
    dict(Task="Sandwell A", Start='2024-04-23', Finish='2024-05-30', Workstream="Investigation", value_bf_vat=15),
    dict(Task="Sandwell B", Start='2024-05-07', Finish='2024-07-06', Workstream="Investigation", value_bf_vat=15),
    dict(Task="PhD", Start='2024-05-15', Finish='2024-05-17', Workstream="GT Seminar", value_bf_vat=20),
    dict(Task="PhD", Start='2024-09-19', Finish='2024-09-20', Workstream="IGTA Conference", value_bf_vat=20),
    dict(Task="Holidays", Start='2024-08-03', Finish='2024-08-17', Workstream="Summer Holiday", value_bf_vat='0'),
    dict(Task="Holidays", Start='2024-05-27', Finish='2024-06-02', Workstream="Half Term", value_bf_vat='0'),
    dict(Task="Holidays", Start='2024-10-28', Finish='2024-11-04', Workstream="Half Term", value_bf_vat='0'),
    dict(Task="Holidays", Start='2024-12-23', Finish='2025-01-05', Workstream="Christmas and New Year", value_bf_vat='0'),
    dict(Task="Radiology Mediation", Start='2024-05-02', Finish='2024-05-03', Workstream="Mediation", value_bf_vat='0'),
    dict(Task="Radiology Mediation", Start='2024-05-20', Finish='2024-05-21', Workstream="Mediation", value_bf_vat='0')
])
fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", color="Task", title="Current Projects for David Jackson", text="Workstream")
#fig.update_yaxes(autorange="reversed")
fig.update_layout(showlegend=False)
fig.show()

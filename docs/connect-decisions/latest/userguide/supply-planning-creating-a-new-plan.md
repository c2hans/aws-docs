---
source_url: https://docs.aws.amazon.com/connect-decisions/latest/userguide/supply-planning-creating-a-new-plan.html
---

# Creating a New Plan
<a name="supply-planning-creating-a-new-plan"></a>

 **To create a supply plan:**

1. Navigate to the Plans section in AWS Connect Decisions and choose **Create Plan** in Supply Plan section. Once a supply plan is created, you have the flexibility to edit it at any time to reflect changing business needs or incorporate new information.

1. **Configure Time Horizon settings:**
   + **Time bucket**: Select Daily or Weekly based on your planning needs.
   + **Plan horizon**: Specify the forecast horizon:
     + Daily: 1 to 365 days
     + Weekly: 1 to 52 weeks
   + **Plan start date**: For weekly plans, a day of the week can be selected as the plan start date. It also indicates the beginning of the week.

1. **Plan Schedule**

   Choose between One time run and **Recurring Schedule**
   + **For Recurring Schedule,** choose **Schedule Frequency**
     + **Daily**: Enter the UTC schedule time
     + **Weekly**: Select the day of the week and enter the UTC schedule time
     + **Monthly**: Select the day of the month and enter the UTC schedule time

1. **Demand Netting:**

   Configure what demands to drive the supply plan generation. Choose Forecast, sales order, or both
   + **Forecast**: Forecasted demand
   + **Sales order**: Actual sales order demand

1. **Demand Time Fence:**

   The period during which the supply plan will ignore the forecasted demand.

1. **Forecast consumption window:**

   The period in which actual customer orders replace or consume forecasted demand.
   + **Forecast consumption window - forward days**
   + **Forecast consumption window - backward days**

1. **Historical Period for Demand**

   Number of historical days to consider for average historical demand calculation

1. **Past due supply days**

   The numbers of days the supply orders can be past due but still considered as supply.

1. **Planning time fence**

   The period in which the supply plan is frozen. No new planned orders will be created with the planning time fence.

1. **Configuration rules**

   Constraint rules that guide the system in generating plans aligned with your business objectives. Add rules using the production capacity constraints template or warehouse space limit template.
   + **Production Capacity Constraints:** Download the Production Capacity Constraints template csv files (zipped). Populate the data and upload 3 csv files (not zipped) back using Decision teammate.
   + **Warehouse Space Limit**: Download the Warehouse Space Limit template csv file. Populate the data and upload it back using Decision teammate.

1. **Generate Supply Plan**

   Choose **Generate supply plan** button on the top to start the plan generation job or wait for the scheduled plan run.

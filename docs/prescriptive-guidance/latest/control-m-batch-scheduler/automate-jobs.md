---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/control-m-batch-scheduler/automate-jobs.html
---

# Automate job runs on a scheduled frequency
<a name="automate-jobs"></a>

Using the flow that you created in the previous steps, you can add basic and runtime scheduling.
+ Basic scheduling defines which days a job is eligible to run (for example, every weekday, only on working days, month end, or quarter end). You can set the basic scheduling on the [Scheduling](https://documents.bmc.com/supportu/9.0.21/en-US/Documentation/Job_scheduling.htm) tab.
+ Runtime scheduling determines when a job runs on the day that it's eligible to run (for example, after predecessor jobs complete, every hour, after specified resources are available, or only after manual confirmation).

You can define some runtime scheduling in the **Scheduling** section and others in **Prerequisites** section.

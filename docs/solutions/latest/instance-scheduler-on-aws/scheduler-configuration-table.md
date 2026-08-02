---
source_url: https://docs.aws.amazon.com/solutions/latest/instance-scheduler-on-aws/scheduler-configuration-table.html
---

# Scheduler configuration table
<a name="scheduler-configuration-table"></a>

When deployed, Instance Scheduler on AWS creates an Amazon DynamoDB table that contains global configuration settings.

Global configuration items contain a type attribute with a value of **config** in the configuration table. Schedules and periods contain type attributes with values of **schedule** and **period**, respectively. You can add, update, or remove schedules and periods from the configuration table using the DynamoDB console or the solution’s [command line interface](scheduler-cli-4.md). However, you don’t edit any items with a type of **config** because these items are managed by the solution.

---
source_url: https://docs.aws.amazon.com/iot/latest/developerguide/jobs-configurations.html
---

# Job configurations
<a name="jobs-configurations"></a>

You can have the following additional configurations for each job that you deploy to the specified targets.
+ **Rollout**: Defines how many devices receive the job document every minute.
+ **Scheduling**: Schedules a job for a future date and time in addition to using recurring maintenance windows.
+ **Abort**: Cancels a job in cases such as when some devices don't receive the job notification, or your devices report failure for their job executions.
+ **Timeout**: If there isn't a response from your job targets within a certain duration after their job executions have started, the job can fail.
+ **Retry**: Retries the job execution if your device reports failure when attempting to complete a job execution, or if your job execution times out.

By using these configurations, you can monitor the status of your job execution and avoid a bad update from being sent to an entire fleet.

**Topics**
+ [How job configurations work](jobs-configurations-details.md)
+ [Specify additional configurations](jobs-configurations-specify.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Core. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

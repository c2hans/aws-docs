---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/control-m-batch-scheduler/aws-mainframe-modernization-managed.html
---

# Managed AWS Mainframe Modernization integration with Control-M
<a name="aws-mainframe-modernization-managed"></a>

This section describes how Control-M integrates with and supports batch jobs that run in a managed AWS Mainframe Modernization environment deployed with a Micro Focus runtime engine. If you are implementing a custom AWS Replatform with Micro Focus environment on Amazon EC2, see the [AWS Mainframe Modernization on Amazon EC2 integration with Control-M](aws-mainframe-modernization-ec2.md) section.

This section assumes the following prerequisites:
+ An active AWS account.
+ The mainframe application is migrated and running in an AWS Replatform with Micro Focus managed runtime environment with multiple defined batch jobs.
+ For this pilot, the BankDemo example application is set up in AWS Mainframe Modernization. For setup instructions, see [Tutorial: Managed Runtime for Micro Focus](https://docs.aws.amazon.com/m2/latest/userguide/tutorial-runtime.html).

The following topics describe step-by-step setup required for integration between Control-M Scheduler and the AWS Mainframe Modernization environment for different types of integration workflows:
+ [Deploy Control-M resources](deploy-control-m-resources.md)
+ [Create a Control-M connection profile for AWS Mainframe Modernization](connection-profile.md)
+ [Create jobs and schedules in Control-M Planning](jobs-schedules-control-m.md)
+ [Monitor jobs](monitor-jobs.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

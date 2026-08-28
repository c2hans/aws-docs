---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/userguide/getting-started.html
---

# Getting started with Deadline Cloud
<a name="getting-started"></a>

To create a farm in AWS Deadline Cloud, you can use either the [Deadline Cloud console](https://console.aws.amazon.com/deadlinecloud/home) or the AWS Command Line Interface (AWS CLI). Use the console for a guided experience creating the farm, including queues and fleets. Use the AWS CLI to work directly with the service, or for developing your own tools that work with Deadline Cloud.

To create a farm and use the Deadline Cloud monitor, set up your account for Deadline Cloud. You only need to set up the Deadline Cloud monitor infrastructure once per account. From your farm, you can manage your project, including user access to your farm and its resources.

To create a farm with minimal resources to accept jobs, select **Quickstart** in the console home page. **[Set up the Deadline Cloud monitor](monitor-onboarding.md)** walks you through those steps. These farms start with a queue and a fleet that are automatically associated. This approach is a convenient way to create sandbox style farms to experiment in.

**Topics**
+ [Set up your AWS account](setting-up.md)
+ [Set up the Deadline Cloud monitor](monitor-onboarding.md)
+ [Set up your workstation](submitter.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

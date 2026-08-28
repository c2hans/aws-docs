---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/getting-started.html
---

# Getting started with Deadline Cloud resources
<a name="getting-started"></a>

To start creating custom solutions for AWS Deadline Cloud, you must set up your resources. These include a farm, at least one queue for the farm, and at least one worker fleet to service the queue. You can create your resources using the Deadline Cloud console, or you can use the AWS Command Line Interface.

In this tutorial, you will use AWS CloudShell to create a simple developer farm and run the worker agent. You can then submit and run a simple job with parameters and attachments, add a service managed fleet, and clean up your farm resources when you're done.

The following sections introduce you to the different features of Deadline Cloud, and how they function and work together. Following these steps is useful for developing and testing new workloads and customizations.

For instructions to set up your farm using the console, see [Getting started](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/getting-started.html) in the *Deadline Cloud User Guide*.

**Topics**
+ [Create a Deadline Cloud farm](create-a-farm.md)
+ [Run the Deadline Cloud worker agent](run-worker.md)
+ [Submit with Deadline Cloud](submit-a-job.md)
+ [Submit jobs with job attachments in Deadline Cloud](run-jobs-job-attachments.md)
+ [Add a service-managed fleet to your developer farm in Deadline Cloud](service-managed-fleet.md)
+ [Clean up your farm resources in Deadline Cloud](cleaning-up.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

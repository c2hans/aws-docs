---
source_url: https://docs.aws.amazon.com/batch/latest/userguide/service-environments.html
---

# Service environments for AWS Batch
<a name="service-environments"></a>

Service environments enable AWS Batch to integrate with SageMaker AI. A service environment contains the SageMaker AI specific configuration parameters required for AWS Batch to submit and manage SageMaker Training jobs while providing AWS Batch's queuing, scheduling, and priority management capabilities.

With service environments, data scientists and ML engineers can submit SageMaker Training jobs with priorities to service job queues. This integration eliminates the need for manual coordination of ML workloads, prevents accidental overspending, and improves resource utilization across your organization's machine learning workflows.

**Topics**
+ [What are service environments in AWS Batch](what-are-service-environments.md)
+ [Service environment states and lifecycle in AWS Batch](service-environment-states.md)
+ [Create a service environment in AWS Batch](create-service-environments.md)
+ [Update a service environment in AWS Batch](updating-service-environments.md)
+ [Delete a service environment in AWS Batch](deleting-service-environments.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Batch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query batch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scperf02-bp01.html
---

# SCPERF02-BP01 Use serverless compute to run tasks
<a name="scperf02-bp01"></a>

 Choosing the correct compute power for the workload provides smooth performance of the application, not only for the end users also for the solution developer community to maintain the software stacks across various infrastructures.

 **Desired outcome:** Smooth performance that elastic in nature with low upkeep.

 **Benefits of establishing this best practice:** Improved user experience, maintenance of software stack, and scalability.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance-37"></a>

 Some supply chain services computing workloads, like supplier data visibility, are typically loosely coupled and can benefit from event-driven architectures using the scaling capacity of AWS serverless compute options like AWS Lambda and AWS Fargate, combined with messaging services including Amazon SQS and Amazon EventBridge to decouple components. These serverless solutions minimize the overhead of capacity management, automatically scaling in or out to meet demands. Where scale is the primary factor, AWS serverless container compute engine AWS Fargate, can be used with both Amazon Elastic Container Service (Amazon ECS) and Amazon Elastic Kubernetes Service (Amazon EKS), removing the overhead of managing and provisioning compute resources.

### Implementation steps
<a name="implementation-steps-37"></a>

1.  Identify supply chain workloads that are suitable for serverless architectures, focusing on event-driven and loosely coupled processes.

1.  Implement AWS Lambda functions for lightweight, short-duration tasks such as data processing and API integrations.

1.  Deploy AWS Fargate for containerized workloads that require more control over the runtime environment while maintaining serverless benefits.

1.  Integrate messaging services like Amazon SQS and Amazon EventBridge to decouple components and enable asynchronous processing.

1.  Configure auto-scaling policies to automatically adjust compute resources based on demand patterns and workload requirements.

1.  Monitor performance metrics and optimize function configurations to facilitate efficient resource utilization and cost-effectiveness.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

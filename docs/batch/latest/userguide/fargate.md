---
source_url: https://docs.aws.amazon.com/batch/latest/userguide/fargate.html
---

# Fargate compute environments
<a name="fargate"></a>

Fargate is a technology that you can use with AWS Batch to run [containers](https://aws.amazon.com/what-are-containers) without having to manage servers or clusters of Amazon EC2 instances. With Fargate, you no longer have to provision, configure, or scale clusters of virtual machines to run containers. This removes the need to choose server types, decide when to scale your clusters, or optimize cluster packing.

When you run your jobs with Fargate resources, you package your application in containers, specify the CPU and memory requirements, define networking and IAM policies, and launch the application. Each Fargate job has its own isolation boundary and does not share the underlying kernel, CPU resources, memory resources, or elastic network interface with another job.

Fargate is only available for AWS Batch compute environments that use Amazon ECS as the orchestrator. Fargate is not supported for AWS Batch on Amazon EKS compute environments. For more information, see [Amazon EKS compute environments](eks.md).

**Topics**
+ [When to use Fargate](when-to-use-fargate.md)
+ [Job definitions on Fargate](fargate-job-definitions.md)
+ [Job queues on Fargate](fargate-job-queues.md)
+ [Compute environments on Fargate](fargate-compute-environments.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Batch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query batch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

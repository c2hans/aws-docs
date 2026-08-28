---
source_url: https://docs.aws.amazon.com/batch/latest/userguide/jobs.html
---

# Jobs
<a name="jobs"></a>

Jobs are the unit of work that's started by AWS Batch. Jobs can be invoked as containerized applications that run on Amazon ECS container instances in an ECS cluster.

Containerized jobs can reference a container image, command, and parameters. For more information, see [JobDefinition](https://docs.aws.amazon.com/batch/latest/APIReference/API_JobDefinition.html).

You can submit a large number of independent, simple jobs.

**Topics**
+ [Tutorial: submit a job](submit_job.md)
+ [Service jobs in AWS Batch](service-jobs.md)
+ [Job states](job_states.md)
+ [AWS Batch job environment variables](job_env_vars.md)
+ [Automated job retries](job_retries.md)
+ [Job dependencies](job_dependencies.md)
+ [Job timeouts](job_timeouts.md)
+ [Amazon EKS jobs](eks-jobs.md)
+ [Multi-node parallel jobs](multi-node-parallel-jobs.md)
+ [Multi-node parallel jobs on Amazon EKS](mnp-eks-jobs.md)
+ [Array jobs](array_jobs.md)
+ [Run GPU jobs](gpu-jobs.md)
+ [View AWS Batch jobs in a job queue](view-jobs.md)
+ [Search AWS Batch for jobs in a job queue](searching-filtering-jobs.md)
+ [Networking modes for AWS Batch jobs](networking-modes-jobs.md)
+ [View AWS Batch job logs in CloudWatch Logs](review-job-logs.md)
+ [Review AWS Batch job information](review-job-info.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Batch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query batch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

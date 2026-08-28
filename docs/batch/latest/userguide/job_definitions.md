---
source_url: https://docs.aws.amazon.com/batch/latest/userguide/job_definitions.html
---

# Job definitions
<a name="job_definitions"></a>

AWS Batch job definitions specify how jobs are to be run. While each job must reference a job definition, many of the parameters that are specified in the job definition can be overridden at runtime.

Some of the attributes specified in a job definition include:
+ Which Docker image to use with the container in your job.
+ How many vCPUs and how much memory to use with the container.
+ The command the container should run when it is started.
+ What (if any) environment variables should be passed to the container when it starts.
+ Any data volumes that should be used with the container.
+ What (if any) IAM role your job should use for AWS permissions.

**Topics**
+ [Create a single-node job definition](create-job-definition.md)
+ [Create a multi-node parallel job definition](create-multi-node-job-def.md)
+ [Job definition template that uses ContainerProperties](job-definition-template.md)
+ [Create job definitions using EcsProperties](multi-container-jobs.md)
+ [Use the awslogs log driver](using_awslogs.md)
+ [Specify sensitive data](specifying-sensitive-data.md)
+ [Private registry authentication for jobs](private-registry.md)
+ [Amazon EFS volumes](efs-volumes.md)
+ [Amazon S3 Files volumes](s3files-volumes.md)
+ [Job definition examples](example-job-definitions.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Batch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query batch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/batch/latest/userguide/quota-management.html
---

# Quota management
<a name="quota-management"></a>

AWS Batch schedules jobs based on the resources that the job requires and the capacity available in the connected Service Environment (SE), enabling high utilization of compute resources. With quota management, administrators can also control how many resources a team or project can consume via finer-grained resource allocations.

Quota management allows administrators to efficiently allocate shared compute resources between teams and projects by defining associated **quota shares** — AWS Batch resources that include compute quotas (**capacity limits**) and resource sharing strategies for idle compute. Each quota share operates as a virtual queue nested within an associated job queue. When scheduling jobs for a job queue, AWS Batch will iterate through all of the attached quota shares.

Administrators can enable resource sharing between quota shares with confidence, as **preemption** will allow any quota share to reclaim resources that it has lent to others when needed. Within a quota share, you can choose whether running jobs should be preempted for higher priority jobs or whether to let running jobs complete. Job priorities can be set at submission and updated later; updated priorities are taken into account as preemption decisions are made. Capacity utilization can be monitored at the queue, quota share and job-level granularity.

Quota management is only supported for job queues connected to a `SAGEMAKER_TRAINING` service environment.

**Topics**
+ [Quota shares](quota-shares.md)
+ [Preemption](preemption.md)
+ [Create quota management resources](create-quota-management-resources.md)
+ [Creating quota shares](create-quota-shares.md)
+ [Submitting jobs to a quota share](submit-job-quota-share.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Batch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query batch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

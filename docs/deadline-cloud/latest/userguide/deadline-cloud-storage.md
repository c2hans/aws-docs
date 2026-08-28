---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/userguide/deadline-cloud-storage.html
---

# File storage for Deadline Cloud
<a name="deadline-cloud-storage"></a>

Workers must have access to the storage locations that contain the input files necessary to process a job, and to the locations that store the output. AWS Deadline Cloud provides the following options for storage:
+ With *persistent storage*, service-managed fleet workers use dedicated Amazon Elastic Block Store (Amazon EBS) volumes that preserve data across worker lifecycle events. Application caches, conda package installations, and workspaces persist when workers are recycled, eliminating cold-start delays. For more information, see [Persistent storage for service-managed fleets](volumes.md).
+ With *job attachments*, Deadline Cloud transfers the input and output files for your jobs back and forth between a workstation and Deadline Cloud workers. To enable the file transfers, Deadline Cloud uses an Amazon Simple Storage Service (Amazon S3) bucket in your AWS account.

  When you use job attachments with a Linux based service-managed fleet, you can enable a virtual file system (VFS) to mount job attachments files and access them as needed instead of syncing them to the worker at the start of the job.
+ With *shared storage*, you use file sharing with your operating system to provide access to files.

  When you use cross-platform shared storage, you can create a *storage profile* so that workers can map the path to files between two different operating systems.

  You can also integrate third-party cloud storage solutions, such as LucidLink, with service-managed fleets using host configuration scripts. For more information, see [Set up LucidLink with service managed fleet scripts for Deadline Cloud](https://aws.amazon.com/blogs/media/set-up-lucidlink-with-service-managed-fleet-scripts-for-aws-deadline-cloud/) on the AWS for M&E Blog.

**Topics**
+ [Storage profiles in Deadline Cloud](storage-profile.md)
+ [Job attachments in Deadline Cloud](storage-job-attachments.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

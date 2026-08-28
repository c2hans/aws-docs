---
source_url: https://docs.aws.amazon.com/fsx/latest/LustreGuide/fsx-data-repositories.html
---

# Using data repositories with Amazon FSx for Lustre
<a name="fsx-data-repositories"></a>

Amazon FSx for Lustre provides high-performance file systems optimized for fast workload processing. It can support workloads such as machine learning, high performance computing (HPC), video processing, financial modeling, and electronic design automation (EDA). These workloads commonly require data to be presented using a scalable, high-speed file system interface for data access. Often, the datasets used for these workloads are stored in long-term data repositories in Amazon S3. FSx for Lustre is natively integrated with Amazon S3, making it easier to process datasets with the Lustre file system.

**Note**
File system backups aren't supported on file systems that are linked an Amazon S3 data repository. For more information, see [Protecting your data with backups](using-backups-fsx.md).
Intelligent-Tiering file systems don't support linking to Amazon S3 data repositories.

**Topics**
+ [Overview of data repositories](overview-dra-data-repo.md)
+ [POSIX metadata support for data repositories](posix-metadata-support.md)
+ [Linking your file system to an Amazon S3 bucket](create-dra-linked-data-repo.md)
+ [Importing changes from your data repository](importing-files-dra.md)
+ [Exporting changes to the data repository](export-changed-data-meta-dra.md)
+ [Data repository tasks](data-repository-tasks.md)
+ [Releasing files](file-release.md)
+ [Using Amazon FSx with your on-premises data](fsx-on-premises.md)
+ [Data repository event logs](data-repo-event-logs.md)
+ [Working with older deployment types](older-deployment-types.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FSx. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fsx` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

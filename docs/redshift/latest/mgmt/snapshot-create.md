---
source_url: https://docs.aws.amazon.com/redshift/latest/mgmt/snapshot-create.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# Creating a manual snapshot
<a name="snapshot-create"></a>

You can create a manual snapshot of a cluster from the snapshots list as follows. Or, you can take a snapshot of a cluster in the cluster configuration pane. For more information, see [Amazon Redshift snapshots and backups](working-with-snapshots.md).

**Note**
No-backup tables aren't supported for RG or RA3 provisioned clusters and Amazon Redshift Serverless workgroups. A table marked as no-backup in an RG or RA3 cluster or serverless workgroup is treated as a permanent table that will always be backed up while taking a snapshot, and always restored when restoring from a snapshot. To avoid snapshot costs for no-backup tables, truncate them before taking a snapshot.

**To create a manual snapshot**

1. Sign in to the AWS Management Console and open the Amazon Redshift console at [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/).

1. On the navigation menu, choose **Clusters**, **Snapshots**, then choose **Create snapshot**. The snapshot page to create a manual snapshot is displayed.

1. Enter the properties of the snapshot definition, then choose **Create snapshot**. It might take some time for the snapshot to be available.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/ug/vpc-lattice-oci-managed-backup.html
---

# Oracle Cloud Infrastructure (OCI) Managed Backup to Amazon S3
<a name="vpc-lattice-oci-managed-backup"></a>

When you create an Oracle Database@AWS database, VPC Lattice creates a resource configuration called `odb-managed-s3-backup-access`. This resource configuration represents an OCI managed backup of your databases to Amazon S3 and only enables connectivity to Amazon S3 buckets owned by OCI. Traffic between the ODB Network and S3 never leaves the Amazon network.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for VPC Lattice. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc-lattice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

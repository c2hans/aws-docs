---
source_url: https://docs.aws.amazon.com/parallelcluster/latest/ug/troubleshooting-fc-v3-access-storage.html
---

# Trying to access storage
<a name="troubleshooting-fc-v3-access-storage"></a>

Learn about the troubleshooting tips for trying to access storage.

## Using an external Amazon FSx for Lustre file system
<a name="access-storage-fsx-lustre-v3"></a>

Make sure that traffic is allowed between the cluster and file system. The file system must be associated with a security group that allows inbound and outbound TCP traffic through ports 988, 1021, 1022, and 1023. For more information about how to set up security groups, see [FileSystemId](SharedStorage-v3.md#yaml-SharedStorage-FsxLustreSettings-FileSystemId).

## Using an external Amazon Elastic File System file system
<a name="access-storage-efs-v3"></a>

Make sure that traffic is allowed between the cluster and file system. The file system must be associated with a security group that allows inbound and outbound TCP traffic through ports 988, 1021, 1022, and 1023. For more information about how to set up security groups, see [FileSystemId](SharedStorage-v3.md#yaml-SharedStorage-EfsSettings-FileSystemId).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

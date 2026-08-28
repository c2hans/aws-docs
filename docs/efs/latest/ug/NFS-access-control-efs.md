---
source_url: https://docs.aws.amazon.com/efs/latest/ug/NFS-access-control-efs.html
---

# Controlling network access to EFS file systems for NFS clients
<a name="NFS-access-control-efs"></a>

You can control access by NFS clients to Amazon EFS file systems using network layer security and EFS file system policies. You can use the network layer security mechanisms available with Amazon EC2, such as VPC security group rules and network ACLs. You can also use AWS IAM to control NFS access with an EFS file system policy and identity-based policies.

**Topics**
+ [Using VPC security groups](network-access.md)
+ [Working with interface VPC endpoints in Amazon EFS](efs-vpc-endpoints.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic File System (EFS). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query efs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

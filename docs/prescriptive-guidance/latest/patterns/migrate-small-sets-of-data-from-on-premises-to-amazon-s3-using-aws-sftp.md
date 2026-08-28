---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-small-sets-of-data-from-on-premises-to-amazon-s3-using-aws-sftp.html
---

# Migrate small sets of data from on premises to Amazon S3 using AWS SFTP
<a name="migrate-small-sets-of-data-from-on-premises-to-amazon-s3-using-aws-sftp"></a>

*Charles Gibson and Sergiy Shevchenko, Amazon Web Services*

## Summary
<a name="migrate-small-sets-of-data-from-on-premises-to-amazon-s3-using-aws-sftp-summary"></a>

This pattern describes how to migrate small sets of data (5 TB or less) from on-premises data centers to Amazon Simple Storage Service (Amazon S3) by using AWS Transfer for SFTP (AWS SFTP). The data can be either database dumps or flat files.

## Prerequisites and limitations
<a name="migrate-small-sets-of-data-from-on-premises-to-amazon-s3-using-aws-sftp-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ An AWS Direct Connect link established between your data center and AWS

**Limitations**
+ The data files must be less than 5 TB. For files over 5 TB, you can perform a multipart upload to Amazon S3 or choose another data transfer method.

## Architecture
<a name="migrate-small-sets-of-data-from-on-premises-to-amazon-s3-using-aws-sftp-architecture"></a>

**Source technology stack**
+ On-premises flat files or database dumps

**Target technology stack**
+ Amazon S3

**Source and target architecture**

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/a9c016ff-3e68-4714-ac51-46cb4727397a/images/5c5bb9ea-d552-44e8-8d0d-df341f84f55d.png)

## Tools
<a name="migrate-small-sets-of-data-from-on-premises-to-amazon-s3-using-aws-sftp-tools"></a>
+ [AWS SFTP](https://docs.aws.amazon.com/transfer/latest/userguide/what-is-aws-transfer-for-sftp.html) – Enables the transfer of files directly into and out of Amazon S3 using Secure File Transfer Protocol (SFTP).
+ [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) – Establishes a dedicated network connection from your on-premises data centers to AWS.
+ [VPC endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints.html) – Enable you to privately connect a VPC to supported AWS services and VPC endpoint services powered by AWS PrivateLink without an internet gateway, network address translation (NAT) device, VPN connection, or Direct Connect connection. Instances in a VPC don't require public IP addresses to communicate with resources in the service.

## Epics
<a name="migrate-small-sets-of-data-from-on-premises-to-amazon-s3-using-aws-sftp-epics"></a>

### Prepare for the migration
<a name="prepare-for-the-migration"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Document the current SFTP requirements. |  | Application owner, SA |
| Identify the authentication requirements. | Requirements may include key-based authentication, user name or password, or identity provider (IdP). | Application owner, SA |
| Identify the application integration requirements. |  | Application owner |
| Identify the users who require the service. |  | Application owner |
| Determine the DNS name for the SFTP server endpoint. |  | Networking |
| Determine the backup strategy. |  | SA, DBA (if data is transferred)  |
| Identify the application migration or cutover strategy. |  | Application owner, SA, DBA |

### Configure the infrastructure
<a name="configure-the-infrastructure"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create one or more virtual private clouds (VPCs) and subnets in your AWS account. |  | Application owner, AMS |
| Create the security groups and network access control list (ACL). |  | Security, Networking, AMS |
| Create the Amazon S3 bucket. |  | Application owner, AMS |
| Create the AWS Identity and Access Management (IAM) role. | Create an IAM policy that includes the permissions to enable AWS SFTP to access your Amazon S3 bucket. This IAM policy determines what level of access you provide SFTP users. Create another IAM policy to establish a trust relationship with AWS SFTP. | Security, AMS |
| Associate a registered domain (optional). | If you have your own registered domain, you can associate it with the SFTP server. You can route SFTP traffic to your SFTP server endpoint from a domain or from a subdomain. | Networking, AMS |
| Create an SFTP server. | Specify the identity provider type used by the service to authenticate your users. | Application owner, AMS |
| Open an SFTP client. | Open an SFTP client and configure the connection to use the SFTP endpoint host. AWS SFTP supports any standard SFTP client. Commonly used SFTP clients include OpenSSH, WinSCP, Cyberduck, and FileZilla. You can get the SFTP server host name from the AWS SFTP console. | Application owner, AMS |

### Plan and test
<a name="plan-and-test"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Plan the application migration. | Plan for any application configuration changes required, set the migration date, and determine the test schedule. | Application owner, AMS |
| Test the infrastructure. | Test in a non-production environment. | Application owner, AMS |

## Related resources
<a name="migrate-small-sets-of-data-from-on-premises-to-amazon-s3-using-aws-sftp-resources"></a>

**References**
+ [AWS Transfer for SFTP User Guide](https://docs.aws.amazon.com/transfer/latest/userguide/what-is-aws-transfer-for-sftp.html)
+ [AWS Direct Connect resources](https://aws.amazon.com/directconnect/resources/)
+ [VPC Endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints.html)

**Tutorials and videos**
+ [AWS Transfer for SFTP (video)](https://www.youtube.com/watch?v=wcnGez5PP1E)
+ [AWS Transfer for SFTP user guide](https://docs.aws.amazon.com/transfer/latest/userguide/what-is-aws-transfer-for-sftp.html)
+ [AWS SA Whiteboarding - Direct Connect (video) ](https://www.youtube.com/watch?v=uP68iqyuqTg)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

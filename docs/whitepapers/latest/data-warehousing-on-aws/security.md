---
source_url: https://docs.aws.amazon.com/whitepapers/latest/data-warehousing-on-aws/security.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Security
<a name="security"></a>

 To help provide data security, you can run Amazon Redshift inside a virtual private cloud based on the [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/) (Amazon VPC) service. You can use the software-defined networking model of the VPC to define firewall rules that restrict traffic based on the rules you configure. Amazon Redshift supports SSL-enabled connections between your client application and your Amazon Redshift data warehouse cluster, which enables data to be encrypted in transit. You can also leverage [Enhanced VPC Routing](https://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html) to manage data flow between your Amazon Redshift cluster and other data sources. Data traffic is routed within the AWS network instead of public internet.

 The Amazon Redshift compute nodes store your data, but the data can be accessed only from the cluster’s leader node. This isolation provides another layer of security. Amazon Redshift integrates with [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) to enable you to audit all Amazon Redshift API calls. To help keep your data secure at rest, Amazon Redshift supports encryption, and can encrypt each block using hardware-accelerated Advanced Encryption Standard (AES)-256 encryption as each block is written to disk. This encryption takes place at a low level in the I/O subsystem; the I/O subsystem encrypts everything written to disk, including intermediate query results. The blocks are backed up as is, which means that backups are also encrypted. By default, Amazon Redshift takes care of key management, but you can choose [to manage your keys using your own hardware security modules](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-db-encryption.html#working-with-HSM), or manage your keys through [AWS Key Management Service](https://aws.amazon.com/kms/) (AWS KMS).

 Database security management is controlled by managing user access, granting the proper privileges to tables and views to user accounts or groups, and leveraging column-level grant and revoke to meet your security and compliance needs in finer granularity.

 In addition, Amazon Redshift provides multiple means of authentication to secure and simplify data warehouse access. You can use [AWS Identity and Access Management](https://aws.amazon.com/iam/) (AWS IAM) within your AWS account. Use federated authentication if you already manage user identifies outside of AWS via [SAML-2.0](https://en.wikipedia.org/wiki/SAML_2.0)-compatible identity providers to enable your users to access the data warehouse without managing database users and passwords. Amazon Redshift also supports multi-factor authentication (MFA) to provide additional security.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

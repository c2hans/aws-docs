---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/encryption-best-practices/efs.html
---

# Amazon Elastic File System
<a name="efs"></a>

[Amazon Elastic File System (Amazon EFS)](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html) helps you create and configure shared file systems in the AWS Cloud.

Consider the following encryption best practices for this service:
+ In AWS Config, implement the [efs-encrypted-check](https://docs.aws.amazon.com/config/latest/developerguide/efs-encrypted-check.html) AWS managed rule. This rule checks if Amazon EFS is configured to encrypt the file data using AWS KMS.
+ Enforce encryption for Amazon EFS file systems by creating an Amazon CloudWatch alarm that monitors CloudTrail logs for `CreateFileSystem` events and triggers an alarm if an unencrypted file system is created. For more information, see [Walkthrough: Enforcing Encryption on an Amazon EFS File System at Rest](https://docs.aws.amazon.com/efs/latest/ug/efs-enforce-encryption.html).
+ Mount the file system by using the [EFS mount helper](https://docs.aws.amazon.com/efs/latest/ug/efs-mount-helper.html). This sets up and maintains a TLS 1.2 tunnel between the client and the Amazon EFS service and routes all Network File System (NFS) traffic over this encrypted tunnel. The following command implements the use of TLS for in-transit encryption.

  ```
  sudo mount -t efs  -o tls file-system-id:/ /mnt/efs
  ```

  For more information, see [Using EFS mount helper to mount EFS file systems](https://docs.aws.amazon.com/efs/latest/ug/efs-mount-helper.html).
+ Using AWS PrivateLink, implement interface VPC endpoints to establish a private connection between VPCs and the Amazon EFS API. Data in transit over the VPN connection to and from the endpoint is encrypted. For more information, see [Access an AWS service using an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html).
+ Use the `elasticfilesystem:Encrypted` condition key in IAM identity-based policies to prevent users from creating EFS file systems that aren't encrypted. For more information, see [Using IAM to enforce creating encrypted file systems](https://docs.aws.amazon.com/efs/latest/ug/using-iam-to-enforce-encryption-at-rest.html).
+ KMS keys used for EFS encryption should be configured for least-privilege access by using resource-based key policies.
+ Use the `aws:SecureTransport` condition key in the EFS file system policy to enforce use of TLS for NFS clients when connecting to an EFS file system. For more information, see [Encryption of data in transit](https://docs.aws.amazon.com/whitepapers/latest/efs-encrypted-file-systems/encryption-of-data-in-transit.html) in *Encrypting File Data with Amazon Elastic File System* (AWS Whitepaper).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

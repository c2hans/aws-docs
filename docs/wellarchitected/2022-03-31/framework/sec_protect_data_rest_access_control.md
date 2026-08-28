---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/sec_protect_data_rest_access_control.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC08-BP04 Enforce access control
<a name="sec_protect_data_rest_access_control"></a>

Enforce access control with least privileges and mechanisms, including backups, isolation, and versioning, to help protect your data at rest. Prevent operators from granting public access to your data.

 Different controls including access (using least privilege), backups (see [Reliability whitepaper](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html)), isolation, and versioning can all help protect your data at rest. Access to your data should be audited using detective mechanisms covered earlier in this paper including CloudTrail, and service level log, such as Amazon Simple Storage Service (Amazon S3) access logs. You should inventory what data is publicly accessible, and plan for how you can reduce the amount of data available over time. Amazon Glacier Vault Lock and Amazon S3 Object Lock are capabilities providing mandatory access control—once a vault policy is locked with the compliance option, not even the root user can change it until the lock expires. The mechanism meets the Books and Records Management requirements of the SEC, CFTC, and FINRA. For more details, see [this whitepaper](https://d1.awsstatic.com/whitepapers/Amazon-GlacierVaultLock_CohassetAssessmentReport.pdf).

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>
+  Enforce access control: Enforce access control with least privileges, including access to encryption keys.
  +  [Introduction to Managing Access Permissions to Your Amazon S3 Resources](https://docs.aws.amazon.com/AmazonS3/latest/dev/intro-managing-access-s3-resources.html)
+  Separate data based on different classification levels: Use different AWS accounts for data classification levels managed by AWS Organizations.
  +  [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html)
+  Review AWS KMS policies: Review the level of access granted in AWS KMS policies.
  +  [Overview of managing access to your AWS KMS resources](https://docs.aws.amazon.com/kms/latest/developerguide/control-access-overview.html)
+  Review Amazon S3 bucket and object permissions: Regularly review the level of access granted in Amazon S3 bucket policies. Best practice is to not have publicly readable or writeable buckets. Consider using AWS Config to detect buckets that are publicly available, and Amazon CloudFront to serve content from Amazon S3.
  +  [AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html)
  +  [Amazon S3 \+ Amazon CloudFront: A Match Made in the Cloud](https://aws.amazon.com/blogs/networking-and-content-delivery/amazon-s3-amazon-cloudfront-a-match-made-in-the-cloud/)
+  Enable Amazon S3 versioning and object lock.
  +  [Using versioning](https://docs.aws.amazon.com/AmazonS3/latest/dev/Versioning.html)
  +  [Locking Objects Using Amazon S3 Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html)
+  Use Amazon S3 Inventory: Amazon S3 inventory is one of the tools you can use to audit and report on the replication and encryption status of your objects.
  +  [Amazon S3 Inventory](https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-inventory.html)
+  Review Amazon EBS and AMI sharing permissions: Sharing permissions can allow images and volumes to be shared to AWS accounts external to your workload.
  +  [Sharing an Amazon EBS Snapshot](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-modifying-snapshot-permissions.html)
  +  [Shared AMIs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sharing-amis.html)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS KMS Cryptographic Details Whitepaper](https://docs.aws.amazon.com/kms/latest/cryptographic-details/intro.html)

 **Related videos:**
+  [Securing Your Block Storage on AWS](https://youtu.be/Y1hE1Nkcxs8)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

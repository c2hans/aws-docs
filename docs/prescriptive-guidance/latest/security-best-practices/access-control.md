---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-best-practices/access-control.html
---

# Step 4. Implement access control mechanisms
<a name="access-control"></a>

When thinking about security in the cloud, your foundational strategy should begin with a strong identity foundation to ensure a user has the right permissions to access data. Appropriate authentication and authorization can mitigate the risk of security events. The shared responsibility model requires AWS customers to implement access control policies. To create and manage access policies at scale, you can use [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/).

When configuring access rights and permissions, implement the principle of least privilege by ensuring each user or system accessing your backup data or vault is given only the permissions necessary to fulfill their job duties. Use AWS Backup to [set access policies on backup vaults](https://docs.aws.amazon.com/aws-backup/latest/devguide/creating-a-vault-access-policy.html) to protect your cloud workloads.

For example, by implementing access control policies, you can grant users access to create backup plans and on-demand backups while limiting their ability to delete recovery points. Using vault access policies, you can share a destination backup vault with a source AWS account, user, or IAM role, as required by your business needs. You can also use access policies to share a backup vault with one or multiple accounts, or with your entire organization in AWS Organizations. For more information, see the [AWS Backup documentation](https://docs.aws.amazon.com/aws-backup/latest/devguide/create-cross-account-backup.html#share-vault-cab).

As you scale your workloads or migrate into AWS, you might need to centrally manage permissions to your backup vaults and operations. Use [service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) to implement centralized control over the maximum available permissions for all accounts in your organization. SCPs offer defense in depth, and they ensure that your users stay within the defined access control guidelines. For more information, see [Managing access to backups using service control policies with AWS Backup](https://aws.amazon.com/blogs/storage/managing-access-to-backups-using-service-control-policies-with-aws-backup/).

To mitigate security risks such as unintended access to your backup resources and data, use [IAM Access Analyzer](https://aws.amazon.com/blogs/aws/identify-unintended-resource-access-with-aws-identity-and-access-management-iam-access-analyzer/) to identify any AWS Backup IAM role shared with the following:
+ An external entity such as an AWS account
+ A root user
+ An IAM user or role
+ A federated user
+ An AWS service
+ An anonymous user
+ Any other entity that could be used to create a filter

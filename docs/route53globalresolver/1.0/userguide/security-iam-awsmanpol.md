---
source_url: https://docs.aws.amazon.com/route53globalresolver/1.0/userguide/security-iam-awsmanpol.html
---

# AWS managed policies for Amazon Route 53 Global Resolver

To add permissions to users, groups, and roles, it is easier to use AWS managed policies than to write policies yourself. It takes time and expertise to [create IAM customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) that provide your team with only the permissions they need. To get started quickly, you can use our AWS managed policies. These policies cover common use cases and are available in your AWS account. For more information about AWS managed policies, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

AWS services maintain and update AWS managed policies. You can't change the permissions in AWS managed policies. Services occasionally add additional permissions to an AWS managed policy to support new features. This type of update affects all identities (users, groups, and roles) where the policy is attached. Services are most likely to update an AWS managed policy when a new feature is launched or when new operations become available. Services do not remove permissions from an AWS managed policy, so policy updates won't break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple services. For example, the **ReadOnlyAccess** AWS managed policy provides read-only access to all AWS services and resources. When a service launches a new feature, AWS adds read-only permissions for new operations and resources. For a list and descriptions of job function policies, see [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*.

## AWS managed policy: AmazonRoute53GlobalResolverReadOnlyAccess
<a name="security-iam-awsmanpol-AmazonRoute53GlobalResolverReadOnlyAccess"></a>

You can attach the `AmazonRoute53GlobalResolverReadOnlyAccess` policy to your IAM identities.

This policy grants read-only permissions that allow principals to view and list Route 53 Global Resolver resources without the ability to modify them.

**Permissions details**

This policy includes the following permissions.
+ `route53globalresolver` – Allows principals to retrieve and list all Route 53 Global Resolver resources including access sources, access tokens, DNS views, firewall domain lists, firewall rules, global resolvers, hosted zone associations, and managed firewall domain lists.

To view more details about the policy, including the latest version of the JSON policy document, see [AmazonRoute53GlobalResolverReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonRoute53GlobalResolverReadOnlyAccess.html) in the *AWS Managed Policy Reference Guide*.

## AWS managed policy: AmazonRoute53GlobalResolverFullAccess
<a name="security-iam-awsmanpol-AmazonRoute53GlobalResolverFullAccess"></a>

You can attach the `AmazonRoute53GlobalResolverFullAccess` policy to your IAM identities.

This policy grants full administrative permissions that allow principals to create, read, update, and delete all Route 53 Global Resolver resources and configurations.

**Permissions details**

This policy includes the following permissions.
+ `ec2` – Allows principals to describe Amazon EC2 regions to support cross-region Route 53 Global Resolver operations.
+ `route53` – Allows principals to get and list hosted zones for integration with Route 53 Global Resolver DNS views.
+ `route53globalresolver` – Allows principals to perform all administrative operations on Route 53 Global Resolver resources including creating, updating, and deleting access sources, access tokens, DNS views, firewall domain lists, firewall rules, global resolvers, and hosted zone associations.

To view more details about the policy, including the latest version of the JSON policy document, see [AmazonRoute53GlobalResolverFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonRoute53GlobalResolverFullAccess.html) in the *AWS Managed Policy Reference Guide*.

## Route 53 Global Resolver updates to AWS managed policies
<a name="security-iam-awsmanpol-updates"></a>

View details about updates to AWS managed policies for Route 53 Global Resolver since this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed on the Route 53 Global Resolver Document history page.

| Change | Description | Date |
| --- | --- | --- |
| [AmazonRoute53GlobalResolverFullAccess](#security-iam-awsmanpol-AmazonRoute53GlobalResolverFullAccess) – New policy | Route 53 Global Resolver added a new policy to allow full administrative access to Route 53 Global Resolver resources.<br />This policy grants permissions to create, read, update, and delete all Route 53 Global Resolver resources including access sources, access tokens, DNS views, firewall domain lists, firewall rules, global resolvers, and hosted zone associations. | February 5, 2026 |
| [AmazonRoute53GlobalResolverReadOnlyAccess](#security-iam-awsmanpol-AmazonRoute53GlobalResolverReadOnlyAccess) – New policy | Route 53 Global Resolver added a new policy to allow read-only access to Route 53 Global Resolver resources.<br />This policy grants permissions to retrieve and list all Route 53 Global Resolver resources including access sources, access tokens, DNS views, firewall domain lists, firewall rules, global resolvers, hosted zone associations, and managed firewall domain lists. | January 7, 2026 |
| Route 53 Global Resolver started tracking changes | Route 53 Global Resolver started tracking changes for its AWS managed policies. | MONTH dd, YYYY |

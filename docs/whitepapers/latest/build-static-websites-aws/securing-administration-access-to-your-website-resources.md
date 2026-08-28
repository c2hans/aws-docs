---
source_url: https://docs.aws.amazon.com/whitepapers/latest/build-static-websites-aws/securing-administration-access-to-your-website-resources.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Securing administration access to your website resources
<a name="securing-administration-access-to-your-website-resources"></a>

 Under the AWS shared responsibility model, the responsibility for a secure website is shared between AWS and the customer (you). AWS provides a global secure infrastructure and foundation compute, storage, networking, and database services, as well as higher level services. AWS also provides a range of security services and features that you can use to secure your assets.

 As an AWS customer, you’re responsible for protecting the confidentiality, integrity, and availability of your data in the cloud, and for meeting your specific business requirements for information protection. We strongly recommend working closely with your Security and Governance teams to implement the recommendations in this whitepaper.

 A benefit of using Amazon S3 and Amazon CloudFront as a serverless architecture is that the security model is also simplified. You have no operating system to harden, servers to patch, or software vulnerabilities to generate concern. Also, S3 offers security options such as [server-side data encryption](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingServerSideEncryption.html) and access control lists. This results in a significantly reduced surface area for potential attacks.

## Managing administrator privileges
<a name="managing-administrator-privileges"></a>

 Enforcing the principle of *least privilege* is a critical part of a [security and governance](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) strategy. In most organizations, the team in charge of DNS configurations is separate from the team that manages web content. You should grant users appropriate levels of permissions to access only the resources they need. In AWS, you can use IAM to lock down permissions.

 You can create multiple IAM users under your AWS account, each with their own login and password. (The AWS account is the account that you create when you first sign up for AWS. Each AWS account has root permissions to all AWS resources and services. The best practice is to enable multi-factor authentication (MFA) for your root account, and then lock away the root credentials so that no person or system uses the root credentials directly for day-to-day operations. Instead, create IAM groups and IAM users for the day-to-day operations.)

 An IAM user can be a person, service, or application that requires access to your AWS resources (in this case, Amazon S3 buckets, Amazon CloudFront distributions, and Amazon Route 53 hosted zones) through the AWS Management Console, command line tools, or APIs. You can then organize them into IAM groups based on functional roles. When an IAM user is placed in an IAM group, it inherits the group’s permissions.

 The fine-grained policies of IAM allow you to grant administrators the minimal privileges needed to accomplish their tasks. The permissions can be scoped to specific Amazon S3 buckets and Amazon Route 53 hosted zones.

 The following is an example *separation of duties*: IAM configuration can be managed by:
+  Super\_Admins

 Amazon Route 53 configuration can be managed by:
+  Super\_Admins
+  Network\_Admins

 CloudFront configuration can be managed by:
+  Super\_Admins
+  Network\_Admins
+  Website\_Admin

 Amazon S3 configuration can be managed by:
+  Super\_Admins
+  Website\_Admin

 Amazon S3 content can be updated by:
+  Super\_Admins
+  Website\_Admin
+  Website\_Content\_Manager

 An IAM user can belong to more than one IAM group. For example, if someone must manage both Amazon Route 53 and Amazon S3, that user can belong to both the *Network\_Admins* and the *Website\_Admins* groups.

 The best practice is to require all IAM users to rotate their IAM passwords periodically. Multi-factor authentication (MFA) should be enabled for any account with administrator privileges.

## Auditing API calls made in your AWS account
<a name="auditing-api-calls-made-in-your-aws-account"></a>

 You can use AWS CloudTrail to see an audit trail for API activity in your AWS account. Toggle it on for all AWS Regions, and the audit logs will be deposited to an Amazon S3 bucket. You can use the AWS Management Console to search against API activity history. Or, you can use a third-party log analyzer to analyze and visualize the CloudTrail logs.

 You can also build a custom analyzer. Start by configuring CloudTrail to send the data to Amazon CloudWatch Logs. CloudWatch Logs allows you to create automated rules that notify you of suspicious API activity. CloudWatch Logs also has seamless integration with OpenSearch Service, and you can configure the data to be automatically streamed over to a managed OpenSearch Service cluster. Once the data is in OpenSearch Service, users can query against that data directly or visualize the analytics using a Kibana dashboard.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

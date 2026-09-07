---
source_url: https://docs.aws.amazon.com/whitepapers/latest/setting-up-multi-user-environments/setting-up-scenario-2-limited-user-access-to-aws-management-console-within-a-single-account.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Setting up scenario 2: Limited user access to AWS Management Console within a single account
<a name="setting-up-scenario-2-limited-user-access-to-aws-management-console-within-a-single-account"></a>

 For this scenario, the administrator creates IAM users and gives each user unique access credentials. With IAM, an administrator can securely control access to AWS services and resources.

 The administrator can create and manage AWS users and groups, and use permissions to allow and deny access to AWS resources. Users can log into the AWS Management Console or AWS Command Line Interface and launch and access different AWS services, subject to the access control policies applied to their account. Users have direct control over the access credentials for their resources.

 By default, when you create IAM users, they don’t have access to any AWS resources. You must explicitly grant them permissions to access the resources that they need for their work. Permissions are rights that you grant to a user or group to let the user perform tasks in AWS. Permissions are attached to an IAM principal or an [AWS Single Sign-On](https://aws.amazon.com/single-sign-on/) (SSO) permission set, and let the administrator specify what that user can do.

 Depending on the context, administrators may be able to construct resource-level permissions for users that control the actions the user is allowed to take for specific resources (for example, limiting which instance the user is allowed to end).

 For an overview of IAM permissions, see [Controlling access to AWS resources using policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/PermissionsOverview.html) in the [AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/IAM_Introduction.html) documentation, and read [Resource-Level Permissions for EC2–Controlling Management Access on Specific Instances](http://blogs.aws.amazon.com/security/post/Tx29HCT3ABL7LP3/Resource-level-Permissions-for-EC2-Controlling-Management-Access-on-Specific-Ins) on the AWS Security Blog.

 To define permissions, administrators use *policies*, which are documents in JSON format. A policy consists of one or more statements, each of which describes one set of permissions. Policies can be attached to IAM users, groups, or roles. [AWS Policy Generator](https://awspolicygen.s3.amazonaws.com/policygen.html) is a handy tool that lets administrators create policies easily.

 For example policies that are relevant to multi-user environments, see [Appendix B: Example IAM user policies](appendix-b.md).

 For more information about policies, see [Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/PoliciesOverview.html).

 A useful option in this scenario is for the administrator to tag resources and write appropriate resource-level permissions to limit IAM users to specific actions and resources. A tag is a label you assign to an AWS resource. For services that support tagging, apply tags using the AWS Management Console, AWS Command Line Interface, or API requests. This approach enables fine-grained control to which resources a user can access, and what actions they can take on those resources.

 The administrator will also need to write policies to prevent users from manipulating the resource tags. For example, for [Amazon EC2 tags,](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html) the administrator should disable the `ec2:CreateTags` and `ec2:DeleteTags` actions.

 This scenario is also good for use cases that require collaboration among users. As described previously, a user can give other IAM users access to specific actions on their resources using a mix of user-level and resource-level permissions. A good example is a collaborative research project where students allow other members of their team access to software in their Amazon EC2 instances and data stored in their Amazon S3 buckets.

 This scenario can be useful when the users need to access the AWS Management Console, launch new services, interact with services for complicated cloud-based application architectures, or exercise more control over accessing and sharing resources. The following figure shows the architecture for this scenario.

![Diagram showing limited user access to AWS Management Console](https://docs.aws.amazon.com/whitepapers/latest/setting-up-multi-user-environments/images/limited-user-access-to-console.png)

 As shown in the preceding figure, this scenario works well with a single AWS account. The administrator needs to create IAM users and groups to apply access control policies for the environment. Example IAM user policies for setting up this scenario are described in [Appendix B: Example IAM user policies](appendix-b.md).

## Account setup
<a name="account-setup-1"></a>

 The administrator creates one AWS account for the group. For example, this can be a shared account for a professor, class, department, or school. An existing AWS account can also be used. New AWS account signup and access to existing AWS accounts is available on the [Account](https://aws.amazon.com/account/) page.

 The administrator then creates an IAM user for each user with the AWS Management Console, AWS Command Line Interface, or AWS API. These IAM users can belong to one or more IAM groups within a single AWS account.

 Alternatively, the administrator can deploy SSO and create an SSO user for each student, teaching assistant, or professor. This approach allows users to log into the account through federation. Each SSO user can have one or more permission sets assigned to them, depending on the role that they need to assume to log into the account.

 Based on environment requirements, the administrator attaches custom policies to IAM users or IAM groups to restrict certain AWS resources that can be launched and used. Thus, users can only launch AWS services for which permissions have been granted. Users are provided credentials for their IAM user, which can be used to log in to the AWS Management Console, access AWS services, and call APIs.

### Information required for account setup
<a name="information-required-for-account-setup"></a>

 To create an account and set up IAM-based access control, an administrator needs the following information:
+  An AWS account for the group. This account could belong to the school, department, or professor. If no account exists, a new account must be created.
+  Name and email address of the user.
+  Required AWS resources and services and the operations permitted on them. This is required to determine the access control policies to be applied to each IAM user.
+  Contact information for the billing reports and alerts.
+  Contact information for the usage reports and alerts.

### Providing access to users
<a name="providing-access-to-users"></a>

 With SSO, the administrator can use the sample IAM policies from [Appendix B](appendix-b.md) to [create custom permission sets](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) to assign to each group of users using the IAM user policies.

 Next, the administrator needs to create an AWS SSO user for each of the students, and assign each user to the relevant permission set. Students then can log in using the AWS SSO Sign-in URL. See this [Basic AWS SSO Configuration](https://www.youtube.com/watch?v=li_ISe96K9E) video tutorial.

 For basic instructions on how to add IAM user policies, see [Appendix A: Adding IAM user policies](appendix-a.md).

 For example, IAM user policies for setting up this scenario, see [Appendix B: Example IAM user policies](appendix-b.md).

 If the administrator decides not to use SSO, they can add IAM users with roles and custom policies to the AWS account directly, to implement required access control logic for the different kinds of users in the group. The administrator then provides the IAM user login information to the corresponding members of the group.

## Cost tracking
<a name="cost-tracking-1"></a>

 All users can tag their resources for services with tagging capability. With the cost allocation feature of AWS Account Billing, the administrator can track AWS costs for each user.

 For more information, see [Using Cost Allocation Tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) in the [AWS Account Billing](https://docs.aws.amazon.com/awsaccountbilling/latest/about/welcome.html) documentation.

## Monitoring resources
<a name="monitoring-resources-1"></a>

 AWS Budgets can help monitor AWS resources. Billing alerts automatically notify users whenever the estimated charges on their current AWS bill reach a threshold they define. Users can choose to receive an alert on their total AWS charges or charges for a specific AWS product or service. If the account has any limits, the administrator can use these as the threshold for sending billing alerts.

 For more information about setting up billing alerts with AWS Budgets, see [Best practices for controlling access to AWS Budgets](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/budgets-best-practices.html#budgets-best-practices-access).

## Reporting
<a name="reporting-1"></a>

 Detailed usage reports are available for the administrator from the AWS Management Console. Reports are available for monthly charges and also for account activity in hourly increments.

 For more information, see [Detailed Billing Reports](https://docs.aws.amazon.com/cur/latest/userguide/detailed-billing.html).

## Runtime environment
<a name="runtime-environment-1"></a>

 Users can log into the AWS Management Console (as an IAM user or with an AWS SSO user) with the login information provided to them by the administrator. They can launch and use resources defined by the rules and policies set by the administrator. For example, if they have the appropriate permissions, they can launch new Amazon EC2 instances or create new Amazon S3 buckets, upload data to them, and share them with others.

 An IAM user might be granted access to create a resource, but the user's permissions, even for that resource, are limited to what's been explicitly granted by the administrator. The administrator can also revoke the user's permission at any time. Setting proper resource and user-based permissions helps prevent an IAM user from taking actions on resources belonging to other IAM users in the AWS account. For example, an IAM user can be prevented from terminating instances belonging to other IAM users in the AWS account.

 For more information, see [Controlling access to AWS resources using policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/PermissionsOverview.html).

## Clean up the environment
<a name="clean-up-the-environment-1"></a>

 When users have finished their work or when the account limits are reached, they (or the administrator) can end the AWS resources. Administrators can also delete the IAM users. If an instance of SSO was created for the users to log in, the directory should be disabled. The users will lose their work unless they take steps to save it (a procedure that is beyond the scope of this whitepaper).

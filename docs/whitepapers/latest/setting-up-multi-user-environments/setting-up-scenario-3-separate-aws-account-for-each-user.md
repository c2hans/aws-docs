---
source_url: https://docs.aws.amazon.com/whitepapers/latest/setting-up-multi-user-environments/setting-up-scenario-3-separate-aws-account-for-each-user.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Setting up Scenario 3: Separate AWS account for each user
<a name="setting-up-scenario-3-separate-aws-account-for-each-user"></a>

 In this scenario, an administrator creates separate AWS accounts for each user who needs a new AWS account. These accounts can optionally be combined into a single AWS Organization, and a single AWS account can be designated as the management account, using [AWS Organizations](https://aws.amazon.com/organizations/). After the student accounts become members of the Organization, the management account can become the payer account and all the accounts can benefit from [consolidated billing,](https://docs.aws.amazon.com/awsaccountbilling/latest/about/consolidatedbilling.html) which provides a single bill for multiple AWS accounts. The administrator then creates an IAM user in each AWS account and applies an access control policy to each user. Users are given access to the IAM user within their AWS account, but do not have access to the AWS account root user.

 The administrator should deploy SSO in the management account to create users to grant access to each account through federation centrally. This allows the accounts to be managed by an administrator, consistent with the required policies for the user environment.

 Users can log into the AWS Management Console with their IAM credentials and then launch and access different AWS services, subject to the access control policies applied to their account. Since students have access to their individual accounts, they have direct control over the access credentials for their resources (such as the creation and deletion of SSH keys), and they can also share these resources with other users and accounts as needed.

 This scenario is good for setting up collaborative multi-user work environments. To implement it, users can create an IAM role, which is an entity that includes permissions, that isn't associated with a specific user. Users from other accounts can then assume the role and access resources according to the permissions assigned to the role.

 For more information, see [Roles terms and concepts](https://docs.aws.amazon.com/IAM/latest/UserGuide/cross-acct-access.html).

 This scenario offers maximum flexibility for users and is helpful when they need to access the AWS Management Console to launch new services. TIt also gives users flexibility in working with complicated cloud-based application architectures and more control over accessing and sharing their resources.

 Having separate AWS accounts for each user works well for both short-term and long-term usage. For short-term usage, AWS resources, IAM users, and even AWS accounts can be terminated after the work is done. For long-term usage, the AWS accounts for some or all users are kept alive at the end of the current engagement. All work done can be easily preserved for future use.

 Users can also be provided full administrator access to their AWS account (besides the IAM-based access they initially had) to continue their work. For example, consider an entrepreneurship class where some students might develop new solutions or intellectual property using AWS resources that they want to retain for future use or for immediate deployment. Their work can be easily turned over to them by giving them full access to their AWS account.

 Another benefit of this scenario is that in the AWS Management Console, users cannot see resources belonging to any other users in the group, since each user is working from their own AWS account. The following figure shows the architecture for this scenario.

![Diagram showing separate AWS account for each user](http://docs.aws.amazon.com/whitepapers/latest/setting-up-multi-user-environments/images/separate-aws-account-per-user.png)

## Account setup
<a name="account-setup-2"></a>

 The administrator deploys AWS Organizations in the management accounts, then provisions an AWS account for each user in the group. Independent AWS accounts (with unique AWS account IDs) are created for each user.

 The administrator creates the accounts using the AWS Organizations [`CreateAccount` API](https://docs.aws.amazon.com/organizations/latest/APIReference/API_CreateAccount.html), which creates an account that requires the credentials of the AWS account root user to be reset.

 In the management account, the administrator deploys AWS SSO, and creates an AWS SSO user for each of users that requires access to the AWS accounts. Based on the environment requirements, the AWS SSO users are assigned to their relevant AWS SSO permission sets, that are customized with IAM policies, allowing each user to only use the services for which permissions have been granted.

 Alternatively, the administrator can create an IAM user in each user’s AWS account. Based on environment requirements, custom policies are attached to IAM users individually to constrain AWS resources that can be launched and used. Users can only launch AWS services for which permissions have been granted.

 Users are provided credentials to log into the AWS Management Console, access AWS services, and call APIs. Users do not have access to the root user credentials of the AWS account and cannot change the IAM access policies enforced on the account.

 Using AWS Organizations, an administrator can set up consolidated billing for the group. Consolidated billing (offered at no additional charge by AWS) enables consolidation of payment for multiple AWS accounts by designating a single payer account, the management account within the AWS Organization. Consolidated billing provides a combined view of AWS charges incurred by all accounts as well as a detailed cost report for each individual member AWS account associated with the management account.

 For detailed information about how to set up consolidated billing, see [Consolidated billing for AWS Organizations](https://docs.aws.amazon.com/awsaccountbilling/latest/about/consolidatedbilling.html).

 Another benefit from this scenario is that the administrator can set controls across every account using [service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) (SCPs) to restrict access to specific resources and services independently of the user’s permissions.

### Information required for account setup
<a name="information-required-for-account-setup-1"></a>

 The following information is required for creating accounts and setting up IAM-based access control:
+  AWS management account for the group. This account could belong to the school, department, or professor. If no account exists, a new account is created. This account is necessary for setting up AWS Organizations and consolidated billing.
+  Name and email addresses of users.
+  AWS account credentials for users who have existing AWS accounts that they want to use in this environment. These accounts will join the AWS Organization users who do not have an AWS account or do not want to use their existing account will need new accounts provisioned for them.
+  Required AWS resources and services and the operations permitted on them. This is required to determine the access control policies to be applied to each IAM user.
+  Contact information for the billing reports and alerts.
+  Contact information for the usage reports and alerts.

### Providing access to users
<a name="providing-access-to-users-1"></a>

 Using SSO, the administrator creates different [permissions sets](https://docs.aws.amazon.com/singlesignon/latest/userguide/permissionsetsconcept.html), which are custom IAM policies that can be used to grant resource access to the accounts within the AWS Organization to a specific user. Then the administrator creates an associated [SSO user](https://docs.aws.amazon.com/singlesignon/latest/userguide/authconcept.html), assigns it to the user’s account, and attaches a permission set to that user, based on the level of permissions that the user needs.

 In this case, there could be a permission set for an administrator, a permission set for the teaching assistant, and a permission set for the students. Changes to the permissions will apply immediately to all the users using the same permission set in their account. Finally, the administrator can generate login credentials for each user, so they can access the accounts each user has access to through the SSO portal.

 For more information on how to manage access to your accounts and assign policies to your permission sets, see [Manage SSO to your AWS Accounts](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html). See this SSO Configuration [tutorial video](https://www.youtube.com/watch?v=li_ISe96K9E) to understand AWS SSO better.

 Alternatively, the administrator can add IAM users with roles and custom policies for each user in each AWS account to implement required access control logic for the different types of users in the group. Login information for the IAM users is provided to the corresponding users in the group.

 For basic instructions on how to add IAM user policies, see [Appendix A: Adding IAM user policies](appendix-a.md).

 For an example of setting up IAM user policies for this scenario, see [Appendix B: Example IAM user policies](appendix-b.md).

## Cost tracking
<a name="cost-tracking-2"></a>

 Consolidated billing makes it easy to track AWS costs because it shows the administrator a combined view of charges incurred by all AWS accounts, as well as a detailed cost report for each individual AWS account within the organization. [Consolidated billing](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html) is included with AWS Organizations, where the management account pays the charges of all member accounts.

 All users can also tag their resources for services with tagging capability. An administrator can then use the cost allocation feature of AWS Account Billing to track AWS costs for each user.

 For more information, see [Using Cost Allocation Tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) and [Viewing your bill](https://docs.aws.amazon.com/awsaccountbilling/latest/about/getbill.html#allocation) in the [AWS Billing and Cost Management and Cost Management](https://docs.aws.amazon.com/awsaccountbilling/latest/about/welcome.html) documentation.

## Monitoring resources
<a name="monitoring-resources-2"></a>

 AWS Budgets alerts can help monitor AWS resources. Billing alerts can automatically notify users whenever the estimated charges on their current AWS bill reach a threshold they define. Users can choose to receive an alert on their total AWS charges or charges for a specific AWS product or service. If the account has any limits, the administrator can use these as the threshold for sending billing alerts.

 For more information about setting up billing alerts with AWS Budgets, see [Best practices for controlling access to AWS Budgets](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/budgets-best-practices.html#budgets-best-practices-access).

## Reporting
<a name="reporting-2"></a>

 Detailed usage reports are available for administrators from the AWS Management Console. Reports are available for monthly charges as well as for account activity in hourly increments.

 For more information, see [Detailed Billing Reports](https://docs.aws.amazon.com/cur/latest/userguide/detailed-billing.html).

## Runtime environment
<a name="runtime-environment-2"></a>

 Users can log into the AWS Management Console as an IAM user with the login information provided to them by the administrator. They can launch and use resources defined by the rules and policies set by the administrator. For example, if they have the appropriate permissions, users can launch new Amazon EC2 instances or create new Amazon S3 buckets, upload data to them, and share them with others.

 Because accounts are independent, each user sees only their own AWS resources in the AWS Management Console.

## Clean up the environment
<a name="clean-up-the-environment-2"></a>

 When the users have finished their work or when the account limits are reached, they (or the administrator) can optionally terminate the AWS services. The administrator can also delete the IAM users or the SSO users and revoke the access to the account.

 When the account is no longer in use, it can be closed, ending all the resources within the account.

## Keeping accounts alive
<a name="keeping-accounts-alive"></a>

 If the users want to retain their AWS accounts, they can request the root user account credentials from their administrator. The administrator would remove the account from the Organization and users would need to provide their own billing information. The users will get login and security credentials to their AWS account.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/whitepapers/latest/setting-up-multi-user-environments/scenario-1-chapter.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Setting up Scenario 1: Individual server environments
<a name="scenario-1-chapter"></a>

 With this scenario, users are provided access credentials to AWS resources. Users cannot access the AWS Management Console or launch new services. They receive the credentials to access specific AWS services that have already been launched by an administrator.

 This scenario is a good match for simpler use cases in which users do not need to launch new AWS services. The following figure shows the architecture for this scenario.

![Diagram showing individual server environments](https://docs.aws.amazon.com/whitepapers/latest/setting-up-multi-user-environments/images/individual-server-environments.png)

 An administrator can give users their own unique SSH keys for Linux and password for Windows for security and separation between users. For labs that do not require security among users (such as collaborative labs), the administrator can keep the keys or access credentials common for all the servers, and provide the unique access public DNS names of instances to the users. The administrator can choose the level of security and management appropriate for their needs.

## Account setup
<a name="account-setup"></a>

 The administrator creates an AWS account for the user group. For example, this can be a shared account for a professor, class, department, or school. The administrator can also use an existing AWS account. New AWS account signup and access to existing AWS accounts is available on your [Account](https://aws.amazon.com/account/) page.

 The administrator launches the required AWS services for each user, and provides resource access credentials to the users.

## Cost tracking
<a name="cost-tracking"></a>

 If needed, the administrator tags the resources launched for different users. Cost allocation and resource tagging can help track usage by different users.

 For more information, see [Using Cost Allocation Tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) in the [AWS Billing and Cost Management and Cost Management](https://docs.aws.amazon.com/awsaccountbilling/latest/about/welcome.html) documentation.

## Monitoring resources
<a name="monitoring-resources"></a>

 The administrator can set up [AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/) to monitor AWS resources. They can create billing alerts that automatically notify the designated recipient whenever the estimated AWS charges reach a specified threshold. The administrator can choose to receive an alert on the total AWS charges, or on charges for a specific AWS product or service. If the account has any limits, the administrator can use these as the threshold for receiving billing alerts.

 For more information about setting up billing alerts with AWS Budgets, see [Best practices for controlling access to AWS Budgets](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/budgets-best-practices.html#budgets-best-practices-access) .

## Reporting
<a name="reporting"></a>

 Detailed usage reports are available for the administrator from the AWS Management Console. Reports are available for monthly charges and also for account activity in hourly increments.

 For more information, see [Detailed Billing Reports](https://docs.aws.amazon.com/cur/latest/userguide/detailed-billing.html) in the [AWS Billing and Cost Management and Cost Management](https://docs.aws.amazon.com/awsaccountbilling/latest/about/welcome.html) documentation.

## Runtime environment
<a name="runtime-environment"></a>

 After the administrator provisions the account and launches the required AWS services, users can access their AWS resources using the provided credentials. For example, if Amazon EC2 instances are part of the class, users would be given keys or passwords to SSH (in Linux instances), or RDP (in Windows instances). Users would not have the credentials to log into the AWS Management Console, or to launch any new services.

## Clean up the environment
<a name="clean-up-the-environment"></a>

 When users have finished their work, or when the account limits are reached, the administrator can end the AWS resources. Because student users do not have their own AWS accounts, ending the launched services ensures that user work is deleted and no further charges are made.

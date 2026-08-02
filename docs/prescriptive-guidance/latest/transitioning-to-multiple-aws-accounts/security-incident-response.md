---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/transitioning-to-multiple-aws-accounts/security-incident-response.html
---

# Security incident response
<a name="security-incident-response"></a>

As you transition to multiple AWS accounts, it is important that you maintain visibility into security events that might occur within your organization. In [Identity management and access control](identity-management.md), you used AWS Control Tower to set up your landing zone. During that setup process, AWS Control Tower designated an AWS account for security. You should delegate administration of security services into the **security-tooling-prod** account and use this account to centrally managed these services.

This guide reviews the use of the following AWS services to help protect your AWS accounts and organization:
+ [Amazon GuardDuty](#amazon-guardduty)
+ [Amazon Macie](#amazon-macie)
+ [AWS Security Hub CSPM](#amazon-security-hub)

## Amazon GuardDuty
<a name="amazon-guardduty"></a>

[Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html) is a continuous security monitoring service that analyzes data sources, such as AWS CloudTrail event logs. For a complete list of supported data sources, see [How Amazon GuardDuty uses its data sources](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_data-sources.html#guardduty_vpc) (GuardDuty documentation). It uses threat intelligence feeds, such as lists of malicious IP addresses and domains, and machine learning to identify unexpected and potentially unauthorized and malicious activity within your AWS environment.

When you use GuardDuty with AWS Organizations, the management account in the organization can designate any account in the organization to be the GuardDuty *delegated administrator*. The delegated administrator becomes the GuardDuty administrator account for the AWS Region. GuardDuty is automatically enabled in that Region, and the delegated administrator account has permissions to enable and manage GuardDuty for all accounts in the organization within that Region. For more information, see [Managing GuardDuty accounts with AWS Organizations](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_organizations.html) (GuardDuty documentation).

GuardDuty is a regional service. This means that you must enableGuardDuty in each Region that you want to monitor.

### Best practices
<a name="best-practices.dca00583-a43a-5a49-9ba3-3d12925b1dcc"></a>
+ Enable GuardDuty in all supported AWS Regions. GuardDuty can generate findings about unauthorized or unusual activity, even in Regions that you aren't actively using. Pricing for GuardDuty is based on the number of analyzed events. Even in Regions where you aren't operating workloads, enabling GuardDuty is an effective and cost-efficient detection tool to alert you about potentially malicious activity. For more information about the Regions where GuardDuty is available, see [Amazon GuardDuty service endpoints](https://docs.aws.amazon.com/general/latest/gr/guardduty.html#guardduty_region) (AWS General Reference).
+ Within every Region, delegate the **security-tooling-prod** account to administer GuardDuty for your organization. For more information, see [Designating a GuardDuty delegated administrator](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_organizations.html#delegated-admin-designate) (GuardDuty documentation).
+ Configure GuardDuty to automatically enroll new AWS accounts as they are added to the organization. For more information, see *Step 3 - automate the addition of new organization accounts as members* in [Managing accounts with AWS Organizations](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_organizations.html#delegated-admin-designate) (GuardDuty documentation).

## Amazon Macie
<a name="amazon-macie"></a>

[Amazon Macie](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html) is a fully managed data security and data privacy service that uses machine learning and pattern matching to help you discover, monitor, and protect sensitive data in Amazon Simple Storage Service (Amazon S3). You can export data from Amazon Relational Database Service (Amazon RDS) and Amazon DynamoDB an S3 bucket and then use Macie to scan the data.

When you use Macie with AWS Organizations, the management account in the organization can designate any account in the organization to be the Macie *administrator account*. The administrator account can enable and manage Macie for the member accounts in the organization, can access Amazon S3 inventory data, and can run sensitive data discovery jobs for the accounts. For more information, see [Managing accounts with AWS Organizations](https://docs.aws.amazon.com/macie/latest/user/accounts-mgmt-ao.html) (Macie documentation).

Macie is a regional service. This means that you must enable Macie in each Region that you want to monitor and that the Macie administrator account can manage member accounts only within the same Region.

### Best practices
<a name="best-practices.2a48be74-b380-5308-b015-d69e5def108e"></a>
+ Adhere to the [Considerations and recommendations for using Macie with AWS Organizations](https://docs.aws.amazon.com/macie/latest/user/accounts-mgmt-ao-notes.html) (Macie documentation).
+ Within every Region, delegate the **security-tooling-prod** account to administer Macie for your organization. To centrally manage Macie accounts in multiple AWS Regions, the management account must log in to each Region where the organization currently uses or will use Macie, and then designate the Macie administrator account in each of those Regions. The Macie administrator account can then configure the organization in each of those Regions. For more information, see [Integrating and configuring an organization](https://docs.aws.amazon.com/macie/latest/user/accounts-mgmt-ao-integrate.html) (Macie documentation).
+ Macie provides a [monthly free tier](https://docs.aws.amazon.com/macie/latest/user/account-mgmt-costs-calculations.html) for sensitive data discovery jobs. If you might have sensitive data stored in Amazon S3, use Macie to analyze your S3 buckets as part of the monthly free tier. If you exceed the free tier, sensitive data discovery charges begin to accrue for your account.

## AWS Security Hub CSPM
<a name="amazon-security-hub"></a>

[AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) provides you with a comprehensive view of your security state in AWS. You can use it to check your environment against security industry standards and best practices. Security Hub CSPM collects security data from across all of your AWS accounts, services (including GuardDuty and Macie), and supported third-party partner products. Security Hub CSPM helps you analyze security trends and identify the highest priority security issues. Security Hub CSPM provides various security standards that you can enable to perform compliance checks in each AWS account.

When you use Security Hub CSPM with AWS Organizations, the management account in the organization can designate any account in the organization to be the Security Hub CSPM *administrator account*. The Security Hub CSPM administrator account can then enable and manage other member accounts in the organization. For more information, see [Using AWS Organizations to manage accounts](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-prereq-orgs.html) (Security Hub CSPM documentation).

Security Hub CSPM is a regional service. This means that you must enable Security Hub CSPM in each Region that you want to analyze, and in AWS Organizations, you must define the delegated administrator for each Region.

### Best practices
<a name="best-practices.64a38cc6-98e6-5583-a857-f69a88578d57"></a>
+ Adhere to the [Prerequisites and recommendations](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-setup-prereqs.html) (Security Hub CSPM documentation).
+ Within every Region, delegate the **security-tooling-prod** account to administer Security Hub CSPM for your organization. For more information, see [Designating a Security Hub CSPM administrator account](https://docs.aws.amazon.com/securityhub/latest/userguide/designate-orgs-admin-account.html) (Security Hub CSPM documentation).
+ Configure Security Hub CSPM to automatically enroll new AWS accounts when they are added into the organization.
+ Enable the [AWS Foundational Security Best Practices standard](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards-fsbp.html) (Security Hub CSPM documentation) to detect when resources deviate from security best practices.
+ Enable [Cross-Region aggregation](https://docs.aws.amazon.com/securityhub/latest/userguide/finding-aggregation.html) (Security Hub CSPM documentation) so that you can view and manage all of your Security Hub CSPM findings from a single Region.

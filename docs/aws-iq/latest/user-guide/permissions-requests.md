---
source_url: https://docs.aws.amazon.com/aws-iq/latest/user-guide/permissions-requests.html
---

End of support notice: On May 28, 2026, AWS will end support for AWS IQ. After May 28, 2026, you will no longer be able to access the AWS IQ console or AWS IQ resources. For more information, see [AWS IQ end of support](https://docs.aws.amazon.com/aws-iq/latest/experts-user-guide/aws-iq-end-of-support.html) in the *AWS IQ User Guide for Experts*.

# Permissions requests in AWS IQ
<a name="permissions-requests"></a>

In AWS IQ, an expert might request a permissions policy to access your AWS account and complete the necessary work. The level of access required depends on the scope of the project. AWS IQ simplifies the process of granting access to experts, which allows experts to implement projects in your account.

AWS IQ creates an IAM role for the expert to use for the duration of the proposal. You can view AWS CloudTrail logs of the expert's activity in your account and can revoke access at any time. Access is automatically revoked at the completion of the proposal, when the final payment is made.

An expert might also include details about why they're requesting a level of permissions. You can review the information in the permission request. To get started, choose the permission request in the AWS IQ console and then choose **Accept** or **Decline**.

**Tip**
It is an AWS security best practice to grant the least amount of privileges necessary to perform a task. If you think the expert is requesting an inappropriate level of access, you should decline the request. Learn more about [Granting least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) in the *AWS Identity and Access Management User Guide*.

## Permission levels in AWS IQ
<a name="permissions-levels"></a>

The following AWS Identity and Access Management permission levels are available for an expert to request in AWS IQ:

**AdministratorAccess**
Provides full access to AWS services and resources. For more information, see [Viewing CloudTrail logs in AWS IQ](#viewing-cloudtrail-logs) and [AWS Managed Policies for Job Functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html#jf_administrator) in the *AWS Identity and Access Management (IAM) User Guide*.

**Billing**
Grants permission for billing and cost management. This includes viewing account usage and viewing and modifying budgets and payment methods. For more information, see [AWS Managed Policies for Job Functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html#jf_accounts-payable) in the *IAM User Guide*.

**DatabaseAdministrator**
Grants permission to AWS services and actions required to set up and configure AWS database services. For more information, see [AWS Managed Policies for Job Functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html#jf_database-administrator) in the *IAM User Guide*.

**NetworkAdministrator**
Grants permission to AWS services and actions required to set up and configure AWS network resources. For more information, see [AWS Managed Policies for Job Functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html#jf_network-administrator) in the *IAM User Guide*.

**PowerUserAccess**
Grants permission to AWS services and resources but doesn't allow management of users and groups. For more information, see [AWS Managed Policies for Job Functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html#jf_developer-power-user) in the *IAM User Guide*.

**SecurityAudit**
Grants permission to read security configuration metadata. This is useful for software that audits the configuration of an AWS account. For more information, see [AWS Managed Policies for Job Functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html#jf_security-auditor) in the *IAM User Guide*.

**SupportUser**
Grants permission to troubleshoot and resolve issues in an AWS account. This policy also enables the user to contact Support to create and manage cases. For more information, see [AWS Managed Policies for Job Functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html#jf_support-user) in the *IAM User Guide*.

**SystemAdministrator**
Grants permission for resources that are required for application and development operations. For more information, see [AWS Managed Policies for Job Functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html#jf_system-administrator) in the *IAM User Guide*.

**ViewOnlyAccess**
Grants permission to view resources and basic metadata across all AWS services. For more information, see [AWS Managed Policies for Job Functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html#jf_view-only-user) in the *IAM User Guide*.

**Tip**
If you prefer, you can grant access to your expert independent of AWS IQ. This access isn't revoked automatically.

## Viewing CloudTrail logs in AWS IQ
<a name="viewing-cloudtrail-logs"></a>

You can view AWS CloudTrail logs of activities taken by using the **AdministratorAccess** IAM role in your AWS account.

**To view CloudTrail logs in AWS IQ**

1. Sign in to the [AWS IQ console](https://iq.aws.amazon.com).

1. From the right menu, locate your **request** and the associated **proposal** card.

1. Choose the **permission request** and then select the **Activity** tab.

**Note**
The logs may experience a delay.

## Revoking permission in AWS IQ
<a name="revoking-permission"></a>

If you grant an expert permission to access your AWS environment, permission is automatically revoked when the proposal is complete. You can also revoke permissions manually using the following process.

**To revoke permissions manually**

1. From the **Permission** page in the AWS IQ console, select your **permission request**.

1. Choose **Revoke**.

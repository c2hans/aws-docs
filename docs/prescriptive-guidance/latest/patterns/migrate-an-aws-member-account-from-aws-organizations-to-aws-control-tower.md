---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-aws-member-account-from-aws-organizations-to-aws-control-tower.html
---

# Migrate an AWS member account from AWS Organizations to AWS Control Tower
<a name="migrate-an-aws-member-account-from-aws-organizations-to-aws-control-tower"></a>

*Rodolfo Jr. Cerrada, Amazon Web Services*

## Summary
<a name="migrate-an-aws-member-account-from-aws-organizations-to-aws-control-tower-summary"></a>

This pattern describes how to migrate an AWS account from AWS Organizations, where it is a member account that's governed by a management account, to AWS Control Tower. By enrolling the account in AWS Control Tower, you can take advantage of preventive and detective controls and features that streamline your account governance. You might also want to migrate your member account if your AWS Organizations management account has been compromised, and you want to move member accounts to a new organization that is governed by AWS Control TowerAWS Control Tower.

AWS Control Tower provides a framework that combines and integrates the capabilities of several other AWS services, including AWS Organizations, and ensures consistent compliance and governance across your multi-account environment. With AWS Control Tower, you can follow a set of prescribed rules and definitions that extend the capabilities of AWS Organizations. For example, you can use controls to ensure that security logs and necessary cross-account access permissions are created, and not altered.

## Prerequisites and limitations
<a name="migrate-an-aws-member-account-from-aws-organizations-to-aws-control-tower-prereqs"></a>

**Prerequisites **
+ An active AWS account
+ AWS Control Tower set up in your target organization in AWS Organizations (for instructions, see [Setting up](https://docs.aws.amazon.com/controltower/latest/userguide/setting-up.html) in the AWS Control Tower documentation)
+ Administrator credentials for AWS Control Tower (member of the **AWSControlTowerAdmins **group)
+ Administrator credentials for the source AWS account

**Limitations**
+ The source management account in AWS Organizations must be different from the target management account in AWS Control Tower.

**Product versions**
+ AWS Control Tower version 2.3 (February 2020) or later (see [release notes](https://docs.aws.amazon.com/controltower/latest/userguide/release-notes.html))

## Architecture
<a name="migrate-an-aws-member-account-from-aws-organizations-to-aws-control-tower-architecture"></a>

The following diagram illustrates the migration process and reference architecture. This pattern migrates the AWS account from the source organization to a target organization that is governed by AWS Control Tower.

![AWS Control Tower enrollment process for an AWS account that's migrated to another organization and moved to a registered OU.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/1fc2c2f0-fa5d-4068-a2b2-9e57cea2aff5/images/0654d242-0faa-4810-9e53-40ef89305b5b.png)

The enrollment process consists of these steps:

1. The target organization sends an invitation for the account to join the organization.

1. The account accepts the invitation and becomes a member of the target organization.

1. The account is enrolled in AWS Control Tower and moved to a registered organizational unit (OU). (We recommend that you check the AWS Control Tower dashboard to confirm the enrollment.) At this point, all controls that are enabled in the registered OU take effect.

## Tools
<a name="migrate-an-aws-member-account-from-aws-organizations-to-aws-control-tower-tools"></a>

**AWS services**
+ [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) is an account management service that enables you to consolidate multiple AWS accounts into a single entity (an *organization*) that you create and centrally manage.
+ [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html) integrates the capabilities of other services, including AWS Organizations, AWS IAM Identity Center, and AWS Service Catalog, to help you enforce and manage governance rules for security, operations, and compliance at scale across all your organizations and accounts in the AWS Cloud.

## Epics
<a name="migrate-an-aws-member-account-from-aws-organizations-to-aws-control-tower-epics"></a>

### Invite the account to join the new organization with AWS Control Tower
<a name="invite-the-account-to-join-the-new-organization-with-ctower"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Sign in to AWS Control Tower. | Sign in to the AWS Control Tower console as an administrator. <br />Currently, there is no direct way to move an AWS account from a source organization to an organization in an OU that's governed by AWS Control Tower. However, you can extend AWS Control Tower governance to an existing AWS account when you enroll it into an OU that's already governed by AWS Control Tower. That's why you have to log in to AWS Control Tower for this step. | AWS Control Tower administrator |
| Invite the member account. | 1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2), and navigate to the **AWS accounts** page. <br />2. On the **Add an AWS account** page, choose **Invite an existing AWS account**. <br />3. Complete the account information, including the 12-digit account number (without dashes) and the optional description and tags, and then choose **Send invitation**.Verify that no applications or network connectivity will be affected by the account transfer.This action sends an invitation email with a link to the member account. When the account administrator follows the link and accepts the invitation, the member account appears in the **AWS accounts **page. For more information, see [Managing account invitations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_invites.html) in the AWS Organizations documentation. | AWS Control Tower administrator |
| Test applications and connectivity. | When the member account has been registered into the new organization, it appears in the OU within a root. It also appears in the [AWS Control Tower console](https://console.aws.amazon.com/controltower), flagged as not enrolled in accounts, because it hasn't yet been enrolled in the AWS Control Tower registered OU.<br />Verify the following:+ Check the AWS Control Tower dashboard to see if there are any guardrail violations.<br />+ Check network connectivity (VPN or AWS Direct Connect) to make sure it wasn't affected by the transfer.<br />+ (Application owners) Test the applications that are associated with this account to verify that they run as expected, and that dependencies weren't affected by the account transfer. | AWS Control Tower administrator, Member account administrator, Application owners |

### Prepare the account for enrollment
<a name="prepare-the-account-for-enrollment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Review controls and fix any violations. | Review the controls that are defined in the target OU, especially the preventive controls, and fix any violations. <br />A number of [mandatory, preventive controls](https://docs.aws.amazon.com/controltower/latest/controlreference/preventive-controls.html) are enabled by default when you set up your AWS Control Tower landing zone. These can't be disabled. You must review these mandatory controls and fix the member account (manually or by using a script) before you enroll the account.Preventive controls keep AWS Control Tower registered accounts compliant and prevent policy violations. Any violation of preventive controls might affect enrollment. Detective control violations appear in the AWS Control Tower dashboard, if detected, after successful enrollment. They do not affect the enrollment process. For more information, see [About controls](https://docs.aws.amazon.com/controltower/latest/controlreference/controls.html) in the AWS Control Tower documentation. | AWS Control Tower administrator, Member account administrator |
| Check for connectivity issues after fixing control violations. | In some cases, you might have to close specific ports or disable services to fix control violations. Make sure that applications that use those ports and services are remediated before you enroll the account. | Application owner |

### Enroll the account into AWS Control Tower
<a name="enroll-the-account-into-ctowerlong"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Sign in to AWS Control Tower. | Sign in to the [AWS Control Tower console](https://console.aws.amazon.com/controltower). Use sign-in credentials that have administrative permissions for AWS Control Tower. Do not use the root user (management account) credentials to enroll an AWS Organizations account. This will display an error message. | AWS Control Tower administrator |
| Enroll the account. | 1. From the **Account Factory** page in AWS Control Tower, choose **Enroll account**.<br />2. Fill in the details, including the email address associated with the account you want to enroll, the display name that will appear in AWS Control Tower, the IAM Identity Center email address, the first and last name of the account owner, and the OU in which you would like to enroll the account. The IAM Identity Center email address is your preferred user email address. You can use the same email address as the account email.<br />3. Choose **Enroll account**.For more information, see [About enrolling existing accounts](https://docs.aws.amazon.com/controltower/latest/userguide/enroll-account.html) in the AWS Control Tower documentation. | AWS Control Tower administrator |

### Verify the account after enrollment
<a name="verify-the-account-after-enrollment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Verify the account. | From AWS Control Tower, choose **Accounts**. The account that you just enrolled has an initial state of **Enrolling**. When enrollment is complete, its state changes to **Enrolled**. | AWS Control Tower administrator, Member account administrator |
| Check for control violations. | Controls defined in the OU will automatically apply to the enrolled member account. Monitor the AWS Control Tower dashboard for violations and fix them accordingly. For more information, see [About controls](https://docs.aws.amazon.com/controltower/latest/controlreference/controls.html) in the AWS Control Tower documentation. | AWS Control Tower administrator, Member account administrator |

## Troubleshooting
<a name="migrate-an-aws-member-account-from-aws-organizations-to-aws-control-tower-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| You receive the error message: **An unknown error occurred. Try again later, or contact AWS Support.**  | This error occurs when you use root user credentials (management account) in AWS Control Tower to enroll a new account. AWS Service Catalog can't map the Account Factory Portfolio or product to the root user, which results in the error message. To remediate this error, use non-root, full-access user (administrator) credentials to enroll the new account. For more information about how to assign administrative access to an administrative user, see [Getting started](https://docs.aws.amazon.com/singlesignon/latest/userguide/getting-started.html) in the IAM Identity Center documentation. |
| The AWS Control Tower **Activities** page displays a **Get Catastrophic Drift** action. | This action reflects a drift check of the service and does not indicate any issues with the AWS Control Tower setup. No action is required. |

## Related resources
<a name="migrate-an-aws-member-account-from-aws-organizations-to-aws-control-tower-resources"></a>

**Documentation**
+ [Terminology and concepts](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html) (AWS Organizations documentation)
+ [What is AWS Control Tower?](https://docs.aws.amazon.com/controltower/latest/userguide/) (AWS Control Tower documentation)
+ [Removing a member account from an organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_remove.html#leave-without-all-info) (AWS Organizations documentation)
+ [Setting up](https://docs.aws.amazon.com/controltower/latest/userguide/setting-up.html#setting-up-iam) (AWS Control Tower documentation)

**Tutorials and videos **
+ [AWS Control Tower workshop](https://catalog.workshops.aws/control-tower/) (self-paced workshop)
+ [What is AWS Control Tower?](https://www.youtube.com/watch?v=daLvEb44d5Q) (video)
+ [Provisioning Users in AWS Control Tower](https://www.youtube.com/watch?v=y_n9xN5mg1g) (video)

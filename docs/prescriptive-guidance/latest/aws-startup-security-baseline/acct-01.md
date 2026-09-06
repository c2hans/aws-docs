---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-startup-security-baseline/acct-01.html
---

# ACCT.01 Set account-level contacts to valid email distribution lists
<a name="acct-01"></a>

When setting up primary and alternate contacts for your AWS account, use an email distribution list instead of an individual's email address. Using an email distribution list makes sure that ownership and reachability are preserved as individuals in your organization come and go. Set alternate contacts for billing, operations, and security notifications, and use appropriate email distribution lists accordingly. AWS uses these email addresses to contact you. Make sure that you retain access to them.

**To update your account name, root user password, or root user email address**

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/)

1. Choose your account name or number, and then choose **Account**.

1. On the [Account](https://console.aws.amazon.com/billing/home?#/account) page, next to **Account details**, choose **Actions**, and then choose the action you want to take.

1. Next to the field you want to update, choose **Edit**.

1. After you have entered your changes, choose **Save changes**.

1. If you are updating the root user password or email address, follow the verification steps that AWS displays.

**To edit your contact information**

1. On the [Account](https://console.aws.amazon.com/billing/home?#/account) page, under **Contact information**, choose **Edit**.

1. For the fields you want to change, enter your updated information, and then choose **Update**.

**To add, update, or remove alternate contacts**

1. On the [Account](https://console.aws.amazon.com/billing/home?#/account) page, under **Alternate Contacts**, choose **Edit**.

1. For the fields you want to change, enter your updated information, and then choose **Update**.

If you have an organization in AWS Organizations enabled, you can also programmatically manage the alternate contacts on your accounts through the AWS Command Line Interface (AWS CLI). For more information, see [Programmatically managing alternate contacts on member accounts with AWS Organizations](https://aws.amazon.com/blogs/mt/programmatically-managing-alternate-contacts-on-member-accounts-with-aws-organizations/) on the AWS Cloud Operations Blog*.*

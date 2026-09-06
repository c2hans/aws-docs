---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-startup-security-baseline/acct-05.html
---

# ACCT.05 Require multi-factor authentication to log in
<a name="acct-05"></a>

With multi-factor authentication (MFA), users have a device that generates a response to an authentication challenge. Each user's credentials and device-generated response are required to complete the sign-in process. Enable MFA for AWS account access, especially for long-term credentials such as the account root user and IAM users.

**To set up MFA for the root user**

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/).

1. Choose your account name, and then choose **Security credentials**.

1. On the **Security credentials** page, under **Multi-factor authentication (MFA)**, choose **Assign MFA device**.

1. Follow the steps to configure your MFA device. For more information, see [Multi-factor authentication for AWS account root user](https://docs.aws.amazon.com/IAM/latest/UserGuide/enable-mfa-for-root.html) in the IAM documentation.

**To set up MFA in IAM Identity Center**

1. See [Enable MFA](https://docs.aws.amazon.com/singlesignon/latest/userguide/enable-mfa.html) in the IAM Identity Center documentation.

**To set up MFA for your own IAM user**

1. Sign in to the [IAM console](https://console.aws.amazon.com/iam).

1. Choose your user name, and then choose **Security credentials**.

1. On the **Security credentials** tab, under **Multi-factor authentication (MFA)**, choose **Assign MFA device**.

1. Follow the steps to configure your MFA device. For more information, see [AWS Multi-Factor Authentication in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html) in the IAM documentation.

**To set up MFA for other IAM users**

1. Sign in to the [IAM console](https://console.aws.amazon.com/iam).

1. In the navigation pane, choose **Users**.

1. Choose the name of the user for whom you want to enable MFA, and then choose the **Security credentials** tab.

1. Under **Multi-factor authentication (MFA)**, choose **Assign MFA device**.

1. Follow the steps to configure the MFA device. For more information, see [AWS Multi-Factor Authentication in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html) in the IAM documentation.

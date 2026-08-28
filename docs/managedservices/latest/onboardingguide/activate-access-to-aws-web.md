---
source_url: https://docs.aws.amazon.com/managedservices/latest/onboardingguide/activate-access-to-aws-web.html
---

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

# Activate access to the AWS website
<a name="activate-access-to-aws-web"></a>

In order to grant your IAM users access to your account's billing information and tools, you must activate the functionality.

Follow these steps:

1. Sign in to the AWS Management Console with your *root account* credentials (the email and password that you used to create your AWS account). Don't sign in with your IAM user credentials.

   The AWS Management Console home page opens.

1. In the top navigation bar, open the drop-down menu for your account name, and then choose **My Account**.

   The Billing home page opens.

1. Scroll down to the **IAM User Access to Billing Information** area, and click **Edit** on the right side. {{The area does not appear unless you are logged in with root credentials}}.

   An **Activate IAM access** area opens.

1. Select the check box and click **Update**.

   You can now use IAM policies to control which pages a user can access.

For more details on this process in AWS, see [Overview of managing access permissions](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/control-access-billing.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

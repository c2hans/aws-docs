---
source_url: https://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/step-2-launch-the-chatbot-content-designer.html
---

# Step 2: Launch the chatbot content designer
<a name="step-2-launch-the-chatbot-content-designer"></a>

After successfully deploying the stack, you will receive an email at the email address listed in the deployment parameters with the subject *QnABot on AWS Signup Verification Code*. This email contains a generated temporary password that you can use to sign in to the content designer and create your own password.

Use the following procedure to launch the content designer, reset your password, and sign in to the content designer UI.

1. Open the verification email and select the link. Alternatively, sign in to the [CloudFormation console](https://console.aws.amazon.com/cloudformation/), choose this guidance’s stack, select the **Outputs** tab, then select the **ContentDesignerURL** link. The content designer opens in a separate browser tab.

1. Sign in with your username and temporary password.

   1. Enter the **username** that you specified in the deployment parameters.

   1. Enter the temporary **password** from the verification email.

1. Follow the prompts to change your password and sign in. Your new password must have a length of at least eight characters, and contain at least one of each of the following: upper-case and lower-case characters, numbers, and special characters.

1. Sign in with your username and new password.

To reset the user password using the **Forgot your password** option on the sign in page, verify the user email.

 **AWS Management Console method for verifying user email**

1. Sign in to the [Amazon Cognito console](https://console.aws.amazon.com/cognito/).

1. Choose **User Pools** and select the user pool belonging to the QnABot stack.

1. Choose **Users** and select the user for which the password needs to be reset.

1. Choose **Edit User attributes**, select **Mark email address as verified**.

1. Choose **Save**.

 **AWS CLI method for verifying user email**

To verify email, run:

```
aws cognito-idp admin-update-user-attributes \
 --user-pool-id <qnabot user pool id> \
 --username <username> \
 --user-attributes Name="email_verified",Value="true"
```

To get the user pool ID, run:

```
aws cognito-idp list-user-pools --max-results 10
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for QnABot on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

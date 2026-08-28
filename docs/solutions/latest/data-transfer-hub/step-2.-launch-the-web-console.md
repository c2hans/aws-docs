---
source_url: https://docs.aws.amazon.com/solutions/latest/data-transfer-hub/step-2.-launch-the-web-console.html
---

# Step 2. Launch the web console
<a name="step-2.-launch-the-web-console"></a>

 After the stack is successfully created, navigate to the CloudFormation **Outputs** tab and select the **PortalUrl** value to access the Data Transfer Hub web console.

 After successful deployment, an email containing a temporary login password will be sent to the email address provided.

 Depending on the Region where you start the stack, you can choose to access the web console from the AWS China Regions or the AWS Regions.
+  Log in with Amazon Cognito User Pool (for AWS Regions)
+  Log in with OpenID using Authing.cn (for AWS China Regions)

## (Option 1) Log in using Amazon Cognito user pool for AWS Regions
<a name="option-1-log-in-using-amazon-cognito-user-pool-for-aws-regions"></a>

1. In a web browser, enter the **PortalURL** from the CloudFormation **Output** tab, then navigate to the Amazon Cognito console.

1.  Sign in with the **AdminEmail** and the temporary password.

   1.  Set a new account password.

   1.  (Optional) Verify your email address for account recovery.

1.  After the verification is complete, the system opens the Data Transfer Hub web console.

## (Option 2) OpenID authentication for AWS China Regions
<a name="option-2-openid-authentication-for-aws-china-regions"></a>

1.  Enter the Data Transfer Hub domain name in a web browser.
**Note**
If you are logging in for the first time, the system will open the Authing.cn login interface.

1.  Enter the username and password you registered when you deployed the Guidance, then choose **Login**. The system opens the Data Transfer Hub web console.

1.  Change your password and then sign in again.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Data Transfer Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/create-saml-app.html
---

# Create a SAML 2.0 application
<a name="create-saml-app"></a>

In this step, you federate your Identity Provider (IdP) to IAM Identity Center through SAML 2.0, and use IAM Identity Center to manage user access to the solution.

1. Log in to the [AWS IAM Identity Center console](https://console.aws.amazon.com/singlesignon/).

1. From the left pane, under **Application assignments**, choose **Applications**.

1. On the Applications page, on the **Customer managed** tab, choose **Add application**.

1. On the **Select application type** page, under **Setup preference**, choose **I have an application I want to set up**.

1. Under **Application type**, choose **SAML 2.0**, and choose **Next**.

1. On the **Configure application** page, under **Configure application**,
   + Enter a **Display name** for the application, such as *MyISBApp*,
   + Enter a description.

1. Under **Application metadata**, choose **Manually type your metadata values**, and provide the **Application ACS URL** and **Application SAML audience** values.
   +  **Application ACS URL**: The URL of the CloudFront distribution (or alternate domain name associated with the distribution) from the Compute stack output appended with `/api/auth/login/callback`. For example: `<ISB_WEB_URL>/api/auth/login/callback` where `ISB_WEB_URL` is the CloudFront Distribution URL or alternate domain (for example: https://duyXXXXXXXeh.cloudfront.net/api/auth/login/callback). To view the Compute stack outputs, navigate to the **AWS CloudFormation > Stacks > Outputs** tab, in the account where you have deployed the Compute stack.
   +  **Application SAML audience**: The audience used to identify the service provider (in this case, Innovation Sandbox web application) configured to consume the SAML assertion. For example: `Isb-<NAMESPACE>-Audience`.

1. Choose **Submit**. The Application details page displays.

---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/log-in-webui.html
---

# Logging into the web UI
<a name="log-in-webui"></a>

**Important**
Only Admins will have access to the CloudFormation console to retrieve the web UI URL. Admins are responsible for providing the Managers and users with this web UI URL.

After you deploy the Innovation Sandbox on AWS solution:

1. Open AWS CloudFormation console (from the Hub account), and from the left, choose **Stacks**. The list of stacks deployed as part of the solution display.

1. Choose the **Compute** stack to view stack details.

1. On the Stack details page, choose the **Outputs** tab. The web UI URL is the value assigned to the `CloudFrontDistributionUrl` key.

![The Outputs tab of the Compute stack showing the CloudFront distribution URL](http://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/screenshots/compute-stack-outputs.png)

**Web UI URL**

1. Choose to open the web UI for the solution. The Amazon Cognito hosted sign-in page opens.

The solution authenticates you through Amazon Cognito, which federates to AWS IAM Identity Center using SAML 2.0. Sign in with your IAM Identity Center credentials.

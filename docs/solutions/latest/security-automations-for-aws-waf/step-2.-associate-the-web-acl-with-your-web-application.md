---
source_url: https://docs.aws.amazon.com/solutions/latest/security-automations-for-aws-waf/step-2.-associate-the-web-acl-with-your-web-application.html
---

# Step 2. Associate the web ACL with your web application
<a name="step-2.-associate-the-web-acl-with-your-web-application"></a>

Update your CloudFront distribution(s) or ALB(s) to activate AWS WAF and logging using the resources you generated in [Step 1. Launch the stack](step-1.-launch-the-stack.md).

1. Sign in to the [AWS WAF console](https://console.aws.amazon.com/wafv2/).

1. Choose the web ACL that you want to use.

1. On the **Associated AWS resources** tab, choose **Add AWS resources**.

1. Under **Resource type**, choose the CloudFront distribution or ALB.

1. Select a resource from the list, then choose **Add** to save your changes.

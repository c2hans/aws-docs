---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/contact-aws-support.html
---

# Contact AWS Support

If you have [AWS Business Support\+](https://aws.amazon.com/premiumsupport/plans/business-plus/), [AWS Enterprise Support](https://aws.amazon.com/premiumsupport/plans/enterprise/), or [AWS Unified Operations](https://aws.amazon.com/premiumsupport/plans/unified-operations/), you can use AWS Support Center to get expert assistance with this solution. The following sections provide instructions.

## Create case
<a name="create-case"></a>

1. Sign in to [Support Center](https://support.console.aws.amazon.com/support/home#/).

1. Choose **Create case**.

## Describe your issue
<a name="describe-your-issue"></a>

With AWS Support, an AI-powered assistant helps route and resolve your case. On the **Support interactions** page, enter a description of your issue in the text box, and then submit it. The following screenshot shows the **Support interactions** page, where the assistant greets you above the description text box.

![The Support interactions page in AWS Support Center, showing the AI assistant greeting and a text box for entering a detailed description of the issue.](https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/images/contact-support-page.png)

Describe your issue in natural language, including relevant details such as:
+ The solution name (Automated Security Response on AWS)
+ The AWS services involved
+ Error messages or unexpected behavior
+ Steps you have already taken to troubleshoot

The AI assistant guides you through the resolution process or connects you with a support engineer.

## Use the form-based workflow
<a name="use-the-form-based-workflow"></a>

If you prefer the form-based case creation workflow, provide the following information:

1. For **Type**, choose **Technical**.

1. For **Service**, select **Solutions**.

1. For **Category**, select **Automated Security Response on AWS**.

1. For **Severity**, select the option that best matches your use case.

1. For **Subject**, enter text summarizing your question or issue.

1. For **Description**, describe the issue in detail, including the name of this product and the version you are using, such as: `Automated Security Response on AWS vX.Y.Z`.

1. In the **Attachments** section, choose **Attach files** to provide any supporting information that AWS Support needs to process the request.

1. At the bottom of the form, choose **Submit**.

## Additional information
<a name="additional-information"></a>

1. For **Subject**, enter text summarizing your question or issue.

1. For **Description**, describe the issue in detail.

1. Choose **Attach files**.

1. Attach a `.zip` file containing the following:
   + The log stream for the affected control and date from the `SO0111-ASR` CloudWatch Logs group in the AWS Security Hub admin account
   + The log stream for the failed Step Functions execution from the `SO0111-ASR-Orchestrator` CloudWatch Logs group in the AWS Security Hub admin account
   + The AWS Systems Manager Automation execution output from the member account, including the execution ID
   + The ARN of the failed CloudFormation stack, if you are reporting a deployment failure

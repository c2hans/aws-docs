---
source_url: https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/contact-aws-support.html
---

# Contact AWS Support
<a name="contact-aws-support"></a>

If you have [AWS Business Support\+](https://aws.amazon.com/premiumsupport/plans/business-plus/), [AWS Enterprise Support](https://aws.amazon.com/premiumsupport/plans/enterprise/), or [AWS Unified Operations](https://aws.amazon.com/premiumsupport/plans/unified-operations/), you can use AWS Support Center to get expert assistance with this solution. The following sections provide instructions.

## Create case
<a name="create-case"></a>

1. Sign in to [Support Center](https://support.console.aws.amazon.com/support/home#/).

1. Choose **Create case**.

## Describe your issue
<a name="describe-your-issue"></a>

AWS Support now uses an AI-powered assistant to help route and resolve your case.

![AI-assisted support in AWS Support Center](http://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/images/AI-assisted-support.png)

Describe your issue in natural language, including relevant details such as:
+ The solution name (**Landing Zone Accelerator on AWS**)
+ The AWS services involved
+ Error messages or unexpected behavior
+ Steps you have already taken to troubleshoot

The AI assistant will guide you through the resolution process or connect you with a support engineer.

## Use the classic experience
<a name="use-the-classic-experience"></a>

If you prefer the form-based case creation workflow, choose **Use the old experience**.

![Use the old experience link in AWS Support Center](http://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/images/use-the-old-experience.png)

Then provide the following information:

1. For **Type**, choose **Technical**.

1. For **Service**, select **Solutions**.

1. For **Category**, select **Landing Zone Accelerator on AWS**.

1. For **Severity**, select the option that best matches your use case.

1. For **Subject**, enter text summarizing your question or issue.

1. For **Description**, describe the issue in detail, including the name of this product and the version you are using, such as: Landing Zone Accelerator on AWS vX.Y.Z.

1. Choose **Attach files** to provide any supporting information that AWS Support needs to process the request.

1. Choose **Submit**.

## Additional information
<a name="additional-information"></a>

1. For **Subject**, enter text summarizing your question or issue.

1. For **Description**, describe the issue in detail.

1. Choose **Attach files**.

1. Attach a `0zip` file containing the following:
   + Your Landing Zone Accelerator on AWS configuration files, noting modifications if applicable
   + Sanitized code build logs from the **Failed** stage which were obtained after setting the `LOG_LEVEL` to debug in the CodeBuild environment
   + Failed CloudFormation template ARN

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Landing Zone Accelerator on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/guardduty/latest/ug/remediate-lambda-protection-finding-types.html
---

# Remediating a potentially compromised Lambda function
<a name="remediate-lambda-protection-finding-types"></a>

When GuardDuty generates [Lambda Protection finding types](lambda-protection-finding-types.md), your Lambda function may be compromised. If the activity that caused GuardDuty to generate this finding was expected, you can consider using [Suppression rules](findings_suppression-rule.md). We recommend completing the following steps to remediate a compromised Lambda function:

**To remediate Lambda Protection findings**

1. **Identify the potentially compromised Lambda function version**.

   A GuardDuty finding for Lambda Protection provides the name, Amazon Resource Name (ARN), function version, and revision ID associated with the Lambda function listed in the finding details.

1. **Identify the source of the potentially suspicious activity**.

   1. Review the code associated with the Lambda function version involved in the finding.

   1. Review the imported libraries and layers of the Lambda function version involved in the finding.

   1. If you have enabled [Scanning AWS Lambda functions with Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/scanning-lambda.html), review the [Amazon Inspector findings](https://docs.aws.amazon.com/inspector/latest/user/findings-understanding-locating-analyzing.html) associated with the Lambda function involved in the finding.

   1. Review the AWS CloudTrail logs to identify the principal that caused the function update and ensure that the activity was authorized or expected.

1. **Remediate the potentially compromised Lambda function**.

   1. Disable the execution triggers of the Lambda function involved in the finding. For more information, see [DeleteFunctionEventInvokeConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_DeleteFunctionEventInvokeConfig.html).

   1. Review the Lambda code and update the libraries imports and [Lambda function layers](https://docs.aws.amazon.com/lambda/latest/dg/chapter-layers.html) to remove the potentially suspicious libraries and layers.

   1. Mitigate Amazon Inspector findings related to the Lambda function involved in the finding.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

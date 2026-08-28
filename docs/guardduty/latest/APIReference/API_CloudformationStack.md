---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_CloudformationStack.html
---

# CloudformationStack
<a name="API_CloudformationStack"></a>

Contains information about the CloudFormation stack involved in a GuardDuty finding, including unique identifiers of the Amazon EC2 instances.

## Contents
<a name="API_CloudformationStack_Contents"></a>

 ** ec2InstanceUids **   <a name="guardduty-Type-CloudformationStack-ec2InstanceUids"></a>
A list of unique identifiers for the compromised Amazon EC2 instances that were created as part of the same CloudFormation stack.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_CloudformationStack_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/CloudformationStack)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/CloudformationStack)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/CloudformationStack)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

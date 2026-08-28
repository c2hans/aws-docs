---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_AccountLimit.html
---

# AccountLimit
<a name="API_AccountLimit"></a>

Describes the current CloudFormation limits for your account.

CloudFormation has the following limits per account:
+ Number of concurrent resources
+ Number of stacks
+ Number of stack outputs

For more information, see [Understand CloudFormation quotas](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html) in the * AWS CloudFormation User Guide*.

## Contents
<a name="API_AccountLimit_Contents"></a>

 ** Name **
The name of the account limit.
Values: `ConcurrentResourcesLimit` \| `StackLimit` \| `StackOutputsLimit`
Type: String
Required: No

 ** Value **
The value that's associated with the account limit name.
Type: Integer
Required: No

## See Also
<a name="API_AccountLimit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/AccountLimit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/AccountLimit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/AccountLimit)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

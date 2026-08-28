---
source_url: https://docs.aws.amazon.com/textract/latest/APIReference/API_HumanLoopConfig.html
---

# HumanLoopConfig
<a name="API_HumanLoopConfig"></a>

Sets up the human review workflow the document will be sent to if one of the conditions is met. You can also set certain attributes of the image before review.

**Note**
Amazon Textract uses Amazon Augmented AI (A2I) to run the human review workflows that you specify in `HumanLoopConfig`. A2I entered maintenance mode in July 2026 and no longer accepts new customers. If your account is not an existing A2I customer, requests fail with an `InvalidParameterException`. For more information, see [AWS service availability](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-service-availability/). If you're an existing A2I customer but receive this error, contact AWS Support and request assistance from the A2I team.

## Contents
<a name="API_HumanLoopConfig_Contents"></a>

 ** FlowDefinitionArn **   <a name="Textract-Type-HumanLoopConfig-FlowDefinitionArn"></a>
The Amazon Resource Name (ARN) of the flow definition.
Type: String
Length Constraints: Maximum length of 256.
Required: Yes

 ** HumanLoopName **   <a name="Textract-Type-HumanLoopConfig-HumanLoopName"></a>
The name of the human workflow used for this image. This should be kept unique within a region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `^[a-z0-9](-*[a-z0-9])*`
Required: Yes

 ** DataAttributes **   <a name="Textract-Type-HumanLoopConfig-DataAttributes"></a>
Sets attributes of the input data.
Type: [HumanLoopDataAttributes](API_HumanLoopDataAttributes.md) object
Required: No

## See Also
<a name="API_HumanLoopConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/textract-2018-06-27/HumanLoopConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/textract-2018-06-27/HumanLoopConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/textract-2018-06-27/HumanLoopConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Textract. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query textract` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

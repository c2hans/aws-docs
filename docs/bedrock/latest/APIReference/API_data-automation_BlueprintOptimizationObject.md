---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_data-automation_BlueprintOptimizationObject.html
---

# BlueprintOptimizationObject
<a name="API_data-automation_BlueprintOptimizationObject"></a>

A blueprint to be optimized.

## Contents
<a name="API_data-automation_BlueprintOptimizationObject_Contents"></a>

 ** blueprintArn **   <a name="bedrock-Type-data-automation_BlueprintOptimizationObject-blueprintArn"></a>
The blueprint's ARN.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `arn:aws(|-cn|-us-gov):bedrock:[a-zA-Z0-9-]*:(aws|[0-9]{12}):blueprint/(bedrock-data-automation-public-[a-zA-Z0-9-_]{1,30}|[a-zA-Z0-9-]{12,36})`
Required: Yes

 ** stage **   <a name="bedrock-Type-data-automation_BlueprintOptimizationObject-stage"></a>
The blueprint's stage.
Type: String
Valid Values: `DEVELOPMENT | LIVE`
Required: No

## See Also
<a name="API_data-automation_BlueprintOptimizationObject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-2023-07-26/BlueprintOptimizationObject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-2023-07-26/BlueprintOptimizationObject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-2023-07-26/BlueprintOptimizationObject)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_DurableConfig.html
---

# DurableConfig
<a name="API_DurableConfig"></a>

Configuration settings for [durable functions](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html), including execution timeout, retention period for execution history, and an optional ARN of the AWS Key Management Service (AWS KMS) customer managed key that is used to encrypt your durable execution's payload data, including input, output, and error payloads.

## Contents
<a name="API_DurableConfig_Contents"></a>

 ** ExecutionTimeout **   <a name="lambda-Type-DurableConfig-ExecutionTimeout"></a>
The maximum time (in seconds) that a durable execution can run before timing out. This timeout applies to the entire durable execution, not individual function invocations.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 31622400.
Required: No

 ** KMSKeyArn **   <a name="lambda-Type-DurableConfig-KMSKeyArn"></a>
The ARN of the AWS Key Management Service (AWS KMS) customer managed key that is used to encrypt your durable execution's payload data, including input, output, and error payloads.
Type: String
Pattern: `(arn:(aws[a-zA-Z-]*)?:[a-z0-9-.]+:.*)|()`
Required: No

 ** RetentionPeriodInDays **   <a name="lambda-Type-DurableConfig-RetentionPeriodInDays"></a>
The number of days to retain execution history after a durable execution completes. After this period, execution history is no longer available through the GetDurableExecutionHistory API.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 90.
Required: No

## See Also
<a name="API_DurableConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/DurableConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/DurableConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/DurableConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

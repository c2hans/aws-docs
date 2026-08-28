---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_ScalingConfig.html
---

# ScalingConfig
<a name="API_ScalingConfig"></a>

(Amazon SQS only) The scaling configuration for the event source. To remove the configuration, pass an empty value.

## Contents
<a name="API_ScalingConfig_Contents"></a>

 ** MaximumConcurrency **   <a name="lambda-Type-ScalingConfig-MaximumConcurrency"></a>
Limits the number of concurrent instances that the Amazon SQS event source can invoke.
Type: Integer
Valid Range: Minimum value of 2. Maximum value of 1000.
Required: No

## See Also
<a name="API_ScalingConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/ScalingConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/ScalingConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/ScalingConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

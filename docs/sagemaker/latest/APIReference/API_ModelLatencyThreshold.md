---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelLatencyThreshold.html
---

# ModelLatencyThreshold
<a name="API_ModelLatencyThreshold"></a>

The model latency threshold.

## Contents
<a name="API_ModelLatencyThreshold_Contents"></a>

 ** Percentile **   <a name="sagemaker-Type-ModelLatencyThreshold-Percentile"></a>
The model latency percentile threshold. Acceptable values are `P95` and `P99`. For custom load tests, specify the value as `P95`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Required: No

 ** ValueInMilliseconds **   <a name="sagemaker-Type-ModelLatencyThreshold-ValueInMilliseconds"></a>
The model latency percentile value in milliseconds.
Type: Integer
Required: No

## See Also
<a name="API_ModelLatencyThreshold_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ModelLatencyThreshold)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ModelLatencyThreshold)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ModelLatencyThreshold)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_FeatureParameter.html
---

# FeatureParameter
<a name="API_FeatureParameter"></a>

A key-value pair that you specify to describe the feature.

## Contents
<a name="API_FeatureParameter_Contents"></a>

 ** Key **   <a name="sagemaker-Type-FeatureParameter-Key"></a>
A key that must contain a value to describe the feature.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-]*)`
Required: No

 ** Value **   <a name="sagemaker-Type-FeatureParameter-Value"></a>
The value that belongs to a key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-]*)`
Required: No

## See Also
<a name="API_FeatureParameter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/FeatureParameter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/FeatureParameter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/FeatureParameter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

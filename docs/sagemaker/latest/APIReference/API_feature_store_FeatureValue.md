---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_FeatureValue.html
---

# FeatureValue
<a name="API_feature_store_FeatureValue"></a>

The value associated with a feature.

## Contents
<a name="API_feature_store_FeatureValue_Contents"></a>

 ** FeatureName **   <a name="sagemaker-Type-feature_store_FeatureValue-FeatureName"></a>
The name of a feature that a feature value corresponds to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9]([-_]*[a-zA-Z0-9]){0,63}`
Required: Yes

 ** ValueAsString **   <a name="sagemaker-Type-feature_store_FeatureValue-ValueAsString"></a>
The value in string format associated with a feature. Used when your `CollectionType` is `None`. Note that features types can be `String`, `Integral`, or `Fractional`. This value represents all three types as a string.
Type: String
Length Constraints: Maximum length of 358400.
Pattern: `.*`
Required: No

 ** ValueAsStringList **   <a name="sagemaker-Type-feature_store_FeatureValue-ValueAsStringList"></a>
The list of values in string format associated with a feature. Used when your `CollectionType` is a `List`, `Set`, or `Vector`. Note that features types can be `String`, `Integral`, or `Fractional`. These values represents all three types as a string.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 358400 items.
Length Constraints: Maximum length of 358400.
Pattern: `.*`
Required: No

## See Also
<a name="API_feature_store_FeatureValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-featurestore-runtime-2020-07-01/FeatureValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-featurestore-runtime-2020-07-01/FeatureValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-featurestore-runtime-2020-07-01/FeatureValue)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

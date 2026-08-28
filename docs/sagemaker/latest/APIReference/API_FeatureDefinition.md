---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_FeatureDefinition.html
---

# FeatureDefinition
<a name="API_FeatureDefinition"></a>

A list of features. You must include `FeatureName` and `FeatureType`. Valid feature `FeatureType`s are `Integral`, `Fractional` and `String`.

## Contents
<a name="API_FeatureDefinition_Contents"></a>

 ** FeatureName **   <a name="sagemaker-Type-FeatureDefinition-FeatureName"></a>
The name of a feature. The type must be a string. `FeatureName` cannot be any of the following: `is_deleted`, `write_time`, `api_invocation_time`.
The name:
+ Must start with an alphanumeric character.
+ Can only include alphanumeric characters, underscores, and hyphens. Spaces are not allowed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9]([-_]*[a-zA-Z0-9]){0,63}`
Required: Yes

 ** FeatureType **   <a name="sagemaker-Type-FeatureDefinition-FeatureType"></a>
The value type of a feature. Valid values are Integral, Fractional, or String.
Type: String
Valid Values: `Integral | Fractional | String`
Required: Yes

 ** CollectionConfig **   <a name="sagemaker-Type-FeatureDefinition-CollectionConfig"></a>
Configuration for your collection.
Type: [CollectionConfig](API_CollectionConfig.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** CollectionType **   <a name="sagemaker-Type-FeatureDefinition-CollectionType"></a>
A grouping of elements where each element within the collection must have the same feature type (`String`, `Integral`, or `Fractional`).
+  `List`: An ordered collection of elements.
+  `Set`: An unordered collection of unique elements.
+  `Vector`: A specialized list that represents a fixed-size array of elements. The vector dimension is determined by you. Must have elements with fractional feature types.
Type: String
Valid Values: `List | Set | Vector`
Required: No

## See Also
<a name="API_FeatureDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/FeatureDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/FeatureDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/FeatureDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

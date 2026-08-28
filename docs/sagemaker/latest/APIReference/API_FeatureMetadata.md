---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_FeatureMetadata.html
---

# FeatureMetadata
<a name="API_FeatureMetadata"></a>

The metadata for a feature. It can either be metadata that you specify, or metadata that is updated automatically.

## Contents
<a name="API_FeatureMetadata_Contents"></a>

 ** CreationTime **   <a name="sagemaker-Type-FeatureMetadata-CreationTime"></a>
A timestamp indicating when the feature was created.
Type: Timestamp
Required: No

 ** Description **   <a name="sagemaker-Type-FeatureMetadata-Description"></a>
An optional description that you specify to better describe the feature.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `.*`
Required: No

 ** FeatureGroupArn **   <a name="sagemaker-Type-FeatureMetadata-FeatureGroupArn"></a>
The Amazon Resource Number (ARN) of the feature group.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:feature-group/.*`
Required: No

 ** FeatureGroupName **   <a name="sagemaker-Type-FeatureMetadata-FeatureGroupName"></a>
The name of the feature group containing the feature.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9]([_-]*[a-zA-Z0-9]){0,63}`
Required: No

 ** FeatureName **   <a name="sagemaker-Type-FeatureMetadata-FeatureName"></a>
The name of feature.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9]([-_]*[a-zA-Z0-9]){0,63}`
Required: No

 ** FeatureType **   <a name="sagemaker-Type-FeatureMetadata-FeatureType"></a>
The data type of the feature.
Type: String
Valid Values: `Integral | Fractional | String`
Required: No

 ** LastModifiedTime **   <a name="sagemaker-Type-FeatureMetadata-LastModifiedTime"></a>
A timestamp indicating when the feature was last modified.
Type: Timestamp
Required: No

 ** Parameters **   <a name="sagemaker-Type-FeatureMetadata-Parameters"></a>
Optional key-value pairs that you specify to better describe the feature.
Type: Array of [FeatureParameter](API_FeatureParameter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Required: No

## See Also
<a name="API_FeatureMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/FeatureMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/FeatureMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/FeatureMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

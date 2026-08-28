---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_RSessionAppSettings.html
---

# RSessionAppSettings
<a name="API_RSessionAppSettings"></a>

A collection of settings that apply to an `RSessionGateway` app.

## Contents
<a name="API_RSessionAppSettings_Contents"></a>

 ** CustomImages **   <a name="sagemaker-Type-RSessionAppSettings-CustomImages"></a>
A list of custom SageMaker AI images that are configured to run as a RSession app.
Type: Array of [CustomImage](API_CustomImage.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** DefaultResourceSpec **   <a name="sagemaker-Type-RSessionAppSettings-DefaultResourceSpec"></a>
Specifies the ARN's of a SageMaker AI image and SageMaker AI image version, and the instance type that the version runs on.
When both `SageMakerImageVersionArn` and `SageMakerImageArn` are passed, `SageMakerImageVersionArn` is used. Any updates to `SageMakerImageArn` will not take effect if `SageMakerImageVersionArn` already exists in the `ResourceSpec` because `SageMakerImageVersionArn` always takes precedence. To clear the value set for `SageMakerImageVersionArn`, pass `None` as the value.
Type: [ResourceSpec](API_ResourceSpec.md) object
Required: No

## See Also
<a name="API_RSessionAppSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/RSessionAppSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/RSessionAppSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/RSessionAppSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

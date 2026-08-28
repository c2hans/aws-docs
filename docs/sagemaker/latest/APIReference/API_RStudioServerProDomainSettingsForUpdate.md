---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_RStudioServerProDomainSettingsForUpdate.html
---

# RStudioServerProDomainSettingsForUpdate
<a name="API_RStudioServerProDomainSettingsForUpdate"></a>

A collection of settings that update the current configuration for the `RStudioServerPro` Domain-level app.

## Contents
<a name="API_RStudioServerProDomainSettingsForUpdate_Contents"></a>

 ** DomainExecutionRoleArn **   <a name="sagemaker-Type-RStudioServerProDomainSettingsForUpdate-DomainExecutionRoleArn"></a>
The execution role for the `RStudioServerPro` Domain-level app.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** DefaultResourceSpec **   <a name="sagemaker-Type-RStudioServerProDomainSettingsForUpdate-DefaultResourceSpec"></a>
Specifies the ARN's of a SageMaker AI image and SageMaker AI image version, and the instance type that the version runs on.
When both `SageMakerImageVersionArn` and `SageMakerImageArn` are passed, `SageMakerImageVersionArn` is used. Any updates to `SageMakerImageArn` will not take effect if `SageMakerImageVersionArn` already exists in the `ResourceSpec` because `SageMakerImageVersionArn` always takes precedence. To clear the value set for `SageMakerImageVersionArn`, pass `None` as the value.
Type: [ResourceSpec](API_ResourceSpec.md) object
Required: No

 ** RStudioConnectUrl **   <a name="sagemaker-Type-RStudioServerProDomainSettingsForUpdate-RStudioConnectUrl"></a>
A URL pointing to an RStudio Connect server.
Type: String
Required: No

 ** RStudioPackageManagerUrl **   <a name="sagemaker-Type-RStudioServerProDomainSettingsForUpdate-RStudioPackageManagerUrl"></a>
A URL pointing to an RStudio Package Manager server.
Type: String
Required: No

## See Also
<a name="API_RStudioServerProDomainSettingsForUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/RStudioServerProDomainSettingsForUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/RStudioServerProDomainSettingsForUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/RStudioServerProDomainSettingsForUpdate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

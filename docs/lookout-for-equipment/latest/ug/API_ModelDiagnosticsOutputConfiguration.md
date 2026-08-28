---
source_url: https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_ModelDiagnosticsOutputConfiguration.html
---

 On October 7, 2026, AWS will discontinue support for Amazon Lookout for Equipment. After October 7, 2026, you will no longer be able to access the Lookout for Equipment console or resources. For more information, [see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/).

# ModelDiagnosticsOutputConfiguration
<a name="API_ModelDiagnosticsOutputConfiguration"></a>

Output configuration information for the pointwise model diagnostics for an Amazon Lookout for Equipment model.

## Contents
<a name="API_ModelDiagnosticsOutputConfiguration_Contents"></a>

 ** S3OutputConfiguration **   <a name="LookoutForEquipment-Type-ModelDiagnosticsOutputConfiguration-S3OutputConfiguration"></a>
The Amazon S3 location for the pointwise model diagnostics.
Type: [ModelDiagnosticsS3OutputConfiguration](API_ModelDiagnosticsS3OutputConfiguration.md) object
Required: Yes

 ** KmsKeyId **   <a name="LookoutForEquipment-Type-ModelDiagnosticsOutputConfiguration-KmsKeyId"></a>
The AWS Key Management Service (KMS) key identifier to encrypt the pointwise model diagnostics files.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,2048}$`
Required: No

## See Also
<a name="API_ModelDiagnosticsOutputConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lookoutequipment-2020-12-15/ModelDiagnosticsOutputConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lookoutequipment-2020-12-15/ModelDiagnosticsOutputConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lookoutequipment-2020-12-15/ModelDiagnosticsOutputConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lookout for Equipment. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lookout-for-equipment` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

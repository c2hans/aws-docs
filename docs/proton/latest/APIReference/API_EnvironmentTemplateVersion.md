---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_EnvironmentTemplateVersion.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# EnvironmentTemplateVersion
<a name="API_EnvironmentTemplateVersion"></a>

The environment template version data.

## Contents
<a name="API_EnvironmentTemplateVersion_Contents"></a>

 ** arn **   <a name="proton-Type-EnvironmentTemplateVersion-arn"></a>
The Amazon Resource Name (ARN) of the version of an environment template.
Type: String
Required: Yes

 ** createdAt **   <a name="proton-Type-EnvironmentTemplateVersion-createdAt"></a>
The time when the version of an environment template was created.
Type: Timestamp
Required: Yes

 ** lastModifiedAt **   <a name="proton-Type-EnvironmentTemplateVersion-lastModifiedAt"></a>
The time when the version of an environment template was last modified.
Type: Timestamp
Required: Yes

 ** majorVersion **   <a name="proton-Type-EnvironmentTemplateVersion-majorVersion"></a>
The latest major version that's associated with the version of an environment template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `(0|([1-9]{1}\d*))`
Required: Yes

 ** minorVersion **   <a name="proton-Type-EnvironmentTemplateVersion-minorVersion"></a>
The minor version of an environment template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `(0|([1-9]{1}\d*))`
Required: Yes

 ** status **   <a name="proton-Type-EnvironmentTemplateVersion-status"></a>
The status of the version of an environment template.
Type: String
Valid Values: `REGISTRATION_IN_PROGRESS | REGISTRATION_FAILED | DRAFT | PUBLISHED`
Required: Yes

 ** templateName **   <a name="proton-Type-EnvironmentTemplateVersion-templateName"></a>
The name of the version of an environment template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

 ** description **   <a name="proton-Type-EnvironmentTemplateVersion-description"></a>
A description of the minor version of an environment template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** recommendedMinorVersion **   <a name="proton-Type-EnvironmentTemplateVersion-recommendedMinorVersion"></a>
The recommended minor version of the environment template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `(0|([1-9]{1}\d*))`
Required: No

 ** schema **   <a name="proton-Type-EnvironmentTemplateVersion-schema"></a>
The schema of the version of an environment template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 51200.
Required: No

 ** statusMessage **   <a name="proton-Type-EnvironmentTemplateVersion-statusMessage"></a>
The status message of the version of an environment template.
Type: String
Required: No

## See Also
<a name="API_EnvironmentTemplateVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/EnvironmentTemplateVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/EnvironmentTemplateVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/EnvironmentTemplateVersion)

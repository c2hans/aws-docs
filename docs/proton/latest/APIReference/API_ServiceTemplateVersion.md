---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_ServiceTemplateVersion.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# ServiceTemplateVersion
<a name="API_ServiceTemplateVersion"></a>

Detailed data of an AWS Proton service template version resource.

## Contents
<a name="API_ServiceTemplateVersion_Contents"></a>

 ** arn **   <a name="proton-Type-ServiceTemplateVersion-arn"></a>
The Amazon Resource Name (ARN) of the version of a service template.
Type: String
Required: Yes

 ** compatibleEnvironmentTemplates **   <a name="proton-Type-ServiceTemplateVersion-compatibleEnvironmentTemplates"></a>
An array of compatible environment template names for the major version of a service template.
Type: Array of [CompatibleEnvironmentTemplate](API_CompatibleEnvironmentTemplate.md) objects
Required: Yes

 ** createdAt **   <a name="proton-Type-ServiceTemplateVersion-createdAt"></a>
The time when the version of a service template was created.
Type: Timestamp
Required: Yes

 ** lastModifiedAt **   <a name="proton-Type-ServiceTemplateVersion-lastModifiedAt"></a>
The time when the version of a service template was last modified.
Type: Timestamp
Required: Yes

 ** majorVersion **   <a name="proton-Type-ServiceTemplateVersion-majorVersion"></a>
The latest major version that's associated with the version of a service template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `(0|([1-9]{1}\d*))`
Required: Yes

 ** minorVersion **   <a name="proton-Type-ServiceTemplateVersion-minorVersion"></a>
The minor version of a service template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `(0|([1-9]{1}\d*))`
Required: Yes

 ** status **   <a name="proton-Type-ServiceTemplateVersion-status"></a>
The service template version status.
Type: String
Valid Values: `REGISTRATION_IN_PROGRESS | REGISTRATION_FAILED | DRAFT | PUBLISHED`
Required: Yes

 ** templateName **   <a name="proton-Type-ServiceTemplateVersion-templateName"></a>
The name of the version of a service template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

 ** description **   <a name="proton-Type-ServiceTemplateVersion-description"></a>
A description of the version of a service template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** recommendedMinorVersion **   <a name="proton-Type-ServiceTemplateVersion-recommendedMinorVersion"></a>
The recommended minor version of the service template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `(0|([1-9]{1}\d*))`
Required: No

 ** schema **   <a name="proton-Type-ServiceTemplateVersion-schema"></a>
The schema of the version of a service template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 51200.
Required: No

 ** statusMessage **   <a name="proton-Type-ServiceTemplateVersion-statusMessage"></a>
A service template version status message.
Type: String
Required: No

 ** supportedComponentSources **   <a name="proton-Type-ServiceTemplateVersion-supportedComponentSources"></a>
An array of supported component sources. Components with supported sources can be attached to service instances based on this service template version.
For more information about components, see [AWS Proton components](https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html) in the * AWS Proton User Guide*.
Type: Array of strings
Valid Values: `DIRECTLY_DEFINED`
Required: No

## See Also
<a name="API_ServiceTemplateVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/ServiceTemplateVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/ServiceTemplateVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/ServiceTemplateVersion)

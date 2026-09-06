---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_ServiceTemplate.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# ServiceTemplate
<a name="API_ServiceTemplate"></a>

Detailed data of an AWS Proton service template resource.

## Contents
<a name="API_ServiceTemplate_Contents"></a>

 ** arn **   <a name="proton-Type-ServiceTemplate-arn"></a>
The Amazon Resource Name (ARN) of the service template.
Type: String
Required: Yes

 ** createdAt **   <a name="proton-Type-ServiceTemplate-createdAt"></a>
The time when the service template was created.
Type: Timestamp
Required: Yes

 ** lastModifiedAt **   <a name="proton-Type-ServiceTemplate-lastModifiedAt"></a>
The time when the service template was last modified.
Type: Timestamp
Required: Yes

 ** name **   <a name="proton-Type-ServiceTemplate-name"></a>
The name of the service template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

 ** description **   <a name="proton-Type-ServiceTemplate-description"></a>
A description of the service template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** displayName **   <a name="proton-Type-ServiceTemplate-displayName"></a>
The service template name as displayed in the developer interface.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** encryptionKey **   <a name="proton-Type-ServiceTemplate-encryptionKey"></a>
The customer provided service template encryption key that's used to encrypt data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `arn:(aws|aws-cn|aws-us-gov):[a-zA-Z0-9-]+:[a-zA-Z0-9-]*:\d{12}:([\w+=,.@-]+[/:])*[\w+=,.@-]+`
Required: No

 ** pipelineProvisioning **   <a name="proton-Type-ServiceTemplate-pipelineProvisioning"></a>
If `pipelineProvisioning` is `true`, a service pipeline is included in the service template. Otherwise, a service pipeline *isn't* included in the service template.
Type: String
Valid Values: `CUSTOMER_MANAGED`
Required: No

 ** recommendedVersion **   <a name="proton-Type-ServiceTemplate-recommendedVersion"></a>
The recommended version of the service template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `(0|([1-9]{1}\d*)).(0|([1-9]{1}\d*))`
Required: No

## See Also
<a name="API_ServiceTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/ServiceTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/ServiceTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/ServiceTemplate)

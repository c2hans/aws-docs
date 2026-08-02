---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_ServiceInstanceState.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# ServiceInstanceState
<a name="API_ServiceInstanceState"></a>

The detailed data about the current state of this service instance.

## Contents
<a name="API_ServiceInstanceState_Contents"></a>

 ** spec **   <a name="proton-Type-ServiceInstanceState-spec"></a>
The service spec that was used to create the service instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 51200.
Required: Yes

 ** templateMajorVersion **   <a name="proton-Type-ServiceInstanceState-templateMajorVersion"></a>
The major version of the service template that was used to create the service pipeline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `(0|([1-9]{1}\d*))`
Required: Yes

 ** templateMinorVersion **   <a name="proton-Type-ServiceInstanceState-templateMinorVersion"></a>
The minor version of the service template that was used to create the service pipeline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `(0|([1-9]{1}\d*))`
Required: Yes

 ** templateName **   <a name="proton-Type-ServiceInstanceState-templateName"></a>
The name of the service template that was used to create the service instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

 ** lastSuccessfulComponentDeploymentIds **   <a name="proton-Type-ServiceInstanceState-lastSuccessfulComponentDeploymentIds"></a>
The IDs for the last successful components deployed for this service instance.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** lastSuccessfulEnvironmentDeploymentId **   <a name="proton-Type-ServiceInstanceState-lastSuccessfulEnvironmentDeploymentId"></a>
The ID for the last successful environment deployed for this service instance.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** lastSuccessfulServicePipelineDeploymentId **   <a name="proton-Type-ServiceInstanceState-lastSuccessfulServicePipelineDeploymentId"></a>
The ID for the last successful service pipeline deployed for this service instance.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

## See Also
<a name="API_ServiceInstanceState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/ServiceInstanceState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/ServiceInstanceState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/ServiceInstanceState)

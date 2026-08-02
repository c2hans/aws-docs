---
source_url: https://docs.aws.amazon.com/greengrass/v2/APIReference/API_EffectiveDeploymentStatusDetails.html
---

# EffectiveDeploymentStatusDetails
<a name="API_EffectiveDeploymentStatusDetails"></a>

Contains all error-related information for the deployment record. The status details will be null if the deployment is in a success state.

**Note**
Greengrass nucleus v2.8.0 or later is required to get an accurate `errorStack` and `errorTypes` response. This field will not be returned for earlier Greengrass nucleus versions.

## Contents
<a name="API_EffectiveDeploymentStatusDetails_Contents"></a>

 ** errorStack **   <a name="greengrassv2-Type-EffectiveDeploymentStatusDetails-errorStack"></a>
Contains an ordered list of short error codes that range from the most generic error to the most specific one. The error codes describe the reason for failure whenever the `coreDeviceExecutionStatus` is in a failed state. The response will be an empty list if there is no error.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** errorTypes **   <a name="greengrassv2-Type-EffectiveDeploymentStatusDetails-errorTypes"></a>
Contains tags which describe the error. You can use the error types to classify errors to assist with remediating the failure. The response will be an empty list if there is no error.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## See Also
<a name="API_EffectiveDeploymentStatusDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/greengrassv2-2020-11-30/EffectiveDeploymentStatusDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/greengrassv2-2020-11-30/EffectiveDeploymentStatusDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/greengrassv2-2020-11-30/EffectiveDeploymentStatusDetails)

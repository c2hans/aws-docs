---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ConfigurationDetails.html
---

# ConfigurationDetails
<a name="API_ConfigurationDetails"></a>

The encryption configuration details that include the status information of the AWS Key Management Service (AWS KMS) key and the AWS KMS access role.

## Contents
<a name="API_ConfigurationDetails_Contents"></a>

 ** configurationStatus **   <a name="iot-Type-ConfigurationDetails-configurationStatus"></a>
The health status of KMS key and AWS KMS access role. If either KMS key or AWS KMS access role is `UNHEALTHY`, the return value will be `UNHEALTHY`. To use a customer managed KMS key, the value of `configurationStatus` must be `HEALTHY`.
Type: String
Valid Values: `HEALTHY | UNHEALTHY`
Required: No

 ** errorCode **   <a name="iot-Type-ConfigurationDetails-errorCode"></a>
The error code that indicates either the KMS key or the AWS KMS access role is `UNHEALTHY`. Valid values: `KMS_KEY_VALIDATION_ERROR` and `ROLE_VALIDATION_ERROR`.
Type: String
Required: No

 ** errorMessage **   <a name="iot-Type-ConfigurationDetails-errorMessage"></a>
The detailed error message that corresponds to the `errorCode`.
Type: String
Length Constraints: Maximum length of 2048.
Required: No

## See Also
<a name="API_ConfigurationDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ConfigurationDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ConfigurationDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ConfigurationDetails)

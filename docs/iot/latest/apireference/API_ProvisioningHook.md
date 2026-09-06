---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ProvisioningHook.html
---

# ProvisioningHook
<a name="API_ProvisioningHook"></a>

Structure that contains `payloadVersion` and `targetArn`.

## Contents
<a name="API_ProvisioningHook_Contents"></a>

 ** targetArn **   <a name="iot-Type-ProvisioningHook-targetArn"></a>
The ARN of the target function.
 *Note:* Only Lambda functions are currently supported.
Type: String
Length Constraints: Maximum length of 2048.
Required: Yes

 ** payloadVersion **   <a name="iot-Type-ProvisioningHook-payloadVersion"></a>
The payload that was sent to the target function.
 *Note:* Only Lambda functions are currently supported.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 32.
Pattern: `^[0-9-]+$`
Required: No

## See Also
<a name="API_ProvisioningHook_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ProvisioningHook)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ProvisioningHook)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ProvisioningHook)

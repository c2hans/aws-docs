---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_EndpointAttributes.html
---

# EndpointAttributes
<a name="API_EndpointAttributes"></a>

The attributes of an `Endpoint`.

## Contents
<a name="API_EndpointAttributes_Contents"></a>

 ** DeviceToken **   <a name="chimesdk-Type-EndpointAttributes-DeviceToken"></a>
The device token for the GCM, APNS, and APNS\_SANDBOX endpoint types.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `.*`
Required: Yes

 ** VoipDeviceToken **   <a name="chimesdk-Type-EndpointAttributes-VoipDeviceToken"></a>
The VOIP device token for the APNS and APNS\_SANDBOX endpoint types.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `.*`
Required: No

## See Also
<a name="API_EndpointAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-identity-2021-04-20/EndpointAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-identity-2021-04-20/EndpointAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-identity-2021-04-20/EndpointAttributes)

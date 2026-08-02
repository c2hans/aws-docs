---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_OriginationRoute.html
---

# OriginationRoute
<a name="API_voice-chime_OriginationRoute"></a>

Origination routes define call distribution properties for your SIP hosts to receive inbound calls using an Amazon Chime SDK Voice Connector. Limit: Ten origination routes for each Voice Connector.

**Note**
The parameters listed below are not required, but you must use at least one.

## Contents
<a name="API_voice-chime_OriginationRoute_Contents"></a>

 ** Host **   <a name="chimesdk-Type-voice-chime_OriginationRoute-Host"></a>
The FQDN or IP address to contact for origination traffic.
Type: String
Required: No

 ** Port **   <a name="chimesdk-Type-voice-chime_OriginationRoute-Port"></a>
The designated origination route port. Defaults to 5060.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 65535.
Required: No

 ** Priority **   <a name="chimesdk-Type-voice-chime_OriginationRoute-Priority"></a>
The priority associated with the host, with 1 being the highest priority. Higher priority hosts are attempted first.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** Protocol **   <a name="chimesdk-Type-voice-chime_OriginationRoute-Protocol"></a>
The protocol to use for the origination route. Encryption-enabled Amazon Chime SDK Voice Connectors use TCP protocol by default.
Type: String
Valid Values: `TCP | UDP`
Required: No

 ** Weight **   <a name="chimesdk-Type-voice-chime_OriginationRoute-Weight"></a>
The weight assigned to an origination route. When hosts have equal priority, calls are distributed between them based on their relative weights.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

## See Also
<a name="API_voice-chime_OriginationRoute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/OriginationRoute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/OriginationRoute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/OriginationRoute)

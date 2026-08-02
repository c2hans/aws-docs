---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_RcsFallbackConfiguration.html
---

# RcsFallbackConfiguration
<a name="API_RcsFallbackConfiguration"></a>

Configuration for SMS or MMS fallback when RCS delivery fails or the TimeToLive expires without delivery confirmation.

## Contents
<a name="API_RcsFallbackConfiguration_Contents"></a>

 ** Channel **   <a name="pinpoint-Type-RcsFallbackConfiguration-Channel"></a>
The fallback channel to use when RCS delivery fails. Valid values are SMS and MMS. SMS and MMS are mutually exclusive.
Type: String
Valid Values: `SMS | MMS`
Required: Yes

 ** MediaUrls **   <a name="pinpoint-Type-RcsFallbackConfiguration-MediaUrls"></a>
An array of S3 URIs to media files for MMS fallback. Only valid when Channel is MMS.
Type: Array of strings
Array Members: Fixed number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `s3://([a-z0-9\.-]{3,63})/(.+)`
Required: No

 ** MessageBody **   <a name="pinpoint-Type-RcsFallbackConfiguration-MessageBody"></a>
The text body of the fallback message. Required for SMS fallback. For MMS fallback, at least one of MessageBody or MediaUrls must be provided.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `(?!\s*$)[\s\S]+`
Required: No

 ** OriginationIdentity **   <a name="pinpoint-Type-RcsFallbackConfiguration-OriginationIdentity"></a>
The origination identity to use for the fallback message. This can be a PhoneNumber, PhoneNumberId, PhoneNumberArn, SenderId, or SenderIdArn. Pool IDs and pool ARNs are not accepted. If not specified and the original message was sent via a pool, the service selects a suitable number from the pool.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/\+-]+`
Required: No

## See Also
<a name="API_RcsFallbackConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/RcsFallbackConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/RcsFallbackConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/RcsFallbackConfiguration)

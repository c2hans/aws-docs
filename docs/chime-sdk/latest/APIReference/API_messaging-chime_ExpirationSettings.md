---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ExpirationSettings.html
---

# ExpirationSettings
<a name="API_messaging-chime_ExpirationSettings"></a>

Settings that control the interval after which a channel is deleted.

## Contents
<a name="API_messaging-chime_ExpirationSettings_Contents"></a>

 ** ExpirationCriterion **   <a name="chimesdk-Type-messaging-chime_ExpirationSettings-ExpirationCriterion"></a>
The conditions that must be met for a channel to expire.
Type: String
Valid Values: `CREATED_TIMESTAMP | LAST_MESSAGE_TIMESTAMP`
Required: Yes

 ** ExpirationDays **   <a name="chimesdk-Type-messaging-chime_ExpirationSettings-ExpirationDays"></a>
The period in days after which the system automatically deletes a channel.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 5475.
Required: Yes

## See Also
<a name="API_messaging-chime_ExpirationSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-messaging-2021-05-15/ExpirationSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-messaging-2021-05-15/ExpirationSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-messaging-2021-05-15/ExpirationSettings)

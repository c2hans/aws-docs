---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_Identity.html
---

# Identity
<a name="API_messaging-chime_Identity"></a>

The details of a user or bot.

## Contents
<a name="API_messaging-chime_Identity_Contents"></a>

 ** Arn **   <a name="chimesdk-Type-messaging-chime_Identity-Arn"></a>
The ARN in an Identity.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: No

 ** Name **   <a name="chimesdk-Type-messaging-chime_Identity-Name"></a>
The name in an Identity.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\u0009\u000A\u000D\u0020-\u007E\u0085\u00A0-\uD7FF\uE000-\uFFFD\u10000-\u10FFFF]*`
Required: No

## See Also
<a name="API_messaging-chime_Identity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-messaging-2021-05-15/Identity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-messaging-2021-05-15/Identity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-messaging-2021-05-15/Identity)

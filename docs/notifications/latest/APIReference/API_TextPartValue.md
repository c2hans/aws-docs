---
source_url: https://docs.aws.amazon.com/notifications/latest/APIReference/API_TextPartValue.html
---

# TextPartValue
<a name="API_TextPartValue"></a>

Describes text information objects containing fields that determine how text part objects are composed.

## Contents
<a name="API_TextPartValue_Contents"></a>

 ** type **   <a name="Notifications-Type-TextPartValue-type"></a>
The type of text part. Determines the usage of all other fields and whether or not they're required.
Type: String
Valid Values: `LOCALIZED_TEXT | PLAIN_TEXT | URL | PORTABLE_TEXT`
Required: Yes

 ** displayText **   <a name="Notifications-Type-TextPartValue-displayText"></a>
A short single line description of the link. Must be hyper-linked with the URL itself.
Used for text parts with the type `URL`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 12000.
Required: No

 ** textByLocale **   <a name="Notifications-Type-TextPartValue-textByLocale"></a>
A map of locales to the text in that locale.
Type: String to string map
Valid Keys: `de_DE | en_CA | en_US | en_UK | es_ES | fr_CA | fr_FR | id_ID | it_IT | ja_JP | ko_KR | pt_BR | tr_TR | zh_CN | zh_TW`
Required: No

 ** url **   <a name="Notifications-Type-TextPartValue-url"></a>
The URL itself.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.
Required: No

## See Also
<a name="API_TextPartValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notifications-2018-05-10/TextPartValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notifications-2018-05-10/TextPartValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notifications-2018-05-10/TextPartValue)

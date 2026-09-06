---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_Tag.html
---

# Tag
<a name="API_meeting-chime_Tag"></a>

A key-value pair that you define.

## Contents
<a name="API_meeting-chime_Tag_Contents"></a>

 ** Key **   <a name="chimesdk-Type-meeting-chime_Tag-Key"></a>
The tag's key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z+-=._:/]+$`
Required: Yes

 ** Value **   <a name="chimesdk-Type-meeting-chime_Tag-Value"></a>
The tag's value.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\w+-=\.:/@]*`
Required: Yes

## See Also
<a name="API_meeting-chime_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-meetings-2021-07-15/Tag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-meetings-2021-07-15/Tag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-meetings-2021-07-15/Tag)

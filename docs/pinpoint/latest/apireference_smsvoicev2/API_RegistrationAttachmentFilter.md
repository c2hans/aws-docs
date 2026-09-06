---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_RegistrationAttachmentFilter.html
---

# RegistrationAttachmentFilter
<a name="API_RegistrationAttachmentFilter"></a>

The filter definition for filtering registration attachments that meets a specified criteria.

## Contents
<a name="API_RegistrationAttachmentFilter_Contents"></a>

 ** Name **   <a name="pinpoint-Type-RegistrationAttachmentFilter-Name"></a>
The name of the attribute to filter on.
Type: String
Valid Values: `attachment-status`
Required: Yes

 ** Values **   <a name="pinpoint-Type-RegistrationAttachmentFilter-Values"></a>
An array of values to filter on.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[/\.:A-Za-z0-9+_-]+`
Required: Yes

## See Also
<a name="API_RegistrationAttachmentFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/RegistrationAttachmentFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/RegistrationAttachmentFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/RegistrationAttachmentFilter)

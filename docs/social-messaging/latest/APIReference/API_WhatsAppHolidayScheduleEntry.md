---
source_url: https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_WhatsAppHolidayScheduleEntry.html
---

# WhatsAppHolidayScheduleEntry
<a name="API_WhatsAppHolidayScheduleEntry"></a>

A date-specific override to the weekly operating hours, such as a holiday.

## Contents
<a name="API_WhatsAppHolidayScheduleEntry_Contents"></a>

 ** date **   <a name="Social-Type-WhatsAppHolidayScheduleEntry-date"></a>
The date that the override applies to, in ISO 8601 format (`YYYY-MM-DD`).
Type: String
Length Constraints: Fixed length of 10.
Pattern: `[0-9]{4}-[0-9]{2}-[0-9]{2}`
Required: Yes

 ** endTime **   <a name="Social-Type-WhatsAppHolidayScheduleEntry-endTime"></a>
The time of day when the business stops accepting calls on the override date.
Type: [WhatsAppTimeOfDay](API_WhatsAppTimeOfDay.md) object
Required: Yes

 ** startTime **   <a name="Social-Type-WhatsAppHolidayScheduleEntry-startTime"></a>
The time of day when the business begins accepting calls on the override date.
Type: [WhatsAppTimeOfDay](API_WhatsAppTimeOfDay.md) object
Required: Yes

## See Also
<a name="API_WhatsAppHolidayScheduleEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/socialmessaging-2024-01-01/WhatsAppHolidayScheduleEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/socialmessaging-2024-01-01/WhatsAppHolidayScheduleEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/socialmessaging-2024-01-01/WhatsAppHolidayScheduleEntry)

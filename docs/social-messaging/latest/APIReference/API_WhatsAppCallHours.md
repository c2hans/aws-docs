---
source_url: https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_WhatsAppCallHours.html
---

# WhatsAppCallHours
<a name="API_WhatsAppCallHours"></a>

The operating hours during which a business phone number accepts WhatsApp calls, including the time zone, weekly schedule, and any holiday overrides.

## Contents
<a name="API_WhatsAppCallHours_Contents"></a>

 ** enabled **   <a name="Social-Type-WhatsAppCallHours-enabled"></a>
Specifies whether call hours are enforced. When disabled, the business accepts calls at any time.
Type: Boolean
Required: Yes

 ** timezone **   <a name="Social-Type-WhatsAppCallHours-timezone"></a>
The IANA time zone in which the operating hours are interpreted, such as `America/New_York`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** weeklyOperatingHours **   <a name="Social-Type-WhatsAppCallHours-weeklyOperatingHours"></a>
The weekly schedule of hours during which the business accepts calls.
Type: Array of [WhatsAppWeeklyOperatingHoursEntry](API_WhatsAppWeeklyOperatingHoursEntry.md) objects
Array Members: Minimum number of 0 items. Maximum number of 14 items.
Required: Yes

 ** holidaySchedule **   <a name="Social-Type-WhatsAppCallHours-holidaySchedule"></a>
Date-specific overrides to the weekly operating hours, such as holidays.
Type: Array of [WhatsAppHolidayScheduleEntry](API_WhatsAppHolidayScheduleEntry.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

## See Also
<a name="API_WhatsAppCallHours_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/socialmessaging-2024-01-01/WhatsAppCallHours)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/socialmessaging-2024-01-01/WhatsAppCallHours)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/socialmessaging-2024-01-01/WhatsAppCallHours)

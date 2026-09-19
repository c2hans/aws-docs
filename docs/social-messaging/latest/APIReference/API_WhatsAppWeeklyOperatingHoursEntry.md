---
source_url: https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_WhatsAppWeeklyOperatingHoursEntry.html
---

# WhatsAppWeeklyOperatingHoursEntry
<a name="API_WhatsAppWeeklyOperatingHoursEntry"></a>

A single entry in a weekly calling schedule, defining the open and close times for one day of the week.

## Contents
<a name="API_WhatsAppWeeklyOperatingHoursEntry_Contents"></a>

 ** closeTime **   <a name="Social-Type-WhatsAppWeeklyOperatingHoursEntry-closeTime"></a>
The time of day when the business stops accepting calls.
Type: [WhatsAppTimeOfDay](API_WhatsAppTimeOfDay.md) object
Required: Yes

 ** dayOfWeek **   <a name="Social-Type-WhatsAppWeeklyOperatingHoursEntry-dayOfWeek"></a>
The day of the week that the entry applies to.
Type: String
Valid Values: `MONDAY | TUESDAY | WEDNESDAY | THURSDAY | FRIDAY | SATURDAY | SUNDAY`
Required: Yes

 ** openTime **   <a name="Social-Type-WhatsAppWeeklyOperatingHoursEntry-openTime"></a>
The time of day when the business begins accepting calls.
Type: [WhatsAppTimeOfDay](API_WhatsAppTimeOfDay.md) object
Required: Yes

## See Also
<a name="API_WhatsAppWeeklyOperatingHoursEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/socialmessaging-2024-01-01/WhatsAppWeeklyOperatingHoursEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/socialmessaging-2024-01-01/WhatsAppWeeklyOperatingHoursEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/socialmessaging-2024-01-01/WhatsAppWeeklyOperatingHoursEntry)

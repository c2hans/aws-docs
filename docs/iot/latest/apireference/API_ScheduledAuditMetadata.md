---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ScheduledAuditMetadata.html
---

# ScheduledAuditMetadata
<a name="API_ScheduledAuditMetadata"></a>

Information about the scheduled audit.

## Contents
<a name="API_ScheduledAuditMetadata_Contents"></a>

 ** dayOfMonth **   <a name="iot-Type-ScheduledAuditMetadata-dayOfMonth"></a>
The day of the month on which the scheduled audit is run (if the `frequency` is "MONTHLY"). If days 29-31 are specified, and the month does not have that many days, the audit takes place on the "LAST" day of the month.
Type: String
Pattern: `^([1-9]|[12][0-9]|3[01])$|^LAST$`
Required: No

 ** dayOfWeek **   <a name="iot-Type-ScheduledAuditMetadata-dayOfWeek"></a>
The day of the week on which the scheduled audit is run (if the `frequency` is "WEEKLY" or "BIWEEKLY").
Type: String
Valid Values: `SUN | MON | TUE | WED | THU | FRI | SAT`
Required: No

 ** frequency **   <a name="iot-Type-ScheduledAuditMetadata-frequency"></a>
How often the scheduled audit occurs.
Type: String
Valid Values: `DAILY | WEEKLY | BIWEEKLY | MONTHLY`
Required: No

 ** scheduledAuditArn **   <a name="iot-Type-ScheduledAuditMetadata-scheduledAuditArn"></a>
The ARN of the scheduled audit.
Type: String
Required: No

 ** scheduledAuditName **   <a name="iot-Type-ScheduledAuditMetadata-scheduledAuditName"></a>
The name of the scheduled audit.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

## See Also
<a name="API_ScheduledAuditMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ScheduledAuditMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ScheduledAuditMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ScheduledAuditMetadata)

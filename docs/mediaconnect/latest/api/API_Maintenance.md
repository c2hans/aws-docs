---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_Maintenance.html
---

# Maintenance
<a name="API_Maintenance"></a>

 The maintenance setting of a flow.

## Contents
<a name="API_Maintenance_Contents"></a>

 ** maintenanceDay **   <a name="mediaconnect-Type-Maintenance-maintenanceDay"></a>
 A day of a week when the maintenance will happen. Use Monday/Tuesday/Wednesday/Thursday/Friday/Saturday/Sunday.
Type: String
Valid Values: `Monday | Tuesday | Wednesday | Thursday | Friday | Saturday | Sunday`
Required: No

 ** maintenanceDeadline **   <a name="mediaconnect-Type-Maintenance-maintenanceDeadline"></a>
 The Maintenance has to be performed before this deadline in ISO UTC format. Example: 2021-01-30T08:30:00Z.
Type: String
Required: No

 ** maintenanceScheduledDate **   <a name="mediaconnect-Type-Maintenance-maintenanceScheduledDate"></a>
 A scheduled date in ISO UTC format when the maintenance will happen. Use YYYY-MM-DD format. Example: 2021-01-30.
Type: String
Required: No

 ** maintenanceStartHour **   <a name="mediaconnect-Type-Maintenance-maintenanceStartHour"></a>
 UTC time when the maintenance will happen. Use 24-hour HH:MM format. Minutes must be 00. Example: 13:00. The default value is 02:00.
Type: String
Required: No

## See Also
<a name="API_Maintenance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/Maintenance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/Maintenance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/Maintenance)

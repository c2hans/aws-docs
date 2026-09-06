---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_MaintenanceWindow.html
---

# MaintenanceWindow
<a name="API_MaintenanceWindow"></a>

The scheduling details for the maintenance window. Patching and system updates take place during the maintenance window.

## Contents
<a name="API_MaintenanceWindow_Contents"></a>

 ** customActionTimeoutInMins **   <a name="odb-Type-MaintenanceWindow-customActionTimeoutInMins"></a>
The custom action timeout in minutes for the maintenance window.
Type: Integer
Valid Range: Minimum value of 15. Maximum value of 120.
Required: No

 ** daysOfWeek **   <a name="odb-Type-MaintenanceWindow-daysOfWeek"></a>
The days of the week when maintenance can be performed.
Type: Array of [DayOfWeek](API_DayOfWeek.md) objects
Required: No

 ** hoursOfDay **   <a name="odb-Type-MaintenanceWindow-hoursOfDay"></a>
The hours of the day when maintenance can be performed.
Type: Array of integers
Required: No

 ** isCustomActionTimeoutEnabled **   <a name="odb-Type-MaintenanceWindow-isCustomActionTimeoutEnabled"></a>
Indicates whether custom action timeout is enabled for the maintenance window.
Type: Boolean
Required: No

 ** leadTimeInWeeks **   <a name="odb-Type-MaintenanceWindow-leadTimeInWeeks"></a>
The lead time in weeks before the maintenance window.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 4.
Required: No

 ** months **   <a name="odb-Type-MaintenanceWindow-months"></a>
The months when maintenance can be performed.
Type: Array of [Month](API_Month.md) objects
Required: No

 ** patchingMode **   <a name="odb-Type-MaintenanceWindow-patchingMode"></a>
The patching mode for the maintenance window.
Type: String
Valid Values: `ROLLING | NONROLLING`
Required: No

 ** preference **   <a name="odb-Type-MaintenanceWindow-preference"></a>
The preference for the maintenance window scheduling.
Type: String
Valid Values: `NO_PREFERENCE | CUSTOM_PREFERENCE`
Required: No

 ** skipRu **   <a name="odb-Type-MaintenanceWindow-skipRu"></a>
Indicates whether to skip release updates during maintenance.
Type: Boolean
Required: No

 ** weeksOfMonth **   <a name="odb-Type-MaintenanceWindow-weeksOfMonth"></a>
The weeks of the month when maintenance can be performed.
Type: Array of integers
Required: No

## See Also
<a name="API_MaintenanceWindow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/MaintenanceWindow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/MaintenanceWindow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/MaintenanceWindow)

---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointOptimizationAccessHoursEntry.html
---

# WaypointOptimizationAccessHoursEntry
<a name="API_WaypointOptimizationAccessHoursEntry"></a>

Hours of entry.

## Contents
<a name="API_WaypointOptimizationAccessHoursEntry_Contents"></a>

 ** DayOfWeek **   <a name="location-Type-WaypointOptimizationAccessHoursEntry-DayOfWeek"></a>
Day of the week.
Type: String
Valid Values: `Monday | Tuesday | Wednesday | Thursday | Friday | Saturday | Sunday`
Required: Yes

 ** TimeOfDay **   <a name="location-Type-WaypointOptimizationAccessHoursEntry-TimeOfDay"></a>
Time of the day.
Type: String
Pattern: `([0-1]?[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](Z|[+-]([0-1]?[0-9]|2[0-3]):[0-5][0-9])`
Required: Yes

## See Also
<a name="API_WaypointOptimizationAccessHoursEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/WaypointOptimizationAccessHoursEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/WaypointOptimizationAccessHoursEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/WaypointOptimizationAccessHoursEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

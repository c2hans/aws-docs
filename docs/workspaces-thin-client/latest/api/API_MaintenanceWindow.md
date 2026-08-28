---
source_url: https://docs.aws.amazon.com/workspaces-thin-client/latest/api/API_MaintenanceWindow.html
---

# MaintenanceWindow
<a name="API_MaintenanceWindow"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkSpaces Thin Client. After March 31, 2027, you will no longer be able to access the WorkSpaces Thin Client console or WorkSpaces Thin Client resources. For more information, see [Amazon WorkSpaces Thin Client end of support](https://docs.aws.amazon.com/workspaces-thin-client/latest/ug/workspacesthinclient-end-of-support.html).

Describes the maintenance window for a thin client device.

## Contents
<a name="API_MaintenanceWindow_Contents"></a>

 ** type **   <a name="workspacesthinclient-Type-MaintenanceWindow-type"></a>
An option to select the default or custom maintenance window.
Type: String
Valid Values: `SYSTEM | CUSTOM`
Required: Yes

 ** applyTimeOf **   <a name="workspacesthinclient-Type-MaintenanceWindow-applyTimeOf"></a>
The option to set the maintenance window during the device local time or Universal Coordinated Time (UTC).
Type: String
Valid Values: `UTC | DEVICE`
Required: No

 ** daysOfTheWeek **   <a name="workspacesthinclient-Type-MaintenanceWindow-daysOfTheWeek"></a>
The days of the week during which the maintenance window is open.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 7 items.
Valid Values: `MONDAY | TUESDAY | WEDNESDAY | THURSDAY | FRIDAY | SATURDAY | SUNDAY`
Required: No

 ** endTimeHour **   <a name="workspacesthinclient-Type-MaintenanceWindow-endTimeHour"></a>
The hour for the maintenance window end (`00`-`23`).
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 23.
Required: No

 ** endTimeMinute **   <a name="workspacesthinclient-Type-MaintenanceWindow-endTimeMinute"></a>
The minutes for the maintenance window end (`00`-`59`).
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 59.
Required: No

 ** startTimeHour **   <a name="workspacesthinclient-Type-MaintenanceWindow-startTimeHour"></a>
The hour for the maintenance window start (`00`-`23`).
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 23.
Required: No

 ** startTimeMinute **   <a name="workspacesthinclient-Type-MaintenanceWindow-startTimeMinute"></a>
The minutes past the hour for the maintenance window start (`00`-`59`).
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 59.
Required: No

## See Also
<a name="API_MaintenanceWindow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-thin-client-2023-08-22/MaintenanceWindow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-thin-client-2023-08-22/MaintenanceWindow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-thin-client-2023-08-22/MaintenanceWindow)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Thin Client. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-thin-client` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

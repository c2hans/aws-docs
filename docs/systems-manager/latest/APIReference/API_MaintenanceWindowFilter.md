---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_MaintenanceWindowFilter.html
---

# MaintenanceWindowFilter
<a name="API_MaintenanceWindowFilter"></a>

Filter used in the request. Supported filter keys depend on the API operation that includes the filter. API operations that use `MaintenanceWindowFilter>` include the following:
+  [DescribeMaintenanceWindowExecutions](API_DescribeMaintenanceWindowExecutions.md)
+  [DescribeMaintenanceWindowExecutionTaskInvocations](API_DescribeMaintenanceWindowExecutionTaskInvocations.md)
+  [DescribeMaintenanceWindowExecutionTasks](API_DescribeMaintenanceWindowExecutionTasks.md)
+  [DescribeMaintenanceWindows](API_DescribeMaintenanceWindows.md)
+  [DescribeMaintenanceWindowTargets](API_DescribeMaintenanceWindowTargets.md)
+  [DescribeMaintenanceWindowTasks](API_DescribeMaintenanceWindowTasks.md)

## Contents
<a name="API_MaintenanceWindowFilter_Contents"></a>

 ** Key **   <a name="systemsmanager-Type-MaintenanceWindowFilter-Key"></a>
The name of the filter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** Values **   <a name="systemsmanager-Type-MaintenanceWindowFilter-Values"></a>
The filter values.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_MaintenanceWindowFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/MaintenanceWindowFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/MaintenanceWindowFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/MaintenanceWindowFilter)

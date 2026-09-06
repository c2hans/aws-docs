---
source_url: https://docs.aws.amazon.com/scheduler/latest/APIReference/API_FlexibleTimeWindow.html
---

# FlexibleTimeWindow
<a name="API_FlexibleTimeWindow"></a>

Allows you to configure a time window during which EventBridge Scheduler invokes the schedule.

## Contents
<a name="API_FlexibleTimeWindow_Contents"></a>

 ** Mode **   <a name="scheduler-Type-FlexibleTimeWindow-Mode"></a>
Determines whether the schedule is invoked within a flexible time window.
Type: String
Valid Values: `OFF | FLEXIBLE`
Required: Yes

 ** MaximumWindowInMinutes **   <a name="scheduler-Type-FlexibleTimeWindow-MaximumWindowInMinutes"></a>
The maximum time window during which a schedule can be invoked.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1440.
Required: No

## See Also
<a name="API_FlexibleTimeWindow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/scheduler-2021-06-30/FlexibleTimeWindow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/scheduler-2021-06-30/FlexibleTimeWindow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/scheduler-2021-06-30/FlexibleTimeWindow)

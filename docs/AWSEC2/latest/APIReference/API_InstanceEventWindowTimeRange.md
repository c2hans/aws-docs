---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_InstanceEventWindowTimeRange.html
---

# InstanceEventWindowTimeRange
<a name="API_InstanceEventWindowTimeRange"></a>

The start day and time and the end day and time of the time range, in UTC.

## Contents
<a name="API_InstanceEventWindowTimeRange_Contents"></a>

 ** endHour **
The hour when the time range ends.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 23.
Required: No

 ** endWeekDay **
The day on which the time range ends.
Type: String
Valid Values: `sunday | monday | tuesday | wednesday | thursday | friday | saturday`
Required: No

 ** startHour **
The hour when the time range begins.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 23.
Required: No

 ** startWeekDay **
The day on which the time range begins.
Type: String
Valid Values: `sunday | monday | tuesday | wednesday | thursday | friday | saturday`
Required: No

## See Also
<a name="API_InstanceEventWindowTimeRange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/InstanceEventWindowTimeRange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/InstanceEventWindowTimeRange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/InstanceEventWindowTimeRange)

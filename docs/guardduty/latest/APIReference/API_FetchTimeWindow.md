---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_FetchTimeWindow.html
---

# FetchTimeWindow
<a name="API_FetchTimeWindow"></a>

Contains the time range of the data that GuardDuty requested. The range is defined by a start time and a duration.

## Contents
<a name="API_FetchTimeWindow_Contents"></a>

 ** durationInMinutes **   <a name="guardduty-Type-FetchTimeWindow-durationInMinutes"></a>
The length of the time range, in minutes. Valid values are 1 to 120.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 120.
Required: No

 ** startedAt **   <a name="guardduty-Type-FetchTimeWindow-startedAt"></a>
The timestamp at which the time range starts.
Type: Timestamp
Required: No

## See Also
<a name="API_FetchTimeWindow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/FetchTimeWindow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/FetchTimeWindow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/FetchTimeWindow)

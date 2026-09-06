---
source_url: https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_TimeRange.html
---

# TimeRange
<a name="API_TimeRange"></a>

A structure that defines the time range that you want to retrieve results from.

## Contents
<a name="API_TimeRange_Contents"></a>

 ** After **   <a name="cloudwatchrum-Type-TimeRange-After"></a>
The beginning of the time range to retrieve performance events from.
Type: Long
Required: Yes

 ** Before **   <a name="cloudwatchrum-Type-TimeRange-Before"></a>
The end of the time range to retrieve performance events from. If you omit this, the time range extends to the time that this operation is performed.
Type: Long
Required: No

## See Also
<a name="API_TimeRange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rum-2018-05-10/TimeRange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rum-2018-05-10/TimeRange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rum-2018-05-10/TimeRange)

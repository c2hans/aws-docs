---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_MetricFilterMatchRecord.html
---

# MetricFilterMatchRecord
<a name="API_MetricFilterMatchRecord"></a>

Represents a matched event.

## Contents
<a name="API_MetricFilterMatchRecord_Contents"></a>

 ** eventMessage **   <a name="CWL-Type-MetricFilterMatchRecord-eventMessage"></a>
The raw event data.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** eventNumber **   <a name="CWL-Type-MetricFilterMatchRecord-eventNumber"></a>
The event number.
Type: Long
Required: No

 ** extractedValues **   <a name="CWL-Type-MetricFilterMatchRecord-extractedValues"></a>
The values extracted from the event data by the filter.
Type: String to string map
Required: No

## See Also
<a name="API_MetricFilterMatchRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/MetricFilterMatchRecord)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/MetricFilterMatchRecord)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/MetricFilterMatchRecord)

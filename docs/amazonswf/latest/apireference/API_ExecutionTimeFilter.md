---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ExecutionTimeFilter.html
---

# ExecutionTimeFilter
<a name="API_ExecutionTimeFilter"></a>

Used to filter the workflow executions in visibility APIs by various time-based rules. Each parameter, if specified, defines a rule that must be satisfied by each returned query result. The parameter values are in the [Unix Time format](https://en.wikipedia.org/wiki/Unix_time). For example: `"oldestDate": 1325376070.`

## Contents
<a name="API_ExecutionTimeFilter_Contents"></a>

 ** oldestDate **   <a name="SWF-Type-ExecutionTimeFilter-oldestDate"></a>
Specifies the oldest start or close date and time to return.
Type: Timestamp
Required: Yes

 ** latestDate **   <a name="SWF-Type-ExecutionTimeFilter-latestDate"></a>
Specifies the latest start or close date and time to return.
Type: Timestamp
Required: No

## See Also
<a name="API_ExecutionTimeFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/ExecutionTimeFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/ExecutionTimeFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/ExecutionTimeFilter)

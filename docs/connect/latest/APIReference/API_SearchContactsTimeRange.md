---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_SearchContactsTimeRange.html
---

# SearchContactsTimeRange
<a name="API_SearchContactsTimeRange"></a>

A structure of time range that you want to search results.

## Contents
<a name="API_SearchContactsTimeRange_Contents"></a>

 ** EndTime **   <a name="connect-Type-SearchContactsTimeRange-EndTime"></a>
The end time of the time range.
Type: Timestamp
Required: Yes

 ** StartTime **   <a name="connect-Type-SearchContactsTimeRange-StartTime"></a>
The start time of the time range.
Type: Timestamp
Required: Yes

 ** Type **   <a name="connect-Type-SearchContactsTimeRange-Type"></a>
The type of timestamp to search.
Type: String
Valid Values: `INITIATION_TIMESTAMP | SCHEDULED_TIMESTAMP | CONNECTED_TO_AGENT_TIMESTAMP | DISCONNECT_TIMESTAMP | ENQUEUE_TIMESTAMP`
Required: Yes

## See Also
<a name="API_SearchContactsTimeRange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/SearchContactsTimeRange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/SearchContactsTimeRange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/SearchContactsTimeRange)

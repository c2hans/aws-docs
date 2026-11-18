---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_UpdateQueueRecordsVisibilityRequestEntry.html
---

# UpdateQueueRecordsVisibilityRequestEntry
<a name="API_UpdateQueueRecordsVisibilityRequestEntry"></a>

A record whose visibility timeout is changed, and the new visibility timeout.

## Contents
<a name="API_UpdateQueueRecordsVisibilityRequestEntry_Contents"></a>

 ** ReceiptHandle **   <a name="Streams-Type-UpdateQueueRecordsVisibilityRequestEntry-ReceiptHandle"></a>
The receipt handle of the record, as returned by [ReceiveQueueRecords](API_ReceiveQueueRecords.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** VisibilityTimeoutSeconds **   <a name="Streams-Type-UpdateQueueRecordsVisibilityRequestEntry-VisibilityTimeoutSeconds"></a>
The new duration, in seconds, that the record is in flight and not visible to any consumer instance, measured from when this request is processed. Specify `0` to make the record visible in the queue immediately.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 43200.
Required: Yes

## See Also
<a name="API_UpdateQueueRecordsVisibilityRequestEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/UpdateQueueRecordsVisibilityRequestEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/UpdateQueueRecordsVisibilityRequestEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/UpdateQueueRecordsVisibilityRequestEntry)

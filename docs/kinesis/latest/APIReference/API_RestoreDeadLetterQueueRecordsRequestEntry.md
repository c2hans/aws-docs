---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_RestoreDeadLetterQueueRecordsRequestEntry.html
---

# RestoreDeadLetterQueueRecordsRequestEntry

A dead-letter record to restore, identified by its receipt handle.

## Contents
<a name="API_RestoreDeadLetterQueueRecordsRequestEntry_Contents"></a>

 ** ReceiptHandle **   <a name="Streams-Type-RestoreDeadLetterQueueRecordsRequestEntry-ReceiptHandle"></a>
The receipt handle of the record to restore, as returned by [ReceiveDeadLetterQueueRecords](API_ReceiveDeadLetterQueueRecords.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

## See Also
<a name="API_RestoreDeadLetterQueueRecordsRequestEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/RestoreDeadLetterQueueRecordsRequestEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/RestoreDeadLetterQueueRecordsRequestEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/RestoreDeadLetterQueueRecordsRequestEntry)

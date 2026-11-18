---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_AcknowledgeQueueRecordsRequestEntry.html
---

# AcknowledgeQueueRecordsRequestEntry
<a name="API_AcknowledgeQueueRecordsRequestEntry"></a>

A record to acknowledge, identified by its receipt handle.

## Contents
<a name="API_AcknowledgeQueueRecordsRequestEntry_Contents"></a>

 ** ReceiptHandle **   <a name="Streams-Type-AcknowledgeQueueRecordsRequestEntry-ReceiptHandle"></a>
The receipt handle of the record to acknowledge, as returned by [ReceiveQueueRecords](API_ReceiveQueueRecords.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

## See Also
<a name="API_AcknowledgeQueueRecordsRequestEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/AcknowledgeQueueRecordsRequestEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/AcknowledgeQueueRecordsRequestEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/AcknowledgeQueueRecordsRequestEntry)

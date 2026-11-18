---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_AcknowledgeQueueRecordsErrorEntry.html
---

# AcknowledgeQueueRecordsErrorEntry
<a name="API_AcknowledgeQueueRecordsErrorEntry"></a>

A record that was not acknowledged, and why.

## Contents
<a name="API_AcknowledgeQueueRecordsErrorEntry_Contents"></a>

 ** ErrorCode **   <a name="Streams-Type-AcknowledgeQueueRecordsErrorEntry-ErrorCode"></a>
A code identifying the type of failure. One of `ResourceNotFoundException`, `InvalidArgumentException`, `ThrottlingException`, or `InternalFailureException`.
Type: String
Required: Yes

 ** ReceiptHandle **   <a name="Streams-Type-AcknowledgeQueueRecordsErrorEntry-ReceiptHandle"></a>
The receipt handle of the record that was not acknowledged.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** ErrorMessage **   <a name="Streams-Type-AcknowledgeQueueRecordsErrorEntry-ErrorMessage"></a>
A description of the cause of the failure.
Type: String
Required: No

## See Also
<a name="API_AcknowledgeQueueRecordsErrorEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/AcknowledgeQueueRecordsErrorEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/AcknowledgeQueueRecordsErrorEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/AcknowledgeQueueRecordsErrorEntry)

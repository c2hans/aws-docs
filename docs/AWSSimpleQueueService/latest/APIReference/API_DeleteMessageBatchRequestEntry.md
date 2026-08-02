---
source_url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_DeleteMessageBatchRequestEntry.html
---

# DeleteMessageBatchRequestEntry
<a name="API_DeleteMessageBatchRequestEntry"></a>

Encloses a receipt handle and an identifier for it.

## Contents
<a name="API_DeleteMessageBatchRequestEntry_Contents"></a>

 ** Id **   <a name="SQS-Type-DeleteMessageBatchRequestEntry-Id"></a>
The identifier for this particular receipt handle. This is used to communicate the result.
The `Id`s of a batch request need to be unique within a request.
This identifier can have up to 80 characters. The following characters are accepted: alphanumeric characters, hyphens(-), and underscores (\_).
Type: String
Required: Yes

 ** ReceiptHandle **   <a name="SQS-Type-DeleteMessageBatchRequestEntry-ReceiptHandle"></a>
A receipt handle.
Type: String
Required: Yes

## See Also
<a name="API_DeleteMessageBatchRequestEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sqs-2012-11-05/DeleteMessageBatchRequestEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sqs-2012-11-05/DeleteMessageBatchRequestEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sqs-2012-11-05/DeleteMessageBatchRequestEntry)

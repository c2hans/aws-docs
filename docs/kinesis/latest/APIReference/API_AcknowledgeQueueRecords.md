---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_AcknowledgeQueueRecords.html
---

# AcknowledgeQueueRecords
<a name="API_AcknowledgeQueueRecords"></a>

Acknowledges up to 10 records from the specified queue. After a record is acknowledged, the queue does not deliver it again. The result for each entry is reported individually in the response.

Acknowledging a record does not affect the record in the data stream. That record remains available to stream consumers and to other queues on the same stream for the rest of its retention period.

Because the request can result in a combination of successful and unsuccessful entries, check the `Failed` list even when the call returns an HTTP status code of `200`.

On rare occasions, you can receive a record again after you acknowledge it. Design your queue consumer to be idempotent, so that processing the same record more than once is safe.

## Request Syntax
<a name="API_AcknowledgeQueueRecords_RequestSyntax"></a>

```
{
   "Entries": [
      {
         "ReceiptHandle": "{{string}}"
      }
   ],
   "QueueARN": "{{string}}"
}
```

## Request Parameters
<a name="API_AcknowledgeQueueRecords_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [Entries](#API_AcknowledgeQueueRecords_RequestSyntax) **   <a name="Streams-AcknowledgeQueueRecords-request-Entries"></a>
The records to acknowledge, identified by their receipt handles.
Type: Array of [AcknowledgeQueueRecordsRequestEntry](API_AcknowledgeQueueRecordsRequestEntry.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

 ** [QueueARN](#API_AcknowledgeQueueRecords_RequestSyntax) **   <a name="Streams-AcknowledgeQueueRecords-request-QueueARN"></a>
The ARN of the queue the records were received from.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws.*:kinesis:.*:\d{12}:queue/\S+`
Required: Yes

## Response Syntax
<a name="API_AcknowledgeQueueRecords_ResponseSyntax"></a>

```
{
   "Failed": [
      {
         "ErrorCode": "string",
         "ErrorMessage": "string",
         "ReceiptHandle": "string"
      }
   ],
   "Successful": [
      {
         "ReceiptHandle": "string"
      }
   ]
}
```

## Response Elements
<a name="API_AcknowledgeQueueRecords_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Failed](#API_AcknowledgeQueueRecords_ResponseSyntax) **   <a name="Streams-AcknowledgeQueueRecords-response-Failed"></a>
The records that were not acknowledged, each with the reason the entry failed.
Type: Array of [AcknowledgeQueueRecordsErrorEntry](API_AcknowledgeQueueRecordsErrorEntry.md) objects

 ** [Successful](#API_AcknowledgeQueueRecords_ResponseSyntax) **   <a name="Streams-AcknowledgeQueueRecords-response-Successful"></a>
The records that were acknowledged.
Type: Array of [AcknowledgeQueueRecordsResultEntry](API_AcknowledgeQueueRecordsResultEntry.md) objects

## Errors
<a name="API_AcknowledgeQueueRecords_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Specifies that you do not have the permissions required to perform this operation.
HTTP Status Code: 400

 ** InternalFailureException **
The processing of the request failed because of an unknown error, exception, or failure.
HTTP Status Code: 500

 ** InvalidArgumentException **
A specified parameter exceeds its restrictions, is not supported, or can't be used. For more information, see the returned message.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The requested resource could not be found. The stream might not be specified correctly.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied because the request rate is too high. Reduce the frequency of your requests, and retry them with exponential backoff.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

## See Also
<a name="API_AcknowledgeQueueRecords_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesis-2013-12-02/AcknowledgeQueueRecords)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesis-2013-12-02/AcknowledgeQueueRecords)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/AcknowledgeQueueRecords)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesis-2013-12-02/AcknowledgeQueueRecords)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/AcknowledgeQueueRecords)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesis-2013-12-02/AcknowledgeQueueRecords)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesis-2013-12-02/AcknowledgeQueueRecords)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesis-2013-12-02/AcknowledgeQueueRecords)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/AcknowledgeQueueRecords)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/AcknowledgeQueueRecords)

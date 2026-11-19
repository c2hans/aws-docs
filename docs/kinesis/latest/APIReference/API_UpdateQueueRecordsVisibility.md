---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_UpdateQueueRecordsVisibility.html
---

# UpdateQueueRecordsVisibility

Changes the visibility timeout of up to 10 records that you have received from the specified queue but not yet acknowledged. The result for each entry is reported individually in the response.

Extend the visibility timeout of a record when your queue consumer needs more time to finish processing it, so the record does not become visible and get redelivered while it is still being processed. Set the visibility timeout to `0` to make a record visible in the queue immediately, so that it can be received again without waiting for its current timeout to expire.

Because the request can result in a combination of successful and unsuccessful entries, check the `Failed` list even when the call returns an HTTP status code of `200`.

## Request Syntax
<a name="API_UpdateQueueRecordsVisibility_RequestSyntax"></a>

```
{
   "Entries": [
      {
         "ReceiptHandle": "{{string}}",
         "VisibilityTimeoutSeconds": {{number}}
      }
   ],
   "QueueARN": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateQueueRecordsVisibility_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [Entries](#API_UpdateQueueRecordsVisibility_RequestSyntax) **   <a name="Streams-UpdateQueueRecordsVisibility-request-Entries"></a>
The records whose visibility timeout is changed, identified by their receipt handles, and the new visibility timeout for each.
Type: Array of [UpdateQueueRecordsVisibilityRequestEntry](API_UpdateQueueRecordsVisibilityRequestEntry.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

 ** [QueueARN](#API_UpdateQueueRecordsVisibility_RequestSyntax) **   <a name="Streams-UpdateQueueRecordsVisibility-request-QueueARN"></a>
The ARN of the queue the records were received from.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws.*:kinesis:.*:\d{12}:queue/\S+`
Required: Yes

## Response Syntax
<a name="API_UpdateQueueRecordsVisibility_ResponseSyntax"></a>

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
<a name="API_UpdateQueueRecordsVisibility_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Failed](#API_UpdateQueueRecordsVisibility_ResponseSyntax) **   <a name="Streams-UpdateQueueRecordsVisibility-response-Failed"></a>
The records whose visibility timeout was not changed, each with the reason the entry failed.
Type: Array of [UpdateQueueRecordsVisibilityErrorEntry](API_UpdateQueueRecordsVisibilityErrorEntry.md) objects

 ** [Successful](#API_UpdateQueueRecordsVisibility_ResponseSyntax) **   <a name="Streams-UpdateQueueRecordsVisibility-response-Successful"></a>
The records whose visibility timeout was changed.
Type: Array of [UpdateQueueRecordsVisibilityResultEntry](API_UpdateQueueRecordsVisibilityResultEntry.md) objects

## Errors
<a name="API_UpdateQueueRecordsVisibility_Errors"></a>

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
<a name="API_UpdateQueueRecordsVisibility_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesis-2013-12-02/UpdateQueueRecordsVisibility)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesis-2013-12-02/UpdateQueueRecordsVisibility)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/UpdateQueueRecordsVisibility)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesis-2013-12-02/UpdateQueueRecordsVisibility)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/UpdateQueueRecordsVisibility)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesis-2013-12-02/UpdateQueueRecordsVisibility)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesis-2013-12-02/UpdateQueueRecordsVisibility)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesis-2013-12-02/UpdateQueueRecordsVisibility)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/UpdateQueueRecordsVisibility)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/UpdateQueueRecordsVisibility)

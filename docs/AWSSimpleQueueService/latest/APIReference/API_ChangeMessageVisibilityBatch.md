---
source_url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ChangeMessageVisibilityBatch.html
---

# ChangeMessageVisibilityBatch
<a name="API_ChangeMessageVisibilityBatch"></a>

Changes the visibility timeout of multiple messages. This is a batch version of ` ChangeMessageVisibility.` The result of the action on each message is reported individually in the response. You can send up to 10 ` ChangeMessageVisibility ` requests with each `ChangeMessageVisibilityBatch` action.

**Important**
Because the batch request can result in a combination of successful and unsuccessful actions, you should check for batch errors even when the call returns an HTTP status code of `200`.

## Request Syntax
<a name="API_ChangeMessageVisibilityBatch_RequestSyntax"></a>

```
{
   "Entries": [
      {
         "Id": "{{string}}",
         "ReceiptHandle": "{{string}}",
         "VisibilityTimeout": {{number}}
      }
   ],
   "QueueUrl": "{{string}}"
}
```

## Request Parameters
<a name="API_ChangeMessageVisibilityBatch_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Entries](#API_ChangeMessageVisibilityBatch_RequestSyntax) **   <a name="SQS-ChangeMessageVisibilityBatch-request-Entries"></a>
Lists the receipt handles of the messages for which the visibility timeout must be changed.
Type: Array of [ChangeMessageVisibilityBatchRequestEntry](API_ChangeMessageVisibilityBatchRequestEntry.md) objects
Required: Yes

 ** [QueueUrl](#API_ChangeMessageVisibilityBatch_RequestSyntax) **   <a name="SQS-ChangeMessageVisibilityBatch-request-QueueUrl"></a>
The URL of the Amazon SQS queue whose messages' visibility is changed.
Queue URLs and names are case-sensitive.
Type: String
Required: Yes

## Response Syntax
<a name="API_ChangeMessageVisibilityBatch_ResponseSyntax"></a>

```
{
   "Failed": [
      {
         "Code": "string",
         "Id": "string",
         "Message": "string",
         "SenderFault": boolean
      }
   ],
   "Successful": [
      {
         "Id": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ChangeMessageVisibilityBatch_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Failed](#API_ChangeMessageVisibilityBatch_ResponseSyntax) **   <a name="SQS-ChangeMessageVisibilityBatch-response-Failed"></a>
A list of ` BatchResultErrorEntry ` items.
Type: Array of [BatchResultErrorEntry](API_BatchResultErrorEntry.md) objects

 ** [Successful](#API_ChangeMessageVisibilityBatch_ResponseSyntax) **   <a name="SQS-ChangeMessageVisibilityBatch-response-Successful"></a>
A list of ` ChangeMessageVisibilityBatchResultEntry ` items.
Type: Array of [ChangeMessageVisibilityBatchResultEntry](API_ChangeMessageVisibilityBatchResultEntry.md) objects

## Errors
<a name="API_ChangeMessageVisibilityBatch_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** BatchEntryIdsNotDistinct **
Two or more batch entries in the request have the same `Id`.
HTTP Status Code: 400

 ** EmptyBatchRequest **
The batch request doesn't contain any entries.
HTTP Status Code: 400

 ** InvalidAddress **
The specified ID is invalid.
HTTP Status Code: 400

 ** InvalidBatchEntryId **
The `Id` of a batch entry in a batch request doesn't abide by the specification.
HTTP Status Code: 400

 ** InvalidSecurity **
The request was not made over HTTPS or did not use SigV4 for signing.
HTTP Status Code: 400

 ** QueueDoesNotExist **
Ensure that the `QueueUrl` is correct and that the queue has not been deleted.
HTTP Status Code: 400

 ** RequestThrottled **
The request was denied due to request throttling.
+ Exceeds the permitted request rate for the queue or for the recipient of the request.
+ Ensure that the request rate is within the Amazon SQS limits for sending messages. For more information, see [Amazon SQS quotas](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-quotas.html#quotas-requests) in the *Amazon SQS Developer Guide*.
HTTP Status Code: 400

 ** TooManyEntriesInBatchRequest **
The batch request contains more entries than permissible. For Amazon SQS, the maximum number of entries you can include in a single [SendMessageBatch](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessageBatch.html), [DeleteMessageBatch](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_DeleteMessageBatch.html), or [ChangeMessageVisibilityBatch](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ChangeMessageVisibilityBatch.html) request is 10.
HTTP Status Code: 400

 ** UnsupportedOperation **
Error code 400. Unsupported operation.
HTTP Status Code: 400

## Examples
<a name="API_ChangeMessageVisibilityBatch_Examples"></a>

 `ChangeMessageVisibilityBatch` request changes the visibility timeout settings for two messages. You must URL-encode the entire URL. However, in this example only the message body is URL-encoded to make the example easier to read.

### Example
<a name="API_ChangeMessageVisibilityBatch_Example_1"></a>

 **Using AWS JSON protocol (Default)**

#### Sample Request
<a name="API_ChangeMessageVisibilityBatch_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: sqs.us-east-1.amazonaws.com
X-Amz-Target: AmazonSQS.ChangeMessageVisibilityBatch
X-Amz-Date: <Date>
Content-Type: application/x-amz-json-1.0
Authorization: <AuthParams>
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
{
    "QueueUrl": "https://sqs.us-east-1.amazonaws.com/177715257436/MyQueue/",
    "Entries": [
        {
            "Id": "change_visibility_msg_1",
            "ReceiptHandle": "AQEBt7JdeB+HGhLUgVF4/Gc+AvTPvgUL+AVpoHQPb3Gw9U6bRBxx4KYy3U5bk+hBLDGAj84UxMMTG1uhCJLMuS+5MrRkuEE0pgJr6B6J12Xk+qstDQNsRuamy21kSzjmDWhdKNexq8mcMy8dbmSYLa+GytNMShSzyOhrBBUbcwkTdbJPW9czNs6nR4Wb8CteMPwzYCYrYHaM/tePfqcMwlq+d7PSXTM965g2DrTP5pF5puB00BA5MkHTkZyMkUZyENTS704HH+uZW06+7IWUTPcBma8aFt8MY0eeDnOhBtM8SD6fcnNxHXHDOmSkE6cpA68ew5wwYkPdQ2U341SxJbNWGPEfmzCtRJKs7Mc3J+cdjfyNR3QzXiVucoqS6mmRDnVe",
            "VisibilityTimeout": 45
        },
        {
            "Id": "change_visibility_msg_2",
            "ReceiptHandle": "AQEB3LQoW7GQWgodQCEJXHjMvO/QkeCHiRldRfLC/E6RUggm+BjpthqxfoUOUn6Vs271qmrBaufFqEmnMKgk2n1EuUBne1pe+hZcrDE8IveUUPmqkUT54FGhAAjPX3oEIryz/XeQ/muKAuLclcZvt2Q+ZDPW8DvZqMa1RoHxOqSq+6kQ4PwgQxB+VqDYvIc/LpHOoL4PTROBXgLPjWrzz/knK6HTzKpqC4ESvFdJ/dkk2nvS0iqYOly5VQknK/lv/rTUOgEYevjJSrNLIPDgZGyvgcLwbm6+yo1cW/c9cPDiVm96gIhVkuiCZ1gtskoOtyroZVPcY71clDG2EPZJeY8akMd3u+sXEMWhiOPFs1cgWQs2ugsL+vdwMCbsZRkXbJv7",
            "VisibilityTimeout": 45
        }
    ]
}
```

#### Sample Response
<a name="API_ChangeMessageVisibilityBatch_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <requestId>
Content-Length: <PayloadSizeBytes>
Date: <Date>
Content-Type: application/x-amz-json-1.0
{
    "Failed": [],
    "Successful": [
        {
            "Id": "change_visibility_msg_1"
        },
        {
            "Id": "change_visibility_msg_2"
        }
    ]
}
```

### Example
<a name="API_ChangeMessageVisibilityBatch_Example_2"></a>

 **Using AWS query protocol**

#### Sample Request
<a name="API_ChangeMessageVisibilityBatch_Example_2_Request"></a>

```
POST /177715257436/MyQueue HTTP/1.1
Host: sqs.us-east-1.amazonaws.com
X-Amz-Date: <Date>
Content-Type: application/x-www-form-urlencoded
Authorization: <AuthParams>
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
Action=ChangeMessageVisibilityBatch
&ChangeMessageVisibilityBatchRequestEntry.1.Id=change_visibility_msg_2
&ChangeMessageVisibilityBatchRequestEntry.1.ReceiptHandle=gfk0T0R0waama4fVFffkjKzmhMCymjQvfTFk2LxT33G4ms5subrE0deLKWSscPU1oD3J9zgeS4PQQ3U30qOumIE6AdAv3w%2F%2Fa1IXW6AqaWhGsEPaLm3Vf6IiWqdM8u5imB%2BNTwj3tQRzOWdTOePjOjPcTpRxBtXix%2BEvwJOZUma9wabv%2BSw6ZHjwmNcVDx8dZXJhVp16Bksiox%2FGrUvrVTCJRTWTLc59oHLLF8sEkKzRmGNzTDGTiV%2BYjHfQj60FD3rVaXmzTsoNxRhKJ72uIHVMGVQiAGgBX6HGv 9LDmYhPXw4hy%2FNgIg%3D%3D
&ChangeMessageVisibilityBatchRequestEntry.1.VisibilityTimeout=45
&ChangeMessageVisibilityBatchRequestEntry.2.Id=change_visibility_msg_3
&ChangeMessageVisibilityBatchRequestEntry.2.ReceiptHandle=gfk0T0R0waama4f VFffkjKzmhMCymjQvfTFk2LxT33FUgBz3%2BnougdeLKWSscPU1%2FXgx%2BxcNnjnQQ3U30q OumIE6AdAv3w%2F%2Fa1IXW6AqaWhGsEPaLm3Vf6IiWqdM8u5imB%2BNTwj3tQRzOWdTOePjO sogjZM%2F7kzn4Ew27XLU9I%2FYaWYmKvDbq%2Fk3HKVB9HfB43kE49atP2aWrzNL4yunG41Q 4cfRRtfJdcGQGNHQ2%2Byd0Usf5qR1dZr1iDo5xk946eQat83AxTRP%2BY4Qi0V7FAeSLH9su 9xpX6HGv9LDmYhPXw4hy%2FNgIg%3D%3D
&ChangeMessageVisibilityBatchRequestEntry.2.VisibilityTimeout=45
```

#### Sample Response
<a name="API_ChangeMessageVisibilityBatch_Example_2_Response"></a>

```
HTTP/1.1 200 OK
<?xml version="1.0"?>
<ChangeMessageVisibilityBatchResponse xmlns="http://queue.amazonaws.com/doc/2012-11-05/">
    <ChangeMessageVisibilityBatchResult>
        <ChangeMessageVisibilityBatchResultEntry>
            <Id>change_visibility_msg_2</Id>
        </ChangeMessageVisibilityBatchResultEntry>
        <ChangeMessageVisibilityBatchResultEntry>
            <Id>change_visibility_msg_3</Id>
        </ChangeMessageVisibilityBatchResultEntry>
    </ChangeMessageVisibilityBatchResult>
    <ResponseMetadata>
        <RequestId>ca9668f7-ab1b-4f7a-8859-f15747ab17a7</RequestId>
    </ResponseMetadata>
</ChangeMessageVisibilityBatchResponse>
```

## See Also
<a name="API_ChangeMessageVisibilityBatch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sqs-2012-11-05/ChangeMessageVisibilityBatch)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sqs-2012-11-05/ChangeMessageVisibilityBatch)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sqs-2012-11-05/ChangeMessageVisibilityBatch)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sqs-2012-11-05/ChangeMessageVisibilityBatch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sqs-2012-11-05/ChangeMessageVisibilityBatch)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sqs-2012-11-05/ChangeMessageVisibilityBatch)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sqs-2012-11-05/ChangeMessageVisibilityBatch)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sqs-2012-11-05/ChangeMessageVisibilityBatch)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sqs-2012-11-05/ChangeMessageVisibilityBatch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sqs-2012-11-05/ChangeMessageVisibilityBatch)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Queue Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSSimpleQueueService` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

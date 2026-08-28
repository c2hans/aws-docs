---
source_url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ListDeadLetterSourceQueues.html
---

# ListDeadLetterSourceQueues
<a name="API_ListDeadLetterSourceQueues"></a>

Returns a list of your queues that have the `RedrivePolicy` queue attribute configured with a dead-letter queue.

 The `ListDeadLetterSourceQueues` methods supports pagination. Set parameter `MaxResults` in the request to specify the maximum number of results to be returned in the response. If you do not set `MaxResults`, the response includes a maximum of 1,000 results. If you set `MaxResults` and there are additional results to display, the response includes a value for `NextToken`. Use `NextToken` as a parameter in your next request to `ListDeadLetterSourceQueues` to receive the next page of results.

For more information about using dead-letter queues, see [Using Amazon SQS Dead-Letter Queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html) in the *Amazon SQS Developer Guide*.

## Request Syntax
<a name="API_ListDeadLetterSourceQueues_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "QueueUrl": "{{string}}"
}
```

## Request Parameters
<a name="API_ListDeadLetterSourceQueues_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListDeadLetterSourceQueues_RequestSyntax) **   <a name="SQS-ListDeadLetterSourceQueues-request-MaxResults"></a>
Maximum number of results to include in the response. Value range is 1 to 1000. You must set `MaxResults` to receive a value for `NextToken` in the response.
Type: Integer
Required: No

 ** [NextToken](#API_ListDeadLetterSourceQueues_RequestSyntax) **   <a name="SQS-ListDeadLetterSourceQueues-request-NextToken"></a>
Pagination token to request the next set of results.
Type: String
Required: No

 ** [QueueUrl](#API_ListDeadLetterSourceQueues_RequestSyntax) **   <a name="SQS-ListDeadLetterSourceQueues-request-QueueUrl"></a>
The URL of a dead-letter queue.
Queue URLs and names are case-sensitive.
Type: String
Required: Yes

## Response Syntax
<a name="API_ListDeadLetterSourceQueues_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "queueUrls": [ "string" ]
}
```

## Response Elements
<a name="API_ListDeadLetterSourceQueues_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListDeadLetterSourceQueues_ResponseSyntax) **   <a name="SQS-ListDeadLetterSourceQueues-response-NextToken"></a>
Pagination token to include in the next request. Token value is `null` if there are no additional results to request, or if you did not set `MaxResults` in the request.
Type: String

 ** [queueUrls](#API_ListDeadLetterSourceQueues_ResponseSyntax) **   <a name="SQS-ListDeadLetterSourceQueues-response-queueUrls"></a>
A list of source queue URLs that have the `RedrivePolicy` queue attribute configured with a dead-letter queue.
Type: Array of strings

## Errors
<a name="API_ListDeadLetterSourceQueues_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** InvalidAddress **
The specified ID is invalid.
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

 ** UnsupportedOperation **
Error code 400. Unsupported operation.
HTTP Status Code: 400

## Examples
<a name="API_ListDeadLetterSourceQueues_Examples"></a>

The following example query request returns a list of dead letter source queues. In this example, only one source queue, `MySourceQueue`, is configured with a dead-letter queue. The structure of `AUTHPARAMS` depends on the signature of the API request. For more information, see [ Examples of Signed Signature Version 4 Requests](https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html) in the * AWS General Reference*.

### Example
<a name="API_ListDeadLetterSourceQueues_Example_1"></a>

 **Using AWS JSON protocol (Default)**

#### Sample Request
<a name="API_ListDeadLetterSourceQueues_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: sqs.us-east-1.amazonaws.com
X-Amz-Target: AmazonSQS.ListDeadLetterSourceQueues
X-Amz-Date: <Date>
Content-Type: application/x-amz-json-1.0
Authorization: <AuthParams>
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
{
    "QueueUrl": "https://sqs.us-east-1.amazonaws.com/177715257436/MyQueue"
}
```

#### Sample Response
<a name="API_ListDeadLetterSourceQueues_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <requestId>
Content-Length: <PayloadSizeBytes>
Date: <Date>
Content-Type: application/x-amz-json-1.0
{
    "queueUrls": [
        "https://sqs.us-east-1.amazonaws.com/123456789012/MySourceQueue</QueueUrl>"
    ]
}
```

### Example
<a name="API_ListDeadLetterSourceQueues_Example_2"></a>

 **Using AWS query protocol**

#### Sample Request
<a name="API_ListDeadLetterSourceQueues_Example_2_Request"></a>

```
POST /177715257436/MyQueue/ HTTP/1.1
Host: sqs.us-east-1.amazonaws.com
Content-Type: application/x-www-form-urlencoded
X-Amz-Date: <Date>
Authorization: <AuthParams>
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
Action=ListDeadLetterSourceQueues
```

#### Sample Response
<a name="API_ListDeadLetterSourceQueues_Example_2_Response"></a>

```
HTTP/1.1 200 OK
<?xml version="1.0"?>
<ListDeadLetterSourceQueuesResponse xmlns="http://queue.amazonaws.com/doc/2012-11-05/">
    <ListDeadLetterSourceQueuesResult/>
    <ResponseMetadata>
        <RequestId>8e70ce7e-e3d4-5109-9204-920e21745daf</RequestId>
    </ResponseMetadata>
</ListDeadLetterSourceQueuesResponse>
```

## See Also
<a name="API_ListDeadLetterSourceQueues_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sqs-2012-11-05/ListDeadLetterSourceQueues)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sqs-2012-11-05/ListDeadLetterSourceQueues)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sqs-2012-11-05/ListDeadLetterSourceQueues)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sqs-2012-11-05/ListDeadLetterSourceQueues)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sqs-2012-11-05/ListDeadLetterSourceQueues)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sqs-2012-11-05/ListDeadLetterSourceQueues)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sqs-2012-11-05/ListDeadLetterSourceQueues)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sqs-2012-11-05/ListDeadLetterSourceQueues)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sqs-2012-11-05/ListDeadLetterSourceQueues)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sqs-2012-11-05/ListDeadLetterSourceQueues)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Queue Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSSimpleQueueService` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

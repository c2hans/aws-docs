---
source_url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ListQueues.html
---

# ListQueues
<a name="API_ListQueues"></a>

Returns a list of your queues in the current region. The response includes a maximum of 1,000 results. If you specify a value for the optional `QueueNamePrefix` parameter, only queues with a name that begins with the specified value are returned.

 The `listQueues` methods supports pagination. Set parameter `MaxResults` in the request to specify the maximum number of results to be returned in the response. If you do not set `MaxResults`, the response includes a maximum of 1,000 results. If you set `MaxResults` and there are additional results to display, the response includes a value for `NextToken`. Use `NextToken` as a parameter in your next request to `listQueues` to receive the next page of results.

**Note**
Cross-account permissions don't apply to this action. For more information, see [Grant cross-account permissions to a role and a username](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-customer-managed-policy-examples.html#grant-cross-account-permissions-to-role-and-user-name) in the *Amazon SQS Developer Guide*.

## Request Syntax
<a name="API_ListQueues_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "QueueNamePrefix": "{{string}}"
}
```

## Request Parameters
<a name="API_ListQueues_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListQueues_RequestSyntax) **   <a name="SQS-ListQueues-request-MaxResults"></a>
Maximum number of results to include in the response. Value range is 1 to 1000. You must set `MaxResults` to receive a value for `NextToken` in the response.
Type: Integer
Required: No

 ** [NextToken](#API_ListQueues_RequestSyntax) **   <a name="SQS-ListQueues-request-NextToken"></a>
Pagination token to request the next set of results.
Type: String
Required: No

 ** [QueueNamePrefix](#API_ListQueues_RequestSyntax) **   <a name="SQS-ListQueues-request-QueueNamePrefix"></a>
A string to use for filtering the list results. Only those queues whose name begins with the specified string are returned.
Queue URLs and names are case-sensitive.
Type: String
Required: No

## Response Syntax
<a name="API_ListQueues_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "QueueUrls": [ "string" ]
}
```

## Response Elements
<a name="API_ListQueues_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListQueues_ResponseSyntax) **   <a name="SQS-ListQueues-response-NextToken"></a>
Pagination token to include in the next request. Token value is `null` if there are no additional results to request, or if you did not set `MaxResults` in the request.
Type: String

 ** [QueueUrls](#API_ListQueues_ResponseSyntax) **   <a name="SQS-ListQueues-response-QueueUrls"></a>
A list of queue URLs, up to 1,000 entries, or the value of `MaxResults` that you sent in the request.
Type: Array of strings

## Errors
<a name="API_ListQueues_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** InvalidAddress **
The specified ID is invalid.
HTTP Status Code: 400

 ** InvalidSecurity **
The request was not made over HTTPS or did not use SigV4 for signing.
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
<a name="API_ListQueues_Examples"></a>

The following example query request returns the queues whose names begin with the letter `t` The structure of `AUTHPARAMS` depends on the signature of the API request. For more information, see [ Examples of Signed Signature Version 4 Requests](https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html) in the * AWS General Reference*.

### Example
<a name="API_ListQueues_Example_1"></a>

 **Using AWS JSON protocol (Default)**

#### Sample Request
<a name="API_ListQueues_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: sqs.us-east-1.amazonaws.com
X-Amz-Target: AmazonSQS.ListQueues
X-Amz-Date: <Date>
Content-Type: application/x-amz-json-1.0
Authorization: <AuthParams>
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
{
    "QueueNamePrefix": "My"
}
```

#### Sample Response
<a name="API_ListQueues_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <requestId>
Content-Length: <PayloadSizeBytes>
Date: <Date>
Content-Type: application/x-amz-json-1.0
{
    "QueueUrls": [
        "https://sqs.us-east-1.amazonaws.com/177715257436/MyQueue",
        "https://sqs.us-east-1.amazonaws.com/177715257436/MyQueue1648169377027",
        "https://sqs.us-east-1.amazonaws.com/177715257436/MyQueue1648169549830",
        "https://sqs.us-east-1.amazonaws.com/177715257436/MyQueue1648227401019",
        "https://sqs.us-east-1.amazonaws.com/177715257436/MyQueue1648248132466",
        "https://sqs.us-east-1.amazonaws.com/177715257436/MyQueue1649201932174",
        "https://sqs.us-east-1.amazonaws.com/177715257436/MyQueue2"
    ]
}
```

### Example
<a name="API_ListQueues_Example_2"></a>

 **Using AWS query protocol**

#### Sample Request
<a name="API_ListQueues_Example_2_Request"></a>

```
POST / HTTP/1.1
Host: sqs.us-east-1.amazonaws.com
Content-Type: application/x-www-form-urlencoded
X-Amz-Date: <Date>
Authorization: <AuthParams>
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
Action=ListQueues&QueueNamePrefix=M
```

#### Sample Response
<a name="API_ListQueues_Example_2_Response"></a>

```
HTTP/1.1 200 OK
<?xml version="1.0"?>
<ListQueuesResponse xmlns="http://queue.amazonaws.com/doc/2012-11-05/">
    <ListQueuesResult>
        <QueueUrl>https://sqs.us-east-1.amazonaws.com/177715257436/MyQueue1648169377027</QueueUrl>
        <QueueUrl>https://sqs.us-east-1.amazonaws.com/177715257436/MyQueue1648169549830</QueueUrl>
        <QueueUrl>https://sqs.us-east-1.amazonaws.com/177715257436/MyQueue1648227401019</QueueUrl>
        <QueueUrl>https://sqs.us-east-1.amazonaws.com/177715257436/MyQueue1648248132466</QueueUrl>
        <QueueUrl>https://sqs.us-east-1.amazonaws.com/177715257436/MyQueue1649201932174</QueueUrl>
        <QueueUrl>https://sqs.us-east-1.amazonaws.com/177715257436/MyQueue22</QueueUrl>
        <QueueUrl>https://sqs.us-east-1.amazonaws.com/177715257436/MyQueue23</QueueUrl>
        <QueueUrl>https://sqs.us-east-1.amazonaws.com/177715257436/MyQueue233</QueueUrl>
        <QueueUrl>https://sqs.us-east-1.amazonaws.com/177715257436/MyQueue5</QueueUrl>
        <QueueUrl>https://sqs.us-east-1.amazonaws.com/177715257436/MyQueueTest</QueueUrl>
    </ListQueuesResult>
    <ResponseMetadata>
        <RequestId>f525e5e2-86cd-5d1b-aee9-b992443254c0</RequestId>
    </ResponseMetadata>
</ListQueuesResponse>
```

## See Also
<a name="API_ListQueues_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sqs-2012-11-05/ListQueues)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sqs-2012-11-05/ListQueues)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sqs-2012-11-05/ListQueues)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sqs-2012-11-05/ListQueues)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sqs-2012-11-05/ListQueues)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sqs-2012-11-05/ListQueues)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sqs-2012-11-05/ListQueues)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sqs-2012-11-05/ListQueues)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sqs-2012-11-05/ListQueues)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sqs-2012-11-05/ListQueues)

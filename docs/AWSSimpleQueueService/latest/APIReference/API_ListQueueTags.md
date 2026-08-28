---
source_url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ListQueueTags.html
---

# ListQueueTags
<a name="API_ListQueueTags"></a>

List all cost allocation tags added to the specified Amazon SQS queue. For an overview, see [Tagging Your Amazon SQS Queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-queue-tags.html) in the *Amazon SQS Developer Guide*.

**Note**
Cross-account permissions don't apply to this action. For more information, see [Grant cross-account permissions to a role and a username](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-customer-managed-policy-examples.html#grant-cross-account-permissions-to-role-and-user-name) in the *Amazon SQS Developer Guide*.

## Request Syntax
<a name="API_ListQueueTags_RequestSyntax"></a>

```
{
   "QueueUrl": "{{string}}"
}
```

## Request Parameters
<a name="API_ListQueueTags_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [QueueUrl](#API_ListQueueTags_RequestSyntax) **   <a name="SQS-ListQueueTags-request-QueueUrl"></a>
The URL of the queue.
Type: String
Required: Yes

## Response Syntax
<a name="API_ListQueueTags_ResponseSyntax"></a>

```
{
   "Tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_ListQueueTags_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Tags](#API_ListQueueTags_ResponseSyntax) **   <a name="SQS-ListQueueTags-response-Tags"></a>
The list of all tags added to the specified queue.
Type: String to string map

## Errors
<a name="API_ListQueueTags_Errors"></a>

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
<a name="API_ListQueueTags_Examples"></a>

This example illustrates one usage of `ListQueueTags`.

### Example
<a name="API_ListQueueTags_Example_1"></a>

 **Using AWS JSON protocol (Default)**

#### Sample Request
<a name="API_ListQueueTags_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: sqs.us-east-1.amazonaws.com
X-Amz-Target: AmazonSQS.ListQueueTags
X-Amz-Date: <Date>
Content-Type: application/x-amz-json-1.0
Authorization: <AuthParams>
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
{
    "QueueUrl": "https://sqs.us-east-1.amazonaws.com/177715257436/MyQueue/"
}
```

#### Sample Response
<a name="API_ListQueueTags_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <requestId>
Content-Length: <PayloadSizeBytes>
Date: <Date>
Content-Type: application/x-amz-json-1.0
{
    "Tags": {
        "QueueType": "Production"
    }
}
```

### Example
<a name="API_ListQueueTags_Example_2"></a>

 **Using AWS query protocol**

#### Sample Request
<a name="API_ListQueueTags_Example_2_Request"></a>

```
POST /177715257436/MyQueue HTTP/1.1
Host: sqs.us-east-1.amazonaws.com
Content-Type: application/x-www-form-urlencoded
X-Amz-Date: <Date>
Authorization: <AuthParams>
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
Action=ListQueueTags
```

#### Sample Response
<a name="API_ListQueueTags_Example_2_Response"></a>

```
HTTP/1.1 200 OK
<?xml version="1.0"?>
<ListQueueTagsResponse xmlns="http://queue.amazonaws.com/doc/2012-11-05/">
    <ListQueueTagsResult>
        <Tag>
            <Key>QueueType</Key>
            <Value>Production</Value>
        </Tag>
    </ListQueueTagsResult>
    <ResponseMetadata>
        <RequestId>02c89a6b-9fc0-564a-9ed1-c61b5cacdc6d</RequestId>
    </ResponseMetadata>
</ListQueueTagsResponse>
```

## See Also
<a name="API_ListQueueTags_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sqs-2012-11-05/ListQueueTags)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sqs-2012-11-05/ListQueueTags)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sqs-2012-11-05/ListQueueTags)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sqs-2012-11-05/ListQueueTags)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sqs-2012-11-05/ListQueueTags)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sqs-2012-11-05/ListQueueTags)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sqs-2012-11-05/ListQueueTags)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sqs-2012-11-05/ListQueueTags)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sqs-2012-11-05/ListQueueTags)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sqs-2012-11-05/ListQueueTags)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Queue Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSSimpleQueueService` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_UntagDeliveryStream.html
---

# UntagDeliveryStream
<a name="API_UntagDeliveryStream"></a>

Removes tags from the specified Firehose stream. Removed tags are deleted, and you can't recover them after this operation successfully completes.

If you specify a tag that doesn't exist, the operation ignores it.

This operation has a limit of five transactions per second per account.

## Request Syntax
<a name="API_UntagDeliveryStream_RequestSyntax"></a>

```
{
   "DeliveryStreamName": "{{string}}",
   "TagKeys": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_UntagDeliveryStream_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DeliveryStreamName](#API_UntagDeliveryStream_RequestSyntax) **   <a name="Firehose-UntagDeliveryStream-request-DeliveryStreamName"></a>
The name of the Firehose stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [TagKeys](#API_UntagDeliveryStream_RequestSyntax) **   <a name="Firehose-UntagDeliveryStream-request-TagKeys"></a>
A list of tag keys. Each corresponding tag is removed from the delivery stream.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:\/=+\-@%]*$`
Required: Yes

## Response Elements
<a name="API_UntagDeliveryStream_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UntagDeliveryStream_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidArgumentException **
The specified input parameter has a value that is not valid.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** LimitExceededException **
You have already reached the limit for a requested resource.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** ResourceInUseException **
The resource is already in use and not available for this operation.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource could not be found.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

## Examples
<a name="API_UntagDeliveryStream_Examples"></a>

### To remove tags from a stream
<a name="API_UntagDeliveryStream_Example_1"></a>

The following JSON example removes the specified tag from the specified stream.

#### Sample Request
<a name="API_UntagDeliveryStream_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: firehose.<region>.<domain>
Content-Length: <PayloadSizeBytes>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Authorization: <AuthParams>
Connection: Keep-Alive
X-Amz-Date: <Date>
X-Amz-Target: Firehose_20150804.UntagDeliveryStream
{
  "DeliveryStreamName": "exampleDeliveryStreamName",
  "TagKeys": ["Project", "Environment"]
}
```

#### Sample Response
<a name="API_UntagDeliveryStream_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
```

## See Also
<a name="API_UntagDeliveryStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/firehose-2015-08-04/UntagDeliveryStream)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/firehose-2015-08-04/UntagDeliveryStream)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/UntagDeliveryStream)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/firehose-2015-08-04/UntagDeliveryStream)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/UntagDeliveryStream)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/firehose-2015-08-04/UntagDeliveryStream)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/firehose-2015-08-04/UntagDeliveryStream)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/firehose-2015-08-04/UntagDeliveryStream)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/firehose-2015-08-04/UntagDeliveryStream)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/UntagDeliveryStream)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

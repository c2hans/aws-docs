---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_TagDeliveryStream.html
---

# TagDeliveryStream
<a name="API_TagDeliveryStream"></a>

Adds or updates tags for the specified Firehose stream. A tag is a key-value pair that you can define and assign to AWS resources. If you specify a tag that already exists, the tag value is replaced with the value that you specify in the request. Tags are metadata. For example, you can add friendly names and descriptions or other types of information that can help you distinguish the Firehose stream. For more information about tags, see [Using Cost Allocation Tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) in the * AWS Billing and Cost Management User Guide*.

Each Firehose stream can have up to 50 tags.

This operation has a limit of five transactions per second per account.

## Request Syntax
<a name="API_TagDeliveryStream_RequestSyntax"></a>

```
{
   "DeliveryStreamName": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_TagDeliveryStream_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DeliveryStreamName](#API_TagDeliveryStream_RequestSyntax) **   <a name="Firehose-TagDeliveryStream-request-DeliveryStreamName"></a>
The name of the Firehose stream to which you want to add the tags.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [Tags](#API_TagDeliveryStream_RequestSyntax) **   <a name="Firehose-TagDeliveryStream-request-Tags"></a>
A set of key-value pairs to use to create the tags.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: Yes

## Response Elements
<a name="API_TagDeliveryStream_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_TagDeliveryStream_Errors"></a>

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
<a name="API_TagDeliveryStream_Examples"></a>

### To add tags to a stream
<a name="API_TagDeliveryStream_Example_1"></a>

The following JSON example adds two tags to the specified stream.

#### Sample Request
<a name="API_TagDeliveryStream_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: firehose.<region>.<domain>
Content-Length: <PayloadSizeBytes>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Authorization: <AuthParams>
Connection: Keep-Alive
X-Amz-Date: <Date>
X-Amz-Target: Firehose_20150804.TagDeliveryStream
{
  "DeliveryStreamName": "exampleDeliveryStreamName",
  "Tags": [
    {
      "Key": "Project",
      "Value": "myProject"
    },
    {
      "Key": "Environment",
      "Value": "Production"
    }
  ]
}
```

#### Sample Response
<a name="API_TagDeliveryStream_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
```

## See Also
<a name="API_TagDeliveryStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/firehose-2015-08-04/TagDeliveryStream)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/firehose-2015-08-04/TagDeliveryStream)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/TagDeliveryStream)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/firehose-2015-08-04/TagDeliveryStream)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/TagDeliveryStream)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/firehose-2015-08-04/TagDeliveryStream)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/firehose-2015-08-04/TagDeliveryStream)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/firehose-2015-08-04/TagDeliveryStream)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/firehose-2015-08-04/TagDeliveryStream)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/TagDeliveryStream)

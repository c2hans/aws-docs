---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_ListTagsForDeliveryStream.html
---

# ListTagsForDeliveryStream
<a name="API_ListTagsForDeliveryStream"></a>

Lists the tags for the specified Firehose stream. This operation has a limit of five transactions per second per account.

## Request Syntax
<a name="API_ListTagsForDeliveryStream_RequestSyntax"></a>

```
{
   "DeliveryStreamName": "{{string}}",
   "ExclusiveStartTagKey": "{{string}}",
   "Limit": {{number}}
}
```

## Request Parameters
<a name="API_ListTagsForDeliveryStream_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DeliveryStreamName](#API_ListTagsForDeliveryStream_RequestSyntax) **   <a name="Firehose-ListTagsForDeliveryStream-request-DeliveryStreamName"></a>
The name of the Firehose stream whose tags you want to list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [ExclusiveStartTagKey](#API_ListTagsForDeliveryStream_RequestSyntax) **   <a name="Firehose-ListTagsForDeliveryStream-request-ExclusiveStartTagKey"></a>
The key to use as the starting point for the list of tags. If you set this parameter, `ListTagsForDeliveryStream` gets all tags that occur after `ExclusiveStartTagKey`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:\/=+\-@%]*$`
Required: No

 ** [Limit](#API_ListTagsForDeliveryStream_RequestSyntax) **   <a name="Firehose-ListTagsForDeliveryStream-request-Limit"></a>
The number of tags to return. If this number is less than the total number of tags associated with the Firehose stream, `HasMoreTags` is set to `true` in the response. To list additional tags, set `ExclusiveStartTagKey` to the last key in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

## Response Syntax
<a name="API_ListTagsForDeliveryStream_ResponseSyntax"></a>

```
{
   "HasMoreTags": boolean,
   "Tags": [
      {
         "Key": "string",
         "Value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListTagsForDeliveryStream_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [HasMoreTags](#API_ListTagsForDeliveryStream_ResponseSyntax) **   <a name="Firehose-ListTagsForDeliveryStream-response-HasMoreTags"></a>
If this is `true` in the response, more tags are available. To list the remaining tags, set `ExclusiveStartTagKey` to the key of the last tag returned and call `ListTagsForDeliveryStream` again.
Type: Boolean

 ** [Tags](#API_ListTagsForDeliveryStream_ResponseSyntax) **   <a name="Firehose-ListTagsForDeliveryStream-response-Tags"></a>
A list of tags associated with `DeliveryStreamName`, starting with the first tag after `ExclusiveStartTagKey` and up to the specified `Limit`.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.

## Errors
<a name="API_ListTagsForDeliveryStream_Errors"></a>

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

 ** ResourceNotFoundException **
The specified resource could not be found.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

## Examples
<a name="API_ListTagsForDeliveryStream_Examples"></a>

### To list the tags for a stream
<a name="API_ListTagsForDeliveryStream_Example_1"></a>

The following JSON example lists the tags for the specified Firehose stream.

#### Sample Request
<a name="API_ListTagsForDeliveryStream_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: firehose.<region>.<domain>
Content-Length: <PayloadSizeBytes>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Authorization: <AuthParams>
Connection: Keep-Alive
X-Amz-Date: <Date>
X-Amz-Target: Firehose_20150804.ListTagsForDeliveryStream
{
  "DeliveryStreamName": "exampleDeliveryStreamName"
}
```

#### Sample Response
<a name="API_ListTagsForDeliveryStream_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
  "HasMoreTags": "false",
  "Tags" : [
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

## See Also
<a name="API_ListTagsForDeliveryStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/firehose-2015-08-04/ListTagsForDeliveryStream)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/firehose-2015-08-04/ListTagsForDeliveryStream)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/ListTagsForDeliveryStream)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/firehose-2015-08-04/ListTagsForDeliveryStream)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/ListTagsForDeliveryStream)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/firehose-2015-08-04/ListTagsForDeliveryStream)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/firehose-2015-08-04/ListTagsForDeliveryStream)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/firehose-2015-08-04/ListTagsForDeliveryStream)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/firehose-2015-08-04/ListTagsForDeliveryStream)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/ListTagsForDeliveryStream)

---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_ListTagsForStream.html
---

# ListTagsForStream
<a name="API_ListTagsForStream"></a>

Lists the tags for the specified Kinesis data stream. This operation has a limit of five transactions per second per account.

**Note**
When invoking this API, you must use either the `StreamARN` or the `StreamName` parameter, or both. It is recommended that you use the `StreamARN` input parameter when you invoke this API.

## Request Syntax
<a name="API_ListTagsForStream_RequestSyntax"></a>

```
{
   "ExclusiveStartTagKey": "{{string}}",
   "Limit": {{number}},
   "StreamARN": "{{string}}",
   "StreamId": "{{string}}",
   "StreamName": "{{string}}"
}
```

## Request Parameters
<a name="API_ListTagsForStream_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ExclusiveStartTagKey](#API_ListTagsForStream_RequestSyntax) **   <a name="Streams-ListTagsForStream-request-ExclusiveStartTagKey"></a>
The key to use as the starting point for the list of tags. If this parameter is set, `ListTagsForStream` gets all tags that occur after `ExclusiveStartTagKey`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [Limit](#API_ListTagsForStream_RequestSyntax) **   <a name="Streams-ListTagsForStream-request-Limit"></a>
The number of tags to return. If this number is less than the total number of tags associated with the stream, `HasMoreTags` is set to `true`. To list additional tags, set `ExclusiveStartTagKey` to the last key in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [StreamARN](#API_ListTagsForStream_RequestSyntax) **   <a name="Streams-ListTagsForStream-request-StreamARN"></a>
The ARN of the stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws.*:kinesis:.*:\d{12}:stream/\S+`
Required: No

 ** [StreamId](#API_ListTagsForStream_RequestSyntax) **   <a name="Streams-ListTagsForStream-request-StreamId"></a>
Not Implemented. Reserved for future use.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 24.
Pattern: `[a-z0-9]{20}-[a-z0-9]{3}`
Required: No

 ** [StreamName](#API_ListTagsForStream_RequestSyntax) **   <a name="Streams-ListTagsForStream-request-StreamName"></a>
The name of the stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

## Response Syntax
<a name="API_ListTagsForStream_ResponseSyntax"></a>

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
<a name="API_ListTagsForStream_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [HasMoreTags](#API_ListTagsForStream_ResponseSyntax) **   <a name="Streams-ListTagsForStream-response-HasMoreTags"></a>
If set to `true`, more tags are available. To request additional tags, set `ExclusiveStartTagKey` to the key of the last tag returned.
Type: Boolean

 ** [Tags](#API_ListTagsForStream_ResponseSyntax) **   <a name="Streams-ListTagsForStream-response-Tags"></a>
A list of tags associated with `StreamName`, starting with the first tag after `ExclusiveStartTagKey` and up to the specified `Limit`.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.

## Errors
<a name="API_ListTagsForStream_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Specifies that you do not have the permissions required to perform this operation.
HTTP Status Code: 400

 ** InvalidArgumentException **
A specified parameter exceeds its restrictions, is not supported, or can't be used. For more information, see the returned message.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** LimitExceededException **
The requested resource exceeds the maximum number allowed, or the number of concurrent stream requests exceeds the maximum number allowed.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The requested resource could not be found. The stream might not be specified correctly.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

## Examples
<a name="API_ListTagsForStream_Examples"></a>

### To list the tags for a stream
<a name="API_ListTagsForStream_Example_1"></a>

The following JSON example lists the tags for the specified stream.

#### Sample Request
<a name="API_ListTagsForStream_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: kinesis.<region>.<domain>
Content-Length: <PayloadSizeBytes>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Authorization: <AuthParams>
Connection: Keep-Alive
X-Amz-Date: <Date>
X-Amz-Target: Kinesis_20131202.ListTagsForStream
{
  "StreamName": "exampleStreamName"
}
```

#### Sample Response
<a name="API_ListTagsForStream_Example_1_Response"></a>

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
<a name="API_ListTagsForStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesis-2013-12-02/ListTagsForStream)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesis-2013-12-02/ListTagsForStream)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/ListTagsForStream)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesis-2013-12-02/ListTagsForStream)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/ListTagsForStream)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesis-2013-12-02/ListTagsForStream)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesis-2013-12-02/ListTagsForStream)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesis-2013-12-02/ListTagsForStream)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/ListTagsForStream)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/ListTagsForStream)

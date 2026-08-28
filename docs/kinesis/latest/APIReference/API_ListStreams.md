---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_ListStreams.html
---

# ListStreams
<a name="API_ListStreams"></a>

Lists your Kinesis data streams.

The number of streams may be too large to return from a single call to `ListStreams`. You can limit the number of returned streams using the `Limit` parameter. If you do not specify a value for the `Limit` parameter, Kinesis Data Streams uses the default limit, which is currently 100.

You can detect if there are more streams available to list by using the `HasMoreStreams` flag from the returned output. If there are more streams available, you can request more streams by using the name of the last stream returned by the `ListStreams` request in the `ExclusiveStartStreamName` parameter in a subsequent request to `ListStreams`. The group of stream names returned by the subsequent request is then added to the list. You can continue this process until all the stream names have been collected in the list.

 [ListStreams](#API_ListStreams) has a limit of five transactions per second per account.

## Request Syntax
<a name="API_ListStreams_RequestSyntax"></a>

```
{
   "ExclusiveStartStreamName": "{{string}}",
   "Limit": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListStreams_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ExclusiveStartStreamName](#API_ListStreams_RequestSyntax) **   <a name="Streams-ListStreams-request-ExclusiveStartStreamName"></a>
The name of the stream to start the list with.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** [Limit](#API_ListStreams_RequestSyntax) **   <a name="Streams-ListStreams-request-Limit"></a>
The maximum number of streams to list. The default value is 100. If you specify a value greater than 100, at most 100 results are returned.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10000.
Required: No

 ** [NextToken](#API_ListStreams_RequestSyntax) **   <a name="Streams-ListStreams-request-NextToken"></a>

Type: String
Length Constraints: Minimum length of 1. Maximum length of 1048576.
Required: No

## Response Syntax
<a name="API_ListStreams_ResponseSyntax"></a>

```
{
   "HasMoreStreams": boolean,
   "NextToken": "string",
   "StreamNames": [ "string" ],
   "StreamSummaries": [
      {
         "StreamARN": "string",
         "StreamCreationTimestamp": number,
         "StreamModeDetails": {
            "StreamMode": "string"
         },
         "StreamName": "string",
         "StreamStatus": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListStreams_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [HasMoreStreams](#API_ListStreams_ResponseSyntax) **   <a name="Streams-ListStreams-response-HasMoreStreams"></a>
If set to `true`, there are more streams available to list.
Type: Boolean

 ** [NextToken](#API_ListStreams_ResponseSyntax) **   <a name="Streams-ListStreams-response-NextToken"></a>

Type: String
Length Constraints: Minimum length of 1. Maximum length of 1048576.

 ** [StreamNames](#API_ListStreams_ResponseSyntax) **   <a name="Streams-ListStreams-response-StreamNames"></a>
The names of the streams that are associated with the AWS account making the `ListStreams` request.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`

 ** [StreamSummaries](#API_ListStreams_ResponseSyntax) **   <a name="Streams-ListStreams-response-StreamSummaries"></a>

Type: Array of [StreamSummary](API_StreamSummary.md) objects

## Errors
<a name="API_ListStreams_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ExpiredNextTokenException **
The pagination token passed to the operation is expired.
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

## Examples
<a name="API_ListStreams_Examples"></a>

### To list your streams
<a name="API_ListStreams_Example_1"></a>

The following JSON example lists your streams, starting with the specified stream.

#### Sample Request
<a name="API_ListStreams_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: kinesis.<region>.<domain>
Content-Length: <PayloadSizeBytes>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Authorization: <AuthParams>
Connection: Keep-Alive
X-Amz-Date: <Date>
X-Amz-Target: Kinesis_20131202.ListStreams
```

#### Sample Response
<a name="API_ListStreams_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
  "HasMoreStreams": false,
  "StreamNames": [
    "exampleStreamName"
  ]
}
```

## See Also
<a name="API_ListStreams_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesis-2013-12-02/ListStreams)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesis-2013-12-02/ListStreams)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/ListStreams)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesis-2013-12-02/ListStreams)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/ListStreams)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesis-2013-12-02/ListStreams)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesis-2013-12-02/ListStreams)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesis-2013-12-02/ListStreams)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/ListStreams)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/ListStreams)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

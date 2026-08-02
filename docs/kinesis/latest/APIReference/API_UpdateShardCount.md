---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_UpdateShardCount.html
---

# UpdateShardCount
<a name="API_UpdateShardCount"></a>

Updates the shard count of the specified stream to the specified number of shards. This API is only supported for the data streams with the provisioned capacity mode.

**Note**
When invoking this API, you must use either the `StreamARN` or the `StreamName` parameter, or both. It is recommended that you use the `StreamARN` input parameter when you invoke this API.

Updating the shard count is an asynchronous operation. Upon receiving the request, Kinesis Data Streams returns immediately and sets the status of the stream to `UPDATING`. After the update is complete, Kinesis Data Streams sets the status of the stream back to `ACTIVE`. Depending on the size of the stream, the scaling action could take a few minutes to complete. You can continue to read and write data to your stream while its status is `UPDATING`.

To update the shard count, Kinesis Data Streams performs splits or merges on individual shards. This can cause short-lived shards to be created, in addition to the final shards. These short-lived shards count towards your total shard limit for your account in the Region.

When using this operation, we recommend that you specify a target shard count that is a multiple of 25% (25%, 50%, 75%, 100%). You can specify any target value within your shard limit. However, if you specify a target that isn't a multiple of 25%, the scaling action might take longer to complete.

This operation has the following default limits. By default, you cannot do the following:
+ Scale more than ten times per rolling 24-hour period per stream
+ Scale up to more than double your current shard count for a stream
+ Scale down below half your current shard count for a stream
+ Scale up to more than 10000 shards in a stream
+ Scale a stream with more than 10000 shards down unless the result is less than 10000 shards
+ Scale up to more than the shard limit for your account
+ Make over 10 TPS. TPS over 10 will trigger the LimitExceededException

For the default limits for an AWS account, see [Streams Limits](https://docs.aws.amazon.com/kinesis/latest/dev/service-sizes-and-limits.html) in the *Amazon Kinesis Data Streams Developer Guide*. To request an increase in the call rate limit, the shard limit for this API, or your overall shard limit, use the [limits form](https://console.aws.amazon.com/support/v1#/case/create?issueType=service-limit-increase&limitType=service-code-kinesis).

## Request Syntax
<a name="API_UpdateShardCount_RequestSyntax"></a>

```
{
   "ScalingType": "{{string}}",
   "StreamARN": "{{string}}",
   "StreamId": "{{string}}",
   "StreamName": "{{string}}",
   "TargetShardCount": {{number}}
}
```

## Request Parameters
<a name="API_UpdateShardCount_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ScalingType](#API_UpdateShardCount_RequestSyntax) **   <a name="Streams-UpdateShardCount-request-ScalingType"></a>
The scaling type. Uniform scaling creates shards of equal size.
Type: String
Valid Values: `UNIFORM_SCALING`
Required: Yes

 ** [StreamARN](#API_UpdateShardCount_RequestSyntax) **   <a name="Streams-UpdateShardCount-request-StreamARN"></a>
The ARN of the stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws.*:kinesis:.*:\d{12}:stream/\S+`
Required: No

 ** [StreamId](#API_UpdateShardCount_RequestSyntax) **   <a name="Streams-UpdateShardCount-request-StreamId"></a>
Not Implemented. Reserved for future use.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 24.
Pattern: `[a-z0-9]{20}-[a-z0-9]{3}`
Required: No

 ** [StreamName](#API_UpdateShardCount_RequestSyntax) **   <a name="Streams-UpdateShardCount-request-StreamName"></a>
The name of the stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** [TargetShardCount](#API_UpdateShardCount_RequestSyntax) **   <a name="Streams-UpdateShardCount-request-TargetShardCount"></a>
The new number of shards. This value has the following default limits. By default, you cannot do the following:
+ Set this value to more than double your current shard count for a stream.
+ Set this value below half your current shard count for a stream.
+ Set this value to more than 10000 shards in a stream (the default limit for shard count per stream is 10000 per account per region), unless you request a limit increase.
+ Scale a stream with more than 10000 shards down unless you set this value to less than 10000 shards.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

## Response Syntax
<a name="API_UpdateShardCount_ResponseSyntax"></a>

```
{
   "CurrentShardCount": number,
   "StreamARN": "string",
   "StreamName": "string",
   "TargetShardCount": number
}
```

## Response Elements
<a name="API_UpdateShardCount_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CurrentShardCount](#API_UpdateShardCount_ResponseSyntax) **   <a name="Streams-UpdateShardCount-response-CurrentShardCount"></a>
The current number of shards.
Type: Integer
Valid Range: Minimum value of 1.

 ** [StreamARN](#API_UpdateShardCount_ResponseSyntax) **   <a name="Streams-UpdateShardCount-response-StreamARN"></a>
The ARN of the stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws.*:kinesis:.*:\d{12}:stream/\S+`

 ** [StreamName](#API_UpdateShardCount_ResponseSyntax) **   <a name="Streams-UpdateShardCount-response-StreamName"></a>
The name of the stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`

 ** [TargetShardCount](#API_UpdateShardCount_ResponseSyntax) **   <a name="Streams-UpdateShardCount-response-TargetShardCount"></a>
The updated number of shards.
Type: Integer
Valid Range: Minimum value of 1.

## Errors
<a name="API_UpdateShardCount_Errors"></a>

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

 ** ResourceInUseException **
The resource is not available for this operation. For successful operation, the resource must be in the `ACTIVE` state.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The requested resource could not be found. The stream might not be specified correctly.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** ValidationException **
Specifies that you tried to invoke this API for a data stream with the on-demand capacity mode. This API is only supported for data streams with the provisioned capacity mode.
HTTP Status Code: 400

## Examples
<a name="API_UpdateShardCount_Examples"></a>

### To update the shard count of the specified stream from 2 to 4
<a name="API_UpdateShardCount_Example_1"></a>

This example illustrates one usage of UpdateShardCount.

#### Sample Request
<a name="API_UpdateShardCount_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: kinesis.<region>.<domain>
Content-Length: <PayloadSizeBytes>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Authorization: <AuthParams>
Connection: Keep-Alive
X-Amz-Date: <Date>
X-Amz-Target: Kinesis_20131202.UpdateShardCount
{
  "StreamName": "exampleStreamName",
  "TargetShardCount": 4,
  "ScalingType": "UNIFORM_SCALING"
}
```

#### Sample Response
<a name="API_UpdateShardCount_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
  "TargetShardCount": 4,
  "StreamName": "exampleStreamName",
  "CurrentShardCount": 2
}
```

## See Also
<a name="API_UpdateShardCount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesis-2013-12-02/UpdateShardCount)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesis-2013-12-02/UpdateShardCount)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/UpdateShardCount)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesis-2013-12-02/UpdateShardCount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/UpdateShardCount)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesis-2013-12-02/UpdateShardCount)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesis-2013-12-02/UpdateShardCount)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesis-2013-12-02/UpdateShardCount)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/UpdateShardCount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/UpdateShardCount)

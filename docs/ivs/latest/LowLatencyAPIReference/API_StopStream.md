---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_StopStream.html
---

# StopStream
<a name="API_StopStream"></a>

Disconnects the incoming RTMPS stream for the specified channel. Can be used in conjunction with [DeleteStreamKey](API_DeleteStreamKey.md) to prevent further streaming to a channel.

**Note**
Many streaming client-software libraries automatically reconnect a dropped RTMPS session, so to stop the stream permanently, you may want to first revoke the `streamKey` attached to the channel.

## Request Syntax
<a name="API_StopStream_RequestSyntax"></a>

```
POST /StopStream HTTP/1.1
Content-type: application/json

{
   "channelArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StopStream_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StopStream_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [channelArn](#API_StopStream_RequestSyntax) **   <a name="ivs-StopStream-request-channelArn"></a>
ARN of the channel for which the stream is to be stopped.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:channel/[a-zA-Z0-9-]+`
Required: Yes

## Response Syntax
<a name="API_StopStream_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_StopStream_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_StopStream_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ChannelNotBroadcasting **
The stream is offline for the given channel ARN.
HTTP Status Code: 404

 ** ResourceNotFoundException **
Request references a resource which does not exist.
HTTP Status Code: 404

 ** StreamUnavailable **
The stream is temporarily unavailable.
HTTP Status Code: 503

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_StopStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivs-2020-07-14/StopStream)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivs-2020-07-14/StopStream)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-2020-07-14/StopStream)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivs-2020-07-14/StopStream)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-2020-07-14/StopStream)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivs-2020-07-14/StopStream)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivs-2020-07-14/StopStream)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivs-2020-07-14/StopStream)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ivs-2020-07-14/StopStream)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-2020-07-14/StopStream)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

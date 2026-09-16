---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_InsertAdBreak.html
---

# InsertAdBreak
<a name="API_InsertAdBreak"></a>

Inserts an ad marker in the playlist for the specified channel and duration using the ad configuration associated with the channel.

 **Note:** AWS Elemental MediaTailor (EMT), the service that handles ad requests, provides CloudWatch metrics to help you monitor the success or failure of each InsertAdBreak operation. See [Monitoring AWS Elemental MediaTailor with Amazon CloudWatch](https://docs.aws.amazon.com/mediatailor/latest/ug/monitoring-cloudwatch-metrics.html) metrics in the *AWS Elemental MediaTailor User Guide* for details on available metrics.

## Request Syntax
<a name="API_InsertAdBreak_RequestSyntax"></a>

```
POST /InsertAdBreak HTTP/1.1
Content-type: application/json

{
   "channelArn": "{{string}}",
   "durationSeconds": {{number}}
}
```

## URI Request Parameters
<a name="API_InsertAdBreak_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_InsertAdBreak_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [channelArn](#API_InsertAdBreak_RequestSyntax) **   <a name="ivs-InsertAdBreak-request-channelArn"></a>
ARN of the channel into which the ad break is inserted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:channel/[a-zA-Z0-9-]+`
Required: Yes

 ** [durationSeconds](#API_InsertAdBreak_RequestSyntax) **   <a name="ivs-InsertAdBreak-request-durationSeconds"></a>
Duration of the ad break, in seconds.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 300.
Required: Yes

## Response Syntax
<a name="API_InsertAdBreak_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "adBreakId": "string"
}
```

## Response Elements
<a name="API_InsertAdBreak_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [adBreakId](#API_InsertAdBreak_ResponseSyntax) **   <a name="ivs-InsertAdBreak-response-adBreakId"></a>
Unique identifier for the ad break that was inserted into the playlist.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[a-zA-Z0-9]+`

## Errors
<a name="API_InsertAdBreak_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ChannelNotBroadcasting **
The stream is offline for the given channel ARN.
HTTP Status Code: 404

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
HTTP Status Code: 409

 ** InternalServerException **
Unexpected error during processing of request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Request references a resource which does not exist.
HTTP Status Code: 404

 ** ThrottlingException **
Request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_InsertAdBreak_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivs-2020-07-14/InsertAdBreak)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivs-2020-07-14/InsertAdBreak)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-2020-07-14/InsertAdBreak)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivs-2020-07-14/InsertAdBreak)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-2020-07-14/InsertAdBreak)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivs-2020-07-14/InsertAdBreak)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivs-2020-07-14/InsertAdBreak)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivs-2020-07-14/InsertAdBreak)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ivs-2020-07-14/InsertAdBreak)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-2020-07-14/InsertAdBreak)

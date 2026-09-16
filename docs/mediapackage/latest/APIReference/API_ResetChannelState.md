---
source_url: https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_ResetChannelState.html
---

# ResetChannelState
<a name="API_ResetChannelState"></a>

Resetting the channel can help to clear errors from misconfigurations in the encoder. A reset refreshes the ingest stream and removes previous content.

 Be sure to stop the encoder before you reset the channel, and wait at least 30 seconds before you restart the encoder.

## Request Syntax
<a name="API_ResetChannelState_RequestSyntax"></a>

```
POST /channelGroup/{{ChannelGroupName}}/channel/{{ChannelName}}/reset HTTP/1.1
```

## URI Request Parameters
<a name="API_ResetChannelState_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ChannelGroupName](#API_ResetChannelState_RequestSyntax) **   <a name="mediapackage-ResetChannelState-request-uri-ChannelGroupName"></a>
The name of the channel group that contains the channel that you are resetting.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [ChannelName](#API_ResetChannelState_RequestSyntax) **   <a name="mediapackage-ResetChannelState-request-uri-ChannelName"></a>
The name of the channel that you are resetting.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

## Request Body
<a name="API_ResetChannelState_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ResetChannelState_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "ChannelGroupName": "string",
   "ChannelName": "string",
   "ResetAt": number
}
```

## Response Elements
<a name="API_ResetChannelState_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_ResetChannelState_ResponseSyntax) **   <a name="mediapackage-ResetChannelState-response-Arn"></a>
The Amazon Resource Name (ARN) associated with the channel that you just reset.
Type: String

 ** [ChannelGroupName](#API_ResetChannelState_ResponseSyntax) **   <a name="mediapackage-ResetChannelState-response-ChannelGroupName"></a>
The name of the channel group that contains the channel that you just reset.
Type: String

 ** [ChannelName](#API_ResetChannelState_ResponseSyntax) **   <a name="mediapackage-ResetChannelState-response-ChannelName"></a>
The name of the channel that you just reset.
Type: String

 ** [ResetAt](#API_ResetChannelState_ResponseSyntax) **   <a name="mediapackage-ResetChannelState-response-ResetAt"></a>
The time that the channel was last reset.
Type: Timestamp

## Errors
<a name="API_ResetChannelState_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied because either you don't have permissions to perform the requested operation or MediaPackage is getting throttling errors with CDN authorization. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see Access Management in the IAM User Guide. Or, if you're using CDN authorization, you will receive this exception if MediaPackage receives a throttling error from Secrets Manager.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting this resource can cause an inconsistent state.
 ** ConflictExceptionType **
The type of ConflictException.
HTTP Status Code: 409

 ** InternalServerException **
Indicates that an error from the service occurred while trying to process a request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource doesn't exist.
 ** ResourceTypeNotFound **
The specified resource type wasn't found.
HTTP Status Code: 404

 ** ThrottlingException **
The request throughput limit was exceeded.
HTTP Status Code: 429

 ** ValidationException **
The input failed to meet the constraints specified by the AWS service.
 ** ValidationExceptionType **
The type of ValidationException.
HTTP Status Code: 400

## See Also
<a name="API_ResetChannelState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediapackagev2-2022-12-25/ResetChannelState)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediapackagev2-2022-12-25/ResetChannelState)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediapackagev2-2022-12-25/ResetChannelState)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediapackagev2-2022-12-25/ResetChannelState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediapackagev2-2022-12-25/ResetChannelState)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediapackagev2-2022-12-25/ResetChannelState)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediapackagev2-2022-12-25/ResetChannelState)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediapackagev2-2022-12-25/ResetChannelState)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mediapackagev2-2022-12-25/ResetChannelState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediapackagev2-2022-12-25/ResetChannelState)

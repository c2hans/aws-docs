---
source_url: https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_ResetOriginEndpointState.html
---

# ResetOriginEndpointState
<a name="API_ResetOriginEndpointState"></a>

Resetting the origin endpoint can help to resolve unexpected behavior and other content packaging issues. It also helps to preserve special events when you don't want the previous content to be available for viewing. A reset clears out all previous content from the origin endpoint.

MediaPackage might return old content from this endpoint in the first 30 seconds after the endpoint reset. For best results, when possible, wait 30 seconds from endpoint reset to send playback requests to this endpoint.

## Request Syntax
<a name="API_ResetOriginEndpointState_RequestSyntax"></a>

```
POST /channelGroup/{{ChannelGroupName}}/channel/{{ChannelName}}/originEndpoint/{{OriginEndpointName}}/reset HTTP/1.1
```

## URI Request Parameters
<a name="API_ResetOriginEndpointState_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ChannelGroupName](#API_ResetOriginEndpointState_RequestSyntax) **   <a name="mediapackage-ResetOriginEndpointState-request-uri-ChannelGroupName"></a>
The name of the channel group that contains the channel with the origin endpoint that you are resetting.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [ChannelName](#API_ResetOriginEndpointState_RequestSyntax) **   <a name="mediapackage-ResetOriginEndpointState-request-uri-ChannelName"></a>
The name of the channel with the origin endpoint that you are resetting.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [OriginEndpointName](#API_ResetOriginEndpointState_RequestSyntax) **   <a name="mediapackage-ResetOriginEndpointState-request-uri-OriginEndpointName"></a>
The name of the origin endpoint that you are resetting.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

## Request Body
<a name="API_ResetOriginEndpointState_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ResetOriginEndpointState_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "ChannelGroupName": "string",
   "ChannelName": "string",
   "OriginEndpointName": "string",
   "ResetAt": number
}
```

## Response Elements
<a name="API_ResetOriginEndpointState_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_ResetOriginEndpointState_ResponseSyntax) **   <a name="mediapackage-ResetOriginEndpointState-response-Arn"></a>
The Amazon Resource Name (ARN) associated with the endpoint that you just reset.
Type: String

 ** [ChannelGroupName](#API_ResetOriginEndpointState_ResponseSyntax) **   <a name="mediapackage-ResetOriginEndpointState-response-ChannelGroupName"></a>
The name of the channel group that contains the channel with the origin endpoint that you just reset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`

 ** [ChannelName](#API_ResetOriginEndpointState_ResponseSyntax) **   <a name="mediapackage-ResetOriginEndpointState-response-ChannelName"></a>
The name of the channel with the origin endpoint that you just reset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`

 ** [OriginEndpointName](#API_ResetOriginEndpointState_ResponseSyntax) **   <a name="mediapackage-ResetOriginEndpointState-response-OriginEndpointName"></a>
The name of the origin endpoint that you just reset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`

 ** [ResetAt](#API_ResetOriginEndpointState_ResponseSyntax) **   <a name="mediapackage-ResetOriginEndpointState-response-ResetAt"></a>
The time that the origin endpoint was last reset.
Type: Timestamp

## Errors
<a name="API_ResetOriginEndpointState_Errors"></a>

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
<a name="API_ResetOriginEndpointState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediapackagev2-2022-12-25/ResetOriginEndpointState)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediapackagev2-2022-12-25/ResetOriginEndpointState)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediapackagev2-2022-12-25/ResetOriginEndpointState)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediapackagev2-2022-12-25/ResetOriginEndpointState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediapackagev2-2022-12-25/ResetOriginEndpointState)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediapackagev2-2022-12-25/ResetOriginEndpointState)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediapackagev2-2022-12-25/ResetOriginEndpointState)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediapackagev2-2022-12-25/ResetOriginEndpointState)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mediapackagev2-2022-12-25/ResetOriginEndpointState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediapackagev2-2022-12-25/ResetOriginEndpointState)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V2 Live API. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_UpdateChannel.html
---

# UpdateChannel
<a name="API_UpdateChannel"></a>

Update the specified channel. You can edit if MediaPackage sends ingest or egress access logs to the CloudWatch log group, if content will be encrypted, the description on a channel, and your channel's policy settings. You can't edit the name of the channel or CloudFront distribution details.

Any edits you make that impact the video output may not be reflected for a few minutes.

## Request Syntax
<a name="API_UpdateChannel_RequestSyntax"></a>

```
PUT /channelGroup/{{ChannelGroupName}}/channel/{{ChannelName}}/ HTTP/1.1
x-amzn-update-if-match: {{ETag}}
Content-type: application/json

{
   "Description": "{{string}}",
   "InputSwitchConfiguration": {
      "MQCSInputSwitching": {{boolean}},
      "PreferredInput": {{number}}
   },
   "OutputHeaderConfiguration": {
      "PublishMQCS": {{boolean}}
   }
}
```

## URI Request Parameters
<a name="API_UpdateChannel_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ChannelGroupName](#API_UpdateChannel_RequestSyntax) **   <a name="mediapackage-UpdateChannel-request-uri-ChannelGroupName"></a>
The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [ChannelName](#API_UpdateChannel_RequestSyntax) **   <a name="mediapackage-UpdateChannel-request-uri-ChannelName"></a>
The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [ETag](#API_UpdateChannel_RequestSyntax) **   <a name="mediapackage-UpdateChannel-request-ETag"></a>
The expected current Entity Tag (ETag) for the resource. If the specified ETag does not match the resource's current entity tag, the update request will be rejected.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\S]+`

## Request Body
<a name="API_UpdateChannel_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_UpdateChannel_RequestSyntax) **   <a name="mediapackage-UpdateChannel-request-Description"></a>
Any descriptive information that you want to add to the channel for future identification purposes.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [InputSwitchConfiguration](#API_UpdateChannel_RequestSyntax) **   <a name="mediapackage-UpdateChannel-request-InputSwitchConfiguration"></a>
The configuration for input switching based on the media quality confidence score (MQCS) as provided from AWS Elemental MediaLive. This setting is valid only when `InputType` is `CMAF`.
Type: [InputSwitchConfiguration](API_InputSwitchConfiguration.md) object
Required: No

 ** [OutputHeaderConfiguration](#API_UpdateChannel_RequestSyntax) **   <a name="mediapackage-UpdateChannel-request-OutputHeaderConfiguration"></a>
The settings for what common media server data (CMSD) headers AWS Elemental MediaPackage includes in responses to the CDN. This setting is valid only when `InputType` is `CMAF`.
Type: [OutputHeaderConfiguration](API_OutputHeaderConfiguration.md) object
Required: No

## Response Syntax
<a name="API_UpdateChannel_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "ChannelGroupName": "string",
   "ChannelName": "string",
   "CreatedAt": number,
   "Description": "string",
   "ETag": "string",
   "IngestEndpoints": [
      {
         "Id": "string",
         "Url": "string"
      }
   ],
   "InputSwitchConfiguration": {
      "MQCSInputSwitching": boolean,
      "PreferredInput": number
   },
   "InputType": "string",
   "ModifiedAt": number,
   "OutputHeaderConfiguration": {
      "PublishMQCS": boolean
   },
   "OutputLockingMode": "string",
   "tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_UpdateChannel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_UpdateChannel_ResponseSyntax) **   <a name="mediapackage-UpdateChannel-response-Arn"></a>
The Amazon Resource Name (ARN) associated with the resource.
Type: String

 ** [ChannelGroupName](#API_UpdateChannel_ResponseSyntax) **   <a name="mediapackage-UpdateChannel-response-ChannelGroupName"></a>
The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.
Type: String

 ** [ChannelName](#API_UpdateChannel_ResponseSyntax) **   <a name="mediapackage-UpdateChannel-response-ChannelName"></a>
The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group.
Type: String

 ** [CreatedAt](#API_UpdateChannel_ResponseSyntax) **   <a name="mediapackage-UpdateChannel-response-CreatedAt"></a>
The date and time the channel was created.
Type: Timestamp

 ** [Description](#API_UpdateChannel_ResponseSyntax) **   <a name="mediapackage-UpdateChannel-response-Description"></a>
The description for your channel.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [ETag](#API_UpdateChannel_ResponseSyntax) **   <a name="mediapackage-UpdateChannel-response-ETag"></a>
The current Entity Tag (ETag) associated with this resource. The entity tag can be used to safely make concurrent updates to the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\S]+`

 ** [IngestEndpoints](#API_UpdateChannel_ResponseSyntax) **   <a name="mediapackage-UpdateChannel-response-IngestEndpoints"></a>
The list of ingest endpoints.
Type: Array of [IngestEndpoint](API_IngestEndpoint.md) objects

 ** [InputSwitchConfiguration](#API_UpdateChannel_ResponseSyntax) **   <a name="mediapackage-UpdateChannel-response-InputSwitchConfiguration"></a>
The configuration for input switching based on the media quality confidence score (MQCS) as provided from AWS Elemental MediaLive. This setting is valid only when `InputType` is `CMAF`.
Type: [InputSwitchConfiguration](API_InputSwitchConfiguration.md) object

 ** [InputType](#API_UpdateChannel_ResponseSyntax) **   <a name="mediapackage-UpdateChannel-response-InputType"></a>
The input type will be an immutable field which will be used to define whether the channel will allow CMAF ingest or HLS ingest. If unprovided, it will default to HLS to preserve current behavior.
The allowed values are:
+  `HLS` - The HLS streaming specification (which defines M3U8 manifests and TS segments).
+  `CMAF` - The DASH-IF CMAF Ingest specification (which defines CMAF segments with optional DASH manifests).
Type: String
Valid Values: `HLS | CMAF`

 ** [ModifiedAt](#API_UpdateChannel_ResponseSyntax) **   <a name="mediapackage-UpdateChannel-response-ModifiedAt"></a>
The date and time the channel was modified.
Type: Timestamp

 ** [OutputHeaderConfiguration](#API_UpdateChannel_ResponseSyntax) **   <a name="mediapackage-UpdateChannel-response-OutputHeaderConfiguration"></a>
The settings for what common media server data (CMSD) headers AWS Elemental MediaPackage includes in responses to the CDN. This setting is valid only when `InputType` is `CMAF`.
Type: [OutputHeaderConfiguration](API_OutputHeaderConfiguration.md) object

 ** [OutputLockingMode](#API_UpdateChannel_ResponseSyntax) **   <a name="mediapackage-UpdateChannel-response-OutputLockingMode"></a>
The output locking mode configured for the channel. This value is immutable after channel creation.
The allowed values are:
+  `EPOCH_LOCKED` - The channel uses epoch-locked behavior with deterministic sequence numbering and fixed segment boundaries aligned to epoch time.
+  `NON_EPOCH_LOCKED` - The channel uses non-epoch-locked behavior with duration-based segment combining and monotonically increasing sequence numbers starting from 0.
Type: String
Valid Values: `EPOCH_LOCKED | NON_EPOCH_LOCKED`

 ** [tags](#API_UpdateChannel_ResponseSyntax) **   <a name="mediapackage-UpdateChannel-response-tags"></a>
The comma-separated list of tag key:value pairs assigned to the channel.
Type: String to string map

## Errors
<a name="API_UpdateChannel_Errors"></a>

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
<a name="API_UpdateChannel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediapackagev2-2022-12-25/UpdateChannel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediapackagev2-2022-12-25/UpdateChannel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediapackagev2-2022-12-25/UpdateChannel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediapackagev2-2022-12-25/UpdateChannel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediapackagev2-2022-12-25/UpdateChannel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediapackagev2-2022-12-25/UpdateChannel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediapackagev2-2022-12-25/UpdateChannel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediapackagev2-2022-12-25/UpdateChannel)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mediapackagev2-2022-12-25/UpdateChannel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediapackagev2-2022-12-25/UpdateChannel)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V2 Live API. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

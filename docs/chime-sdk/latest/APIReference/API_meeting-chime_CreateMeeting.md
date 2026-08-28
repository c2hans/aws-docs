---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_CreateMeeting.html
---

# CreateMeeting
<a name="API_meeting-chime_CreateMeeting"></a>

Creates a new Amazon Chime SDK meeting in the specified media Region with no initial attendees. For more information about specifying media Regions, see [Available Regions](https://docs.aws.amazon.com/chime-sdk/latest/dg/sdk-available-regions) and [Using meeting Regions](https://docs.aws.amazon.com/chime-sdk/latest/dg/chime-sdk-meetings-regions.html), both in the *Amazon Chime SDK Developer Guide*. For more information about the Amazon Chime SDK, see [Using the Amazon Chime SDK](https://docs.aws.amazon.com/chime-sdk/latest/dg/meetings-sdk.html) in the *Amazon Chime SDK Developer Guide*.

**Note**
If you use this API in conjuction with the [AudioFeatures](API_meeting-chime_AudioFeatures.md) and [VideoFeatures](API_meeting-chime_VideoFeatures.md) APIs, and you don't specify the `MeetingFeatures.Content.MaxResolution` or `MeetingFeatures.Video.MaxResolution` parameters, the following defaults are used:
Content.MaxResolution: FHD
Video.MaxResolution: HD

## Request Syntax
<a name="API_meeting-chime_CreateMeeting_RequestSyntax"></a>

```
POST /meetings HTTP/1.1
Content-type: application/json

{
   "ClientRequestToken": "{{string}}",
   "ExternalMeetingId": "{{string}}",
   "MediaPlacementNetworkType": "{{string}}",
   "MediaRegion": "{{string}}",
   "MeetingFeatures": {
      "Attendee": {
         "MaxCount": {{number}}
      },
      "Audio": {
         "EchoReduction": "{{string}}"
      },
      "Content": {
         "MaxResolution": "{{string}}"
      },
      "Video": {
         "MaxResolution": "{{string}}"
      }
   },
   "MeetingHostId": "{{string}}",
   "NotificationsConfiguration": {
      "LambdaFunctionArn": "{{string}}",
      "SnsTopicArn": "{{string}}",
      "SqsQueueArn": "{{string}}"
   },
   "PrimaryMeetingId": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "TenantIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_meeting-chime_CreateMeeting_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_meeting-chime_CreateMeeting_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_meeting-chime_CreateMeeting_RequestSyntax) **   <a name="chimesdk-meeting-chime_CreateMeeting-request-ClientRequestToken"></a>
The unique identifier for the client request. Use a different token for different meetings.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 64.
Pattern: `[-_a-zA-Z0-9]*`
Required: Yes

 ** [ExternalMeetingId](#API_meeting-chime_CreateMeeting_RequestSyntax) **   <a name="chimesdk-meeting-chime_CreateMeeting-request-ExternalMeetingId"></a>
The external meeting ID.
Pattern: `[-_&@+=,(){}\[\]\/«».:|'"#a-zA-Z0-9À-ÿ\s]*`
Values that begin with `aws:` are reserved. You can't configure a value that uses this prefix. Case insensitive.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 64.
Required: Yes

 ** [MediaPlacementNetworkType](#API_meeting-chime_CreateMeeting_RequestSyntax) **   <a name="chimesdk-meeting-chime_CreateMeeting-request-MediaPlacementNetworkType"></a>
The type of network for the media placement. Either IPv4 only or dual-stack (IPv4 and IPv6).
Type: String
Valid Values: `Ipv4Only | DualStack`
Required: No

 ** [MediaRegion](#API_meeting-chime_CreateMeeting_RequestSyntax) **   <a name="chimesdk-meeting-chime_CreateMeeting-request-MediaRegion"></a>
The Region in which to create the meeting.
 Available values: `af-south-1`, `ap-northeast-1`, `ap-northeast-2`, `ap-south-1`, `ap-southeast-1`, `ap-southeast-2`, `ca-central-1`, `eu-central-1`, `eu-north-1`, `eu-south-1`, `eu-west-1`, `eu-west-2`, `eu-west-3`, `sa-east-1`, `us-east-1`, `us-east-2`, `us-west-1`, `us-west-2`.
Available values in AWS GovCloud (US) Regions: `us-gov-east-1`, `us-gov-west-1`.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 64.
Required: Yes

 ** [MeetingFeatures](#API_meeting-chime_CreateMeeting_RequestSyntax) **   <a name="chimesdk-meeting-chime_CreateMeeting-request-MeetingFeatures"></a>
Lists the audio and video features enabled for a meeting, such as echo reduction.
Type: [MeetingFeaturesConfiguration](API_meeting-chime_MeetingFeaturesConfiguration.md) object
Required: No

 ** [MeetingHostId](#API_meeting-chime_CreateMeeting_RequestSyntax) **   <a name="chimesdk-meeting-chime_CreateMeeting-request-MeetingHostId"></a>
Reserved.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 64.
Required: No

 ** [NotificationsConfiguration](#API_meeting-chime_CreateMeeting_RequestSyntax) **   <a name="chimesdk-meeting-chime_CreateMeeting-request-NotificationsConfiguration"></a>
The configuration for resource targets to receive notifications when meeting and attendee events occur.
Type: [NotificationsConfiguration](API_meeting-chime_NotificationsConfiguration.md) object
Required: No

 ** [PrimaryMeetingId](#API_meeting-chime_CreateMeeting_RequestSyntax) **   <a name="chimesdk-meeting-chime_CreateMeeting-request-PrimaryMeetingId"></a>
When specified, replicates the media from the primary meeting to the new meeting.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 64.
Required: No

 ** [Tags](#API_meeting-chime_CreateMeeting_RequestSyntax) **   <a name="chimesdk-meeting-chime_CreateMeeting-request-Tags"></a>
Applies one or more tags to an Amazon Chime SDK meeting. Note the following:
+ Not all resources have tags. For a list of services with resources that support tagging using this operation, see [Services that support the Resource Groups Tagging API](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/supported-services.html). If the resource doesn't yet support this operation, the resource's service might support tagging using its own API operations. For more information, refer to the documentation for that service.
+ Each resource can have up to 50 tags. For other limits, see [Tag Naming and Usage Conventions](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-conventions) in the *AWS General Reference*.
+ You can only tag resources that are located in the specified AWS Region for the AWS account.
+ To add tags to a resource, you need the necessary permissions for the service that the resource belongs to as well as permissions for adding tags. For more information, see the documentation for each service.
Do not store personally identifiable information (PII) or other confidential or sensitive information in tags. We use tags to provide you with billing and administration services. Tags are not intended to be used for private or sensitive data.
 **Minimum permissions**
In addition to the `tag:TagResources` permission required by this operation, you must also have the tagging permission defined by the service that created the resource. For example, to tag a `ChimeSDKMeetings` instance using the `TagResources` operation, you must have both of the following permissions:
 `tag:TagResources`
 `ChimeSDKMeetings:CreateTags`
Some services might have specific requirements for tagging some resources. For example, to tag an Amazon S3 bucket, you must also have the `s3:GetBucketTagging` permission. If the expected minimum permissions don't work, check the documentation for that service's tagging APIs for more information.
Type: Array of [Tag](API_meeting-chime_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [TenantIds](#API_meeting-chime_CreateMeeting_RequestSyntax) **   <a name="chimesdk-meeting-chime_CreateMeeting-request-TenantIds"></a>
A consistent and opaque identifier, created and maintained by the builder to represent a segment of their users.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 2. Maximum length of 256.
Pattern: `^(?!.*?(.)\1{3})[-_!@#$a-zA-Z0-9]*$`
Required: No

## Response Syntax
<a name="API_meeting-chime_CreateMeeting_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Meeting": {
      "ExternalMeetingId": "string",
      "MediaPlacement": {
         "AudioFallbackUrl": "string",
         "AudioHostUrl": "string",
         "EventIngestionUrl": "string",
         "ScreenDataUrl": "string",
         "ScreenSharingUrl": "string",
         "ScreenViewingUrl": "string",
         "SignalingUrl": "string",
         "TurnControlUrl": "string"
      },
      "MediaRegion": "string",
      "MeetingArn": "string",
      "MeetingFeatures": {
         "Attendee": {
            "MaxCount": number
         },
         "Audio": {
            "EchoReduction": "string"
         },
         "Content": {
            "MaxResolution": "string"
         },
         "Video": {
            "MaxResolution": "string"
         }
      },
      "MeetingHostId": "string",
      "MeetingId": "string",
      "PrimaryMeetingId": "string",
      "TenantIds": [ "string" ]
   }
}
```

## Response Elements
<a name="API_meeting-chime_CreateMeeting_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Meeting](#API_meeting-chime_CreateMeeting_ResponseSyntax) **   <a name="chimesdk-meeting-chime_CreateMeeting-response-Meeting"></a>
The meeting information, including the meeting ID and `MediaPlacement`.
Type: [Meeting](API_meeting-chime_Meeting.md) object

## Errors
<a name="API_meeting-chime_CreateMeeting_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** BadRequestException **
The input parameters don't match the service's restrictions.
 ** RequestId **
The request id associated with the call responsible for the exception.
HTTP Status Code: 400

 ** ConflictException **
Multiple instances of the same request have been made simultaneously.
 ** RequestId **
The ID of the request involved in the conflict.
HTTP Status Code: 409

 ** ForbiddenException **
The client is permanently forbidden from making the request.
 ** RequestId **
The request id associated with the call responsible for the exception.
HTTP Status Code: 403

 ** LimitExceededException **
The request exceeds the resource limit.
 ** RequestId **
The request id associated with the call responsible for the exception.
HTTP Status Code: 400

 ** ServiceFailureException **
The service encountered an unexpected error.
 ** RequestId **
The ID of the failed request.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is currently unavailable.
 ** RequestId **
The request id associated with the call responsible for the exception.
 ** RetryAfterSeconds **
The number of seconds the caller should wait before retrying.
HTTP Status Code: 503

 ** ThrottlingException **
The number of customer requests exceeds the request rate limit.
 ** RequestId **
The ID of the request that exceeded the throttling limit.
HTTP Status Code: 429

 ** UnauthorizedException **
The user isn't authorized to request a resource.
 ** RequestId **
The request id associated with the call responsible for the exception.
HTTP Status Code: 401

## See Also
<a name="API_meeting-chime_CreateMeeting_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-meetings-2021-07-15/CreateMeeting)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-meetings-2021-07-15/CreateMeeting)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-meetings-2021-07-15/CreateMeeting)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-meetings-2021-07-15/CreateMeeting)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-meetings-2021-07-15/CreateMeeting)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-meetings-2021-07-15/CreateMeeting)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-meetings-2021-07-15/CreateMeeting)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-meetings-2021-07-15/CreateMeeting)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-sdk-meetings-2021-07-15/CreateMeeting)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-meetings-2021-07-15/CreateMeeting)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

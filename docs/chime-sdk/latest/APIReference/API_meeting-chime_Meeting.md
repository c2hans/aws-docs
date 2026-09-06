---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_Meeting.html
---

# Meeting
<a name="API_meeting-chime_Meeting"></a>

A meeting created using the Amazon Chime SDK.

## Contents
<a name="API_meeting-chime_Meeting_Contents"></a>

 ** ExternalMeetingId **   <a name="chimesdk-Type-meeting-chime_Meeting-ExternalMeetingId"></a>
The external meeting ID.
Pattern: `[-_&@+=,(){}\[\]\/«».:|'"#a-zA-Z0-9À-ÿ\s]*`
Values that begin with `aws:` are reserved. You can't configure a value that uses this prefix. Case insensitive.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 64.
Required: No

 ** MediaPlacement **   <a name="chimesdk-Type-meeting-chime_Meeting-MediaPlacement"></a>
The media placement for the meeting.
Type: [MediaPlacement](API_meeting-chime_MediaPlacement.md) object
Required: No

 ** MediaRegion **   <a name="chimesdk-Type-meeting-chime_Meeting-MediaRegion"></a>
The Region in which you create the meeting. Available values: `af-south-1`, `ap-northeast-1`, `ap-northeast-2`, `ap-south-1`, `ap-southeast-1`, `ap-southeast-2`, `ca-central-1`, `eu-central-1`, `eu-north-1`, `eu-south-1`, `eu-west-1`, `eu-west-2`, `eu-west-3`, `sa-east-1`, `us-east-1`, `us-east-2`, `us-west-1`, `us-west-2`.
Available values in AWS GovCloud (US) Regions: `us-gov-east-1`, `us-gov-west-1`.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 64.
Required: No

 ** MeetingArn **   <a name="chimesdk-Type-meeting-chime_Meeting-MeetingArn"></a>
The ARN of the meeting.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `^arn:.*`
Required: No

 ** MeetingFeatures **   <a name="chimesdk-Type-meeting-chime_Meeting-MeetingFeatures"></a>
The features available to a meeting, such as echo reduction.
Type: [MeetingFeaturesConfiguration](API_meeting-chime_MeetingFeaturesConfiguration.md) object
Required: No

 ** MeetingHostId **   <a name="chimesdk-Type-meeting-chime_Meeting-MeetingHostId"></a>
Reserved.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 64.
Required: No

 ** MeetingId **   <a name="chimesdk-Type-meeting-chime_Meeting-MeetingId"></a>
The Amazon Chime SDK meeting ID.
Type: String
Pattern: `[a-fA-F0-9]{8}(?:-[a-fA-F0-9]{4}){3}-[a-fA-F0-9]{12}`
Required: No

 ** PrimaryMeetingId **   <a name="chimesdk-Type-meeting-chime_Meeting-PrimaryMeetingId"></a>
When specified, replicates the media from the primary meeting to this meeting.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 64.
Required: No

 ** TenantIds **   <a name="chimesdk-Type-meeting-chime_Meeting-TenantIds"></a>
Array of strings.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 2. Maximum length of 256.
Pattern: `^(?!.*?(.)\1{3})[-_!@#$a-zA-Z0-9]*$`
Required: No

## See Also
<a name="API_meeting-chime_Meeting_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-meetings-2021-07-15/Meeting)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-meetings-2021-07-15/Meeting)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-meetings-2021-07-15/Meeting)

---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_KinesisVideoStreamConfiguration.html
---

# KinesisVideoStreamConfiguration
<a name="API_media-pipelines-chime_KinesisVideoStreamConfiguration"></a>

The configuration of an Kinesis video stream.

**Note**
If a meeting uses an opt-in Region as its [MediaRegion](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_CreateMeeting.html#chimesdk-meeting-chime_CreateMeeting-request-MediaRegion), the KVS stream must be in that same Region. For example, if a meeting uses the `af-south-1` Region, the KVS stream must also be in `af-south-1`. However, if the meeting uses a Region that AWS turns on by default, the KVS stream can be in any available Region, including an opt-in Region. For example, if the meeting uses `ca-central-1`, the KVS stream can be in `eu-west-2`, `us-east-1`, `af-south-1`, or any other Region that the Amazon Chime SDK supports.
To learn which AWS Region a meeting uses, call the [GetMeeting](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_GetMeeting.html) API and use the [MediaRegion](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_CreateMeeting.html#chimesdk-meeting-chime_CreateMeeting-request-MediaRegion) parameter from the response.
For more information about opt-in Regions, refer to [Available Regions](https://docs.aws.amazon.com/chime-sdk/latest/dg/sdk-available-regions.html) in the *Amazon Chime SDK Developer Guide*, and [Specify which AWS Regions your account can use](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html#rande-manage-enable.html), in the *AWS Account Management Reference Guide*.

## Contents
<a name="API_media-pipelines-chime_KinesisVideoStreamConfiguration_Contents"></a>

 ** Region **   <a name="chimesdk-Type-media-pipelines-chime_KinesisVideoStreamConfiguration-Region"></a>
The AWS Region of the video stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `^([a-z]+-){2,}\d+$`
Required: Yes

 ** DataRetentionInHours **   <a name="chimesdk-Type-media-pipelines-chime_KinesisVideoStreamConfiguration-DataRetentionInHours"></a>
The amount of time that data is retained.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_media-pipelines-chime_KinesisVideoStreamConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-media-pipelines-2021-07-15/KinesisVideoStreamConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-media-pipelines-2021-07-15/KinesisVideoStreamConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-media-pipelines-2021-07-15/KinesisVideoStreamConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/sdk-available-regions.html
---

# Available AWS Regions for the Amazon Chime SDK
<a name="sdk-available-regions"></a>

The following tables list the features of the Amazon Chime SDK service and the AWS Regions that provide each service.

**Note**
Regions marked with an asterisk (**\***) must be enabled in your AWS account. AWS blocks those Regions by default. For more information about enabling Regions, see [Specify which AWS Regions your account can use](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html), in the *AWS Account Management Reference*.

**Topics**
+ [Console Regions](#sdk-console-regions)
+ [Call analytics Regions](#call-analytics-regions)
+ [Meeting Regions](#sdk-meeting-regions)
+ [Media pipeline Regions](#sdk-media-pipelines)
+ [Messaging Regions](#sdk-messaging-regions)
+ [Voice Regions](#voice-regions)

## Console Regions
<a name="sdk-console-regions"></a>

You use the Amazon Chime SDK console to configure resources and learn more about the Amazon Chime SDK service.

| **AWS Region** | **Console** |
| --- | --- |
| Asia Pacific (Seoul) | Yes |
| Asia Pacific (Singapore) | Yes |
| Asia Pacific (Sydney) | Yes |
| Asia Pacific (Tokyo) (ap-northeast-1) | Yes |
| Canada (Central) (ca-central-1) | Yes |
| Europe (Frankfurt) (eu-central-1) | Yes |
| Europe (Ireland) (eu-west-1) | Yes |
| Europe (London) (eu-west-2) | Yes |
| US East (N. Virginia) (us-east-1) | Yes |
| US West (Oregon) (us-west-2) | Yes |

## Call analytics Regions
<a name="call-analytics-regions"></a>

The following table lists the AWS Regions available for analytics, transcription, and call recording.

|  **AWS Region**  |  **Voice analytics**  | **Transcription** |  **Call recording**  |
| --- | --- | --- | --- |
| US East (N. Virginia) (us-east-1) |  Yes  |  Yes  |  Yes  |
| US West (Oregon) (us-west-2) |  Yes  |  Yes  | Yes |
| Europe (Frankfurt) (eu-central-1) | No |  Yes  |  Yes  |

## Meeting Regions
<a name="sdk-meeting-regions"></a>

Amazon Chime SDK meetings have *control Regions* and *media Regions*. A control Region provides the API endpoint used to create, update and delete meetings. Control Regions also receive and process [Understanding Amazon Chime SDK meeting lifecycle events](using-events.md).

Media Regions host the actual meetings, and clients connect to your media Regions. You specify the media Region when you call the [CreateMeeting](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_CreateMeeting.html) API.

A control Region can create a meeting in any media Region in the same AWS partition. However, you can only update a meeting in the control Region used to create the meeting.

For more information about selecting control and media Regions, see [Using meeting Regions for Amazon Chime SDK meetings](chime-sdk-meetings-regions.md).

The following table lists the Regions that provide control, media, or both.

| **AWS Region** | **Meeting control** | **Meeting media** |
| --- | --- | --- |
| Africa (Cape Town) (af-south-1)**\*** | Yes\*\* | Yes |
| Asia Pacific (Mumbai) (ap-south-1) | Yes | Yes |
| Asia Pacific (Seoul) (ap-northeast-2) | Yes | Yes |
| Asia Pacific (Singapore) (ap-southeast-1) | Yes | Yes |
| Asia Pacific (Sydney) (ap-southeast-2) | Yes | Yes |
| Asia Pacific (Tokyo) (ap-northeast-1) | Yes | Yes |
| Canada (Central) (ca-central-1) | Yes | Yes |
| Europe (Frankfurt) (eu-central-1) | Yes | Yes |
| Europe (Ireland) (eu-west-1) |  | Yes |
| Europe (London) (eu-west-2) | Yes | Yes |
| Europe (Milan) (eu-south-1)**\*** |  | Yes |
| Europe (Paris) (eu-west-3) |  | Yes |
| Europe (Stockholm) (eu-north-1) |  | Yes |
| Israel (Tel Aviv) (il-central-1)**\*** | Yes**\*\*** | Yes |
| South America (São Paulo) (sa-east-1) |  | Yes |
| US East (Ohio) (us-east-2) |  | Yes |
| US East (N. Virginia) (us-east-1) | Yes | Yes |
| US West (N. California) (us-west-1) |  | Yes |
| US West (Oregon) (us-west-2) | Yes | Yes |
| AWS GovCloud (US-East) (us-gov-east-1) | Yes | Yes |
| AWS GovCloud (US-West) (us-gov-west-1) | Yes | Yes |

**\***You must enable these Regions in your AWS account. For more information, refer to [Enable a Region](https://docs.aws.amazon.com/general/latest/gr/rande-manage.html#rande-manage-enable) in the *AWS General Reference*.

**\*\***Meetings that use meeting control in this Region can only host media in this Region.

**Note**
To create a meeting in an AWS GovCloud (US) Region, you must use a control Region in GovCloud. Also, control Regions in GovCloud can only make meetings in AWS GovCloud (US) Regions.

## Media pipeline Regions
<a name="sdk-media-pipelines"></a>

Amazon Chime SDK media pipelines have *control Regions* and *media Regions*. A control Region provides the media pipeline API endpoint used to create and delete media pipelines. You also use control Regions to receive and process [media pipeline events](media-pipe-events.md).

Media Regions run your media pipelines, and the system automatically selects the same media Region as the meeting.

You can use a control Region to create a media pipeline in any data Region. The media pipeline can join a meeting in any meeting media Region.

| **AWS Region** | **Control** | **Media** |
| --- | --- | --- |
| Africa (Cape Town) (af-south-1)**\*** |  | Yes |
| Asia Pacific (Mumbai) (ap-south-1) | Yes | Yes |
| Asia Pacific (Seoul) (ap-northeast-2) | Yes | Yes |
| Asia Pacific (Singapore) (ap-southeast-1) | Yes | Yes |
| Asia Pacific (Sydney) (ap-southeast-2) | Yes | Yes |
| Asia Pacific (Tokyo) (ap-northeast-1) | Yes |  Yes |
| Canada (Central) (ca-central-1) | Yes | Yes |
| Europe (Frankfurt) (eu-central-1) | Yes | Yes |
| Europe (Ireland) (eu-west-1) |  | Yes |
| Europe (London) (eu-west-2) | Yes | Yes |
| Europe (Milan) (eu-south-1)**\*** |  | Yes |
| Europe (Paris) (eu-west-3) |  | Yes |
| Europe (Stockholm) (eu-north-1) |  | Yes |
| South America (São Paulo) (sa-east-1) |  | Yes |
| US East (Ohio) (us-east-2) |  | Yes |
| US East (N. Virginia) (us-east-1) | Yes | Yes |
| US West (N. California) (us-west-1) |  | Yes |
| US West (Oregon) (us-west-2) | Yes | Yes |

**\***You must enable these Regions in your AWS account. For more information, refer to [Enable a Region](https://docs.aws.amazon.com/general/latest/gr/rande-manage.html#rande-manage-enable) in the *AWS General Reference*.

## Messaging Regions
<a name="sdk-messaging-regions"></a>

Amazon Chime SDK messaging has *control regions* and *data regions*. The control Region exposes the messaging API endpoint, and the data Region stores the messages. If you use Amazon Kinesis to stream messaging data, or AWS Lambda functions for channel flows, they should reside in the control Region.

| **AWS Region** | **Control** | **Data** |
| --- | --- | --- |
| Europe (Frankfurt) (eu-central-1) | Yes | Yes |
| US East (N. Virginia) (us-east-1) | Yes | Yes |

## Voice Regions
<a name="voice-regions"></a>

Amazon Chime SDK SIP (Session Initiation Protocol) features have *API regions* and *media regions*, and *PSTN regions*. The API regions provide the API endpoints for creating and configuring SIP features. The media Regions contain Amazon Chime SDK Voice Connectors and SIP media applications. The PSTN Regions enable customers to connect on-premises phone systems to the public telephone network. Additionally, PSTN Regions support phone number provisioning and management.

| **AWS Region** | **API** | **Media** | **PSTN** |
| --- | --- | --- | --- |
| Asia Pacific (Seoul) (ap-northeast-2)  | Yes | Yes |  |
| Asia Pacific (Singapore) (ap-southeast-1) | Yes | Yes |  |
| Asia Pacific (Sydney) (ap-southeast-2) | Yes | Yes |  |
| Asia Pacific (Tokyo) (ap-northeast-1) | Yes | Yes |  |
| Canada (Central) (ca-central-1) | Yes | Yes |  |
| Europe (Frankfurt) (eu-central-1) | Yes | Yes |  |
| Europe (Ireland) (eu-west-1) | Yes | Yes |  |
| Europe (London) (eu-west-2) | Yes | Yes |  |
| US East (N. Virginia) (us-east-1) | Yes | Yes | Yes**\*** |
| US West (Oregon) (us-west-2) | Yes | Yes | Yes**\*** |

**\***See the [Amazon Chime SDK Pricing](https://aws.amazon.com/chime/chime-sdk/pricing/) page for information about the availability of phone numbers in specific AWS regions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

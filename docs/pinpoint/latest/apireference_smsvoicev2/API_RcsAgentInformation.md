---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_RcsAgentInformation.html
---

# RcsAgentInformation
<a name="API_RcsAgentInformation"></a>

The information for an RCS agent in an AWS account.

## Contents
<a name="API_RcsAgentInformation_Contents"></a>

 ** CreatedTimestamp **   <a name="pinpoint-Type-RcsAgentInformation-CreatedTimestamp"></a>
The time when the RCS agent was created, in [UNIX epoch time](https://www.epochconverter.com/) format.
Type: Timestamp
Required: Yes

 ** DeletionProtectionEnabled **   <a name="pinpoint-Type-RcsAgentInformation-DeletionProtectionEnabled"></a>
When set to true the RCS agent can't be deleted.
Type: Boolean
Required: Yes

 ** RcsAgentArn **   <a name="pinpoint-Type-RcsAgentInformation-RcsAgentArn"></a>
The Amazon Resource Name (ARN) of the RCS agent.
Type: String
Required: Yes

 ** RcsAgentId **   <a name="pinpoint-Type-RcsAgentInformation-RcsAgentId"></a>
The unique identifier for the RCS agent.
Type: String
Required: Yes

 ** SelfManagedOptOutsEnabled **   <a name="pinpoint-Type-RcsAgentInformation-SelfManagedOptOutsEnabled"></a>
When set to true you're responsible for responding to HELP and STOP requests. You're also responsible for tracking and honoring opt-out requests.
Type: Boolean
Required: Yes

 ** Status **   <a name="pinpoint-Type-RcsAgentInformation-Status"></a>
The current status of the RCS agent.
Type: String
Valid Values: `CREATED | PENDING | TESTING | PARTIAL | ACTIVE | DELETED`
Required: Yes

 ** TwoWayEnabled **   <a name="pinpoint-Type-RcsAgentInformation-TwoWayEnabled"></a>
When set to true you can receive incoming text messages from your end recipients using the TwoWayChannelArn.
Type: Boolean
Required: Yes

 ** MessagingLimits **   <a name="pinpoint-Type-RcsAgentInformation-MessagingLimits"></a>
The messaging limits that apply to the RCS agent, including the per-capability send rates.
Type: [MessagingLimits](API_MessagingLimits.md) object
Required: No

 ** OptOutListName **   <a name="pinpoint-Type-RcsAgentInformation-OptOutListName"></a>
The name of the OptOutList associated with the RCS agent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_-]+`
Required: No

 ** PoolId **   <a name="pinpoint-Type-RcsAgentInformation-PoolId"></a>
The unique identifier of the pool associated with the RCS agent.
Type: String
Required: No

 ** TestingAgent **   <a name="pinpoint-Type-RcsAgentInformation-TestingAgent"></a>
The testing agent information associated with the RCS agent.
Type: [TestingAgentInformation](API_TestingAgentInformation.md) object
Required: No

 ** TwoWayChannelArn **   <a name="pinpoint-Type-RcsAgentInformation-TwoWayChannelArn"></a>
The Amazon Resource Name (ARN) of the two way channel.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `\S+`
Required: No

 ** TwoWayChannelRole **   <a name="pinpoint-Type-RcsAgentInformation-TwoWayChannelRole"></a>
An optional IAM Role Arn for a service to assume, to be able to post inbound SMS messages.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:\S+`
Required: No

 ** TwoWayMediaS3BucketName **   <a name="pinpoint-Type-RcsAgentInformation-TwoWayMediaS3BucketName"></a>
The name of the S3 bucket where inbound RCS media files are stored.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-z0-9][a-z0-9.-]*[a-z0-9]`
Required: No

 ** TwoWayMediaS3KeyPrefix **   <a name="pinpoint-Type-RcsAgentInformation-TwoWayMediaS3KeyPrefix"></a>
The key prefix used for inbound RCS media objects in the S3 bucket.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\S]+`
Required: No

 ** TwoWayMediaS3Role **   <a name="pinpoint-Type-RcsAgentInformation-TwoWayMediaS3Role"></a>
The ARN of the IAM role used to write inbound RCS media files to the S3 bucket.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:\S+`
Required: No

 ** TwoWayRcsEventsEnabled **   <a name="pinpoint-Type-RcsAgentInformation-TwoWayRcsEventsEnabled"></a>
The list of RCS event types enabled for two-way messaging on the agent.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: No

## See Also
<a name="API_RcsAgentInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/RcsAgentInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/RcsAgentInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/RcsAgentInformation)

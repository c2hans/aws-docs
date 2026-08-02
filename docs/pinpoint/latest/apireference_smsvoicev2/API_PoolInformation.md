---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_PoolInformation.html
---

# PoolInformation
<a name="API_PoolInformation"></a>

The information for a pool in an AWS account.

## Contents
<a name="API_PoolInformation_Contents"></a>

 ** CreatedTimestamp **   <a name="pinpoint-Type-PoolInformation-CreatedTimestamp"></a>
The time when the pool was created, in [UNIX epoch time](https://www.epochconverter.com/) format.
Type: Timestamp
Required: Yes

 ** DeletionProtectionEnabled **   <a name="pinpoint-Type-PoolInformation-DeletionProtectionEnabled"></a>
When set to true the pool can't be deleted.
Type: Boolean
Required: Yes

 ** MessageType **   <a name="pinpoint-Type-PoolInformation-MessageType"></a>
The type of message. Valid values are TRANSACTIONAL for messages that are critical or time-sensitive and PROMOTIONAL for messages that aren't critical or time-sensitive.
Type: String
Valid Values: `TRANSACTIONAL | PROMOTIONAL`
Required: Yes

 ** OptOutListName **   <a name="pinpoint-Type-PoolInformation-OptOutListName"></a>
The name of the OptOutList associated with the pool.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_-]+`
Required: Yes

 ** PoolArn **   <a name="pinpoint-Type-PoolInformation-PoolArn"></a>
The Amazon Resource Name (ARN) for the pool.
Type: String
Required: Yes

 ** PoolId **   <a name="pinpoint-Type-PoolInformation-PoolId"></a>
The unique identifier for the pool.
Type: String
Required: Yes

 ** SelfManagedOptOutsEnabled **   <a name="pinpoint-Type-PoolInformation-SelfManagedOptOutsEnabled"></a>
When set to false, an end recipient sends a message that begins with HELP or STOP to one of your dedicated numbers, AWS End User Messaging SMS automatically replies with a customizable message and adds the end recipient to the OptOutList. When set to true you're responsible for responding to HELP and STOP requests. You're also responsible for tracking and honoring opt-out requests. For more information see [Self-managed opt-outs](https://docs.aws.amazon.com/pinpoint/latest/userguide/settings-sms-managing.html#settings-account-sms-self-managed-opt-out)
Type: Boolean
Required: Yes

 ** SharedRoutesEnabled **   <a name="pinpoint-Type-PoolInformation-SharedRoutesEnabled"></a>
Allows you to enable shared routes on your pool.
By default, this is set to `False`. If you set this value to `True`, your messages are sent using phone numbers or sender IDs (depending on the country) that are shared with other users. In some countries, such as the United States, senders aren't allowed to use shared routes and must use a dedicated phone number or short code.
Type: Boolean
Required: Yes

 ** Status **   <a name="pinpoint-Type-PoolInformation-Status"></a>
The current status of the pool.
Type: String
Valid Values: `CREATING | ACTIVE | DELETING`
Required: Yes

 ** TwoWayEnabled **   <a name="pinpoint-Type-PoolInformation-TwoWayEnabled"></a>
When set to true you can receive incoming text messages from your end recipients using the TwoWayChannelArn.
Type: Boolean
Required: Yes

 ** TwoWayChannelArn **   <a name="pinpoint-Type-PoolInformation-TwoWayChannelArn"></a>
The Amazon Resource Name (ARN) of the two way channel.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `\S+`
Required: No

 ** TwoWayChannelRole **   <a name="pinpoint-Type-PoolInformation-TwoWayChannelRole"></a>
An optional IAM Role Arn for a service to assume, to be able to post inbound SMS messages.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:\S+`
Required: No

## See Also
<a name="API_PoolInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/PoolInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/PoolInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/PoolInformation)

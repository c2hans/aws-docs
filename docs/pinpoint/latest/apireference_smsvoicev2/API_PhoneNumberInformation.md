---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_PhoneNumberInformation.html
---

# PhoneNumberInformation
<a name="API_PhoneNumberInformation"></a>

The information for a phone number, in E.164 format, in an AWS account.

## Contents
<a name="API_PhoneNumberInformation_Contents"></a>

 ** CreatedTimestamp **   <a name="pinpoint-Type-PhoneNumberInformation-CreatedTimestamp"></a>
The time when the phone number was created, in [UNIX epoch time](https://www.epochconverter.com/) format.
Type: Timestamp
Required: Yes

 ** DeletionProtectionEnabled **   <a name="pinpoint-Type-PhoneNumberInformation-DeletionProtectionEnabled"></a>
When set to true the phone number can't be deleted.
Type: Boolean
Required: Yes

 ** IsoCountryCode **   <a name="pinpoint-Type-PhoneNumberInformation-IsoCountryCode"></a>
The two-character code, in ISO 3166-1 alpha-2 format, for the country or region.
Type: String
Length Constraints: Fixed length of 2.
Pattern: `[A-Z]{2}`
Required: Yes

 ** MessageType **   <a name="pinpoint-Type-PhoneNumberInformation-MessageType"></a>
The type of message. Valid values are TRANSACTIONAL for messages that are critical or time-sensitive and PROMOTIONAL for messages that aren't critical or time-sensitive.
Type: String
Valid Values: `TRANSACTIONAL | PROMOTIONAL`
Required: Yes

 ** MonthlyLeasingPrice **   <a name="pinpoint-Type-PhoneNumberInformation-MonthlyLeasingPrice"></a>
The price, in US dollars, to lease the phone number.
Type: String
Required: Yes

 ** NumberCapabilities **   <a name="pinpoint-Type-PhoneNumberInformation-NumberCapabilities"></a>
Describes if the origination identity can be used for text messages, voice calls or both.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 4 items.
Valid Values: `SMS | VOICE | MMS | RCS`
Required: Yes

 ** NumberType **   <a name="pinpoint-Type-PhoneNumberInformation-NumberType"></a>
The type of phone number.
Type: String
Valid Values: `SHORT_CODE | LONG_CODE | TOLL_FREE | TEN_DLC | SIMULATOR`
Required: Yes

 ** OptOutListName **   <a name="pinpoint-Type-PhoneNumberInformation-OptOutListName"></a>
The name of the OptOutList associated with the phone number.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_-]+`
Required: Yes

 ** PhoneNumber **   <a name="pinpoint-Type-PhoneNumberInformation-PhoneNumber"></a>
The phone number in E.164 format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `\+?[1-9][0-9]{1,18}`
Required: Yes

 ** PhoneNumberArn **   <a name="pinpoint-Type-PhoneNumberInformation-PhoneNumberArn"></a>
The Amazon Resource Name (ARN) associated with the phone number.
Type: String
Required: Yes

 ** SelfManagedOptOutsEnabled **   <a name="pinpoint-Type-PhoneNumberInformation-SelfManagedOptOutsEnabled"></a>
When set to false and an end recipient sends a message that begins with HELP or STOP to one of your dedicated numbers, AWS End User Messaging SMS automatically replies with a customizable message and adds the end recipient to the OptOutList. When set to true you're responsible for responding to HELP and STOP requests. You're also responsible for tracking and honoring opt-out request. For more information see [Self-managed opt-outs](https://docs.aws.amazon.com/pinpoint/latest/userguide/settings-sms-managing.html#settings-account-sms-self-managed-opt-out)
Type: Boolean
Required: Yes

 ** Status **   <a name="pinpoint-Type-PhoneNumberInformation-Status"></a>
The current status of the phone number.
Type: String
Valid Values: `PENDING | ACTIVE | ASSOCIATING | DISASSOCIATING | DELETED`
Required: Yes

 ** TwoWayEnabled **   <a name="pinpoint-Type-PhoneNumberInformation-TwoWayEnabled"></a>
By default this is set to false. When set to true you can receive incoming text messages from your end recipients using the TwoWayChannelArn.
Type: Boolean
Required: Yes

 ** InternationalSendingEnabled **   <a name="pinpoint-Type-PhoneNumberInformation-InternationalSendingEnabled"></a>
When set to true the international sending of phone number is Enabled.
Type: Boolean
Required: No

 ** PhoneNumberId **   <a name="pinpoint-Type-PhoneNumberInformation-PhoneNumberId"></a>
The unique identifier for the phone number.
Type: String
Required: No

 ** PoolId **   <a name="pinpoint-Type-PhoneNumberInformation-PoolId"></a>
The unique identifier of the pool associated with the phone number.
Type: String
Required: No

 ** RegistrationId **   <a name="pinpoint-Type-PhoneNumberInformation-RegistrationId"></a>
The unique identifier for the registration.
Type: String
Required: No

 ** TwoWayChannelArn **   <a name="pinpoint-Type-PhoneNumberInformation-TwoWayChannelArn"></a>
The Amazon Resource Name (ARN) of the two way channel.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `\S+`
Required: No

 ** TwoWayChannelRole **   <a name="pinpoint-Type-PhoneNumberInformation-TwoWayChannelRole"></a>
An optional IAM Role Arn for a service to assume, to be able to post inbound SMS messages.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:\S+`
Required: No

## See Also
<a name="API_PhoneNumberInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/PhoneNumberInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/PhoneNumberInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/PhoneNumberInformation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

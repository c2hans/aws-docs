---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_SenderIdInformation.html
---

# SenderIdInformation
<a name="API_SenderIdInformation"></a>

The information for all SenderIds in an AWS account.

## Contents
<a name="API_SenderIdInformation_Contents"></a>

 ** DeletionProtectionEnabled **   <a name="pinpoint-Type-SenderIdInformation-DeletionProtectionEnabled"></a>
By default this is set to false. When set to true the sender ID can't be deleted.
Type: Boolean
Required: Yes

 ** IsoCountryCode **   <a name="pinpoint-Type-SenderIdInformation-IsoCountryCode"></a>
The two-character code, in ISO 3166-1 alpha-2 format, for the country or region.
Type: String
Length Constraints: Fixed length of 2.
Pattern: `[A-Z]{2}`
Required: Yes

 ** MessageTypes **   <a name="pinpoint-Type-SenderIdInformation-MessageTypes"></a>
The type of message. Valid values are TRANSACTIONAL for messages that are critical or time-sensitive and PROMOTIONAL for messages that aren't critical or time-sensitive.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 2 items.
Valid Values: `TRANSACTIONAL | PROMOTIONAL`
Required: Yes

 ** MonthlyLeasingPrice **   <a name="pinpoint-Type-SenderIdInformation-MonthlyLeasingPrice"></a>
The monthly leasing price, in US dollars.
Type: String
Required: Yes

 ** Registered **   <a name="pinpoint-Type-SenderIdInformation-Registered"></a>
True if the sender ID is registered.
Type: Boolean
Required: Yes

 ** SenderId **   <a name="pinpoint-Type-SenderIdInformation-SenderId"></a>
The alphanumeric sender ID in a specific country that you'd like to describe.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 11.
Pattern: `[A-Za-z0-9_-]+`
Required: Yes

 ** SenderIdArn **   <a name="pinpoint-Type-SenderIdInformation-SenderIdArn"></a>
The Amazon Resource Name (ARN) associated with the SenderId.
Type: String
Required: Yes

 ** RegistrationId **   <a name="pinpoint-Type-SenderIdInformation-RegistrationId"></a>
The unique identifier for the registration.
Type: String
Required: No

## See Also
<a name="API_SenderIdInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/SenderIdInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/SenderIdInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/SenderIdInformation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_UserPhoneConfig.html
---

# UserPhoneConfig
<a name="API_UserPhoneConfig"></a>

Contains information about the phone configuration settings for a user.

## Contents
<a name="API_UserPhoneConfig_Contents"></a>

 ** AfterContactWorkTimeLimit **   <a name="connect-Type-UserPhoneConfig-AfterContactWorkTimeLimit"></a>
The After Call Work (ACW) timeout setting, in seconds. This parameter has a minimum value of 0 and a maximum value of 2,000,000 seconds (24 days). Enter 0 if you don't want to allocate a specific amount of ACW time. It essentially means an indefinite amount of time. When the conversation ends, ACW starts; the agent must choose Close contact to end ACW.
When returned by a `SearchUsers` call, `AfterContactWorkTimeLimit` is returned in milliseconds.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** AutoAccept **   <a name="connect-Type-UserPhoneConfig-AutoAccept"></a>
The Auto accept setting.
Type: Boolean
Required: No

 ** DeskPhoneNumber **   <a name="connect-Type-UserPhoneConfig-DeskPhoneNumber"></a>
The phone number for the user's desk phone.
Type: String
Pattern: `\+[1-9]\d{1,14}$`
Required: No

 ** PersistentConnection **   <a name="connect-Type-UserPhoneConfig-PersistentConnection"></a>
The persistent connection setting for the user.
Type: Boolean
Required: No

 ** PhoneType **   <a name="connect-Type-UserPhoneConfig-PhoneType"></a>
The phone type.
Type: String
Valid Values: `SOFT_PHONE | DESK_PHONE`
Required: No

## See Also
<a name="API_UserPhoneConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/UserPhoneConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/UserPhoneConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/UserPhoneConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

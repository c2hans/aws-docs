---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_ContactChannel.html
---

# ContactChannel
<a name="API_SSMContacts_ContactChannel"></a>

The method that Incident Manager uses to engage a contact.

## Contents
<a name="API_SSMContacts_ContactChannel_Contents"></a>

 ** ActivationStatus **   <a name="IncidentManager-Type-SSMContacts_ContactChannel-ActivationStatus"></a>
A Boolean value describing if the contact channel has been activated or not. If the contact channel isn't activated, Incident Manager can't engage the contact through it.
Type: String
Valid Values: `ACTIVATED | NOT_ACTIVATED`
Required: Yes

 ** ContactArn **   <a name="IncidentManager-Type-SSMContacts_ContactChannel-ContactArn"></a>
The ARN of the contact that contains the contact channel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`
Required: Yes

 ** ContactChannelArn **   <a name="IncidentManager-Type-SSMContacts_ContactChannel-ContactChannelArn"></a>
The Amazon Resource Name (ARN) of the contact channel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`
Required: Yes

 ** DeliveryAddress **   <a name="IncidentManager-Type-SSMContacts_ContactChannel-DeliveryAddress"></a>
The details that Incident Manager uses when trying to engage the contact channel.
Type: [ContactChannelAddress](API_SSMContacts_ContactChannelAddress.md) object
Required: Yes

 ** Name **   <a name="IncidentManager-Type-SSMContacts_ContactChannel-Name"></a>
The name of the contact channel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[\p{L}\p{Z}\p{N}_.\-]*$`
Required: Yes

 ** Type **   <a name="IncidentManager-Type-SSMContacts_ContactChannel-Type"></a>
The type of the contact channel. Incident Manager supports three contact methods:
+ SMS
+ VOICE
+ EMAIL
Type: String
Valid Values: `SMS | VOICE | EMAIL`
Required: No

## See Also
<a name="API_SSMContacts_ContactChannel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-contacts-2021-05-03/ContactChannel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-contacts-2021-05-03/ContactChannel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-contacts-2021-05-03/ContactChannel)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Incident Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query incident-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

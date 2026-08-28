---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_SenderContact.html
---

# SenderContact
<a name="API_SenderContact"></a>

An object that contains the details of the sender-provided contact person for the `EngagementInvitation`.

## Contents
<a name="API_SenderContact_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Email **   <a name="AWSPartnerCentral-Type-SenderContact-Email"></a>
The sender-provided contact's email address associated with the `EngagementInvitation`.
Type: String
Pattern: `(?=.{1,80}$)[a-zA-Z0-9.!#$%&'*+/=?^_{|}~-]+@[a-zA-Z0-9-]+(?:.[a-zA-Z0-9-]+)*`
Required: Yes

 ** BusinessTitle **   <a name="AWSPartnerCentral-Type-SenderContact-BusinessTitle"></a>
The sender-provided contact's title (job title or role) associated with the `EngagementInvitation`.
Type: String
Pattern: `(?s).{0,80}`
Required: No

 ** FirstName **   <a name="AWSPartnerCentral-Type-SenderContact-FirstName"></a>
The sender-provided contact's last name associated with the `EngagementInvitation`.
Type: String
Pattern: `(?s).{0,80}`
Required: No

 ** LastName **   <a name="AWSPartnerCentral-Type-SenderContact-LastName"></a>
The sender-provided contact's first name associated with the `EngagementInvitation`.
Type: String
Pattern: `(?s).{0,80}`
Required: No

 ** Phone **   <a name="AWSPartnerCentral-Type-SenderContact-Phone"></a>
The sender-provided contact's phone number associated with the `EngagementInvitation`.
Type: String
Pattern: `\+[1-9]\d{1,14}`
Required: No

## See Also
<a name="API_SenderContact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/SenderContact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/SenderContact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/SenderContact)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

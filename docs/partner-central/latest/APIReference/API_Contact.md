---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_Contact.html
---

# Contact
<a name="API_Contact"></a>

An object that contains a `Customer Partner`'s contact details.

## Contents
<a name="API_Contact_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** BusinessTitle **   <a name="AWSPartnerCentral-Type-Contact-BusinessTitle"></a>
The partner contact's title (job title or role) associated with the `Opportunity`. `BusinessTitle` supports either `PartnerAccountManager` or `OpportunityOwner`.
Type: String
Pattern: `(?s).{0,80}`
Required: No

 ** Email **   <a name="AWSPartnerCentral-Type-Contact-Email"></a>
The contact's email address associated with the `Opportunity`.
Type: String
Pattern: `(?=.{0,80}$)[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?`
Required: No

 ** FirstName **   <a name="AWSPartnerCentral-Type-Contact-FirstName"></a>
The contact's first name associated with the `Opportunity`.
Type: String
Pattern: `(?s).{0,80}`
Required: No

 ** LastName **   <a name="AWSPartnerCentral-Type-Contact-LastName"></a>
The contact's last name associated with the `Opportunity`.
Type: String
Pattern: `(?s).{0,80}`
Required: No

 ** Phone **   <a name="AWSPartnerCentral-Type-Contact-Phone"></a>
The contact's phone number associated with the `Opportunity`.
Type: String
Pattern: `\+[1-9]\d{1,14}`
Required: No

## See Also
<a name="API_Contact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/Contact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/Contact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/Contact)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

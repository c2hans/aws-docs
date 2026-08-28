---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_Customer.html
---

# Customer
<a name="API_Customer"></a>

An object that contains the customer's `Account` and `Contact`.

## Contents
<a name="API_Customer_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Account **   <a name="AWSPartnerCentral-Type-Customer-Account"></a>
An object that contains the customer's account details.
Type: [Account](API_Account.md) object
Required: No

 ** Contacts **   <a name="AWSPartnerCentral-Type-Customer-Contacts"></a>
Represents the contact details for individuals associated with the customer of the `Opportunity`. This field captures relevant contacts, including decision-makers, influencers, and technical stakeholders within the customer organization. These contacts are key to progressing the opportunity.
Type: Array of [Contact](API_Contact.md) objects
Required: No

## See Also
<a name="API_Customer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/Customer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/Customer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/Customer)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

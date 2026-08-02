---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_LeadContact.html
---

# LeadContact
<a name="API_LeadContact"></a>

An object that contains a lead contact's details associated with the engagement. This provides contact information for individuals involved in lead-related activities.

## Contents
<a name="API_LeadContact_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** BusinessTitle **   <a name="AWSPartnerCentral-Type-LeadContact-BusinessTitle"></a>
The lead contact's business title or job role associated with the engagement.
Type: String
Pattern: `(?s).{0,80}`
Required: Yes

 ** Email **   <a name="AWSPartnerCentral-Type-LeadContact-Email"></a>
The lead contact's email address associated with the engagement.
Type: String
Pattern: `(?=.{0,80}$)[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?`
Required: Yes

 ** FirstName **   <a name="AWSPartnerCentral-Type-LeadContact-FirstName"></a>
The lead contact's first name associated with the engagement.
Type: String
Pattern: `(?s).{0,80}`
Required: Yes

 ** LastName **   <a name="AWSPartnerCentral-Type-LeadContact-LastName"></a>
The lead contact's last name associated with the engagement.
Type: String
Pattern: `(?s).{0,80}`
Required: Yes

 ** Phone **   <a name="AWSPartnerCentral-Type-LeadContact-Phone"></a>
The lead contact's phone number associated with the engagement.
Type: String
Pattern: `\+[1-9]\d{1,14}`
Required: No

## See Also
<a name="API_LeadContact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/LeadContact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/LeadContact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/LeadContact)

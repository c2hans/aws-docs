---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_AssigneeContact.html
---

# AssigneeContact
<a name="API_AssigneeContact"></a>

Represents the contact details of the individual assigned to manage the opportunity within the partner organization. This helps to ensure that there is a point of contact for the opportunity's progress.

## Contents
<a name="API_AssigneeContact_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** BusinessTitle **   <a name="AWSPartnerCentral-Type-AssigneeContact-BusinessTitle"></a>
Specifies the business title of the assignee managing the opportunity. This helps clarify the individual's role and responsibilities within the organization. Use the value `PartnerAccountManager` to update details of the opportunity owner.
Type: String
Pattern: `(?s).{0,80}`
Required: Yes

 ** Email **   <a name="AWSPartnerCentral-Type-AssigneeContact-Email"></a>
Provides the email address of the assignee. This email is used for communications and notifications related to the opportunity.
Type: String
Pattern: `(?=.{0,80}$)[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?`
Required: Yes

 ** FirstName **   <a name="AWSPartnerCentral-Type-AssigneeContact-FirstName"></a>
Specifies the first name of the assignee managing the opportunity. The system automatically retrieves this value from the user profile by referencing the associated email address.
Type: String
Pattern: `(?s).{0,80}`
Required: Yes

 ** LastName **   <a name="AWSPartnerCentral-Type-AssigneeContact-LastName"></a>
Specifies the last name of the assignee managing the opportunity. The system automatically retrieves this value from the user profile by referencing the associated email address.
Type: String
Pattern: `(?s).{0,80}`
Required: Yes

 ** Phone **   <a name="AWSPartnerCentral-Type-AssigneeContact-Phone"></a>
Specifies the contact phone number of the assignee responsible for the opportunity or engagement. This field enables direct communication for time-sensitive matters and facilitates coordination between AWS and partner teams.
Type: String
Pattern: `\+[1-9]\d{1,14}`
Required: No

## See Also
<a name="API_AssigneeContact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/AssigneeContact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/AssigneeContact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/AssigneeContact)

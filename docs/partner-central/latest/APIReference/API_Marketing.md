---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_Marketing.html
---

# Marketing
<a name="API_Marketing"></a>

An object that contains marketing details for the `Opportunity`.

## Contents
<a name="API_Marketing_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AwsFundingUsed **   <a name="AWSPartnerCentral-Type-Marketing-AwsFundingUsed"></a>
Indicates if the `Opportunity` is a marketing development fund (MDF) funded activity.
Type: String
Valid Values: `Yes | No`
Required: No

 ** CampaignName **   <a name="AWSPartnerCentral-Type-Marketing-CampaignName"></a>
Specifies the `Opportunity` marketing campaign code. The AWS campaign code is a reference to specific marketing initiatives, promotions, or activities. This field captures the identifier used to track and categorize the `Opportunity` within marketing campaigns. If you don't have a campaign code, contact your AWS point of contact to obtain one.
Type: String
Required: No

 ** Channels **   <a name="AWSPartnerCentral-Type-Marketing-Channels"></a>
Specifies the `Opportunity`'s channel that the marketing activity is associated with or was contacted through. This field provides information about the specific marketing channel that contributed to the generation of the lead or contact.
Type: Array of strings
Valid Values: `AWS Marketing Central | Content Syndication | Display | Email | Live Event | Out Of Home (OOH) | Print | Search | Social | Telemarketing | TV | Video | Virtual Event`
Required: No

 ** Source **   <a name="AWSPartnerCentral-Type-Marketing-Source"></a>
Indicates if the `Opportunity` was sourced from an AWS marketing activity. Use the value `Marketing Activity`. Use `None` if it's not associated with an AWS marketing activity. This field helps AWS track the return on marketing investments and enables better distribution of marketing budgets among partners.
Type: String
Valid Values: `Marketing Activity | None`
Required: No

 ** UseCases **   <a name="AWSPartnerCentral-Type-Marketing-UseCases"></a>
Specifies the marketing activity use case or purpose that led to the `Opportunity`'s creation or contact. This field captures the context or marketing activity's execution's intention and the direct correlation to the generated opportunity or contact. Must be empty when `Marketing.AWSFundingUsed = No`.
Valid values: `AI/ML | Analytics | Application Integration | Blockchain | Business Applications | Cloud Financial Management | Compute | Containers | Customer Engagement | Databases | Developer Tools | End User Computing | Front End Web & Mobile | Game Tech | IoT | Management & Governance | Media Services | Migration & Transfer | Networking & Content Delivery | Quantum Technologies | Robotics | Satellite | Security | Serverless | Storage | VR & AR`
Type: Array of strings
Required: No

## See Also
<a name="API_Marketing_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/Marketing)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/Marketing)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/Marketing)

---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_OpportunitySearchAccount.html
---

# OpportunitySearchAccount

Contains the end customer account fields (company name, industry, AWS account ID, and address) returned for an opportunity in search results.

## Contents
<a name="API_OpportunitySearchAccount_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Address **   <a name="AWSPartnerCentral-Type-OpportunitySearchAccount-Address"></a>
The end customer address details for the opportunity.
Type: [OpportunitySearchAddress](API_OpportunitySearchAddress.md) object
Required: No

 ** AwsAccountId **   <a name="AWSPartnerCentral-Type-OpportunitySearchAccount-AwsAccountId"></a>
The end customer company's AWS account ID, if known or available.
Type: String
Required: No

 ** CompanyName **   <a name="AWSPartnerCentral-Type-OpportunitySearchAccount-CompanyName"></a>
The name of the end customer company on the opportunity.
Type: String
Pattern: `(?s).{0,120}`
Required: No

 ** Industry **   <a name="AWSPartnerCentral-Type-OpportunitySearchAccount-Industry"></a>
The industry of the end customer on the opportunity.
Type: String
Valid Values: `Aerospace | Agriculture | Automotive | Computers and Electronics | Consumer Goods | Education | Energy - Oil and Gas | Energy - Power and Utilities | Financial Services | Gaming | Government | Healthcare | Hospitality | Life Sciences | Manufacturing | Marketing and Advertising | Media and Entertainment | Mining | Non-Profit Organization | Professional Services | Real Estate and Construction | Retail | Software and Internet | Telecommunications | Transportation and Logistics | Travel | Wholesale and Distribution | Other`
Required: No

## See Also
<a name="API_OpportunitySearchAccount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/OpportunitySearchAccount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/OpportunitySearchAccount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/OpportunitySearchAccount)

---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_LeadInvitationCustomer.html
---

# LeadInvitationCustomer
<a name="API_LeadInvitationCustomer"></a>

Contains customer information included in a lead invitation payload. This structure provides essential details about the customer to help partners evaluate the lead opportunity and determine their interest in engagement.

## Contents
<a name="API_LeadInvitationCustomer_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CompanyName **   <a name="AWSPartnerCentral-Type-LeadInvitationCustomer-CompanyName"></a>
The name of the customer company associated with the lead invitation. This field identifies the target organization for the lead engagement opportunity.
Type: String
Pattern: `(?s).{1,120}`
Required: Yes

 ** AwsMaturity **   <a name="AWSPartnerCentral-Type-LeadInvitationCustomer-AwsMaturity"></a>
Indicates the customer's level of experience and adoption with AWS services. This assessment helps partners understand the customer's cloud maturity and tailor their engagement approach accordingly.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

 ** CountryCode **   <a name="AWSPartnerCentral-Type-LeadInvitationCustomer-CountryCode"></a>
The country code indicating the geographic location of the customer company. This information helps partners understand regional requirements and assess their ability to serve the customer effectively.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10.
Required: No

 ** Industry **   <a name="AWSPartnerCentral-Type-LeadInvitationCustomer-Industry"></a>
Specifies the industry sector of the customer company associated with the lead invitation. This categorization helps partners understand the customer's business context and assess solution fit.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

 ** MarketSegment **   <a name="AWSPartnerCentral-Type-LeadInvitationCustomer-MarketSegment"></a>
Specifies the market segment classification of the customer, such as enterprise, mid-market, or small business. This segmentation helps partners determine the appropriate solution complexity and engagement strategy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

 ** WebsiteUrl **   <a name="AWSPartnerCentral-Type-LeadInvitationCustomer-WebsiteUrl"></a>
The website URL of the customer company. This provides additional context about the customer organization and helps partners verify company details and assess business size and legitimacy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

## See Also
<a name="API_LeadInvitationCustomer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/LeadInvitationCustomer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/LeadInvitationCustomer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/LeadInvitationCustomer)

---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_LeadCustomer.html
---

# LeadCustomer
<a name="API_LeadCustomer"></a>

Contains detailed information about the customer associated with the lead, including company details, industry classification, and AWS maturity level. This information helps qualify and categorize the lead for appropriate engagement strategies.

## Contents
<a name="API_LeadCustomer_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CompanyName **   <a name="AWSPartnerCentral-Type-LeadCustomer-CompanyName"></a>
The name of the lead customer's company. This field is essential for identifying and tracking the customer organization associated with the lead.
Type: String
Pattern: `(?s).{1,120}`
Required: Yes

 ** Address **   <a name="AWSPartnerCentral-Type-LeadCustomer-Address"></a>
The address information for the lead customer.
Type: [LeadAddress](API_LeadAddress.md) object
Required: No

 ** AwsMaturity **   <a name="AWSPartnerCentral-Type-LeadCustomer-AwsMaturity"></a>
Indicates the customer's level of experience and adoption with AWS services. This assessment helps determine the appropriate engagement approach and solution complexity.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

 ** Industry **   <a name="AWSPartnerCentral-Type-LeadCustomer-Industry"></a>
Specifies the industry sector to which the lead customer's company belongs. This categorization helps in understanding the customer's business context and tailoring appropriate solutions.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

 ** MarketSegment **   <a name="AWSPartnerCentral-Type-LeadCustomer-MarketSegment"></a>
Specifies the market segment classification of the lead customer, such as enterprise, mid-market, or small business. This segmentation helps in targeting appropriate solutions and engagement strategies.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

 ** WebsiteUrl **   <a name="AWSPartnerCentral-Type-LeadCustomer-WebsiteUrl"></a>
The website URL of the lead customer's company. This provides additional context about the customer organization and helps verify company legitimacy and size.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

## See Also
<a name="API_LeadCustomer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/LeadCustomer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/LeadCustomer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/LeadCustomer)

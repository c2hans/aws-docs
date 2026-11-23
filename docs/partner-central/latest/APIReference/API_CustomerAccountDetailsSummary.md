---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_CustomerAccountDetailsSummary.html
---

# CustomerAccountDetailsSummary

The customer information for an account in search results. It carries a reduced set of fields compared to the full customer information that `GetCustomerAccount` returns, omitting sensitive fields such as the Data Universal Numbering System (DUNS) number and the street address. To read those fields, use `GetCustomerAccount`.

## Contents
<a name="API_CustomerAccountDetailsSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CompanyName **   <a name="AWSPartnerCentral-Type-CustomerAccountDetailsSummary-CompanyName"></a>
The name of the customer company.
Type: String
Pattern: `(?s).{0,120}`
Required: Yes

## See Also
<a name="API_CustomerAccountDetailsSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/CustomerAccountDetailsSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/CustomerAccountDetailsSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/CustomerAccountDetailsSummary)

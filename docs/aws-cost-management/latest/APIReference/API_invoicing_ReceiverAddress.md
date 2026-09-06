---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_ReceiverAddress.html
---

# ReceiverAddress
<a name="API_invoicing_ReceiverAddress"></a>

 The details of the address associated with the receiver.

## Contents
<a name="API_invoicing_ReceiverAddress_Contents"></a>

 ** AddressLine1 **   <a name="awscostmanagement-Type-invoicing_ReceiverAddress-AddressLine1"></a>
 The first line of the address.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\s\S]*`
Required: No

 ** AddressLine2 **   <a name="awscostmanagement-Type-invoicing_ReceiverAddress-AddressLine2"></a>
 The second line of the address, if applicable.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\s\S]*`
Required: No

 ** AddressLine3 **   <a name="awscostmanagement-Type-invoicing_ReceiverAddress-AddressLine3"></a>
 The third line of the address, if applicable.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\s\S]*`
Required: No

 ** City **   <a name="awscostmanagement-Type-invoicing_ReceiverAddress-City"></a>
 The city that the address is in.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\s\S]*`
Required: No

 ** CompanyName **   <a name="awscostmanagement-Type-invoicing_ReceiverAddress-CompanyName"></a>
 A unique company name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\s\S]*`
Required: No

 ** CountryCode **   <a name="awscostmanagement-Type-invoicing_ReceiverAddress-CountryCode"></a>
 The country code for the country the address is in.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\s\S]*`
Required: No

 ** DistrictOrCounty **   <a name="awscostmanagement-Type-invoicing_ReceiverAddress-DistrictOrCounty"></a>
 The district or country the address is located in.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\s\S]*`
Required: No

 ** PostalCode **   <a name="awscostmanagement-Type-invoicing_ReceiverAddress-PostalCode"></a>
 The postal code associated with the address.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\s\S]*`
Required: No

 ** StateOrRegion **   <a name="awscostmanagement-Type-invoicing_ReceiverAddress-StateOrRegion"></a>
 The state, region, or province the address is located.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\s\S]*`
Required: No

## See Also
<a name="API_invoicing_ReceiverAddress_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/invoicing-2024-12-01/ReceiverAddress)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/invoicing-2024-12-01/ReceiverAddress)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/invoicing-2024-12-01/ReceiverAddress)

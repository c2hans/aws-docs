---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_Jurisdiction.html
---

# Jurisdiction
<a name="API_taxSettings_Jurisdiction"></a>

The jurisdiction details of the TRN information of the customers. This doesn't contain full legal address, and contains only country code and state/region/province.

## Contents
<a name="API_taxSettings_Jurisdiction_Contents"></a>

 ** countryCode **   <a name="awscostmanagement-Type-taxSettings_Jurisdiction-countryCode"></a>
 The country code of the jurisdiction.
Type: String
Length Constraints: Fixed length of 2.
Pattern: `[a-zA-Z]+`
Required: Yes

 ** stateOrRegion **   <a name="awscostmanagement-Type-taxSettings_Jurisdiction-stateOrRegion"></a>
 The state, region, or province associated with the country of the jurisdiction, if applicable.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `(?!\s*$)[\s\S]+`
Required: No

## See Also
<a name="API_taxSettings_Jurisdiction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/taxsettings-2018-05-10/Jurisdiction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/taxsettings-2018-05-10/Jurisdiction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/taxsettings-2018-05-10/Jurisdiction)

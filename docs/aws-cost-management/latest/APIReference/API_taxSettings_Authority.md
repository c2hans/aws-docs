---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_Authority.html
---

# Authority
<a name="API_taxSettings_Authority"></a>

The address domain associate with the tax information.

## Contents
<a name="API_taxSettings_Authority_Contents"></a>

 ** country **   <a name="awscostmanagement-Type-taxSettings_Authority-country"></a>
 The country code for the country that the address is in.
Type: String
Length Constraints: Fixed length of 2.
Pattern: `[a-zA-Z]+`
Required: Yes

 ** state **   <a name="awscostmanagement-Type-taxSettings_Authority-state"></a>
 The state that the address is located.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `(?!\s*$)[\s\S]+`
Required: No

## See Also
<a name="API_taxSettings_Authority_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/taxsettings-2018-05-10/Authority)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/taxsettings-2018-05-10/Authority)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/taxsettings-2018-05-10/Authority)

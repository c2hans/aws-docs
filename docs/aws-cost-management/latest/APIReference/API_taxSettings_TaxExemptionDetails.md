---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_TaxExemptionDetails.html
---

# TaxExemptionDetails
<a name="API_taxSettings_TaxExemptionDetails"></a>

The tax exemption details.

## Contents
<a name="API_taxSettings_TaxExemptionDetails_Contents"></a>

 ** heritageObtainedDetails **   <a name="awscostmanagement-Type-taxSettings_TaxExemptionDetails-heritageObtainedDetails"></a>
The indicator if the tax exemption is inherited from the consolidated billing family management account.
Type: Boolean
Required: No

 ** heritageObtainedParentEntity **   <a name="awscostmanagement-Type-taxSettings_TaxExemptionDetails-heritageObtainedParentEntity"></a>
The consolidated billing family management account the tax exemption inherited from.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[\s\S]*`
Required: No

 ** heritageObtainedReason **   <a name="awscostmanagement-Type-taxSettings_TaxExemptionDetails-heritageObtainedReason"></a>
The reason of the heritage inheritance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[\s\S]*`
Required: No

 ** taxExemptions **   <a name="awscostmanagement-Type-taxSettings_TaxExemptionDetails-taxExemptions"></a>
Tax exemptions.
Type: Array of [TaxExemption](API_taxSettings_TaxExemption.md) objects
Required: No

## See Also
<a name="API_taxSettings_TaxExemptionDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/taxsettings-2018-05-10/TaxExemptionDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/taxsettings-2018-05-10/TaxExemptionDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/taxsettings-2018-05-10/TaxExemptionDetails)

---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_CanadaAdditionalInfo.html
---

# CanadaAdditionalInfo
<a name="API_taxSettings_CanadaAdditionalInfo"></a>

 Additional tax information associated with your TRN in Canada .

## Contents
<a name="API_taxSettings_CanadaAdditionalInfo_Contents"></a>

 ** canadaQuebecSalesTaxNumber **   <a name="awscostmanagement-Type-taxSettings_CanadaAdditionalInfo-canadaQuebecSalesTaxNumber"></a>
 The Quebec Sales Tax ID number. Leave blank if you do not have a Quebec Sales Tax ID number.
Type: String
Pattern: `([0-9]{10})(TQ[0-9]{4})?`
Required: No

 ** canadaRetailSalesTaxNumber **   <a name="awscostmanagement-Type-taxSettings_CanadaAdditionalInfo-canadaRetailSalesTaxNumber"></a>
 Manitoba Retail Sales Tax ID number. Customers purchasing AWS services for resale in Manitoba must provide a valid Retail Sales Tax ID number for Manitoba. Leave this blank if you do not have a Retail Sales Tax ID number in Manitoba or are not purchasing AWS services for resale.
Type: String
Pattern: `([0-9]{6}-[0-9]{1})`
Required: No

 ** isResellerAccount **   <a name="awscostmanagement-Type-taxSettings_CanadaAdditionalInfo-isResellerAccount"></a>
 The value for this parameter must be `true` if the `provincialSalesTaxId` value is provided for a TRN in British Columbia, Saskatchewan, or Manitoba provinces.
To claim a provincial sales tax (PST) and retail sales tax (RST) reseller exemption, you must confirm that purchases from this account were made for resale. Otherwise, remove the PST or RST number from the `provincialSalesTaxId` parameter from your request.
Type: Boolean
Required: No

 ** provincialSalesTaxId **   <a name="awscostmanagement-Type-taxSettings_CanadaAdditionalInfo-provincialSalesTaxId"></a>
 The provincial sales tax ID for your TRN in Canada. This parameter can represent the following:
+ Provincial sales tax ID number for British Columbia and Saskatchewan provinces
+ Manitoba retail sales tax ID number for Manitoba province
+ Quebec sales tax ID number for Quebec province
The Tax Setting API only accepts this parameter if the TRN is specified for the previous provinces. For other provinces, the Tax Settings API doesn't accept this parameter.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 16.
Pattern: `([0-9A-Z/-]+)`
Required: No

## See Also
<a name="API_taxSettings_CanadaAdditionalInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/taxsettings-2018-05-10/CanadaAdditionalInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/taxsettings-2018-05-10/CanadaAdditionalInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/taxsettings-2018-05-10/CanadaAdditionalInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

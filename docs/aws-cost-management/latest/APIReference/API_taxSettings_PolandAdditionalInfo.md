---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_PolandAdditionalInfo.html
---

# PolandAdditionalInfo
<a name="API_taxSettings_PolandAdditionalInfo"></a>

 Additional tax information associated with your TRN in Poland.

## Contents
<a name="API_taxSettings_PolandAdditionalInfo_Contents"></a>

 ** individualRegistrationNumber **   <a name="awscostmanagement-Type-taxSettings_PolandAdditionalInfo-individualRegistrationNumber"></a>
 The individual tax registration number (NIP). Individual NIP is valid for other taxes excluding VAT purposes.
Type: String
Pattern: `([0-9]{10})`
Required: No

 ** isGroupVatEnabled **   <a name="awscostmanagement-Type-taxSettings_PolandAdditionalInfo-isGroupVatEnabled"></a>
 True if your business is a member of a VAT group with a NIP active for VAT purposes. Otherwise, this is false.
Type: Boolean
Required: No

 ** taxRegistrationNumberType **   <a name="awscostmanagement-Type-taxSettings_PolandAdditionalInfo-taxRegistrationNumberType"></a>
The tax registration number type. Valid values are `EUTaxRegistrationNumber`, `LocalTaxRegistrationNumber`, or `LocalRegistrationNumber`.
Type: String
Valid Values: `EUTaxRegistrationNumber | LocalTaxRegistrationNumber | LocalRegistrationNumber`
Required: No

## See Also
<a name="API_taxSettings_PolandAdditionalInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/taxsettings-2018-05-10/PolandAdditionalInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/taxsettings-2018-05-10/PolandAdditionalInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/taxsettings-2018-05-10/PolandAdditionalInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_IndonesiaAdditionalInfo.html
---

# IndonesiaAdditionalInfo
<a name="API_taxSettings_IndonesiaAdditionalInfo"></a>

Additional tax information associated with your TRN in Indonesia.

## Contents
<a name="API_taxSettings_IndonesiaAdditionalInfo_Contents"></a>

 ** decisionNumber **   <a name="awscostmanagement-Type-taxSettings_IndonesiaAdditionalInfo-decisionNumber"></a>
VAT-exempt customers have a Directorate General of Taxation (DGT) exemption letter or certificate (Surat Keterangan Bebas) decision number. Non-collected VAT have a DGT letter or certificate (Surat Keterangan Tidak Dipungut).
Type: String
Pattern: `([a-zA-Z0-9/.\-]{0,200})`
Required: No

 ** ppnExceptionDesignationCode **   <a name="awscostmanagement-Type-taxSettings_IndonesiaAdditionalInfo-ppnExceptionDesignationCode"></a>
Exception code if you are designated by Directorate General of Taxation (DGT) as a VAT collector, non-collected VAT, or VAT-exempt customer.
Type: String
Pattern: `(01|02|03|07|08)`
Required: No

 ** taxRegistrationNumberType **   <a name="awscostmanagement-Type-taxSettings_IndonesiaAdditionalInfo-taxRegistrationNumberType"></a>
The tax registration number type.
Type: String
Valid Values: `NIK | PassportNumber | NPWP | NITKU`
Required: No

## See Also
<a name="API_taxSettings_IndonesiaAdditionalInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/taxsettings-2018-05-10/IndonesiaAdditionalInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/taxsettings-2018-05-10/IndonesiaAdditionalInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/taxsettings-2018-05-10/IndonesiaAdditionalInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

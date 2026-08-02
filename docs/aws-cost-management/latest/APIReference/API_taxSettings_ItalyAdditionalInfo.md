---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_ItalyAdditionalInfo.html
---

# ItalyAdditionalInfo
<a name="API_taxSettings_ItalyAdditionalInfo"></a>

 Additional tax information associated with your TRN in Italy.

## Contents
<a name="API_taxSettings_ItalyAdditionalInfo_Contents"></a>

 ** cigNumber **   <a name="awscostmanagement-Type-taxSettings_ItalyAdditionalInfo-cigNumber"></a>
 The tender procedure identification code.
Type: String
Pattern: `([0-9A-Z]{1,15})`
Required: No

 ** cupNumber **   <a name="awscostmanagement-Type-taxSettings_ItalyAdditionalInfo-cupNumber"></a>
 Additional tax information to specify for a TRN in Italy. This is managed by the Interministerial Committee for Economic Planning (CIPE) which characterizes every public investment project (Individual Project Code).
Type: String
Pattern: `([0-9A-Z]{1,15})`
Required: No

 ** customerType **   <a name="awscostmanagement-Type-taxSettings_ItalyAdditionalInfo-customerType"></a>
The customer type for tax registration in Italy. Valid values are `Business` or `Individual`.
Type: String
Valid Values: `Business | Individual`
Required: No

 ** sdiAccountId **   <a name="awscostmanagement-Type-taxSettings_ItalyAdditionalInfo-sdiAccountId"></a>
 Additional tax information to specify for a TRN in Italy. Use CodiceDestinatario to receive your invoices via web service (API) or FTP.
Type: String
Pattern: `[0-9A-Z]{6,7}`
Required: No

 ** taxCode **   <a name="awscostmanagement-Type-taxSettings_ItalyAdditionalInfo-taxCode"></a>
List of service tax codes for your TRN in Italy. You can use your customer tax code as part of a VAT Group.
Type: String
Pattern: `([0-9]{11}|[A-Z]{6}[0-9]{2}[A-Z][0-9]{2}[A-Z][0-9]{3}[A-Z])`
Required: No

## See Also
<a name="API_taxSettings_ItalyAdditionalInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/taxsettings-2018-05-10/ItalyAdditionalInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/taxsettings-2018-05-10/ItalyAdditionalInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/taxsettings-2018-05-10/ItalyAdditionalInfo)

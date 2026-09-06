---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_IsraelAdditionalInfo.html
---

# IsraelAdditionalInfo
<a name="API_taxSettings_IsraelAdditionalInfo"></a>

 Additional tax information associated with your TRN in Israel.

## Contents
<a name="API_taxSettings_IsraelAdditionalInfo_Contents"></a>

 ** customerType **   <a name="awscostmanagement-Type-taxSettings_IsraelAdditionalInfo-customerType"></a>
 Customer type for your TRN in Israel. The value can be `Business` or `Individual`. Use `Business`for entities such as not-for-profit and financial institutions.
Type: String
Valid Values: `Business | Individual`
Required: Yes

 ** dealerType **   <a name="awscostmanagement-Type-taxSettings_IsraelAdditionalInfo-dealerType"></a>
 Dealer type for your TRN in Israel. If you're not a local authorized dealer with an Israeli VAT ID, specify your tax identification number so that AWS can send you a compliant tax invoice.
Type: String
Valid Values: `Authorized | Non-authorized`
Required: Yes

## See Also
<a name="API_taxSettings_IsraelAdditionalInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/taxsettings-2018-05-10/IsraelAdditionalInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/taxsettings-2018-05-10/IsraelAdditionalInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/taxsettings-2018-05-10/IsraelAdditionalInfo)

---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_TurkeyAdditionalInfo.html
---

# TurkeyAdditionalInfo
<a name="API_taxSettings_TurkeyAdditionalInfo"></a>

Additional tax information associated with your TRN in Turkey.

## Contents
<a name="API_taxSettings_TurkeyAdditionalInfo_Contents"></a>

 ** industries **   <a name="awscostmanagement-Type-taxSettings_TurkeyAdditionalInfo-industries"></a>
The industry information that tells the Tax Settings API if you're subject to additional withholding taxes. This information required for business-to-business (B2B) customers. This information is conditionally mandatory for B2B customers who are subject to KDV tax.
Type: String
Valid Values: `CirculatingOrg | ProfessionalOrg | Banks | Insurance | PensionAndBenefitFunds | DevelopmentAgencies`
Required: No

 ** kepEmailId **   <a name="awscostmanagement-Type-taxSettings_TurkeyAdditionalInfo-kepEmailId"></a>
The Registered Electronic Mail (REM) that is used to send notarized communication. This parameter is optional for business-to-business (B2B) and business-to-government (B2G) customers. It's not required for business-to-consumer (B2C) customers.
Type: String
Pattern: `[\s\S]*`
Required: No

 ** secondaryTaxId **   <a name="awscostmanagement-Type-taxSettings_TurkeyAdditionalInfo-secondaryTaxId"></a>
 Secondary tax ID (“harcama birimi VKN”si”). If one isn't provided, we will use your VKN as the secondary ID.
Type: String
Pattern: `([0-9]{10})`
Required: No

 ** taxOffice **   <a name="awscostmanagement-Type-taxSettings_TurkeyAdditionalInfo-taxOffice"></a>
The tax office where you're registered. You can enter this information as a string. The Tax Settings API will add this information to your invoice. This parameter is required for business-to-business (B2B) and business-to-government customers. It's not required for business-to-consumer (B2C) customers.
Type: String
Pattern: `[\s\S]*`
Required: No

## See Also
<a name="API_taxSettings_TurkeyAdditionalInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/taxsettings-2018-05-10/TurkeyAdditionalInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/taxsettings-2018-05-10/TurkeyAdditionalInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/taxsettings-2018-05-10/TurkeyAdditionalInfo)

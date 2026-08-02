---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_EgyptAdditionalInfo.html
---

# EgyptAdditionalInfo
<a name="API_taxSettings_EgyptAdditionalInfo"></a>

Additional tax information to specify for a TRN in Egypt.

## Contents
<a name="API_taxSettings_EgyptAdditionalInfo_Contents"></a>

 ** uniqueIdentificationNumber **   <a name="awscostmanagement-Type-taxSettings_EgyptAdditionalInfo-uniqueIdentificationNumber"></a>
The unique identification number provided by the Egypt Tax Authority.
Type: String
Pattern: `[a-zA-Z0-9]{39}`
Required: No

 ** uniqueIdentificationNumberExpirationDate **   <a name="awscostmanagement-Type-taxSettings_EgyptAdditionalInfo-uniqueIdentificationNumberExpirationDate"></a>
The expiration date of the unique identification number provided by the Egypt Tax Authority.
Type: String
Pattern: `(\d{4}-(0[0-9]|1[0-2])-([0-2][0-9]|3[0-1]))`
Required: No

## See Also
<a name="API_taxSettings_EgyptAdditionalInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/taxsettings-2018-05-10/EgyptAdditionalInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/taxsettings-2018-05-10/EgyptAdditionalInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/taxsettings-2018-05-10/EgyptAdditionalInfo)

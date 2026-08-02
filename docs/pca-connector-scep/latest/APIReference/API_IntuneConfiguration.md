---
source_url: https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_IntuneConfiguration.html
---

# IntuneConfiguration
<a name="API_IntuneConfiguration"></a>

Contains configuration details for use with Microsoft Intune. For information about using Connector for SCEP for Microsoft Intune, see [Using Connector for SCEP for Microsoft Intune](https://docs.aws.amazon.com/privateca/latest/userguide/scep-connector.htmlconnector-for-scep-intune.html).

When you use Connector for SCEP for Microsoft Intune, certain functionalities are enabled by accessing Microsoft Intune through the Microsoft API. Your use of the Connector for SCEP and accompanying AWS services doesn't remove your need to have a valid license for your use of the Microsoft Intune service. You should also review the [Microsoft Intune® App Protection Policies](https://learn.microsoft.com/en-us/mem/intune/apps/app-protection-policy).

## Contents
<a name="API_IntuneConfiguration_Contents"></a>

 ** AzureApplicationId **   <a name="pcaconnectorscep-Type-IntuneConfiguration-AzureApplicationId"></a>
The directory (tenant) ID from your Microsoft Entra ID app registration.
Type: String
Length Constraints: Minimum length of 15. Maximum length of 100.
Pattern: `[a-zA-Z0-9]{2,15}-[a-zA-Z0-9]{2,15}-[a-zA-Z0-9]{2,15}-[a-zA-Z0-9]{2,15}-[a-zA-Z0-9]{2,15}`
Required: Yes

 ** Domain **   <a name="pcaconnectorscep-Type-IntuneConfiguration-Domain"></a>
The primary domain from your Microsoft Entra ID app registration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9._-]+`
Required: Yes

## See Also
<a name="API_IntuneConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pca-connector-scep-2018-05-10/IntuneConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pca-connector-scep-2018-05-10/IntuneConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pca-connector-scep-2018-05-10/IntuneConfiguration)

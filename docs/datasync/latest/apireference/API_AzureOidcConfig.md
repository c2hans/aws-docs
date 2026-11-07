---
source_url: https://docs.aws.amazon.com/datasync/latest/apireference/API_AzureOidcConfig.html
---

# AzureOidcConfig
<a name="API_AzureOidcConfig"></a>

External identity parameters for Azure Blob Storage.

## Contents
<a name="API_AzureOidcConfig_Contents"></a>

 ** ClientId **   <a name="DataSync-Type-AzureOidcConfig-ClientId"></a>
Azure client ID string.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`
Required: Yes

 ** TenantId **   <a name="DataSync-Type-AzureOidcConfig-TenantId"></a>
Azure tenant ID string.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`
Required: Yes

## See Also
<a name="API_AzureOidcConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datasync-2018-11-09/AzureOidcConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datasync-2018-11-09/AzureOidcConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datasync-2018-11-09/AzureOidcConfig)

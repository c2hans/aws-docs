---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_AzureProviderDetailUpdate.html
---

# AzureProviderDetailUpdate
<a name="API_AzureProviderDetailUpdate"></a>

The Azure-specific configuration details for updating a connector, including the scan scope and regions to scan.

## Contents
<a name="API_AzureProviderDetailUpdate_Contents"></a>

 ** autoInstallVMScanner **   <a name="inspector2-Type-AzureProviderDetailUpdate-autoInstallVMScanner"></a>
Specifies whether to automatically install the VM scanner on connected Azure resources.
Type: Boolean
Required: No

 ** azureRegions **   <a name="inspector2-Type-AzureProviderDetailUpdate-azureRegions"></a>
The updated Azure regions to scan.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`
Required: No

 ** scopeConfiguration **   <a name="inspector2-Type-AzureProviderDetailUpdate-scopeConfiguration"></a>
The updated scope configuration that defines which Azure resources to scan.
Type: [AzureScopeConfigurationInput](API_AzureScopeConfigurationInput.md) object
Required: No

## See Also
<a name="API_AzureProviderDetailUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/AzureProviderDetailUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/AzureProviderDetailUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/AzureProviderDetailUpdate)

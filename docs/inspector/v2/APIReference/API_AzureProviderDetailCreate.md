---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_AzureProviderDetailCreate.html
---

# AzureProviderDetailCreate
<a name="API_AzureProviderDetailCreate"></a>

The Azure-specific configuration details for creating a connector, including the AWS Config connector association, scan scope, and regions to scan.

## Contents
<a name="API_AzureProviderDetailCreate_Contents"></a>

 ** awsConfigConnectorArn **   <a name="inspector2-Type-AzureProviderDetailCreate-awsConfigConnectorArn"></a>
The ARN of the AWS Config connector to associate with this connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:([^:]+):config:([^:]+):([^:]+):connector/([^/]+)/([^/]+)/([^/:\s]+)`
Required: Yes

 ** azureRegions **   <a name="inspector2-Type-AzureProviderDetailCreate-azureRegions"></a>
The Azure regions to scan.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

 ** scopeConfiguration **   <a name="inspector2-Type-AzureProviderDetailCreate-scopeConfiguration"></a>
The scope configuration that defines which Azure resources to scan.
Type: [AzureScopeConfigurationInput](API_AzureScopeConfigurationInput.md) object
Required: Yes

 ** autoInstallVMScanner **   <a name="inspector2-Type-AzureProviderDetailCreate-autoInstallVMScanner"></a>
Specifies whether to automatically install the VM scanner on connected Azure resources. Defaults to `true`.
Type: Boolean
Required: No

## See Also
<a name="API_AzureProviderDetailCreate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/AzureProviderDetailCreate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/AzureProviderDetailCreate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/AzureProviderDetailCreate)

---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_AzureScopeConfigurationInput.html
---

# AzureScopeConfigurationInput
<a name="API_AzureScopeConfigurationInput"></a>

The scope of Azure resources to scan, defined separately for VM, container image, and serverless scanning. Provide this when you create or update an Azure connector.

## Contents
<a name="API_AzureScopeConfigurationInput_Contents"></a>

 ** containerImageScanning **   <a name="inspector2-Type-AzureScopeConfigurationInput-containerImageScanning"></a>
The scope configuration input for container image scanning.
Type: [ScopeConfigurationInput](API_ScopeConfigurationInput.md) object
Required: No

 ** serverlessScanning **   <a name="inspector2-Type-AzureScopeConfigurationInput-serverlessScanning"></a>
The scope configuration input for serverless scanning.
Type: [ScopeConfigurationInput](API_ScopeConfigurationInput.md) object
Required: No

 ** vmScanning **   <a name="inspector2-Type-AzureScopeConfigurationInput-vmScanning"></a>
The scope configuration input for VM scanning.
Type: [ScopeConfigurationInput](API_ScopeConfigurationInput.md) object
Required: No

## See Also
<a name="API_AzureScopeConfigurationInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/AzureScopeConfigurationInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/AzureScopeConfigurationInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/AzureScopeConfigurationInput)

---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_GcpScopeConfigurationInput.html
---

# GcpScopeConfigurationInput

The scope of Google Cloud Platform (GCP) resources to scan, defined separately for VM, container image, and serverless scanning. Provide this when you create or update a GCP connector.

## Contents
<a name="API_GcpScopeConfigurationInput_Contents"></a>

 ** containerImageScanning **   <a name="inspector2-Type-GcpScopeConfigurationInput-containerImageScanning"></a>
The scope configuration input for container image scanning.
Type: [GcpCapabilityScopeInput](API_GcpCapabilityScopeInput.md) object
Required: No

 ** serverlessScanning **   <a name="inspector2-Type-GcpScopeConfigurationInput-serverlessScanning"></a>
The scope configuration input for serverless scanning.
Type: [GcpCapabilityScopeInput](API_GcpCapabilityScopeInput.md) object
Required: No

 ** vmScanning **   <a name="inspector2-Type-GcpScopeConfigurationInput-vmScanning"></a>
The scope configuration input for VM scanning.
Type: [GcpCapabilityScopeInput](API_GcpCapabilityScopeInput.md) object
Required: No

## See Also
<a name="API_GcpScopeConfigurationInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/GcpScopeConfigurationInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/GcpScopeConfigurationInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/GcpScopeConfigurationInput)

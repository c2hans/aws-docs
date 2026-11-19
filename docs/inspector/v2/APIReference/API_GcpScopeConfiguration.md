---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_GcpScopeConfiguration.html
---

# GcpScopeConfiguration

The scope of Google Cloud Platform (GCP) resources that Amazon Inspector scans, defined separately for VM, container image, and serverless scanning. Returned as part of a connector's configuration.

## Contents
<a name="API_GcpScopeConfiguration_Contents"></a>

 ** containerImageScanning **   <a name="inspector2-Type-GcpScopeConfiguration-containerImageScanning"></a>
The scope configuration for container image scanning.
Type: [GcpCapabilityScope](API_GcpCapabilityScope.md) object
Required: No

 ** serverlessScanning **   <a name="inspector2-Type-GcpScopeConfiguration-serverlessScanning"></a>
The scope configuration for serverless scanning.
Type: [GcpCapabilityScope](API_GcpCapabilityScope.md) object
Required: No

 ** vmScanning **   <a name="inspector2-Type-GcpScopeConfiguration-vmScanning"></a>
The scope configuration for VM scanning.
Type: [GcpCapabilityScope](API_GcpCapabilityScope.md) object
Required: No

## See Also
<a name="API_GcpScopeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/GcpScopeConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/GcpScopeConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/GcpScopeConfiguration)

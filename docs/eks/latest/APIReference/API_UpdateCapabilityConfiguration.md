---
source_url: https://docs.aws.amazon.com/eks/latest/APIReference/API_UpdateCapabilityConfiguration.html
---

# UpdateCapabilityConfiguration
<a name="API_UpdateCapabilityConfiguration"></a>

Configuration updates for a capability. The structure varies depending on the capability type.

## Contents
<a name="API_UpdateCapabilityConfiguration_Contents"></a>

 ** ack **   <a name="AmazonEKS-Type-UpdateCapabilityConfiguration-ack"></a>
Configuration updates specific to ACK (AWS Controllers for Kubernetes) capabilities.
Type: [UpdateAckConfig](API_UpdateAckConfig.md) object
Required: No

 ** argoCd **   <a name="AmazonEKS-Type-UpdateCapabilityConfiguration-argoCd"></a>
Configuration updates specific to Argo CD capabilities.
Type: [UpdateArgoCdConfig](API_UpdateArgoCdConfig.md) object
Required: No

## See Also
<a name="API_UpdateCapabilityConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/UpdateCapabilityConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/UpdateCapabilityConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/UpdateCapabilityConfiguration)

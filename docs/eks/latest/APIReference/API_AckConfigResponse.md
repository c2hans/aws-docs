---
source_url: https://docs.aws.amazon.com/eks/latest/APIReference/API_AckConfigResponse.html
---

# AckConfigResponse
<a name="API_AckConfigResponse"></a>

The response object containing configuration details for an ACK (AWS Controllers for Kubernetes) capability.

## Contents
<a name="API_AckConfigResponse_Contents"></a>

 ** disabledServices **   <a name="AmazonEKS-Type-AckConfigResponse-disabledServices"></a>
The list of ACK service names whose controllers are turned off for this capability. Existing custom resource definitions remain installed, and resources of a disabled service aren't reconciled until the service is re-enabled.
Type: Array of strings
Array Members: Maximum number of 200 items.
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `^[a-z][a-z0-9]*$`
Required: No

 ** enableCrossNamespace **   <a name="AmazonEKS-Type-AckConfigResponse-enableCrossNamespace"></a>
Indicates whether ACK controllers resolve resource references to resources in a different Kubernetes namespace. This value reflects the setting that's in effect, and is `false` if you never specified a value. Capabilities that were using cross-namespace references before this setting became available have this value set to `true`, so their behavior is unchanged.
Type: Boolean
Required: No

## See Also
<a name="API_AckConfigResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/AckConfigResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/AckConfigResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/AckConfigResponse)

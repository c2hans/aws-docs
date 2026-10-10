---
source_url: https://docs.aws.amazon.com/eks/latest/APIReference/API_UpdateAckConfig.html
---

# UpdateAckConfig
<a name="API_UpdateAckConfig"></a>

Configuration updates for an ACK (AWS Controllers for Kubernetes) capability. You only need to specify the fields that you want to update.

## Contents
<a name="API_UpdateAckConfig_Contents"></a>

 ** disabledServices **   <a name="AmazonEKS-Type-UpdateAckConfig-disabledServices"></a>
An updated list of ACK service names whose controllers are turned off for this capability. This list replaces the previous list instead of merging with it, so specify the complete set of services that you want turned off. If you omit this field, the previous list is unchanged. To turn all services back on, specify an empty list.
Type: Array of strings
Array Members: Maximum number of 200 items.
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `^[a-z][a-z0-9]*$`
Required: No

 ** enableCrossNamespace **   <a name="AmazonEKS-Type-UpdateAckConfig-enableCrossNamespace"></a>
Specifies whether ACK controllers resolve resource references to resources in a different Kubernetes namespace. Set this value to `false` to require references to remain within the same namespace, or `true` to allow cross-namespace references. If you omit this field, the current value is unchanged.
Type: Boolean
Required: No

## See Also
<a name="API_UpdateAckConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/UpdateAckConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/UpdateAckConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/UpdateAckConfig)

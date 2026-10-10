---
source_url: https://docs.aws.amazon.com/eks/latest/APIReference/API_AckConfigRequest.html
---

# AckConfigRequest
<a name="API_AckConfigRequest"></a>

Configuration settings for an ACK (AWS Controllers for Kubernetes) capability. This includes whether controllers can resolve cross-namespace resource references and which ACK service controllers are disabled.

## Contents
<a name="API_AckConfigRequest_Contents"></a>

 ** disabledServices **   <a name="AmazonEKS-Type-AckConfigRequest-disabledServices"></a>
A list of ACK service names whose controllers are turned off for this capability, for example `s3`, `ec2`, and `iam`. Resources of a disabled service aren't reconciled until you re-enable the service. To keep all services enabled, omit this field or specify an empty list. An unrecognized service name is accepted and stored but turns nothing off, and `DescribeCapability` returns the list exactly as you supplied it. For more information, see [ACK capability configuration options](https://docs.aws.amazon.com/eks/latest/userguide/create-ack-capability.html#ack-configuration-options) in the *Amazon EKS User Guide*.
Type: Array of strings
Array Members: Maximum number of 200 items.
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `^[a-z][a-z0-9]*$`
Required: No

 ** enableCrossNamespace **   <a name="AmazonEKS-Type-AckConfigRequest-enableCrossNamespace"></a>
Specifies whether ACK controllers resolve resource references to resources in a different Kubernetes namespace. Set this value to `true` to allow references to resolve to resources in another namespace. If you don't specify this value, or you omit the `ack` configuration entirely, the capability is created with this value set to `false` and references must remain within the same namespace.
Type: Boolean
Required: No

## See Also
<a name="API_AckConfigRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/AckConfigRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/AckConfigRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/AckConfigRequest)

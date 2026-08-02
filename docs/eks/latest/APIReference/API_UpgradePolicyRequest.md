---
source_url: https://docs.aws.amazon.com/eks/latest/APIReference/API_UpgradePolicyRequest.html
---

# UpgradePolicyRequest
<a name="API_UpgradePolicyRequest"></a>

The support policy to use for the cluster. Extended support allows you to remain on specific Kubernetes versions for longer. Clusters in extended support have higher costs. The default value is `EXTENDED`. Use `STANDARD` to disable extended support.

 [Learn more about EKS Extended Support in the *Amazon EKS User Guide*.](https://docs.aws.amazon.com/eks/latest/userguide/extended-support-control.html)

## Contents
<a name="API_UpgradePolicyRequest_Contents"></a>

 ** supportType **   <a name="AmazonEKS-Type-UpgradePolicyRequest-supportType"></a>
If the cluster is set to `EXTENDED`, it will enter extended support at the end of standard support. If the cluster is set to `STANDARD`, it will be automatically upgraded at the end of standard support.
 [Learn more about EKS Extended Support in the *Amazon EKS User Guide*.](https://docs.aws.amazon.com/eks/latest/userguide/extended-support-control.html)
Type: String
Valid Values: `STANDARD | EXTENDED`
Required: No

## See Also
<a name="API_UpgradePolicyRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/UpgradePolicyRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/UpgradePolicyRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/UpgradePolicyRequest)

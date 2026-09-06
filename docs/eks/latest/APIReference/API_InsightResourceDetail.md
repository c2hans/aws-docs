---
source_url: https://docs.aws.amazon.com/eks/latest/APIReference/API_InsightResourceDetail.html
---

# InsightResourceDetail
<a name="API_InsightResourceDetail"></a>

Returns information about the resource being evaluated.

## Contents
<a name="API_InsightResourceDetail_Contents"></a>

 ** arn **   <a name="AmazonEKS-Type-InsightResourceDetail-arn"></a>
The Amazon Resource Name (ARN) if applicable.
Type: String
Required: No

 ** insightStatus **   <a name="AmazonEKS-Type-InsightResourceDetail-insightStatus"></a>
An object containing more detail on the status of the insight resource.
Type: [InsightStatus](API_InsightStatus.md) object
Required: No

 ** kubernetesResourceUri **   <a name="AmazonEKS-Type-InsightResourceDetail-kubernetesResourceUri"></a>
The Kubernetes resource URI if applicable.
Type: String
Required: No

## See Also
<a name="API_InsightResourceDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/InsightResourceDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/InsightResourceDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/InsightResourceDetail)

---
source_url: https://docs.aws.amazon.com/eks/latest/APIReference/API_Cancellation.html
---

# Cancellation
<a name="API_Cancellation"></a>

Contains information about the latest cancellation of an update to an Amazon EKS cluster.

## Contents
<a name="API_Cancellation_Contents"></a>

 ** reason **   <a name="AmazonEKS-Type-Cancellation-reason"></a>
A message providing additional details about the cancellation, such as the reason for the cancellation or failure details.
Type: String
Required: No

 ** status **   <a name="AmazonEKS-Type-Cancellation-status"></a>
The current status of the cancellation. Valid values are `InProgress`, `Failed`, and `Successful`.
Type: String
Valid Values: `InProgress | Failed | Successful`
Required: No

## See Also
<a name="API_Cancellation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/Cancellation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/Cancellation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/Cancellation)

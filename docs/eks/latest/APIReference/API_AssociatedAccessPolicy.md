---
source_url: https://docs.aws.amazon.com/eks/latest/APIReference/API_AssociatedAccessPolicy.html
---

# AssociatedAccessPolicy
<a name="API_AssociatedAccessPolicy"></a>

An access policy association.

## Contents
<a name="API_AssociatedAccessPolicy_Contents"></a>

 ** accessScope **   <a name="AmazonEKS-Type-AssociatedAccessPolicy-accessScope"></a>
The scope of the access policy.
Type: [AccessScope](API_AccessScope.md) object
Required: No

 ** associatedAt **   <a name="AmazonEKS-Type-AssociatedAccessPolicy-associatedAt"></a>
The date and time the `AccessPolicy` was associated with an `AccessEntry`.
Type: Timestamp
Required: No

 ** modifiedAt **   <a name="AmazonEKS-Type-AssociatedAccessPolicy-modifiedAt"></a>
The Unix epoch timestamp for the last modification to the object.
Type: Timestamp
Required: No

 ** policyArn **   <a name="AmazonEKS-Type-AssociatedAccessPolicy-policyArn"></a>
The ARN of the `AccessPolicy`.
Type: String
Required: No

## See Also
<a name="API_AssociatedAccessPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/AssociatedAccessPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/AssociatedAccessPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/AssociatedAccessPolicy)

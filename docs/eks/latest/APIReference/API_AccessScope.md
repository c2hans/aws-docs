---
source_url: https://docs.aws.amazon.com/eks/latest/APIReference/API_AccessScope.html
---

# AccessScope
<a name="API_AccessScope"></a>

The scope of an `AccessPolicy` that's associated to an `AccessEntry`.

## Contents
<a name="API_AccessScope_Contents"></a>

 ** namespaces **   <a name="AmazonEKS-Type-AccessScope-namespaces"></a>
A Kubernetes `namespace` that an access policy is scoped to. A value is required if you specified `namespace` for `Type`.
Type: Array of strings
Required: No

 ** type **   <a name="AmazonEKS-Type-AccessScope-type"></a>
The scope type of an access policy.
Type: String
Valid Values: `cluster | namespace`
Required: No

## See Also
<a name="API_AccessScope_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/AccessScope)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/AccessScope)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/AccessScope)

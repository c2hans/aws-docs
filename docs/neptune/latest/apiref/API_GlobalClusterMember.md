---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_GlobalClusterMember.html
---

# GlobalClusterMember
<a name="API_GlobalClusterMember"></a>

 A data structure with information about any primary and secondary clusters associated with an Neptune global database.

## Contents
<a name="API_GlobalClusterMember_Contents"></a>

 ** DBClusterArn **
 The Amazon Resource Name (ARN) for each Neptune cluster.
Type: String
Required: No

 ** IsWriter **
 Specifies whether the Neptune cluster is the primary cluster (that is, has read-write capability) for the Neptune global database with which it is associated.
Type: Boolean
Required: No

 ** Readers.member.N **
 The Amazon Resource Name (ARN) for each read-only secondary cluster associated with the Neptune global database.
Type: Array of strings
Required: No

## See Also
<a name="API_GlobalClusterMember_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/GlobalClusterMember)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/GlobalClusterMember)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/GlobalClusterMember)

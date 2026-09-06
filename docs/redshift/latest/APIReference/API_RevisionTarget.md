---
source_url: https://docs.aws.amazon.com/redshift/latest/APIReference/API_RevisionTarget.html
---

# RevisionTarget
<a name="API_RevisionTarget"></a>

Describes a `RevisionTarget`.

## Contents
<a name="API_RevisionTarget_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DatabaseRevision **
A unique string that identifies the version to update the cluster to. You can use this value in [ModifyClusterDbRevision](API_ModifyClusterDbRevision.md).
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** DatabaseRevisionReleaseDate **
The date on which the database revision was released.
Type: Timestamp
Required: No

 ** Description **
A string that describes the changes and features that will be applied to the cluster when it is updated to the corresponding [ClusterDbRevision](API_ClusterDbRevision.md).
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

## See Also
<a name="API_RevisionTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/RevisionTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/RevisionTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/RevisionTarget)

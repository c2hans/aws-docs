---
source_url: https://docs.aws.amazon.com/redshift/latest/APIReference/API_SnapshotCopyGrant.html
---

# SnapshotCopyGrant
<a name="API_SnapshotCopyGrant"></a>

The snapshot copy grant that grants Amazon Redshift permission to encrypt copied snapshots with the specified encrypted symmetric key from AWS KMS in the destination region.

 For more information about managing snapshot copy grants, go to [Amazon Redshift Database Encryption](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-db-encryption.html) in the *Amazon Redshift Cluster Management Guide*.

## Contents
<a name="API_SnapshotCopyGrant_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** KmsKeyId **
The unique identifier of the encrypted symmetric key in AWS KMS to which Amazon Redshift is granted permission.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** SnapshotCopyGrantName **
The name of the snapshot copy grant.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** Tags.Tag.N **
A list of tag instances.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_SnapshotCopyGrant_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/SnapshotCopyGrant)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/SnapshotCopyGrant)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/SnapshotCopyGrant)

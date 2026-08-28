---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_CopyDBClusterSnapshot.html
---

# CopyDBClusterSnapshot
<a name="API_CopyDBClusterSnapshot"></a>

Copies a snapshot of a DB cluster.

To copy a DB cluster snapshot from a shared manual DB cluster snapshot, `SourceDBClusterSnapshotIdentifier` must be the Amazon Resource Name (ARN) of the shared DB cluster snapshot.

## Request Parameters
<a name="API_CopyDBClusterSnapshot_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** CopyTags **
True to copy all tags from the source DB cluster snapshot to the target DB cluster snapshot, and otherwise false. The default is false.
Type: Boolean
Required: No

 ** KmsKeyId **
The Amazon Amazon KMS key ID for an encrypted DB cluster snapshot. The KMS key ID is the Amazon Resource Name (ARN), KMS key identifier, or the KMS key alias for the KMS encryption key.
If you copy an encrypted DB cluster snapshot from your Amazon account, you can specify a value for `KmsKeyId` to encrypt the copy with a new KMS encryption key. If you don't specify a value for `KmsKeyId`, then the copy of the DB cluster snapshot is encrypted with the same KMS key as the source DB cluster snapshot.
If you copy an encrypted DB cluster snapshot that is shared from another Amazon account, then you must specify a value for `KmsKeyId`.
 KMS encryption keys are specific to the Amazon Region that they are created in, and you can't use encryption keys from one Amazon Region in another Amazon Region.
You cannot encrypt an unencrypted DB cluster snapshot when you copy it. If you try to copy an unencrypted DB cluster snapshot and specify a value for the KmsKeyId parameter, an error is returned.
Type: String
Required: No

 ** PreSignedUrl **
Not currently supported.
Type: String
Required: No

 ** SourceDBClusterSnapshotIdentifier **
The identifier of the DB cluster snapshot to copy. This parameter is not case-sensitive. If the source DB cluster snapshot is in a different region or owned by another account, specify the snapshot ARN.
Constraints:
+ Must specify a valid system snapshot in the "available" state.
+ Specify a valid DB snapshot identifier.
Example: `my-cluster-snapshot1`
Type: String
Required: Yes

 **Tags.Tag.N**
The tags to assign to the new DB cluster snapshot copy.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** TargetDBClusterSnapshotIdentifier **
The identifier of the new DB cluster snapshot to create from the source DB cluster snapshot. This parameter is not case-sensitive.
Constraints:
+ Must contain from 1 to 63 letters, numbers, or hyphens.
+ First character must be a letter.
+ Cannot end with a hyphen or contain two consecutive hyphens.
Example: `my-cluster-snapshot2`
Type: String
Required: Yes

## Response Elements
<a name="API_CopyDBClusterSnapshot_ResponseElements"></a>

The following element is returned by the service.

 ** DBClusterSnapshot **
Contains the details for an Amazon Neptune DB cluster snapshot
This data type is used as a response element in the [DescribeDBClusterSnapshots](API_DescribeDBClusterSnapshots.md) action.
Type: [DBClusterSnapshot](API_DBClusterSnapshot.md) object

## Errors
<a name="API_CopyDBClusterSnapshot_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBClusterSnapshotAlreadyExistsFault **
User already has a DB cluster snapshot with the given identifier.
HTTP Status Code: 400

 ** DBClusterSnapshotNotFoundFault **
 *DBClusterSnapshotIdentifier* does not refer to an existing DB cluster snapshot.
HTTP Status Code: 404

 ** InvalidDBClusterSnapshotStateFault **
The supplied value is not a valid DB cluster snapshot state.
HTTP Status Code: 400

 ** InvalidDBClusterStateFault **
The DB cluster is not in a valid state.
HTTP Status Code: 400

 ** KMSKeyNotAccessibleFault **
Error accessing KMS key.
HTTP Status Code: 400

 ** SnapshotQuotaExceeded **
Request would result in user exceeding the allowed number of DB snapshots.
HTTP Status Code: 400

## See Also
<a name="API_CopyDBClusterSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-2014-10-31/CopyDBClusterSnapshot)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-2014-10-31/CopyDBClusterSnapshot)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/CopyDBClusterSnapshot)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-2014-10-31/CopyDBClusterSnapshot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/CopyDBClusterSnapshot)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-2014-10-31/CopyDBClusterSnapshot)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-2014-10-31/CopyDBClusterSnapshot)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-2014-10-31/CopyDBClusterSnapshot)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/CopyDBClusterSnapshot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/CopyDBClusterSnapshot)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

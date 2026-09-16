---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_DeleteDBClusterSnapshot.html
---

# DeleteDBClusterSnapshot
<a name="API_DeleteDBClusterSnapshot"></a>

Deletes a DB cluster snapshot. If the snapshot is being copied, the copy operation is terminated.

**Note**
The DB cluster snapshot must be in the `available` state to be deleted.

## Request Parameters
<a name="API_DeleteDBClusterSnapshot_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBClusterSnapshotIdentifier **
The identifier of the DB cluster snapshot to delete.
Constraints: Must be the name of an existing DB cluster snapshot in the `available` state.
Type: String
Required: Yes

## Response Elements
<a name="API_DeleteDBClusterSnapshot_ResponseElements"></a>

The following element is returned by the service.

 ** DBClusterSnapshot **
Contains the details for an Amazon Neptune DB cluster snapshot
This data type is used as a response element in the [DescribeDBClusterSnapshots](API_DescribeDBClusterSnapshots.md) action.
Type: [DBClusterSnapshot](API_DBClusterSnapshot.md) object

## Errors
<a name="API_DeleteDBClusterSnapshot_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBClusterSnapshotNotFoundFault **
 *DBClusterSnapshotIdentifier* does not refer to an existing DB cluster snapshot.
HTTP Status Code: 404

 ** InvalidDBClusterSnapshotStateFault **
The supplied value is not a valid DB cluster snapshot state.
HTTP Status Code: 400

## See Also
<a name="API_DeleteDBClusterSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-2014-10-31/DeleteDBClusterSnapshot)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-2014-10-31/DeleteDBClusterSnapshot)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/DeleteDBClusterSnapshot)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-2014-10-31/DeleteDBClusterSnapshot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/DeleteDBClusterSnapshot)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-2014-10-31/DeleteDBClusterSnapshot)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-2014-10-31/DeleteDBClusterSnapshot)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-2014-10-31/DeleteDBClusterSnapshot)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/DeleteDBClusterSnapshot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/DeleteDBClusterSnapshot)

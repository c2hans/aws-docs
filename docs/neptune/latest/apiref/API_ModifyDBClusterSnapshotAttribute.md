---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_ModifyDBClusterSnapshotAttribute.html
---

# ModifyDBClusterSnapshotAttribute
<a name="API_ModifyDBClusterSnapshotAttribute"></a>

Adds an attribute and values to, or removes an attribute and values from, a manual DB cluster snapshot.

To share a manual DB cluster snapshot with other Amazon accounts, specify `restore` as the `AttributeName` and use the `ValuesToAdd` parameter to add a list of IDs of the Amazon accounts that are authorized to restore the manual DB cluster snapshot. Use the value `all` to make the manual DB cluster snapshot public, which means that it can be copied or restored by all Amazon accounts. Do not add the `all` value for any manual DB cluster snapshots that contain private information that you don't want available to all Amazon accounts. If a manual DB cluster snapshot is encrypted, it can be shared, but only by specifying a list of authorized Amazon account IDs for the `ValuesToAdd` parameter. You can't use `all` as a value for that parameter in this case.

To view which Amazon accounts have access to copy or restore a manual DB cluster snapshot, or whether a manual DB cluster snapshot public or private, use the [DescribeDBClusterSnapshotAttributes](API_DescribeDBClusterSnapshotAttributes.md) API action.

## Request Parameters
<a name="API_ModifyDBClusterSnapshotAttribute_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** AttributeName **
The name of the DB cluster snapshot attribute to modify.
To manage authorization for other Amazon accounts to copy or restore a manual DB cluster snapshot, set this value to `restore`.
Type: String
Required: Yes

 ** DBClusterSnapshotIdentifier **
The identifier for the DB cluster snapshot to modify the attributes for.
Type: String
Required: Yes

 **ValuesToAdd.AttributeValue.N**
A list of DB cluster snapshot attributes to add to the attribute specified by `AttributeName`.
To authorize other Amazon accounts to copy or restore a manual DB cluster snapshot, set this list to include one or more Amazon account IDs, or `all` to make the manual DB cluster snapshot restorable by any Amazon account. Do not add the `all` value for any manual DB cluster snapshots that contain private information that you don't want available to all Amazon accounts.
Type: Array of strings
Required: No

 **ValuesToRemove.AttributeValue.N**
A list of DB cluster snapshot attributes to remove from the attribute specified by `AttributeName`.
To remove authorization for other Amazon accounts to copy or restore a manual DB cluster snapshot, set this list to include one or more Amazon account identifiers, or `all` to remove authorization for any Amazon account to copy or restore the DB cluster snapshot. If you specify `all`, an Amazon account whose account ID is explicitly added to the `restore` attribute can still copy or restore a manual DB cluster snapshot.
Type: Array of strings
Required: No

## Response Elements
<a name="API_ModifyDBClusterSnapshotAttribute_ResponseElements"></a>

The following element is returned by the service.

 ** DBClusterSnapshotAttributesResult **
Contains the results of a successful call to the [DescribeDBClusterSnapshotAttributes](API_DescribeDBClusterSnapshotAttributes.md) API action.
Manual DB cluster snapshot attributes are used to authorize other Amazon accounts to copy or restore a manual DB cluster snapshot. For more information, see the [ModifyDBClusterSnapshotAttribute](#API_ModifyDBClusterSnapshotAttribute) API action.
Type: [DBClusterSnapshotAttributesResult](API_DBClusterSnapshotAttributesResult.md) object

## Errors
<a name="API_ModifyDBClusterSnapshotAttribute_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBClusterSnapshotNotFoundFault **
 *DBClusterSnapshotIdentifier* does not refer to an existing DB cluster snapshot.
HTTP Status Code: 404

 ** InvalidDBClusterSnapshotStateFault **
The supplied value is not a valid DB cluster snapshot state.
HTTP Status Code: 400

 ** SharedSnapshotQuotaExceeded **
You have exceeded the maximum number of accounts that you can share a manual DB snapshot with.
HTTP Status Code: 400

## See Also
<a name="API_ModifyDBClusterSnapshotAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-2014-10-31/ModifyDBClusterSnapshotAttribute)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-2014-10-31/ModifyDBClusterSnapshotAttribute)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/ModifyDBClusterSnapshotAttribute)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-2014-10-31/ModifyDBClusterSnapshotAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/ModifyDBClusterSnapshotAttribute)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-2014-10-31/ModifyDBClusterSnapshotAttribute)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-2014-10-31/ModifyDBClusterSnapshotAttribute)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-2014-10-31/ModifyDBClusterSnapshotAttribute)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/ModifyDBClusterSnapshotAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/ModifyDBClusterSnapshotAttribute)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

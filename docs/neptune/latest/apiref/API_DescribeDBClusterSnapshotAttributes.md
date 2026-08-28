---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_DescribeDBClusterSnapshotAttributes.html
---

# DescribeDBClusterSnapshotAttributes
<a name="API_DescribeDBClusterSnapshotAttributes"></a>

Returns a list of DB cluster snapshot attribute names and values for a manual DB cluster snapshot.

When sharing snapshots with other Amazon accounts, `DescribeDBClusterSnapshotAttributes` returns the `restore` attribute and a list of IDs for the Amazon accounts that are authorized to copy or restore the manual DB cluster snapshot. If `all` is included in the list of values for the `restore` attribute, then the manual DB cluster snapshot is public and can be copied or restored by all Amazon accounts.

To add or remove access for an Amazon account to copy or restore a manual DB cluster snapshot, or to make the manual DB cluster snapshot public or private, use the [ModifyDBClusterSnapshotAttribute](API_ModifyDBClusterSnapshotAttribute.md) API action.

## Request Parameters
<a name="API_DescribeDBClusterSnapshotAttributes_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBClusterSnapshotIdentifier **
The identifier for the DB cluster snapshot to describe the attributes for.
Type: String
Required: Yes

## Response Elements
<a name="API_DescribeDBClusterSnapshotAttributes_ResponseElements"></a>

The following element is returned by the service.

 ** DBClusterSnapshotAttributesResult **
Contains the results of a successful call to the [DescribeDBClusterSnapshotAttributes](#API_DescribeDBClusterSnapshotAttributes) API action.
Manual DB cluster snapshot attributes are used to authorize other Amazon accounts to copy or restore a manual DB cluster snapshot. For more information, see the [ModifyDBClusterSnapshotAttribute](API_ModifyDBClusterSnapshotAttribute.md) API action.
Type: [DBClusterSnapshotAttributesResult](API_DBClusterSnapshotAttributesResult.md) object

## Errors
<a name="API_DescribeDBClusterSnapshotAttributes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBClusterSnapshotNotFoundFault **
 *DBClusterSnapshotIdentifier* does not refer to an existing DB cluster snapshot.
HTTP Status Code: 404

## See Also
<a name="API_DescribeDBClusterSnapshotAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-2014-10-31/DescribeDBClusterSnapshotAttributes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-2014-10-31/DescribeDBClusterSnapshotAttributes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/DescribeDBClusterSnapshotAttributes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-2014-10-31/DescribeDBClusterSnapshotAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/DescribeDBClusterSnapshotAttributes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-2014-10-31/DescribeDBClusterSnapshotAttributes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-2014-10-31/DescribeDBClusterSnapshotAttributes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-2014-10-31/DescribeDBClusterSnapshotAttributes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/DescribeDBClusterSnapshotAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/DescribeDBClusterSnapshotAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

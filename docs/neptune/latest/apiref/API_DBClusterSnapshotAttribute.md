---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_DBClusterSnapshotAttribute.html
---

# DBClusterSnapshotAttribute
<a name="API_DBClusterSnapshotAttribute"></a>

Contains the name and values of a manual DB cluster snapshot attribute.

Manual DB cluster snapshot attributes are used to authorize other Amazon accounts to restore a manual DB cluster snapshot. For more information, see the [ModifyDBClusterSnapshotAttribute](API_ModifyDBClusterSnapshotAttribute.md) API action.

## Contents
<a name="API_DBClusterSnapshotAttribute_Contents"></a>

 ** AttributeName **
The name of the manual DB cluster snapshot attribute.
The attribute named `restore` refers to the list of Amazon accounts that have permission to copy or restore the manual DB cluster snapshot. For more information, see the [ModifyDBClusterSnapshotAttribute](API_ModifyDBClusterSnapshotAttribute.md) API action.
Type: String
Required: No

 ** AttributeValues.AttributeValue.N **
The value(s) for the manual DB cluster snapshot attribute.
If the `AttributeName` field is set to `restore`, then this element returns a list of IDs of the Amazon accounts that are authorized to copy or restore the manual DB cluster snapshot. If a value of `all` is in the list, then the manual DB cluster snapshot is public and available for any Amazon account to copy or restore.
Type: Array of strings
Required: No

## See Also
<a name="API_DBClusterSnapshotAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/DBClusterSnapshotAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/DBClusterSnapshotAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/DBClusterSnapshotAttribute)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

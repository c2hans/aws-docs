---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DBSnapshotAttributesResult.html
---

# DBSnapshotAttributesResult
<a name="API_DBSnapshotAttributesResult"></a>

Contains the results of a successful call to the `DescribeDBSnapshotAttributes` API action.

Manual DB snapshot attributes are used to authorize other AWS accounts to copy or restore a manual DB snapshot. For more information, see the `ModifyDBSnapshotAttribute` API action.

## Contents
<a name="API_DBSnapshotAttributesResult_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DBSnapshotAttributes.DBSnapshotAttribute.N **
The list of attributes and values for the manual DB snapshot.
Type: Array of [DBSnapshotAttribute](API_DBSnapshotAttribute.md) objects
Required: No

 ** DBSnapshotIdentifier **
The identifier of the manual DB snapshot that the attributes apply to.
Type: String
Required: No

## See Also
<a name="API_DBSnapshotAttributesResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DBSnapshotAttributesResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DBSnapshotAttributesResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DBSnapshotAttributesResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Relational Database Service (RDS). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

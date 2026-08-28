---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DBSnapshotAttribute.html
---

# DBSnapshotAttribute
<a name="API_DBSnapshotAttribute"></a>

Contains the name and values of a manual DB snapshot attribute

Manual DB snapshot attributes are used to authorize other AWS accounts to restore a manual DB snapshot. For more information, see the `ModifyDBSnapshotAttribute` API.

## Contents
<a name="API_DBSnapshotAttribute_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AttributeName **
The name of the manual DB snapshot attribute.
The attribute named `restore` refers to the list of AWS accounts that have permission to copy or restore the manual DB cluster snapshot. For more information, see the `ModifyDBSnapshotAttribute` API action.
Type: String
Required: No

 ** AttributeValues.AttributeValue.N **
The value or values for the manual DB snapshot attribute.
If the `AttributeName` field is set to `restore`, then this element returns a list of IDs of the AWS accounts that are authorized to copy or restore the manual DB snapshot. If a value of `all` is in the list, then the manual DB snapshot is public and available for any AWS account to copy or restore.
Type: Array of strings
Required: No

## See Also
<a name="API_DBSnapshotAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DBSnapshotAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DBSnapshotAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DBSnapshotAttribute)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Relational Database Service (RDS). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_RdsDbClusterSnapshotAttributeValue.html
---

# RdsDbClusterSnapshotAttributeValue
<a name="API_RdsDbClusterSnapshotAttributeValue"></a>

The values for a manual Amazon RDS DB cluster snapshot attribute.

## Contents
<a name="API_RdsDbClusterSnapshotAttributeValue_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** accountIds **   <a name="accessanalyzer-Type-RdsDbClusterSnapshotAttributeValue-accountIds"></a>
The AWS account IDs that have access to the manual Amazon RDS DB cluster snapshot. If the value `all` is specified, then the Amazon RDS DB cluster snapshot is public and can be copied or restored by all AWS accounts.
+ If the configuration is for an existing Amazon RDS DB cluster snapshot and you do not specify the `accountIds` in `RdsDbClusterSnapshotAttributeValue`, then the access preview uses the existing shared `accountIds` for the snapshot.
+ If the access preview is for a new resource and you do not specify the specify the `accountIds` in `RdsDbClusterSnapshotAttributeValue`, then the access preview considers the snapshot without any attributes.
+ To propose deletion of existing shared `accountIds`, you can specify an empty list for `accountIds` in the `RdsDbClusterSnapshotAttributeValue`.
Type: Array of strings
Required: No

## See Also
<a name="API_RdsDbClusterSnapshotAttributeValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/RdsDbClusterSnapshotAttributeValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/RdsDbClusterSnapshotAttributeValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/RdsDbClusterSnapshotAttributeValue)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Access Analyzer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query access-analyzer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

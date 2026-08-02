---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_RdsDbSnapshotAttributeValue.html
---

# RdsDbSnapshotAttributeValue
<a name="API_RdsDbSnapshotAttributeValue"></a>

The name and values of a manual Amazon RDS DB snapshot attribute. Manual DB snapshot attributes are used to authorize other AWS accounts to restore a manual DB snapshot.

## Contents
<a name="API_RdsDbSnapshotAttributeValue_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** accountIds **   <a name="accessanalyzer-Type-RdsDbSnapshotAttributeValue-accountIds"></a>
The AWS account IDs that have access to the manual Amazon RDS DB snapshot. If the value `all` is specified, then the Amazon RDS DB snapshot is public and can be copied or restored by all AWS accounts.
+ If the configuration is for an existing Amazon RDS DB snapshot and you do not specify the `accountIds` in `RdsDbSnapshotAttributeValue`, then the access preview uses the existing shared `accountIds` for the snapshot.
+ If the access preview is for a new resource and you do not specify the specify the `accountIds` in `RdsDbSnapshotAttributeValue`, then the access preview considers the snapshot without any attributes.
+ To propose deletion of an existing shared `accountIds`, you can specify an empty list for `accountIds` in the `RdsDbSnapshotAttributeValue`.
Type: Array of strings
Required: No

## See Also
<a name="API_RdsDbSnapshotAttributeValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/RdsDbSnapshotAttributeValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/RdsDbSnapshotAttributeValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/RdsDbSnapshotAttributeValue)

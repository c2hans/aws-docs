---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_DBClusterMember.html
---

# DBClusterMember
<a name="API_DBClusterMember"></a>

Contains information about an instance that is part of a DB cluster.

## Contents
<a name="API_DBClusterMember_Contents"></a>

 ** DBClusterParameterGroupStatus **
Specifies the status of the DB cluster parameter group for this member of the DB cluster.
Type: String
Required: No

 ** DBInstanceIdentifier **
Specifies the instance identifier for this member of the DB cluster.
Type: String
Required: No

 ** IsClusterWriter **
Value that is `true` if the cluster member is the primary instance for the DB cluster and `false` otherwise.
Type: Boolean
Required: No

 ** PromotionTier **
A value that specifies the order in which a Read Replica is promoted to the primary instance after a failure of the existing primary instance.
Type: Integer
Required: No

## See Also
<a name="API_DBClusterMember_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/DBClusterMember)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/DBClusterMember)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/DBClusterMember)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

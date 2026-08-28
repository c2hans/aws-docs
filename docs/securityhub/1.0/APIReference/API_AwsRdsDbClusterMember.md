---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsRdsDbClusterMember.html
---

# AwsRdsDbClusterMember
<a name="API_AwsRdsDbClusterMember"></a>

Information about an instance in the DB cluster.

## Contents
<a name="API_AwsRdsDbClusterMember_Contents"></a>

 ** DbClusterParameterGroupStatus **   <a name="securityhub-Type-AwsRdsDbClusterMember-DbClusterParameterGroupStatus"></a>
The status of the DB cluster parameter group for this member of the DB cluster.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DbInstanceIdentifier **   <a name="securityhub-Type-AwsRdsDbClusterMember-DbInstanceIdentifier"></a>
The instance identifier for this member of the DB cluster.
Type: String
Pattern: `.*\S.*`
Required: No

 ** IsClusterWriter **   <a name="securityhub-Type-AwsRdsDbClusterMember-IsClusterWriter"></a>
Whether the cluster member is the primary instance for the DB cluster.
Type: Boolean
Required: No

 ** PromotionTier **   <a name="securityhub-Type-AwsRdsDbClusterMember-PromotionTier"></a>
Specifies the order in which an Aurora replica is promoted to the primary instance when the existing primary instance fails.
Type: Integer
Required: No

## See Also
<a name="API_AwsRdsDbClusterMember_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsRdsDbClusterMember)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsRdsDbClusterMember)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsRdsDbClusterMember)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

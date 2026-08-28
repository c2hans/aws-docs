---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_ReshardingConfiguration.html
---

# ReshardingConfiguration
<a name="API_ReshardingConfiguration"></a>

A list of `PreferredAvailabilityZones` objects that specifies the configuration of a node group in the resharded cluster.

## Contents
<a name="API_ReshardingConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** NodeGroupId **
Either the ElastiCache supplied 4-digit id or a user supplied id for the node group these configuration values apply to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4.
Pattern: `\d+`
Required: No

 ** PreferredAvailabilityZones.AvailabilityZone.N **
A list of preferred availability zones for the nodes in this cluster.
Type: Array of strings
Required: No

## See Also
<a name="API_ReshardingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/ReshardingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/ReshardingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/ReshardingConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

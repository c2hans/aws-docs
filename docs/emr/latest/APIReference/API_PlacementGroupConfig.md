---
source_url: https://docs.aws.amazon.com/emr/latest/APIReference/API_PlacementGroupConfig.html
---

# PlacementGroupConfig
<a name="API_PlacementGroupConfig"></a>

Placement group configuration for an Amazon EMR cluster. The configuration specifies the placement strategy that can be applied to instance roles during cluster creation.

To use this configuration, consider attaching managed policy AmazonElasticMapReducePlacementGroupPolicy to the Amazon EMR role.

## Contents
<a name="API_PlacementGroupConfig_Contents"></a>

 ** InstanceRole **   <a name="EMR-Type-PlacementGroupConfig-InstanceRole"></a>
Role of the instance in the cluster.
Starting with Amazon EMR release 5.23.0, the only supported instance role is `MASTER`.
Type: String
Valid Values: `MASTER | CORE | TASK`
Required: Yes

 ** PlacementStrategy **   <a name="EMR-Type-PlacementGroupConfig-PlacementStrategy"></a>
Amazon EC2 Placement Group strategy associated with instance role.
Starting with Amazon EMR release 5.23.0, the only supported placement strategy is `SPREAD` for the `MASTER` instance role.
Type: String
Valid Values: `SPREAD | PARTITION | CLUSTER | NONE`
Required: No

## See Also
<a name="API_PlacementGroupConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/PlacementGroupConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/PlacementGroupConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/PlacementGroupConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

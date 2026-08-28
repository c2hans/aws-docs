---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-msk-replicator-amazonmskcluster.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::Replicator AmazonMskCluster
<a name="aws-properties-msk-replicator-amazonmskcluster"></a>

Details of an Amazon MSK Cluster.

## Syntax
<a name="aws-properties-msk-replicator-amazonmskcluster-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-msk-replicator-amazonmskcluster-syntax.json"></a>

```
{
  "[MskClusterArn](#cfn-msk-replicator-amazonmskcluster-mskclusterarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-msk-replicator-amazonmskcluster-syntax.yaml"></a>

```
  [MskClusterArn](#cfn-msk-replicator-amazonmskcluster-mskclusterarn): {{String}}
```

## Properties
<a name="aws-properties-msk-replicator-amazonmskcluster-properties"></a>

`MskClusterArn`  <a name="cfn-msk-replicator-amazonmskcluster-mskclusterarn"></a>
The Amazon Resource Name (ARN) of an Amazon MSK cluster.
*Required*: Yes
*Type*: String
*Pattern*: `arn:(aws|aws-us-gov|aws-cn):kafka:.*`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

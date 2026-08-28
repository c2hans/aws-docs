---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-redshift-scheduledaction-pauseclustermessage.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Redshift::ScheduledAction PauseClusterMessage
<a name="aws-properties-redshift-scheduledaction-pauseclustermessage"></a>

Describes a pause cluster operation. For example, a scheduled action to run the `PauseCluster` API operation.

## Syntax
<a name="aws-properties-redshift-scheduledaction-pauseclustermessage-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-redshift-scheduledaction-pauseclustermessage-syntax.json"></a>

```
{
  "[ClusterIdentifier](#cfn-redshift-scheduledaction-pauseclustermessage-clusteridentifier)" : {{String}}
}
```

### YAML
<a name="aws-properties-redshift-scheduledaction-pauseclustermessage-syntax.yaml"></a>

```
  [ClusterIdentifier](#cfn-redshift-scheduledaction-pauseclustermessage-clusteridentifier): {{String}}
```

## Properties
<a name="aws-properties-redshift-scheduledaction-pauseclustermessage-properties"></a>

`ClusterIdentifier`  <a name="cfn-redshift-scheduledaction-pauseclustermessage-clusteridentifier"></a>
The identifier of the cluster to be paused.
*Required*: Yes
*Type*: String
*Maximum*: `2147483647`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

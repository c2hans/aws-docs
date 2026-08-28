---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-redshift-scheduledaction-resizeclustermessage.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Redshift::ScheduledAction ResizeClusterMessage
<a name="aws-properties-redshift-scheduledaction-resizeclustermessage"></a>

Describes a resize cluster operation. For example, a scheduled action to run the `ResizeCluster` API operation.

## Syntax
<a name="aws-properties-redshift-scheduledaction-resizeclustermessage-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-redshift-scheduledaction-resizeclustermessage-syntax.json"></a>

```
{
  "[Classic](#cfn-redshift-scheduledaction-resizeclustermessage-classic)" : {{Boolean}},
  "[ClusterIdentifier](#cfn-redshift-scheduledaction-resizeclustermessage-clusteridentifier)" : {{String}},
  "[ClusterType](#cfn-redshift-scheduledaction-resizeclustermessage-clustertype)" : {{String}},
  "[NodeType](#cfn-redshift-scheduledaction-resizeclustermessage-nodetype)" : {{String}},
  "[NumberOfNodes](#cfn-redshift-scheduledaction-resizeclustermessage-numberofnodes)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-redshift-scheduledaction-resizeclustermessage-syntax.yaml"></a>

```
  [Classic](#cfn-redshift-scheduledaction-resizeclustermessage-classic): {{Boolean}}
  [ClusterIdentifier](#cfn-redshift-scheduledaction-resizeclustermessage-clusteridentifier): {{String}}
  [ClusterType](#cfn-redshift-scheduledaction-resizeclustermessage-clustertype): {{String}}
  [NodeType](#cfn-redshift-scheduledaction-resizeclustermessage-nodetype): {{String}}
  [NumberOfNodes](#cfn-redshift-scheduledaction-resizeclustermessage-numberofnodes): {{Integer}}
```

## Properties
<a name="aws-properties-redshift-scheduledaction-resizeclustermessage-properties"></a>

`Classic`  <a name="cfn-redshift-scheduledaction-resizeclustermessage-classic"></a>
A boolean value indicating whether the resize operation is using the classic resize process. If you don't provide this parameter or set the value to `false`, the resize type is elastic.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClusterIdentifier`  <a name="cfn-redshift-scheduledaction-resizeclustermessage-clusteridentifier"></a>
The unique identifier for the cluster to resize.
*Required*: Yes
*Type*: String
*Maximum*: `2147483647`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClusterType`  <a name="cfn-redshift-scheduledaction-resizeclustermessage-clustertype"></a>
The new cluster type for the specified cluster.
*Required*: No
*Type*: String
*Maximum*: `2147483647`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NodeType`  <a name="cfn-redshift-scheduledaction-resizeclustermessage-nodetype"></a>
The new node type for the nodes you are adding. If not specified, the cluster's current node type is used.
*Required*: No
*Type*: String
*Maximum*: `2147483647`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NumberOfNodes`  <a name="cfn-redshift-scheduledaction-resizeclustermessage-numberofnodes"></a>
The new number of nodes for the cluster. If not specified, the cluster's current number of nodes is used.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

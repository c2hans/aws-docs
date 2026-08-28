---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-redshift-scheduledaction-resumeclustermessage.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Redshift::ScheduledAction ResumeClusterMessage
<a name="aws-properties-redshift-scheduledaction-resumeclustermessage"></a>

Describes a resume cluster operation. For example, a scheduled action to run the `ResumeCluster` API operation.

## Syntax
<a name="aws-properties-redshift-scheduledaction-resumeclustermessage-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-redshift-scheduledaction-resumeclustermessage-syntax.json"></a>

```
{
  "[ClusterIdentifier](#cfn-redshift-scheduledaction-resumeclustermessage-clusteridentifier)" : {{String}}
}
```

### YAML
<a name="aws-properties-redshift-scheduledaction-resumeclustermessage-syntax.yaml"></a>

```
  [ClusterIdentifier](#cfn-redshift-scheduledaction-resumeclustermessage-clusteridentifier): {{String}}
```

## Properties
<a name="aws-properties-redshift-scheduledaction-resumeclustermessage-properties"></a>

`ClusterIdentifier`  <a name="cfn-redshift-scheduledaction-resumeclustermessage-clusteridentifier"></a>
The identifier of the cluster to be resumed.
*Required*: Yes
*Type*: String
*Maximum*: `2147483647`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-redshift-clustersubnetgroup-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Redshift::ClusterSubnetGroup Tag
<a name="aws-properties-redshift-clustersubnetgroup-tag"></a>

A tag consisting of a name/value pair for a resource.

## Syntax
<a name="aws-properties-redshift-clustersubnetgroup-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-redshift-clustersubnetgroup-tag-syntax.json"></a>

```
{
  "[Key](#cfn-redshift-clustersubnetgroup-tag-key)" : {{String}},
  "[Value](#cfn-redshift-clustersubnetgroup-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-redshift-clustersubnetgroup-tag-syntax.yaml"></a>

```
  [Key](#cfn-redshift-clustersubnetgroup-tag-key): {{String}}
  [Value](#cfn-redshift-clustersubnetgroup-tag-value): {{String}}
```

## Properties
<a name="aws-properties-redshift-clustersubnetgroup-tag-properties"></a>

`Key`  <a name="cfn-redshift-clustersubnetgroup-tag-key"></a>
The key, or name, for the resource tag.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-redshift-clustersubnetgroup-tag-value"></a>
The value for the resource tag.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

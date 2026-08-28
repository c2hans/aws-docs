---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resourceexplorer2-view-includedproperty.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ResourceExplorer2::View IncludedProperty
<a name="aws-properties-resourceexplorer2-view-includedproperty"></a>

Information about an additional property that describes a resource, that you can optionally include in a view.

## Syntax
<a name="aws-properties-resourceexplorer2-view-includedproperty-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-resourceexplorer2-view-includedproperty-syntax.json"></a>

```
{
  "[Name](#cfn-resourceexplorer2-view-includedproperty-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-resourceexplorer2-view-includedproperty-syntax.yaml"></a>

```
  [Name](#cfn-resourceexplorer2-view-includedproperty-name): {{String}}
```

## Properties
<a name="aws-properties-resourceexplorer2-view-includedproperty-properties"></a>

`Name`  <a name="cfn-resourceexplorer2-view-includedproperty-name"></a>
The name of the property that is included in this view.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1011`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

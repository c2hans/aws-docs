---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resourcegroups-group-configurationparameter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ResourceGroups::Group ConfigurationParameter
<a name="aws-properties-resourcegroups-group-configurationparameter"></a>

One parameter for a group configuration item. For details about service configurations and how to construct them, see [Service configurations for resource groups](https://docs.aws.amazon.com/ARG/latest/APIReference/about-slg.html) in the *AWS Resource Groups User Guide*.

## Syntax
<a name="aws-properties-resourcegroups-group-configurationparameter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-resourcegroups-group-configurationparameter-syntax.json"></a>

```
{
  "[Name](#cfn-resourcegroups-group-configurationparameter-name)" : {{String}},
  "[Values](#cfn-resourcegroups-group-configurationparameter-values)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-resourcegroups-group-configurationparameter-syntax.yaml"></a>

```
  [Name](#cfn-resourcegroups-group-configurationparameter-name): {{String}}
  [Values](#cfn-resourcegroups-group-configurationparameter-values): {{
    - String}}
```

## Properties
<a name="aws-properties-resourcegroups-group-configurationparameter-properties"></a>

`Name`  <a name="cfn-resourcegroups-group-configurationparameter-name"></a>
The name of the group configuration parameter. For the list of parameters that you can use with each configuration item type, see [Supported resource types and parameters](https://docs.aws.amazon.com/ARG/latest/APIReference/about-slg.html#about-slg-types) in the *AWS Resource Groups User Guide*.
*Required*: No
*Type*: String
*Pattern*: `[a-z-]+`
*Minimum*: `1`
*Maximum*: `80`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-resourcegroups-group-configurationparameter-values"></a>
The value or values to be used for the specified parameter. For the list of values you can use with each parameter, see [Supported resource types and parameters](https://docs.aws.amazon.com/ARG/latest/APIReference/about-slg.html#about-slg-types).
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

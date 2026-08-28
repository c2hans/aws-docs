---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rtbfabric-link-moduleconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RTBFabric::Link ModuleConfiguration
<a name="aws-properties-rtbfabric-link-moduleconfiguration"></a>

Describes the configuration of a module.

## Syntax
<a name="aws-properties-rtbfabric-link-moduleconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rtbfabric-link-moduleconfiguration-syntax.json"></a>

```
{
  "[DependsOn](#cfn-rtbfabric-link-moduleconfiguration-dependson)" : {{[ String, ... ]}},
  "[ModuleParameters](#cfn-rtbfabric-link-moduleconfiguration-moduleparameters)" : {{ModuleParameters}},
  "[Name](#cfn-rtbfabric-link-moduleconfiguration-name)" : {{String}},
  "[Version](#cfn-rtbfabric-link-moduleconfiguration-version)" : {{String}}
}
```

### YAML
<a name="aws-properties-rtbfabric-link-moduleconfiguration-syntax.yaml"></a>

```
  [DependsOn](#cfn-rtbfabric-link-moduleconfiguration-dependson): {{
    - String}}
  [ModuleParameters](#cfn-rtbfabric-link-moduleconfiguration-moduleparameters): {{
    ModuleParameters}}
  [Name](#cfn-rtbfabric-link-moduleconfiguration-name): {{String}}
  [Version](#cfn-rtbfabric-link-moduleconfiguration-version): {{String}}
```

## Properties
<a name="aws-properties-rtbfabric-link-moduleconfiguration-properties"></a>

`DependsOn`  <a name="cfn-rtbfabric-link-moduleconfiguration-dependson"></a>
The dependencies of the module.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ModuleParameters`  <a name="cfn-rtbfabric-link-moduleconfiguration-moduleparameters"></a>
Describes the parameters of a module.
*Required*: No
*Type*: [ModuleParameters](aws-properties-rtbfabric-link-moduleparameters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-rtbfabric-link-moduleconfiguration-name"></a>
The name of the module.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9 -]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Version`  <a name="cfn-rtbfabric-link-moduleconfiguration-version"></a>
The version of the module.
*Required*: No
*Type*: String
*Pattern*: `^[a-z0-9]{1,25}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-project-environmentconfigurationuserparameter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::Project EnvironmentConfigurationUserParameter
<a name="aws-properties-datazone-project-environmentconfigurationuserparameter"></a>

The environment configuration user parameters.

## Syntax
<a name="aws-properties-datazone-project-environmentconfigurationuserparameter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-project-environmentconfigurationuserparameter-syntax.json"></a>

```
{
  "[EnvironmentConfigurationName](#cfn-datazone-project-environmentconfigurationuserparameter-environmentconfigurationname)" : {{String}},
  "[EnvironmentId](#cfn-datazone-project-environmentconfigurationuserparameter-environmentid)" : {{String}},
  "[EnvironmentParameters](#cfn-datazone-project-environmentconfigurationuserparameter-environmentparameters)" : {{[ EnvironmentParameter, ... ]}}
}
```

### YAML
<a name="aws-properties-datazone-project-environmentconfigurationuserparameter-syntax.yaml"></a>

```
  [EnvironmentConfigurationName](#cfn-datazone-project-environmentconfigurationuserparameter-environmentconfigurationname): {{String}}
  [EnvironmentId](#cfn-datazone-project-environmentconfigurationuserparameter-environmentid): {{String}}
  [EnvironmentParameters](#cfn-datazone-project-environmentconfigurationuserparameter-environmentparameters): {{
    - EnvironmentParameter}}
```

## Properties
<a name="aws-properties-datazone-project-environmentconfigurationuserparameter-properties"></a>

`EnvironmentConfigurationName`  <a name="cfn-datazone-project-environmentconfigurationuserparameter-environmentconfigurationname"></a>
The environment configuration name.
*Required*: No
*Type*: String
*Pattern*: `^[\w -]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnvironmentId`  <a name="cfn-datazone-project-environmentconfigurationuserparameter-environmentid"></a>
The ID of the environment.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]{1,36}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnvironmentParameters`  <a name="cfn-datazone-project-environmentconfigurationuserparameter-environmentparameters"></a>
The environment parameters.
*Required*: No
*Type*: Array of [EnvironmentParameter](aws-properties-datazone-project-environmentparameter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

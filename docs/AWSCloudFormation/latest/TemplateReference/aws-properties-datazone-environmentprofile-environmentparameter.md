---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-environmentprofile-environmentparameter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::EnvironmentProfile EnvironmentParameter
<a name="aws-properties-datazone-environmentprofile-environmentparameter"></a>

The parameter details of an environment profile.

## Syntax
<a name="aws-properties-datazone-environmentprofile-environmentparameter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-environmentprofile-environmentparameter-syntax.json"></a>

```
{
  "[Name](#cfn-datazone-environmentprofile-environmentparameter-name)" : {{String}},
  "[Value](#cfn-datazone-environmentprofile-environmentparameter-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-datazone-environmentprofile-environmentparameter-syntax.yaml"></a>

```
  [Name](#cfn-datazone-environmentprofile-environmentparameter-name): {{String}}
  [Value](#cfn-datazone-environmentprofile-environmentparameter-value): {{String}}
```

## Properties
<a name="aws-properties-datazone-environmentprofile-environmentparameter-properties"></a>

`Name`  <a name="cfn-datazone-environmentprofile-environmentparameter-name"></a>
The name specified in the environment parameter.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-datazone-environmentprofile-environmentparameter-value"></a>
The value of the environment profile.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

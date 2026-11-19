---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-runtimeversion-compatibility.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::RuntimeVersion Compatibility

The compatibility of the runtime version: the integration models and architectures it supports, and whether it supports Lambda Managed Instances.

It is a read-only type. You don't declare `Compatibility` in a template. CloudFormation returns it as the runtime version's `Compatibility` attribute, which you retrieve with `Fn::GetAtt`.

## Syntax
<a name="aws-properties-lambda-runtimeversion-compatibility-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-runtimeversion-compatibility-syntax.json"></a>

```
{
  "[Architectures](#cfn-lambda-runtimeversion-compatibility-architectures)" : {{[ String, ... ]}},
  "[IntegrationModels](#cfn-lambda-runtimeversion-compatibility-integrationmodels)" : {{[ String, ... ]}},
  "[ManagedInstances](#cfn-lambda-runtimeversion-compatibility-managedinstances)" : {{String}}
}
```

### YAML
<a name="aws-properties-lambda-runtimeversion-compatibility-syntax.yaml"></a>

```
  [Architectures](#cfn-lambda-runtimeversion-compatibility-architectures): {{
    - String}}
  [IntegrationModels](#cfn-lambda-runtimeversion-compatibility-integrationmodels): {{
    - String}}
  [ManagedInstances](#cfn-lambda-runtimeversion-compatibility-managedinstances): {{String}}
```

## Properties
<a name="aws-properties-lambda-runtimeversion-compatibility-properties"></a>

`Architectures`  <a name="cfn-lambda-runtimeversion-compatibility-architectures"></a>
Supported architectures for the runtime version.
*Required*: No
*Type*: Array of String
*Allowed values*: `x86_64 | arm64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IntegrationModels`  <a name="cfn-lambda-runtimeversion-compatibility-integrationmodels"></a>
Supported integration models for the runtime version.
*Required*: No
*Type*: Array of String
*Allowed values*: `RuntimeAPI`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ManagedInstances`  <a name="cfn-lambda-runtimeversion-compatibility-managedinstances"></a>
Whether the runtime version is compatible with managed instances.
*Required*: No
*Type*: String
*Allowed values*: `Supported | NotSupported`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

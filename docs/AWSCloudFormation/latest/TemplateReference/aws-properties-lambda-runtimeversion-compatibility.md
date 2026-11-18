---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-runtimeversion-compatibility.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::RuntimeVersion Compatibility
<a name="aws-properties-lambda-runtimeversion-compatibility"></a>

<a name="aws-properties-lambda-runtimeversion-compatibility-description"></a>The `Compatibility` property type specifies Property description not available. for an [AWS::Lambda::RuntimeVersion](aws-resource-lambda-runtimeversion.md).

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
Property description not available.
*Required*: No
*Type*: Array of String
*Allowed values*: `x86_64 | arm64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IntegrationModels`  <a name="cfn-lambda-runtimeversion-compatibility-integrationmodels"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Allowed values*: `RuntimeAPI`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ManagedInstances`  <a name="cfn-lambda-runtimeversion-compatibility-managedinstances"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `Supported | NotSupported`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

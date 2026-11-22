---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-function-acceleratorconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::Function AcceleratorConfig

The accelerator resource settings for a Lambda execution environment, including the amount of accelerator memory to allocate. To use an accelerator, the function must also have a capacity provider configuration (`CapacityProviderConfig`) for Lambda Managed Instances.

## Syntax
<a name="aws-properties-lambda-function-acceleratorconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-function-acceleratorconfig-syntax.json"></a>

```json
{
  "[AcceleratorMemorySize](#cfn-lambda-function-acceleratorconfig-acceleratormemorysize)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-lambda-function-acceleratorconfig-syntax.yaml"></a>

```yaml
  [AcceleratorMemorySize](#cfn-lambda-function-acceleratorconfig-acceleratormemorysize): {{Integer}}
```

## Properties
<a name="aws-properties-lambda-function-acceleratorconfig-properties"></a>

`AcceleratorMemorySize`  <a name="cfn-lambda-function-acceleratorconfig-acceleratormemorysize"></a>
The minimum amount of memory (in GB) of each accelerator device exposed to the execution environment. Lambda might allocate more, depending on the accelerator instance types available. Valid values: 3, 6, 12, 16, 24, 48.
*Required*: Yes
*Type*: Integer
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

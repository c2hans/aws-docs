---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-synthetics-canary-dependency.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Synthetics::Canary Dependency
<a name="aws-properties-synthetics-canary-dependency"></a>

A structure that contains information about a dependency for a canary.

## Syntax
<a name="aws-properties-synthetics-canary-dependency-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-synthetics-canary-dependency-syntax.json"></a>

```
{
  "[Reference](#cfn-synthetics-canary-dependency-reference)" : {{String}},
  "[Type](#cfn-synthetics-canary-dependency-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-synthetics-canary-dependency-syntax.yaml"></a>

```
  [Reference](#cfn-synthetics-canary-dependency-reference): {{String}}
  [Type](#cfn-synthetics-canary-dependency-type): {{String}}
```

## Properties
<a name="aws-properties-synthetics-canary-dependency-properties"></a>

`Reference`  <a name="cfn-synthetics-canary-dependency-reference"></a>
The dependency reference. For Lambda layers, this is the ARN of the Lambda layer. For more information about Lambda ARN format, see [Lambda](https://docs.aws.amazon.com/lambda/latest/api/API_Layer.html).
*Required*: Yes
*Type*: String
*Pattern*: `arn:[a-zA-Z0-9-]+:lambda:[a-zA-Z0-9-]+:\d{12}:layer:[a-zA-Z0-9-_]+:[0-9]+`
*Minimum*: `1`
*Maximum*: `140`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-synthetics-canary-dependency-type"></a>
The type of dependency. Valid value is `LambdaLayer`.
*Required*: No
*Type*: String
*Allowed values*: `LambdaLayer`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

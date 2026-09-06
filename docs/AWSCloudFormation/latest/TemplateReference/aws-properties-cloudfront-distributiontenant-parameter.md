---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-distributiontenant-parameter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::DistributionTenant Parameter
<a name="aws-properties-cloudfront-distributiontenant-parameter"></a>

A list of parameter values to add to the resource. A parameter is specified as a key-value pair. A valid parameter value must exist for any parameter that is marked as required in the multi-tenant distribution.

## Syntax
<a name="aws-properties-cloudfront-distributiontenant-parameter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-distributiontenant-parameter-syntax.json"></a>

```
{
  "[Name](#cfn-cloudfront-distributiontenant-parameter-name)" : {{String}},
  "[Value](#cfn-cloudfront-distributiontenant-parameter-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudfront-distributiontenant-parameter-syntax.yaml"></a>

```
  [Name](#cfn-cloudfront-distributiontenant-parameter-name): {{String}}
  [Value](#cfn-cloudfront-distributiontenant-parameter-value): {{String}}
```

## Properties
<a name="aws-properties-cloudfront-distributiontenant-parameter-properties"></a>

`Name`  <a name="cfn-cloudfront-distributiontenant-parameter-name"></a>
The parameter name.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z0-9-_]+`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-cloudfront-distributiontenant-parameter-value"></a>
The parameter value.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

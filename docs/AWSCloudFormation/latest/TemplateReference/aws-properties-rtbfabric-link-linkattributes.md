---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rtbfabric-link-linkattributes.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RTBFabric::Link LinkAttributes
<a name="aws-properties-rtbfabric-link-linkattributes"></a>

Describes the attributes of a link.

## Syntax
<a name="aws-properties-rtbfabric-link-linkattributes-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rtbfabric-link-linkattributes-syntax.json"></a>

```
{
  "[CustomerProvidedId](#cfn-rtbfabric-link-linkattributes-customerprovidedid)" : {{String}},
  "[ResponderErrorMasking](#cfn-rtbfabric-link-linkattributes-respondererrormasking)" : {{[ ResponderErrorMaskingForHttpCode, ... ]}}
}
```

### YAML
<a name="aws-properties-rtbfabric-link-linkattributes-syntax.yaml"></a>

```
  [CustomerProvidedId](#cfn-rtbfabric-link-linkattributes-customerprovidedid): {{String}}
  [ResponderErrorMasking](#cfn-rtbfabric-link-linkattributes-respondererrormasking): {{
    - ResponderErrorMaskingForHttpCode}}
```

## Properties
<a name="aws-properties-rtbfabric-link-linkattributes-properties"></a>

`CustomerProvidedId`  <a name="cfn-rtbfabric-link-linkattributes-customerprovidedid"></a>
The customer-provided unique identifier of the link.
*Required*: No
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`ResponderErrorMasking`  <a name="cfn-rtbfabric-link-linkattributes-respondererrormasking"></a>
Describes the masking for HTTP error codes.
*Required*: No
*Type*: Array of [ResponderErrorMaskingForHttpCode](aws-properties-rtbfabric-link-respondererrormaskingforhttpcode.md)
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

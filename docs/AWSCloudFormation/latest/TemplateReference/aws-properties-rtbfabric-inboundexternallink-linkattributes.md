---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rtbfabric-inboundexternallink-linkattributes.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RTBFabric::InboundExternalLink LinkAttributes
<a name="aws-properties-rtbfabric-inboundexternallink-linkattributes"></a>

<a name="aws-properties-rtbfabric-inboundexternallink-linkattributes-description"></a>The `LinkAttributes` property type specifies Property description not available. for an [AWS::RTBFabric::InboundExternalLink](aws-resource-rtbfabric-inboundexternallink.md).

## Syntax
<a name="aws-properties-rtbfabric-inboundexternallink-linkattributes-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rtbfabric-inboundexternallink-linkattributes-syntax.json"></a>

```
{
  "[CustomerProvidedId](#cfn-rtbfabric-inboundexternallink-linkattributes-customerprovidedid)" : {{String}},
  "[ResponderErrorMasking](#cfn-rtbfabric-inboundexternallink-linkattributes-respondererrormasking)" : {{[ ResponderErrorMaskingForHttpCode, ... ]}}
}
```

### YAML
<a name="aws-properties-rtbfabric-inboundexternallink-linkattributes-syntax.yaml"></a>

```
  [CustomerProvidedId](#cfn-rtbfabric-inboundexternallink-linkattributes-customerprovidedid): {{String}}
  [ResponderErrorMasking](#cfn-rtbfabric-inboundexternallink-linkattributes-respondererrormasking): {{
    - ResponderErrorMaskingForHttpCode}}
```

## Properties
<a name="aws-properties-rtbfabric-inboundexternallink-linkattributes-properties"></a>

`CustomerProvidedId`  <a name="cfn-rtbfabric-inboundexternallink-linkattributes-customerprovidedid"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`ResponderErrorMasking`  <a name="cfn-rtbfabric-inboundexternallink-linkattributes-respondererrormasking"></a>
Property description not available.
*Required*: No
*Type*: Array of [ResponderErrorMaskingForHttpCode](aws-properties-rtbfabric-inboundexternallink-respondererrormaskingforhttpcode.md)
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-msk-channel-catalog.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::Channel Catalog
<a name="aws-properties-msk-channel-catalog"></a>

<a name="aws-properties-msk-channel-catalog-description"></a>The `Catalog` property type specifies Property description not available. for an [AWS::MSK::Channel](aws-resource-msk-channel.md).

## Syntax
<a name="aws-properties-msk-channel-catalog-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-msk-channel-catalog-syntax.json"></a>

```
{
  "[CatalogArn](#cfn-msk-channel-catalog-catalogarn)" : {{String}},
  "[WarehouseLocation](#cfn-msk-channel-catalog-warehouselocation)" : {{String}}
}
```

### YAML
<a name="aws-properties-msk-channel-catalog-syntax.yaml"></a>

```
  [CatalogArn](#cfn-msk-channel-catalog-catalogarn): {{String}}
  [WarehouseLocation](#cfn-msk-channel-catalog-warehouselocation): {{String}}
```

## Properties
<a name="aws-properties-msk-channel-catalog-properties"></a>

`CatalogArn`  <a name="cfn-msk-channel-catalog-catalogarn"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^arn:[\w-]+:glue:[\w-]+:\d+:catalog.*\Z`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`WarehouseLocation`  <a name="cfn-msk-channel-catalog-warehouselocation"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

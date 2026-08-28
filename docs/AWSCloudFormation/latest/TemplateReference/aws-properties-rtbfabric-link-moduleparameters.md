---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rtbfabric-link-moduleparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RTBFabric::Link ModuleParameters
<a name="aws-properties-rtbfabric-link-moduleparameters"></a>

Describes the parameters of a module.

## Syntax
<a name="aws-properties-rtbfabric-link-moduleparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rtbfabric-link-moduleparameters-syntax.json"></a>

```
{
  "[NoBid](#cfn-rtbfabric-link-moduleparameters-nobid)" : {{NoBidModuleParameters}},
  "[OpenRtbAttribute](#cfn-rtbfabric-link-moduleparameters-openrtbattribute)" : {{OpenRtbAttributeModuleParameters}}
}
```

### YAML
<a name="aws-properties-rtbfabric-link-moduleparameters-syntax.yaml"></a>

```
  [NoBid](#cfn-rtbfabric-link-moduleparameters-nobid): {{
    NoBidModuleParameters}}
  [OpenRtbAttribute](#cfn-rtbfabric-link-moduleparameters-openrtbattribute): {{
    OpenRtbAttributeModuleParameters}}
```

## Properties
<a name="aws-properties-rtbfabric-link-moduleparameters-properties"></a>

`NoBid`  <a name="cfn-rtbfabric-link-moduleparameters-nobid"></a>
Describes the parameters of a no bid module.
*Required*: No
*Type*: [NoBidModuleParameters](aws-properties-rtbfabric-link-nobidmoduleparameters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OpenRtbAttribute`  <a name="cfn-rtbfabric-link-moduleparameters-openrtbattribute"></a>
Describes the parameters of an open RTB attribute module.
*Required*: No
*Type*: [OpenRtbAttributeModuleParameters](aws-properties-rtbfabric-link-openrtbattributemoduleparameters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

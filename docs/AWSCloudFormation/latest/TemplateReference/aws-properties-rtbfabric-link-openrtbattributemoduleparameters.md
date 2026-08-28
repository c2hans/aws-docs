---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rtbfabric-link-openrtbattributemoduleparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RTBFabric::Link OpenRtbAttributeModuleParameters
<a name="aws-properties-rtbfabric-link-openrtbattributemoduleparameters"></a>

Describes the parameters of an open RTB attribute module.

## Syntax
<a name="aws-properties-rtbfabric-link-openrtbattributemoduleparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rtbfabric-link-openrtbattributemoduleparameters-syntax.json"></a>

```
{
  "[Action](#cfn-rtbfabric-link-openrtbattributemoduleparameters-action)" : {{Action}},
  "[FilterConfiguration](#cfn-rtbfabric-link-openrtbattributemoduleparameters-filterconfiguration)" : {{[ Filter, ... ]}},
  "[FilterType](#cfn-rtbfabric-link-openrtbattributemoduleparameters-filtertype)" : {{String}},
  "[HoldbackPercentage](#cfn-rtbfabric-link-openrtbattributemoduleparameters-holdbackpercentage)" : {{Number}}
}
```

### YAML
<a name="aws-properties-rtbfabric-link-openrtbattributemoduleparameters-syntax.yaml"></a>

```
  [Action](#cfn-rtbfabric-link-openrtbattributemoduleparameters-action): {{
    Action}}
  [FilterConfiguration](#cfn-rtbfabric-link-openrtbattributemoduleparameters-filterconfiguration): {{
    - Filter}}
  [FilterType](#cfn-rtbfabric-link-openrtbattributemoduleparameters-filtertype): {{String}}
  [HoldbackPercentage](#cfn-rtbfabric-link-openrtbattributemoduleparameters-holdbackpercentage): {{Number}}
```

## Properties
<a name="aws-properties-rtbfabric-link-openrtbattributemoduleparameters-properties"></a>

`Action`  <a name="cfn-rtbfabric-link-openrtbattributemoduleparameters-action"></a>
Describes a bid action.
*Required*: Yes
*Type*: [Action](aws-properties-rtbfabric-link-action.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FilterConfiguration`  <a name="cfn-rtbfabric-link-openrtbattributemoduleparameters-filterconfiguration"></a>
Describes the configuration of a filter.
*Required*: Yes
*Type*: Array of [Filter](aws-properties-rtbfabric-link-filter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FilterType`  <a name="cfn-rtbfabric-link-openrtbattributemoduleparameters-filtertype"></a>
The filter type.
*Required*: Yes
*Type*: String
*Allowed values*: `INCLUDE | EXCLUDE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HoldbackPercentage`  <a name="cfn-rtbfabric-link-openrtbattributemoduleparameters-holdbackpercentage"></a>
The hold back percentage.
*Required*: Yes
*Type*: Number
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

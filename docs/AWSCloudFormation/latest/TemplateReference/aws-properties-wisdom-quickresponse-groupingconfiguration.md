---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-quickresponse-groupingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::QuickResponse GroupingConfiguration
<a name="aws-properties-wisdom-quickresponse-groupingconfiguration"></a>

The configuration information of the grouping of Amazon Q in Connect users.

## Syntax
<a name="aws-properties-wisdom-quickresponse-groupingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-quickresponse-groupingconfiguration-syntax.json"></a>

```
{
  "[Criteria](#cfn-wisdom-quickresponse-groupingconfiguration-criteria)" : {{String}},
  "[Values](#cfn-wisdom-quickresponse-groupingconfiguration-values)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-wisdom-quickresponse-groupingconfiguration-syntax.yaml"></a>

```
  [Criteria](#cfn-wisdom-quickresponse-groupingconfiguration-criteria): {{String}}
  [Values](#cfn-wisdom-quickresponse-groupingconfiguration-values): {{
    - String}}
```

## Properties
<a name="aws-properties-wisdom-quickresponse-groupingconfiguration-properties"></a>

`Criteria`  <a name="cfn-wisdom-quickresponse-groupingconfiguration-criteria"></a>
The criteria used for grouping Amazon Q in Connect users.
The following is the list of supported criteria values.
+ `RoutingProfileArn`: Grouping the users by their [Amazon Connect routing profile ARN](https://docs.aws.amazon.com/connect/latest/APIReference/API_RoutingProfile.html). User should have [SearchRoutingProfile](https://docs.aws.amazon.com/connect/latest/APIReference/API_SearchRoutingProfiles.html) and [DescribeRoutingProfile](https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeRoutingProfile.html) permissions when setting criteria to this value.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-wisdom-quickresponse-groupingconfiguration-values"></a>
The list of values that define different groups of Amazon Q in Connect users.
+ When setting `criteria` to `RoutingProfileArn`, you need to provide a list of ARNs of [Connect Customer routing profiles](https://docs.aws.amazon.com/connect/latest/APIReference/API_RoutingProfile.html) as values of this parameter.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cases-layout-basiclayout.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cases::Layout BasicLayout
<a name="aws-properties-cases-layout-basiclayout"></a>

Content specific to `BasicLayout` type. It configures fields in the top panel and More Info tab of agent application.

## Syntax
<a name="aws-properties-cases-layout-basiclayout-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cases-layout-basiclayout-syntax.json"></a>

```
{
  "[MoreInfo](#cfn-cases-layout-basiclayout-moreinfo)" : {{LayoutSections}},
  "[TopPanel](#cfn-cases-layout-basiclayout-toppanel)" : {{LayoutSections}}
}
```

### YAML
<a name="aws-properties-cases-layout-basiclayout-syntax.yaml"></a>

```
  [MoreInfo](#cfn-cases-layout-basiclayout-moreinfo): {{
    LayoutSections}}
  [TopPanel](#cfn-cases-layout-basiclayout-toppanel): {{
    LayoutSections}}
```

## Properties
<a name="aws-properties-cases-layout-basiclayout-properties"></a>

`MoreInfo`  <a name="cfn-cases-layout-basiclayout-moreinfo"></a>
This represents sections in a tab of the page layout.
*Required*: No
*Type*: [LayoutSections](aws-properties-cases-layout-layoutsections.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TopPanel`  <a name="cfn-cases-layout-basiclayout-toppanel"></a>
This represents sections in a panel of the page layout.
*Required*: No
*Type*: [LayoutSections](aws-properties-cases-layout-layoutsections.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

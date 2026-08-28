---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cases-layout-layoutcontent.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cases::Layout LayoutContent
<a name="aws-properties-cases-layout-layoutcontent"></a>

Object to store union of different versions of layout content.

## Syntax
<a name="aws-properties-cases-layout-layoutcontent-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cases-layout-layoutcontent-syntax.json"></a>

```
{
  "[Basic](#cfn-cases-layout-layoutcontent-basic)" : {{BasicLayout}}
}
```

### YAML
<a name="aws-properties-cases-layout-layoutcontent-syntax.yaml"></a>

```
  [Basic](#cfn-cases-layout-layoutcontent-basic): {{
    BasicLayout}}
```

## Properties
<a name="aws-properties-cases-layout-layoutcontent-properties"></a>

`Basic`  <a name="cfn-cases-layout-layoutcontent-basic"></a>
Content specific to `BasicLayout` type. It configures fields in the top panel and More Info tab of agent application.
*Required*: Yes
*Type*: [BasicLayout](aws-properties-cases-layout-basiclayout.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

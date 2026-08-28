---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-messagetemplate-messagetemplatebodycontentprovider.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::MessageTemplate MessageTemplateBodyContentProvider
<a name="aws-properties-wisdom-messagetemplate-messagetemplatebodycontentprovider"></a>

The container of the message template body.

## Syntax
<a name="aws-properties-wisdom-messagetemplate-messagetemplatebodycontentprovider-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-messagetemplate-messagetemplatebodycontentprovider-syntax.json"></a>

```
{
  "[Content](#cfn-wisdom-messagetemplate-messagetemplatebodycontentprovider-content)" : {{String}}
}
```

### YAML
<a name="aws-properties-wisdom-messagetemplate-messagetemplatebodycontentprovider-syntax.yaml"></a>

```
  [Content](#cfn-wisdom-messagetemplate-messagetemplatebodycontentprovider-content): {{String}}
```

## Properties
<a name="aws-properties-wisdom-messagetemplate-messagetemplatebodycontentprovider-properties"></a>

`Content`  <a name="cfn-wisdom-messagetemplate-messagetemplatebodycontentprovider-content"></a>
The content of the message template.
*Required*: No
*Type*: [String](aws-properties-wisdom-messagetemplate-content.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

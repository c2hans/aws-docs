---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-quickresponse-quickresponsecontents.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::QuickResponse QuickResponseContents
<a name="aws-properties-wisdom-quickresponse-quickresponsecontents"></a>

The content of the quick response stored in different media types.

## Syntax
<a name="aws-properties-wisdom-quickresponse-quickresponsecontents-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-quickresponse-quickresponsecontents-syntax.json"></a>

```
{
  "[Markdown](#cfn-wisdom-quickresponse-quickresponsecontents-markdown)" : {{QuickResponseContentProvider}},
  "[PlainText](#cfn-wisdom-quickresponse-quickresponsecontents-plaintext)" : {{QuickResponseContentProvider}}
}
```

### YAML
<a name="aws-properties-wisdom-quickresponse-quickresponsecontents-syntax.yaml"></a>

```
  [Markdown](#cfn-wisdom-quickresponse-quickresponsecontents-markdown): {{
    QuickResponseContentProvider}}
  [PlainText](#cfn-wisdom-quickresponse-quickresponsecontents-plaintext): {{
    QuickResponseContentProvider}}
```

## Properties
<a name="aws-properties-wisdom-quickresponse-quickresponsecontents-properties"></a>

`Markdown`  <a name="cfn-wisdom-quickresponse-quickresponsecontents-markdown"></a>
The quick response content in markdown format.
*Required*: No
*Type*: [QuickResponseContentProvider](aws-properties-wisdom-quickresponse-quickresponsecontentprovider.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PlainText`  <a name="cfn-wisdom-quickresponse-quickresponsecontents-plaintext"></a>
The quick response content in plaintext format.
*Required*: No
*Type*: [QuickResponseContentProvider](aws-properties-wisdom-quickresponse-quickresponsecontentprovider.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

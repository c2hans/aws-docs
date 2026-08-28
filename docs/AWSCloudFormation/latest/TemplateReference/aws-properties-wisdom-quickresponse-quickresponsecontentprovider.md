---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-quickresponse-quickresponsecontentprovider.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::QuickResponse QuickResponseContentProvider
<a name="aws-properties-wisdom-quickresponse-quickresponsecontentprovider"></a>

The container quick response content.

## Syntax
<a name="aws-properties-wisdom-quickresponse-quickresponsecontentprovider-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-quickresponse-quickresponsecontentprovider-syntax.json"></a>

```
{
  "[Content](#cfn-wisdom-quickresponse-quickresponsecontentprovider-content)" : {{String}}
}
```

### YAML
<a name="aws-properties-wisdom-quickresponse-quickresponsecontentprovider-syntax.yaml"></a>

```
  [Content](#cfn-wisdom-quickresponse-quickresponsecontentprovider-content): {{String}}
```

## Properties
<a name="aws-properties-wisdom-quickresponse-quickresponsecontentprovider-properties"></a>

`Content`  <a name="cfn-wisdom-quickresponse-quickresponsecontentprovider-content"></a>
The content of the quick response.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `4000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

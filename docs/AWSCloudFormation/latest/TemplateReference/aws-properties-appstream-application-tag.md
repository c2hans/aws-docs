---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appstream-application-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppStream::Application Tag
<a name="aws-properties-appstream-application-tag"></a>

The tag of the application.

## Syntax
<a name="aws-properties-appstream-application-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appstream-application-tag-syntax.json"></a>

```
{
  "[TagItems](#cfn-appstream-application-tag-tagitems)" : {{TagItems}}
}
```

### YAML
<a name="aws-properties-appstream-application-tag-syntax.yaml"></a>

```
  [TagItems](#cfn-appstream-application-tag-tagitems): {{
    TagItems}}
```

## Properties
<a name="aws-properties-appstream-application-tag-properties"></a>

`TagItems`  <a name="cfn-appstream-application-tag-tagitems"></a>
The items of the tag.
*Required*: No
*Type*: [TagItems](aws-properties-appstream-application-tagitems.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appstream-application-tagitems.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppStream::Application TagItems
<a name="aws-properties-appstream-application-tagitems"></a>

The tag items of the application.

## Syntax
<a name="aws-properties-appstream-application-tagitems-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appstream-application-tagitems-syntax.json"></a>

```
{
  "[Key](#cfn-appstream-application-tagitems-key)" : {{String}},
  "[Value](#cfn-appstream-application-tagitems-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-appstream-application-tagitems-syntax.yaml"></a>

```
  [Key](#cfn-appstream-application-tagitems-key): {{String}}
  [Value](#cfn-appstream-application-tagitems-value): {{String}}
```

## Properties
<a name="aws-properties-appstream-application-tagitems-properties"></a>

`Key`  <a name="cfn-appstream-application-tagitems-key"></a>
The key of the tag items.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-appstream-application-tagitems-value"></a>
The value of the tag items.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

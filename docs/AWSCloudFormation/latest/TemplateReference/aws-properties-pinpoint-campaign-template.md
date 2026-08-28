---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pinpoint-campaign-template.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pinpoint::Campaign Template
<a name="aws-properties-pinpoint-campaign-template"></a>

Specifies the name and version of the message template to use for the message.

## Syntax
<a name="aws-properties-pinpoint-campaign-template-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pinpoint-campaign-template-syntax.json"></a>

```
{
  "[Name](#cfn-pinpoint-campaign-template-name)" : {{String}},
  "[Version](#cfn-pinpoint-campaign-template-version)" : {{String}}
}
```

### YAML
<a name="aws-properties-pinpoint-campaign-template-syntax.yaml"></a>

```
  [Name](#cfn-pinpoint-campaign-template-name): {{String}}
  [Version](#cfn-pinpoint-campaign-template-version): {{String}}
```

## Properties
<a name="aws-properties-pinpoint-campaign-template-properties"></a>

`Name`  <a name="cfn-pinpoint-campaign-template-name"></a>
The name of the message template to use for the message. If specified, this value must match the name of an existing message template.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Version`  <a name="cfn-pinpoint-campaign-template-version"></a>
The unique identifier for the version of the message template to use for the message. If specified, this value must match the identifier for an existing template version. To retrieve a list of versions and version identifiers for a template, use the [Template Versions](https://docs.aws.amazon.com/pinpoint/latest/apireference/templates-template-name-template-type-versions.html) resource.
If you don't specify a value for this property, Amazon Pinpoint uses the *active version* of the template. The *active version* is typically the version of a template that's been most recently reviewed and approved for use, depending on your workflow. It isn't necessarily the latest version of a template.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

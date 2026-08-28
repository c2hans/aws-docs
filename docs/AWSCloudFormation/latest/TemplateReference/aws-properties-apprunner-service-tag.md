---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apprunner-service-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppRunner::Service Tag
<a name="aws-properties-apprunner-service-tag"></a>

Describes a tag that is applied to an AWS App Runner resource. A tag is a metadata item consisting of a key-value pair.

## Syntax
<a name="aws-properties-apprunner-service-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-apprunner-service-tag-syntax.json"></a>

```
{
  "[Key](#cfn-apprunner-service-tag-key)" : {{String}},
  "[Value](#cfn-apprunner-service-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-apprunner-service-tag-syntax.yaml"></a>

```
  [Key](#cfn-apprunner-service-tag-key): {{String}}
  [Value](#cfn-apprunner-service-tag-value): {{String}}
```

## Properties
<a name="aws-properties-apprunner-service-tag-properties"></a>

`Key`  <a name="cfn-apprunner-service-tag-key"></a>
The key of the tag assigned to an App Runner service.
*Required*: No
*Type*: String
*Pattern*: `^(?!aws:).+`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Value`  <a name="cfn-apprunner-service-tag-value"></a>
The value of the tag assigned to an App Runner service.
*Required*: No
*Type*: String
*Pattern*: `.*`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

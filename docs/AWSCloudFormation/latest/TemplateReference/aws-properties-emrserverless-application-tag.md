---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrserverless-application-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRServerless::Application Tag
<a name="aws-properties-emrserverless-application-tag"></a>

A map of key-value pairs to help you manage EMR Serverless resources. One resource can have a maximum of 50 tags. For more information, see [Tagging resources](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/tagging.html).

## Syntax
<a name="aws-properties-emrserverless-application-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrserverless-application-tag-syntax.json"></a>

```
{
  "[Key](#cfn-emrserverless-application-tag-key)" : {{String}},
  "[Value](#cfn-emrserverless-application-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-emrserverless-application-tag-syntax.yaml"></a>

```
  [Key](#cfn-emrserverless-application-tag-key): {{String}}
  [Value](#cfn-emrserverless-application-tag-value): {{String}}
```

## Properties
<a name="aws-properties-emrserverless-application-tag-properties"></a>

`Key`  <a name="cfn-emrserverless-application-tag-key"></a>
The key to use in the tag.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9 /_.:=+@-]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-emrserverless-application-tag-value"></a>
The value of the tag.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9 /_.:=+@-]*$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

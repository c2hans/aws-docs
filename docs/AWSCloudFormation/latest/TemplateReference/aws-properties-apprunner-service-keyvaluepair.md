---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apprunner-service-keyvaluepair.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppRunner::Service KeyValuePair
<a name="aws-properties-apprunner-service-keyvaluepair"></a>

Describes a key-value pair, which is a string-to-string mapping.

## Syntax
<a name="aws-properties-apprunner-service-keyvaluepair-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-apprunner-service-keyvaluepair-syntax.json"></a>

```
{
  "[Name](#cfn-apprunner-service-keyvaluepair-name)" : {{String}},
  "[Value](#cfn-apprunner-service-keyvaluepair-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-apprunner-service-keyvaluepair-syntax.yaml"></a>

```
  [Name](#cfn-apprunner-service-keyvaluepair-name): {{String}}
  [Value](#cfn-apprunner-service-keyvaluepair-value): {{String}}
```

## Properties
<a name="aws-properties-apprunner-service-keyvaluepair-properties"></a>

`Name`  <a name="cfn-apprunner-service-keyvaluepair-name"></a>
The key name string to map to a value.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-apprunner-service-keyvaluepair-value"></a>
The value string to which the key name is mapped.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

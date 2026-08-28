---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-schema-registry.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Schema Registry
<a name="aws-properties-glue-schema-registry"></a>

Specifies a registry in the AWS Glue Schema Registry.

## Syntax
<a name="aws-properties-glue-schema-registry-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-schema-registry-syntax.json"></a>

```
{
  "[Arn](#cfn-glue-schema-registry-arn)" : {{String}},
  "[Name](#cfn-glue-schema-registry-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-glue-schema-registry-syntax.yaml"></a>

```
  [Arn](#cfn-glue-schema-registry-arn): {{String}}
  [Name](#cfn-glue-schema-registry-name): {{String}}
```

## Properties
<a name="aws-properties-glue-schema-registry-properties"></a>

`Arn`  <a name="cfn-glue-schema-registry-arn"></a>
The Amazon Resource Name (ARN) of the registry.
*Required*: No
*Type*: String
*Pattern*: `arn:aws(-(cn|us-gov|iso(-[bef])?))?:glue:.*`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-glue-schema-registry-name"></a>
The name of the registry.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

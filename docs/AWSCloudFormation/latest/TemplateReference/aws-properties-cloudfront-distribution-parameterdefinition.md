---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-distribution-parameterdefinition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::Distribution ParameterDefinition
<a name="aws-properties-cloudfront-distribution-parameterdefinition"></a>

A list of parameter values to add to the resource. A parameter is specified as a key-value pair. A valid parameter value must exist for any parameter that is marked as required in the multi-tenant distribution.

## Syntax
<a name="aws-properties-cloudfront-distribution-parameterdefinition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-distribution-parameterdefinition-syntax.json"></a>

```
{
  "[Definition](#cfn-cloudfront-distribution-parameterdefinition-definition)" : {{Definition}},
  "[Name](#cfn-cloudfront-distribution-parameterdefinition-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudfront-distribution-parameterdefinition-syntax.yaml"></a>

```
  [Definition](#cfn-cloudfront-distribution-parameterdefinition-definition): {{
    Definition}}
  [Name](#cfn-cloudfront-distribution-parameterdefinition-name): {{String}}
```

## Properties
<a name="aws-properties-cloudfront-distribution-parameterdefinition-properties"></a>

`Definition`  <a name="cfn-cloudfront-distribution-parameterdefinition-definition"></a>
The value that you assigned to the parameter.
*Required*: Yes
*Type*: [Definition](aws-properties-cloudfront-distribution-definition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-cloudfront-distribution-parameterdefinition-name"></a>
The name of the parameter.
*Required*: Yes
*Type*: String
*Pattern*: `[a-zA-Z0-9-_]+`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

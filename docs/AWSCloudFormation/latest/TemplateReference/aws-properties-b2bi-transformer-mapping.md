---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-b2bi-transformer-mapping.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::B2BI::Transformer Mapping
<a name="aws-properties-b2bi-transformer-mapping"></a>

Specifies the mapping template for the transformer. This template is used to map the parsed EDI file using JSONata or XSLT.

## Syntax
<a name="aws-properties-b2bi-transformer-mapping-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-b2bi-transformer-mapping-syntax.json"></a>

```
{
  "[Template](#cfn-b2bi-transformer-mapping-template)" : {{String}},
  "[TemplateLanguage](#cfn-b2bi-transformer-mapping-templatelanguage)" : {{String}}
}
```

### YAML
<a name="aws-properties-b2bi-transformer-mapping-syntax.yaml"></a>

```
  [Template](#cfn-b2bi-transformer-mapping-template): {{String}}
  [TemplateLanguage](#cfn-b2bi-transformer-mapping-templatelanguage): {{String}}
```

## Properties
<a name="aws-properties-b2bi-transformer-mapping-properties"></a>

`Template`  <a name="cfn-b2bi-transformer-mapping-template"></a>
A string that represents the mapping template, in the transformation language specified in `templateLanguage`.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `350000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TemplateLanguage`  <a name="cfn-b2bi-transformer-mapping-templatelanguage"></a>
The transformation language for the template, either XSLT or JSONATA.
*Required*: Yes
*Type*: String
*Allowed values*: `XSLT | JSONATA`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

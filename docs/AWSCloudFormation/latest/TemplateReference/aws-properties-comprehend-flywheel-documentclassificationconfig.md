---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-comprehend-flywheel-documentclassificationconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Comprehend::Flywheel DocumentClassificationConfig
<a name="aws-properties-comprehend-flywheel-documentclassificationconfig"></a>

Configuration required for a document classification model.

## Syntax
<a name="aws-properties-comprehend-flywheel-documentclassificationconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-comprehend-flywheel-documentclassificationconfig-syntax.json"></a>

```
{
  "[Labels](#cfn-comprehend-flywheel-documentclassificationconfig-labels)" : {{[ String, ... ]}},
  "[Mode](#cfn-comprehend-flywheel-documentclassificationconfig-mode)" : {{String}}
}
```

### YAML
<a name="aws-properties-comprehend-flywheel-documentclassificationconfig-syntax.yaml"></a>

```
  [Labels](#cfn-comprehend-flywheel-documentclassificationconfig-labels): {{
    - String}}
  [Mode](#cfn-comprehend-flywheel-documentclassificationconfig-mode): {{String}}
```

## Properties
<a name="aws-properties-comprehend-flywheel-documentclassificationconfig-properties"></a>

`Labels`  <a name="cfn-comprehend-flywheel-documentclassificationconfig-labels"></a>
One or more labels to associate with the custom classifier.
*Required*: No
*Type*: Array of String
*Maximum*: `5000 | 1000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Mode`  <a name="cfn-comprehend-flywheel-documentclassificationconfig-mode"></a>
Classification mode indicates whether the documents are `MULTI_CLASS` or `MULTI_LABEL`.
*Required*: Yes
*Type*: String
*Allowed values*: `MULTI_CLASS | MULTI_LABEL`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

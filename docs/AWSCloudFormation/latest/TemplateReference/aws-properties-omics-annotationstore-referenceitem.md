---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-omics-annotationstore-referenceitem.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Omics::AnnotationStore ReferenceItem
<a name="aws-properties-omics-annotationstore-referenceitem"></a>

A genome reference.

## Syntax
<a name="aws-properties-omics-annotationstore-referenceitem-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-omics-annotationstore-referenceitem-syntax.json"></a>

```
{
  "[ReferenceArn](#cfn-omics-annotationstore-referenceitem-referencearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-omics-annotationstore-referenceitem-syntax.yaml"></a>

```
  [ReferenceArn](#cfn-omics-annotationstore-referenceitem-referencearn): {{String}}
```

## Properties
<a name="aws-properties-omics-annotationstore-referenceitem-properties"></a>

`ReferenceArn`  <a name="cfn-omics-annotationstore-referenceitem-referencearn"></a>
The reference's ARN.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:.+$`
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

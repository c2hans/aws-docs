---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-omics-variantstore-sseconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Omics::VariantStore SseConfig
<a name="aws-properties-omics-variantstore-sseconfig"></a>

Server-side encryption (SSE) settings for a store.

## Syntax
<a name="aws-properties-omics-variantstore-sseconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-omics-variantstore-sseconfig-syntax.json"></a>

```
{
  "[KeyArn](#cfn-omics-variantstore-sseconfig-keyarn)" : {{String}},
  "[Type](#cfn-omics-variantstore-sseconfig-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-omics-variantstore-sseconfig-syntax.yaml"></a>

```
  [KeyArn](#cfn-omics-variantstore-sseconfig-keyarn): {{String}}
  [Type](#cfn-omics-variantstore-sseconfig-type): {{String}}
```

## Properties
<a name="aws-properties-omics-variantstore-sseconfig-properties"></a>

`KeyArn`  <a name="cfn-omics-variantstore-sseconfig-keyarn"></a>
An encryption key ARN.
*Required*: No
*Type*: String
*Pattern*: `arn:([^: ]*):([^: ]*):([^: ]*):([0-9]{12}):([^: ]*)`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Type`  <a name="cfn-omics-variantstore-sseconfig-type"></a>
The encryption type.
*Required*: Yes
*Type*: String
*Allowed values*: `KMS`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

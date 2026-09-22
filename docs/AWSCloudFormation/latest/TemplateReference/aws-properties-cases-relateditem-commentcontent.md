---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cases-relateditem-commentcontent.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cases::RelatedItem CommentContent
<a name="aws-properties-cases-relateditem-commentcontent"></a>

Represents the content of a `Comment` to be returned to agents.

## Syntax
<a name="aws-properties-cases-relateditem-commentcontent-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cases-relateditem-commentcontent-syntax.json"></a>

```
{
  "[Body](#cfn-cases-relateditem-commentcontent-body)" : {{String}},
  "[ContentType](#cfn-cases-relateditem-commentcontent-contenttype)" : {{String}}
}
```

### YAML
<a name="aws-properties-cases-relateditem-commentcontent-syntax.yaml"></a>

```
  [Body](#cfn-cases-relateditem-commentcontent-body): {{String}}
  [ContentType](#cfn-cases-relateditem-commentcontent-contenttype): {{String}}
```

## Properties
<a name="aws-properties-cases-relateditem-commentcontent-properties"></a>

`Body`  <a name="cfn-cases-relateditem-commentcontent-body"></a>
Text in the body of a `Comment` on a case.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `15000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ContentType`  <a name="cfn-cases-relateditem-commentcontent-contenttype"></a>
Type of the text in the box of a `Comment` on a case.
*Required*: Yes
*Type*: String
*Allowed values*: `Text/Plain`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

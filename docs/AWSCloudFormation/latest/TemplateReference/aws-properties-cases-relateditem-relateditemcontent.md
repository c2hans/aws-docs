---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cases-relateditem-relateditemcontent.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cases::RelatedItem RelatedItemContent
<a name="aws-properties-cases-relateditem-relateditemcontent"></a>

Represents the content of a particular type of related item.

## Syntax
<a name="aws-properties-cases-relateditem-relateditemcontent-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cases-relateditem-relateditemcontent-syntax.json"></a>

```
{
  "[Comment](#cfn-cases-relateditem-relateditemcontent-comment)" : {{CommentContent}}
}
```

### YAML
<a name="aws-properties-cases-relateditem-relateditemcontent-syntax.yaml"></a>

```
  [Comment](#cfn-cases-relateditem-relateditemcontent-comment): {{
    CommentContent}}
```

## Properties
<a name="aws-properties-cases-relateditem-relateditemcontent-properties"></a>

`Comment`  <a name="cfn-cases-relateditem-relateditemcontent-comment"></a>
Represents the content of a comment to be returned to agents.
*Required*: No
*Type*: [CommentContent](aws-properties-cases-relateditem-commentcontent.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

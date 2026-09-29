---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-wisdom-content.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::Content
<a name="aws-resource-wisdom-content"></a>

Creates Amazon Q in Connect content. Before to calling this API, use [StartContentUpload](https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_StartContentUpload.html) to upload an asset.

## Syntax
<a name="aws-resource-wisdom-content-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-wisdom-content-syntax.json"></a>

```
{
  "Type" : "AWS::Wisdom::Content",
  "Properties" : {
      "[KnowledgeBaseId](#cfn-wisdom-content-knowledgebaseid)" : {{String}},
      "[Metadata](#cfn-wisdom-content-metadata)" : {{{{{Key}}: {{Value}}, ...}}},
      "[Name](#cfn-wisdom-content-name)" : {{String}},
      "[OverrideLinkOutUri](#cfn-wisdom-content-overridelinkouturi)" : {{String}},
      "[Tags](#cfn-wisdom-content-tags)" : {{[ Tag, ... ]}},
      "[Title](#cfn-wisdom-content-title)" : {{String}},
      "[UploadId](#cfn-wisdom-content-uploadid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-wisdom-content-syntax.yaml"></a>

```
Type: AWS::Wisdom::Content
Properties:
  [KnowledgeBaseId](#cfn-wisdom-content-knowledgebaseid): {{String}}
  [Metadata](#cfn-wisdom-content-metadata): {{
    {{Key}}: {{Value}}}}
  [Name](#cfn-wisdom-content-name): {{String}}
  [OverrideLinkOutUri](#cfn-wisdom-content-overridelinkouturi): {{String}}
  [Tags](#cfn-wisdom-content-tags): {{
    - Tag}}
  [Title](#cfn-wisdom-content-title): {{String}}
  [UploadId](#cfn-wisdom-content-uploadid): {{String}}
```

## Properties
<a name="aws-resource-wisdom-content-properties"></a>

`KnowledgeBaseId`  <a name="cfn-wisdom-content-knowledgebaseid"></a>
The identifier of the knowledge base.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Metadata`  <a name="cfn-wisdom-content-metadata"></a>
A key/value map to store attributes without affecting tagging or recommendations. For example, when synchronizing data between an external system and Amazon Q in Connect, you can store an external version identifier as metadata to utilize for determining drift.
*Required*: No
*Type*: Object of String
*Pattern*: `^.+$`
*Minimum*: `1`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-wisdom-content-name"></a>
The name of the content.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9\s_.,-]+`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OverrideLinkOutUri`  <a name="cfn-wisdom-content-overridelinkouturi"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-wisdom-content-tags"></a>
The tags used to organize, track, or control access for this resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-wisdom-content-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Title`  <a name="cfn-wisdom-content-title"></a>
The title of the content.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UploadId`  <a name="cfn-wisdom-content-uploadid"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-wisdom-content-return-values"></a>

### Ref
<a name="aws-resource-wisdom-content-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-wisdom-content-return-values-fn--getatt"></a>

####
<a name="aws-resource-wisdom-content-return-values-fn--getatt-fn--getatt"></a>

`ContentArn`  <a name="ContentArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the content.

`ContentId`  <a name="ContentId-fn::getatt"></a>
The identifier of the content.

`ContentType`  <a name="ContentType-fn::getatt"></a>
The media type of the content.

`KnowledgeBaseArn`  <a name="KnowledgeBaseArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the knowledge base.

`LinkOutUri`  <a name="LinkOutUri-fn::getatt"></a>
The URI of the content.

`RevisionId`  <a name="RevisionId-fn::getatt"></a>
The identifier of the content revision.

`Status`  <a name="Status-fn::getatt"></a>
The status of the content.

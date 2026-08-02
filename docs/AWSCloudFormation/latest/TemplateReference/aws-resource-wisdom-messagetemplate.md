---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-wisdom-messagetemplate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::MessageTemplate
<a name="aws-resource-wisdom-messagetemplate"></a>

Creates an Amazon Q in Connect message template. The name of the message template has to be unique for each knowledge base. The channel subtype of the message template is immutable and cannot be modified after creation. After the message template is created, you can use the `$LATEST` qualifier to reference the created message template.

## Syntax
<a name="aws-resource-wisdom-messagetemplate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-wisdom-messagetemplate-syntax.json"></a>

```
{
  "Type" : "AWS::Wisdom::MessageTemplate",
  "Properties" : {
      "[ChannelSubtype](#cfn-wisdom-messagetemplate-channelsubtype)" : {{String}},
      "[Content](#cfn-wisdom-messagetemplate-content)" : {{Content}},
      "[DefaultAttributes](#cfn-wisdom-messagetemplate-defaultattributes)" : {{MessageTemplateAttributes}},
      "[Description](#cfn-wisdom-messagetemplate-description)" : {{String}},
      "[GroupingConfiguration](#cfn-wisdom-messagetemplate-groupingconfiguration)" : {{GroupingConfiguration}},
      "[KnowledgeBaseArn](#cfn-wisdom-messagetemplate-knowledgebasearn)" : {{String}},
      "[Language](#cfn-wisdom-messagetemplate-language)" : {{String}},
      "[MessageTemplateAttachments](#cfn-wisdom-messagetemplate-messagetemplateattachments)" : {{[ MessageTemplateAttachment, ... ]}},
      "[Name](#cfn-wisdom-messagetemplate-name)" : {{String}},
      "[Tags](#cfn-wisdom-messagetemplate-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-wisdom-messagetemplate-syntax.yaml"></a>

```
Type: AWS::Wisdom::MessageTemplate
Properties:
  [ChannelSubtype](#cfn-wisdom-messagetemplate-channelsubtype): {{String}}
  [Content](#cfn-wisdom-messagetemplate-content): {{
    Content}}
  [DefaultAttributes](#cfn-wisdom-messagetemplate-defaultattributes): {{
    MessageTemplateAttributes}}
  [Description](#cfn-wisdom-messagetemplate-description): {{String}}
  [GroupingConfiguration](#cfn-wisdom-messagetemplate-groupingconfiguration): {{
    GroupingConfiguration}}
  [KnowledgeBaseArn](#cfn-wisdom-messagetemplate-knowledgebasearn): {{String}}
  [Language](#cfn-wisdom-messagetemplate-language): {{String}}
  [MessageTemplateAttachments](#cfn-wisdom-messagetemplate-messagetemplateattachments): {{
    - MessageTemplateAttachment}}
  [Name](#cfn-wisdom-messagetemplate-name): {{String}}
  [Tags](#cfn-wisdom-messagetemplate-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-wisdom-messagetemplate-properties"></a>

`ChannelSubtype`  <a name="cfn-wisdom-messagetemplate-channelsubtype"></a>
The channel subtype this message template applies to.
*Required*: Yes
*Type*: String
*Allowed values*: `EMAIL | SMS`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Content`  <a name="cfn-wisdom-messagetemplate-content"></a>
The content of the message template.
*Required*: Yes
*Type*: [Content](aws-properties-wisdom-messagetemplate-content.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultAttributes`  <a name="cfn-wisdom-messagetemplate-defaultattributes"></a>
An object that specifies the default values to use for variables in the message template. This object contains different categories of key-value pairs. Each key defines a variable or placeholder in the message template. The corresponding value defines the default value for that variable.
*Required*: No
*Type*: [MessageTemplateAttributes](aws-properties-wisdom-messagetemplate-messagetemplateattributes.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-wisdom-messagetemplate-description"></a>
The description of the message template.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9\\s_.,-]+`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GroupingConfiguration`  <a name="cfn-wisdom-messagetemplate-groupingconfiguration"></a>
The configuration information of the external data source.
*Required*: No
*Type*: [GroupingConfiguration](aws-properties-wisdom-messagetemplate-groupingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KnowledgeBaseArn`  <a name="cfn-wisdom-messagetemplate-knowledgebasearn"></a>
The Amazon Resource Name (ARN) of the knowledge base.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})?$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Language`  <a name="cfn-wisdom-messagetemplate-language"></a>
The language code value for the language in which the quick response is written. The supported language codes include `de_DE`, `en_US`, `es_ES`, `fr_FR`, `id_ID`, `it_IT`, `ja_JP`, `ko_KR`, `pt_BR`, `zh_CN`, `zh_TW`
*Required*: No
*Type*: String
*Minimum*: `2`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MessageTemplateAttachments`  <a name="cfn-wisdom-messagetemplate-messagetemplateattachments"></a>
List of message template attachments.
*Required*: No
*Type*: Array of [MessageTemplateAttachment](aws-properties-wisdom-messagetemplate-messagetemplateattachment.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-wisdom-messagetemplate-name"></a>
The name of the message template.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9\\s_.,-]+`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-wisdom-messagetemplate-tags"></a>
The tags used to organize, track, or control access for this resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-wisdom-messagetemplate-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-wisdom-messagetemplate-return-values"></a>

### Ref
<a name="aws-resource-wisdom-messagetemplate-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-wisdom-messagetemplate-return-values-fn--getatt"></a>

####
<a name="aws-resource-wisdom-messagetemplate-return-values-fn--getatt-fn--getatt"></a>

`MessageTemplateArn`  <a name="MessageTemplateArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the message template.

`MessageTemplateContentSha256`  <a name="MessageTemplateContentSha256-fn::getatt"></a>
The checksum value of the message template content that is referenced by the `$LATEST` qualifier. It can be returned in `MessageTemplateData` or `ExtendedMessageTemplateData`. It’s calculated by content, language, `defaultAttributes` and `Attachments` of the message template.

`MessageTemplateId`  <a name="MessageTemplateId-fn::getatt"></a>
The identifier of the message template.

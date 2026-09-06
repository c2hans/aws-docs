---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-wisdom-quickresponse.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::QuickResponse
<a name="aws-resource-wisdom-quickresponse"></a>

Creates an Amazon Q in Connect quick response.

## Syntax
<a name="aws-resource-wisdom-quickresponse-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-wisdom-quickresponse-syntax.json"></a>

```
{
  "Type" : "AWS::Wisdom::QuickResponse",
  "Properties" : {
      "[Channels](#cfn-wisdom-quickresponse-channels)" : {{[ String, ... ]}},
      "[Content](#cfn-wisdom-quickresponse-content)" : {{QuickResponseContentProvider}},
      "[ContentType](#cfn-wisdom-quickresponse-contenttype)" : {{String}},
      "[Description](#cfn-wisdom-quickresponse-description)" : {{String}},
      "[GroupingConfiguration](#cfn-wisdom-quickresponse-groupingconfiguration)" : {{GroupingConfiguration}},
      "[IsActive](#cfn-wisdom-quickresponse-isactive)" : {{Boolean}},
      "[KnowledgeBaseArn](#cfn-wisdom-quickresponse-knowledgebasearn)" : {{String}},
      "[Language](#cfn-wisdom-quickresponse-language)" : {{String}},
      "[Name](#cfn-wisdom-quickresponse-name)" : {{String}},
      "[ShortcutKey](#cfn-wisdom-quickresponse-shortcutkey)" : {{String}},
      "[Tags](#cfn-wisdom-quickresponse-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-wisdom-quickresponse-syntax.yaml"></a>

```
Type: AWS::Wisdom::QuickResponse
Properties:
  [Channels](#cfn-wisdom-quickresponse-channels): {{
    - String}}
  [Content](#cfn-wisdom-quickresponse-content): {{
    QuickResponseContentProvider}}
  [ContentType](#cfn-wisdom-quickresponse-contenttype): {{String}}
  [Description](#cfn-wisdom-quickresponse-description): {{String}}
  [GroupingConfiguration](#cfn-wisdom-quickresponse-groupingconfiguration): {{
    GroupingConfiguration}}
  [IsActive](#cfn-wisdom-quickresponse-isactive): {{Boolean}}
  [KnowledgeBaseArn](#cfn-wisdom-quickresponse-knowledgebasearn): {{String}}
  [Language](#cfn-wisdom-quickresponse-language): {{String}}
  [Name](#cfn-wisdom-quickresponse-name): {{String}}
  [ShortcutKey](#cfn-wisdom-quickresponse-shortcutkey): {{String}}
  [Tags](#cfn-wisdom-quickresponse-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-wisdom-quickresponse-properties"></a>

`Channels`  <a name="cfn-wisdom-quickresponse-channels"></a>
The Connect Customer contact channels this quick response applies to. The supported contact channel types include `Chat`.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Content`  <a name="cfn-wisdom-quickresponse-content"></a>
The content of the quick response.
*Required*: Yes
*Type*: [QuickResponseContentProvider](aws-properties-wisdom-quickresponse-quickresponsecontentprovider.md)
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ContentType`  <a name="cfn-wisdom-quickresponse-contenttype"></a>
The media type of the quick response content.
+ Use `application/x.quickresponse;format=plain` for quick response written in plain text.
+ Use `application/x.quickresponse;format=markdown` for quick response written in richtext.
*Required*: No
*Type*: String
*Pattern*: `^(application/x\.quickresponse;format=(plain|markdown))$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-wisdom-quickresponse-description"></a>
The description of the quick response.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GroupingConfiguration`  <a name="cfn-wisdom-quickresponse-groupingconfiguration"></a>
The configuration information of the user groups that the quick response is accessible to.
*Required*: No
*Type*: [GroupingConfiguration](aws-properties-wisdom-quickresponse-groupingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IsActive`  <a name="cfn-wisdom-quickresponse-isactive"></a>
Whether the quick response is active.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KnowledgeBaseArn`  <a name="cfn-wisdom-quickresponse-knowledgebasearn"></a>
The Amazon Resource Name (ARN) of the knowledge base.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Language`  <a name="cfn-wisdom-quickresponse-language"></a>
The language code value for the language in which the quick response is written. The supported language codes include `de_DE`, `en_US`, `es_ES`, `fr_FR`, `id_ID`, `it_IT`, `ja_JP`, `ko_KR`, `pt_BR`, `zh_CN`, `zh_TW`
*Required*: No
*Type*: String
*Minimum*: `2`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-wisdom-quickresponse-name"></a>
The name of the quick response.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShortcutKey`  <a name="cfn-wisdom-quickresponse-shortcutkey"></a>
The shortcut key of the quick response. The value should be unique across the knowledge base.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-wisdom-quickresponse-tags"></a>
The tags used to organize, track, or control access for this resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-wisdom-quickresponse-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-wisdom-quickresponse-return-values"></a>

### Ref
<a name="aws-resource-wisdom-quickresponse-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-wisdom-quickresponse-return-values-fn--getatt"></a>

####
<a name="aws-resource-wisdom-quickresponse-return-values-fn--getatt-fn--getatt"></a>

`QuickResponseArn`  <a name="QuickResponseArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the quick response.

`QuickResponseId`  <a name="QuickResponseId-fn::getatt"></a>
The identifier of the quick response.

`Status`  <a name="Status-fn::getatt"></a>
The status of the quick response data.

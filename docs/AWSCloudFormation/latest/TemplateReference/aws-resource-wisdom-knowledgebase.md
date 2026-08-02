---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-wisdom-knowledgebase.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::KnowledgeBase
<a name="aws-resource-wisdom-knowledgebase"></a>

Specifies a knowledge base.

## Syntax
<a name="aws-resource-wisdom-knowledgebase-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-wisdom-knowledgebase-syntax.json"></a>

```
{
  "Type" : "AWS::Wisdom::KnowledgeBase",
  "Properties" : {
      "[Description](#cfn-wisdom-knowledgebase-description)" : {{String}},
      "[KnowledgeBaseType](#cfn-wisdom-knowledgebase-knowledgebasetype)" : {{String}},
      "[Name](#cfn-wisdom-knowledgebase-name)" : {{String}},
      "[RenderingConfiguration](#cfn-wisdom-knowledgebase-renderingconfiguration)" : {{RenderingConfiguration}},
      "[ServerSideEncryptionConfiguration](#cfn-wisdom-knowledgebase-serversideencryptionconfiguration)" : {{ServerSideEncryptionConfiguration}},
      "[SourceConfiguration](#cfn-wisdom-knowledgebase-sourceconfiguration)" : {{SourceConfiguration}},
      "[Tags](#cfn-wisdom-knowledgebase-tags)" : {{[ Tag, ... ]}},
      "[VectorIngestionConfiguration](#cfn-wisdom-knowledgebase-vectoringestionconfiguration)" : {{VectorIngestionConfiguration}}
    }
}
```

### YAML
<a name="aws-resource-wisdom-knowledgebase-syntax.yaml"></a>

```
Type: AWS::Wisdom::KnowledgeBase
Properties:
  [Description](#cfn-wisdom-knowledgebase-description): {{String}}
  [KnowledgeBaseType](#cfn-wisdom-knowledgebase-knowledgebasetype): {{String}}
  [Name](#cfn-wisdom-knowledgebase-name): {{String}}
  [RenderingConfiguration](#cfn-wisdom-knowledgebase-renderingconfiguration): {{
    RenderingConfiguration}}
  [ServerSideEncryptionConfiguration](#cfn-wisdom-knowledgebase-serversideencryptionconfiguration): {{
    ServerSideEncryptionConfiguration}}
  [SourceConfiguration](#cfn-wisdom-knowledgebase-sourceconfiguration): {{
    SourceConfiguration}}
  [Tags](#cfn-wisdom-knowledgebase-tags): {{
    - Tag}}
  [VectorIngestionConfiguration](#cfn-wisdom-knowledgebase-vectoringestionconfiguration): {{
    VectorIngestionConfiguration}}
```

## Properties
<a name="aws-resource-wisdom-knowledgebase-properties"></a>

`Description`  <a name="cfn-wisdom-knowledgebase-description"></a>
The description.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`KnowledgeBaseType`  <a name="cfn-wisdom-knowledgebase-knowledgebasetype"></a>
The type of knowledge base. Only CUSTOM knowledge bases allow you to upload your own content. EXTERNAL knowledge bases support integrations with third-party systems whose content is synchronized automatically.
*Required*: Yes
*Type*: String
*Allowed values*: `EXTERNAL | CUSTOM | MESSAGE_TEMPLATES | MANAGED | QUICK_RESPONSES`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-wisdom-knowledgebase-name"></a>
The name of the knowledge base.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RenderingConfiguration`  <a name="cfn-wisdom-knowledgebase-renderingconfiguration"></a>
Information about how to render the content.
*Required*: No
*Type*: [RenderingConfiguration](aws-properties-wisdom-knowledgebase-renderingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServerSideEncryptionConfiguration`  <a name="cfn-wisdom-knowledgebase-serversideencryptionconfiguration"></a>
This customer managed key must have a policy that allows `kms:CreateGrant` and `kms:DescribeKey` permissions to the IAM identity using the key to invoke Wisdom. For more information about setting up a customer managed key for Wisdom, see [Enable Connect Customer Wisdom for your instance](https://docs.aws.amazon.com/connect/latest/adminguide/enable-wisdom.html). For information about valid ID values, see [Key identifiers (KeyId)](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id) in the *AWS Key Management Service Developer Guide*.
*Required*: No
*Type*: [ServerSideEncryptionConfiguration](aws-properties-wisdom-knowledgebase-serversideencryptionconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SourceConfiguration`  <a name="cfn-wisdom-knowledgebase-sourceconfiguration"></a>
The source of the knowledge base content. Only set this argument for EXTERNAL or Managed knowledge bases.
*Required*: No
*Type*: [SourceConfiguration](aws-properties-wisdom-knowledgebase-sourceconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-wisdom-knowledgebase-tags"></a>
The tags used to organize, track, or control access for this resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-wisdom-knowledgebase-tag.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VectorIngestionConfiguration`  <a name="cfn-wisdom-knowledgebase-vectoringestionconfiguration"></a>
Contains details about how to ingest the documents in a data source.
*Required*: No
*Type*: [VectorIngestionConfiguration](aws-properties-wisdom-knowledgebase-vectoringestionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-wisdom-knowledgebase-return-values"></a>

### Ref
<a name="aws-resource-wisdom-knowledgebase-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the knowledge base ID.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-wisdom-knowledgebase-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-wisdom-knowledgebase-return-values-fn--getatt-fn--getatt"></a>

`KnowledgeBaseArn`  <a name="KnowledgeBaseArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the knowledge base.

`KnowledgeBaseId`  <a name="KnowledgeBaseId-fn::getatt"></a>
The ID of the knowledge base.

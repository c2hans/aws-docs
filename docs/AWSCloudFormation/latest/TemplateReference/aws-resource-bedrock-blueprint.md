---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrock-blueprint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Blueprint
<a name="aws-resource-bedrock-blueprint"></a>

Details about a data automation blueprint.

## Syntax
<a name="aws-resource-bedrock-blueprint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bedrock-blueprint-syntax.json"></a>

```
{
  "Type" : "AWS::Bedrock::Blueprint",
  "Properties" : {
      "[BlueprintName](#cfn-bedrock-blueprint-blueprintname)" : {{String}},
      "[KmsEncryptionContext](#cfn-bedrock-blueprint-kmsencryptioncontext)" : {{{{{Key}}: {{Value}}, ...}}},
      "[KmsKeyId](#cfn-bedrock-blueprint-kmskeyid)" : {{String}},
      "[Schema](#cfn-bedrock-blueprint-schema)" : {{Json}},
      "[Tags](#cfn-bedrock-blueprint-tags)" : {{[ Tag, ... ]}},
      "[Type](#cfn-bedrock-blueprint-type)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-bedrock-blueprint-syntax.yaml"></a>

```
Type: AWS::Bedrock::Blueprint
Properties:
  [BlueprintName](#cfn-bedrock-blueprint-blueprintname): {{String}}
  [KmsEncryptionContext](#cfn-bedrock-blueprint-kmsencryptioncontext): {{
    {{Key}}: {{Value}}}}
  [KmsKeyId](#cfn-bedrock-blueprint-kmskeyid): {{String}}
  [Schema](#cfn-bedrock-blueprint-schema): {{Json}}
  [Tags](#cfn-bedrock-blueprint-tags): {{
    - Tag}}
  [Type](#cfn-bedrock-blueprint-type): {{String}}
```

## Properties
<a name="aws-resource-bedrock-blueprint-properties"></a>

`BlueprintName`  <a name="cfn-bedrock-blueprint-blueprintname"></a>
The blueprint's name.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9-_]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`KmsEncryptionContext`  <a name="cfn-bedrock-blueprint-kmsencryptioncontext"></a>
Name-value pairs to include as an encryption context.
*Required*: No
*Type*: Object of String
*Pattern*: `^.*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyId`  <a name="cfn-bedrock-blueprint-kmskeyid"></a>
The AWS KMS key to use for encryption.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Schema`  <a name="cfn-bedrock-blueprint-schema"></a>
The blueprint's schema.
*Required*: Yes
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-bedrock-blueprint-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-bedrock-blueprint-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-bedrock-blueprint-type"></a>
The blueprint's type.
*Required*: Yes
*Type*: String
*Allowed values*: `DOCUMENT | IMAGE | AUDIO | VIDEO`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-bedrock-blueprint-return-values"></a>

### Ref
<a name="aws-resource-bedrock-blueprint-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-bedrock-blueprint-return-values-fn--getatt"></a>

####
<a name="aws-resource-bedrock-blueprint-return-values-fn--getatt-fn--getatt"></a>

`BlueprintArn`  <a name="BlueprintArn-fn::getatt"></a>
The blueprint's ARN.

`BlueprintStage`  <a name="BlueprintStage-fn::getatt"></a>
The blueprint's stage.

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
When the blueprint was created.

`LastModifiedTime`  <a name="LastModifiedTime-fn::getatt"></a>
When the blueprint was last updated.

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrock-dataautomationlibrary.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataAutomationLibrary
<a name="aws-resource-bedrock-dataautomationlibrary"></a>

A data automation library.

## Syntax
<a name="aws-resource-bedrock-dataautomationlibrary-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bedrock-dataautomationlibrary-syntax.json"></a>

```
{
  "Type" : "AWS::Bedrock::DataAutomationLibrary",
  "Properties" : {
      "[EncryptionConfiguration](#cfn-bedrock-dataautomationlibrary-encryptionconfiguration)" : {{EncryptionConfiguration}},
      "[LibraryDescription](#cfn-bedrock-dataautomationlibrary-librarydescription)" : {{String}},
      "[LibraryName](#cfn-bedrock-dataautomationlibrary-libraryname)" : {{String}},
      "[Tags](#cfn-bedrock-dataautomationlibrary-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-bedrock-dataautomationlibrary-syntax.yaml"></a>

```
Type: AWS::Bedrock::DataAutomationLibrary
Properties:
  [EncryptionConfiguration](#cfn-bedrock-dataautomationlibrary-encryptionconfiguration): {{
    EncryptionConfiguration}}
  [LibraryDescription](#cfn-bedrock-dataautomationlibrary-librarydescription): {{String}}
  [LibraryName](#cfn-bedrock-dataautomationlibrary-libraryname): {{String}}
  [Tags](#cfn-bedrock-dataautomationlibrary-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-bedrock-dataautomationlibrary-properties"></a>

`EncryptionConfiguration`  <a name="cfn-bedrock-dataautomationlibrary-encryptionconfiguration"></a>
Encryption settings for an invocation.
*Required*: No
*Type*: [EncryptionConfiguration](aws-properties-bedrock-dataautomationlibrary-encryptionconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LibraryDescription`  <a name="cfn-bedrock-dataautomationlibrary-librarydescription"></a>
The library's description.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `300`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LibraryName`  <a name="cfn-bedrock-dataautomationlibrary-libraryname"></a>
The library's name.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9-_]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-bedrock-dataautomationlibrary-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-bedrock-dataautomationlibrary-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-bedrock-dataautomationlibrary-return-values"></a>

### Ref
<a name="aws-resource-bedrock-dataautomationlibrary-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-bedrock-dataautomationlibrary-return-values-fn--getatt"></a>

####
<a name="aws-resource-bedrock-dataautomationlibrary-return-values-fn--getatt-fn--getatt"></a>

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
When the library was created.

`EntityTypes`  <a name="EntityTypes-fn::getatt"></a>
The entity types supported by the library.

`LibraryArn`  <a name="LibraryArn-fn::getatt"></a>
The library's ARN.

`Status`  <a name="Status-fn::getatt"></a>
The library's status.

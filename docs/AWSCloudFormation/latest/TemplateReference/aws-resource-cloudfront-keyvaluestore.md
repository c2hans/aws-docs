---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudfront-keyvaluestore.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::KeyValueStore
<a name="aws-resource-cloudfront-keyvaluestore"></a>

The key value store. Use this to separate data from function code, allowing you to update data without having to publish a new version of a function. The key value store holds keys and their corresponding values.

## Syntax
<a name="aws-resource-cloudfront-keyvaluestore-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cloudfront-keyvaluestore-syntax.json"></a>

```
{
  "Type" : "AWS::CloudFront::KeyValueStore",
  "Properties" : {
      "[Comment](#cfn-cloudfront-keyvaluestore-comment)" : {{String}},
      "[ImportSource](#cfn-cloudfront-keyvaluestore-importsource)" : {{ImportSource}},
      "[Name](#cfn-cloudfront-keyvaluestore-name)" : {{String}},
      "[Tags](#cfn-cloudfront-keyvaluestore-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-cloudfront-keyvaluestore-syntax.yaml"></a>

```
Type: AWS::CloudFront::KeyValueStore
Properties:
  [Comment](#cfn-cloudfront-keyvaluestore-comment): {{String}}
  [ImportSource](#cfn-cloudfront-keyvaluestore-importsource): {{
    ImportSource}}
  [Name](#cfn-cloudfront-keyvaluestore-name): {{String}}
  [Tags](#cfn-cloudfront-keyvaluestore-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-cloudfront-keyvaluestore-properties"></a>

`Comment`  <a name="cfn-cloudfront-keyvaluestore-comment"></a>
A comment to describe the Key Value Store. Omitting `Comment` from the template during updates will clear the existing comment (set to empty string). To preserve an existing comment, you must explicitly include it in the template.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ImportSource`  <a name="cfn-cloudfront-keyvaluestore-importsource"></a>
The import source for the key value store.
*Required*: No
*Type*: [ImportSource](aws-properties-cloudfront-keyvaluestore-importsource.md)
*Update requires*: Updates are not supported.

`Name`  <a name="cfn-cloudfront-keyvaluestore-name"></a>
The name of the key value store.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-cloudfront-keyvaluestore-tags"></a>
A complex type that contains zero or more `Tag` elements.
*Required*: No
*Type*: Array of [Tag](aws-properties-cloudfront-keyvaluestore-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cloudfront-keyvaluestore-return-values"></a>

### Ref
<a name="aws-resource-cloudfront-keyvaluestore-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-cloudfront-keyvaluestore-return-values-fn--getatt"></a>

####
<a name="aws-resource-cloudfront-keyvaluestore-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the key value store.

`Id`  <a name="Id-fn::getatt"></a>
The unique Id for the key value store.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the key value store. For more information, see [Key value store statuses](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/kvs-with-functions-create.html#key-value-store-status) in the *Amazon CloudFront Developer Guide.*

## Examples
<a name="aws-resource-cloudfront-keyvaluestore--examples"></a>

### Key value store
<a name="aws-resource-cloudfront-keyvaluestore--examples--Key_value_store"></a>

The following example creates a key value store named DemoKeyValueStore and a CloudFront function named DemoFunction.

#### JSON
<a name="aws-resource-cloudfront-keyvaluestore--examples--Key_value_store--json"></a>

```
{
    "Resources": {
        "KeyValueStore": {
            "Type": "AWS::CloudFront::KeyValueStore",
            "Properties": {"Name": "DemoKeyValueStore"}
        },
        "Function": {
            "Type": "AWS::CloudFront::Function",
            "Name": "DemoFunction",
            "FunctionConfig": {
                "Comment": "Function with KeyValueStore",
                "Runtime": "cloudfront-js-2.0",
                "KeyValueStoreAssociations": [
                    {
                        "KeyValueStoreARN": {"Fn::Sub": "${KeyValueStore.Arn}"}
                    }
                ]
            },
            "FunctionCode": {"Fn::Sub": "const kvsId = '${KeyValueStore.Id}';\n// ... remaining function code ..."},
            "AutoPublish": true
        }
    }
}
```

#### YAML
<a name="aws-resource-cloudfront-keyvaluestore--examples--Key_value_store--yaml"></a>

```
Resources:
  KeyValueStore:
    Type: 'AWS::CloudFront::KeyValueStore'
    Properties:
      Name: 'DemoKeyValueStore'
  Function:
    Type: 'AWS::CloudFront::Function'
    Properties:
      Name: 'DemoFunction'
      FunctionConfig:
        Comment: 'Function with KeyValueStore'
        Runtime: 'cloudfront-js-2.0'
        KeyValueStoreAssociations:
          - KeyValueStoreARN: !Sub '${KeyValueStore.Arn}'
      FunctionCode: !Sub |
        const kvsId = '${KeyValueStore.Id}';
        // ... Remaining function code ...
      AutoPublish: true
```

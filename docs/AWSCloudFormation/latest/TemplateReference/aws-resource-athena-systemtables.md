---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-athena-systemtables.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Athena::SystemTables
<a name="aws-resource-athena-systemtables"></a>

<a name="aws-resource-athena-systemtables-description"></a>The `AWS::Athena::SystemTables` resource Property description not available. for Athena.

## Syntax
<a name="aws-resource-athena-systemtables-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-athena-systemtables-syntax.json"></a>

```
{
  "Type" : "AWS::Athena::SystemTables",
  "Properties" : {
      "[KmsKeyArn](#cfn-athena-systemtables-kmskeyarn)" : {{String}},
      "[TableName](#cfn-athena-systemtables-tablename)" : {{String}},
      "[Tags](#cfn-athena-systemtables-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-athena-systemtables-syntax.yaml"></a>

```
Type: AWS::Athena::SystemTables
Properties:
  [KmsKeyArn](#cfn-athena-systemtables-kmskeyarn): {{String}}
  [TableName](#cfn-athena-systemtables-tablename): {{String}}
  [Tags](#cfn-athena-systemtables-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-athena-systemtables-properties"></a>

`KmsKeyArn`  <a name="cfn-athena-systemtables-kmskeyarn"></a>
The Amazon Resource Name (ARN) of the AWS Key Management Service (AWS KMS) key used for encrypting the system table data.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[a-z\-]*:kms:[a-z0-9\-]+:[0-9]{12}:key/(mrk-)?[0-9a-f\-]+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TableName`  <a name="cfn-athena-systemtables-tablename"></a>
The system table configuration. Always `ALL`.
*Required*: Yes
*Type*: String
*Allowed values*: `ALL`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-athena-systemtables-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-athena-systemtables-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-athena-systemtables-return-values"></a>

### Ref
<a name="aws-resource-athena-systemtables-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-athena-systemtables-return-values-fn--getatt"></a>

####
<a name="aws-resource-athena-systemtables-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date and time the system table configuration was created.

`LastModifiedAt`  <a name="LastModifiedAt-fn::getatt"></a>
The date and time the system table configuration was last modified.

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-glue-tableversion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::TableVersion
<a name="aws-resource-glue-tableversion"></a>

Specifies a version of a table.

## Syntax
<a name="aws-resource-glue-tableversion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-glue-tableversion-syntax.json"></a>

```
{
  "Type" : "AWS::Glue::TableVersion",
  "Properties" : {
      "[DatabaseName](#cfn-glue-tableversion-databasename)" : {{String}},
      "[TableName](#cfn-glue-tableversion-tablename)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-glue-tableversion-syntax.yaml"></a>

```
Type: AWS::Glue::TableVersion
Properties:
  [DatabaseName](#cfn-glue-tableversion-databasename): {{String}}
  [TableName](#cfn-glue-tableversion-tablename): {{String}}
```

## Properties
<a name="aws-resource-glue-tableversion-properties"></a>

`DatabaseName`  <a name="cfn-glue-tableversion-databasename"></a>
The name of the database. For Hive compatibility, this is folded to lowercase when it is stored.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TableName`  <a name="cfn-glue-tableversion-tablename"></a>
The name of the table in question.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-glue-tableversion-return-values"></a>

### Ref
<a name="aws-resource-glue-tableversion-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-glue-tableversion-return-values-fn--getatt"></a>

####
<a name="aws-resource-glue-tableversion-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`VersionId`  <a name="VersionId-fn::getatt"></a>
The ID value that identifies this table version. A `VersionId` is a string representation of an integer. Each version is incremented by 1.

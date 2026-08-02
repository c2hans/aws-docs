---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bcmdataexports-table.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BCMDataExports::Table
<a name="aws-resource-bcmdataexports-table"></a>

The details for the data export table.

## Syntax
<a name="aws-resource-bcmdataexports-table-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bcmdataexports-table-syntax.json"></a>

```
{
  "Type" : "AWS::BCMDataExports::Table",
  "Properties" : {
      "[TableName](#cfn-bcmdataexports-table-tablename)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-bcmdataexports-table-syntax.yaml"></a>

```
Type: AWS::BCMDataExports::Table
Properties:
  [TableName](#cfn-bcmdataexports-table-tablename): {{String}}
```

## Properties
<a name="aws-resource-bcmdataexports-table-properties"></a>

`TableName`  <a name="cfn-bcmdataexports-table-tablename"></a>
The name of the table.
*Required*: Yes
*Type*: String
*Pattern*: `^[\S\s]*$`
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-bcmdataexports-table-return-values"></a>

### Ref
<a name="aws-resource-bcmdataexports-table-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-bcmdataexports-table-return-values-fn--getatt"></a>

####
<a name="aws-resource-bcmdataexports-table-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`Description`  <a name="Description-fn::getatt"></a>
The description for the table.

`Schema`  <a name="Schema-fn::getatt"></a>
Property description not available.

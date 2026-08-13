---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-connect-datatableattribute.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::DataTableAttribute
<a name="aws-resource-connect-datatableattribute"></a>

Represents an attribute (column) in a data table. Attributes define the schema and validation rules for values that can be stored in the table. They specify the data type, constraints, and whether the attribute is used as a primary key for record identification.

## Syntax
<a name="aws-resource-connect-datatableattribute-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-connect-datatableattribute-syntax.json"></a>

```
{
  "Type" : "AWS::Connect::DataTableAttribute",
  "Properties" : {
      "[DataTableArn](#cfn-connect-datatableattribute-datatablearn)" : {{String}},
      "[Description](#cfn-connect-datatableattribute-description)" : {{String}},
      "[InstanceArn](#cfn-connect-datatableattribute-instancearn)" : {{String}},
      "[Name](#cfn-connect-datatableattribute-name)" : {{String}},
      "[Primary](#cfn-connect-datatableattribute-primary)" : {{Boolean}},
      "[Validation](#cfn-connect-datatableattribute-validation)" : {{Validation}},
      "[ValueType](#cfn-connect-datatableattribute-valuetype)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-connect-datatableattribute-syntax.yaml"></a>

```
Type: AWS::Connect::DataTableAttribute
Properties:
  [DataTableArn](#cfn-connect-datatableattribute-datatablearn): {{String}}
  [Description](#cfn-connect-datatableattribute-description): {{String}}
  [InstanceArn](#cfn-connect-datatableattribute-instancearn): {{String}}
  [Name](#cfn-connect-datatableattribute-name): {{String}}
  [Primary](#cfn-connect-datatableattribute-primary): {{Boolean}}
  [Validation](#cfn-connect-datatableattribute-validation): {{
    Validation}}
  [ValueType](#cfn-connect-datatableattribute-valuetype): {{String}}
```

## Properties
<a name="aws-resource-connect-datatableattribute-properties"></a>

`DataTableArn`  <a name="cfn-connect-datatableattribute-datatablearn"></a>
The Amazon Resource Name (ARN) of the data table that contains this attribute.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-connect-datatableattribute-description"></a>
An optional description explaining the purpose and usage of this attribute.
*Required*: No
*Type*: String
*Pattern*: `^[\P{C} ]+$`
*Minimum*: `0`
*Maximum*: `250`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceArn`  <a name="cfn-connect-datatableattribute-instancearn"></a>
The Amazon Resource Name (ARN) of the instance.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-connect-datatableattribute-name"></a>
The human-readable name of the attribute. Must be unique within the data table and conform to Connect naming standards.
*Required*: Yes
*Type*: String
*Pattern*: `^[\p{L}\p{Z}\p{N}\-_.:=@'|]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`Primary`  <a name="cfn-connect-datatableattribute-primary"></a>
Boolean indicating whether this attribute is used as a primary key for record identification. Primary attributes must have unique value combinations and cannot contain expressions.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Validation`  <a name="cfn-connect-datatableattribute-validation"></a>
The validation rules applied to values of this attribute. Based on JSON Schema Draft 2020-12 with additional Connect-specific validations for data integrity.
*Required*: No
*Type*: [Validation](aws-properties-connect-datatableattribute-validation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ValueType`  <a name="cfn-connect-datatableattribute-valuetype"></a>
The type of value allowed for this attribute. Must be one of TEXT, TEXT\_LIST, NUMBER, NUMBER\_LIST, or BOOLEAN. Determines how values are validated and processed.
*Required*: Yes
*Type*: String
*Allowed values*: `TEXT | NUMBER | BOOLEAN | TEXT_LIST | NUMBER_LIST`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-connect-datatableattribute-return-values"></a>

### Ref
<a name="aws-resource-connect-datatableattribute-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-connect-datatableattribute-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-connect-datatableattribute-return-values-fn--getatt-fn--getatt"></a>

`AttributeId`  <a name="AttributeId-fn::getatt"></a>
The unique identifier for the attribute within the data table.

`LastModifiedRegion`  <a name="LastModifiedRegion-fn::getatt"></a>
The AWS Region where this attribute was last modified, used for region replication.

`LastModifiedTime`  <a name="LastModifiedTime-fn::getatt"></a>
The timestamp when this attribute was last modified.

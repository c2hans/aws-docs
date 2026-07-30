---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cassandra-type-field.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cassandra::Type Field
<a name="aws-properties-cassandra-type-field"></a>

The name and data type of an individual field in a user-defined type (UDT). In addition to a Cassandra data type, you can also use another UDT. When you nest another UDT or collection data type, you have to declare them with the `FROZEN` keyword.

## Syntax
<a name="aws-properties-cassandra-type-field-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cassandra-type-field-syntax.json"></a>

```
{
  "[FieldName](#cfn-cassandra-type-field-fieldname)" : {{String}},
  "[FieldType](#cfn-cassandra-type-field-fieldtype)" : {{String}}
}
```

### YAML
<a name="aws-properties-cassandra-type-field-syntax.yaml"></a>

```
  [FieldName](#cfn-cassandra-type-field-fieldname): {{String}}
  [FieldType](#cfn-cassandra-type-field-fieldtype): {{String}}
```

## Properties
<a name="aws-properties-cassandra-type-field-properties"></a>

`FieldName`  <a name="cfn-cassandra-type-field-fieldname"></a>
The name of the field.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FieldType`  <a name="cfn-cassandra-type-field-fieldtype"></a>
The data type of the field. This can be any Cassandra data type or another user-defined type.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

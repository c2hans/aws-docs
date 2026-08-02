---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-globaltable-attributedefinition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DynamoDB::GlobalTable AttributeDefinition
<a name="aws-properties-dynamodb-globaltable-attributedefinition"></a>

Represents an attribute for describing the schema for the table and indexes.

## Syntax
<a name="aws-properties-dynamodb-globaltable-attributedefinition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dynamodb-globaltable-attributedefinition-syntax.json"></a>

```
{
  "[AttributeName](#cfn-dynamodb-globaltable-attributedefinition-attributename)" : {{String}},
  "[AttributeType](#cfn-dynamodb-globaltable-attributedefinition-attributetype)" : {{String}}
}
```

### YAML
<a name="aws-properties-dynamodb-globaltable-attributedefinition-syntax.yaml"></a>

```
  [AttributeName](#cfn-dynamodb-globaltable-attributedefinition-attributename): {{String}}
  [AttributeType](#cfn-dynamodb-globaltable-attributedefinition-attributetype): {{String}}
```

## Properties
<a name="aws-properties-dynamodb-globaltable-attributedefinition-properties"></a>

`AttributeName`  <a name="cfn-dynamodb-globaltable-attributedefinition-attributename"></a>
A name for the attribute.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AttributeType`  <a name="cfn-dynamodb-globaltable-attributedefinition-attributetype"></a>
The data type for the attribute, where:
+ `S` - the attribute is of type String
+ `N` - the attribute is of type Number
+ `B` - the attribute is of type Binary
*Required*: Yes
*Type*: String
*Allowed values*: `S | N | B`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

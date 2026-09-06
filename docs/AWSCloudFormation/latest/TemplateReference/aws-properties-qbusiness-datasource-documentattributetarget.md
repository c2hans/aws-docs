---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-qbusiness-datasource-documentattributetarget.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QBusiness::DataSource DocumentAttributeTarget
<a name="aws-properties-qbusiness-datasource-documentattributetarget"></a>

The target document attribute or metadata field you want to alter when ingesting documents into Amazon Q Business.

For example, you can delete all customer identification numbers associated with the documents, stored in the document metadata field called 'Customer\_ID' by setting the target key as 'Customer\_ID' and the deletion flag to `TRUE`. This removes all customer ID values in the field 'Customer\_ID'. This would scrub personally identifiable information from each document's metadata.

Amazon Q Business can't create a target field if it has not already been created as an index field. After you create your index field, you can create a document metadata field using [`DocumentAttributeTarget`](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeTarget.html). Amazon Q Business will then map your newly created document attribute to your index field.

You can also use this with [`DocumentAttributeCondition`](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeCondition.html).

## Syntax
<a name="aws-properties-qbusiness-datasource-documentattributetarget-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-qbusiness-datasource-documentattributetarget-syntax.json"></a>

```
{
  "[AttributeValueOperator](#cfn-qbusiness-datasource-documentattributetarget-attributevalueoperator)" : {{String}},
  "[Key](#cfn-qbusiness-datasource-documentattributetarget-key)" : {{String}},
  "[Value](#cfn-qbusiness-datasource-documentattributetarget-value)" : {{DocumentAttributeValue}}
}
```

### YAML
<a name="aws-properties-qbusiness-datasource-documentattributetarget-syntax.yaml"></a>

```
  [AttributeValueOperator](#cfn-qbusiness-datasource-documentattributetarget-attributevalueoperator): {{String}}
  [Key](#cfn-qbusiness-datasource-documentattributetarget-key): {{String}}
  [Value](#cfn-qbusiness-datasource-documentattributetarget-value): {{
    DocumentAttributeValue}}
```

## Properties
<a name="aws-properties-qbusiness-datasource-documentattributetarget-properties"></a>

`AttributeValueOperator`  <a name="cfn-qbusiness-datasource-documentattributetarget-attributevalueoperator"></a>
`TRUE` to delete the existing target value for your specified target attribute key. You cannot create a target value and set this to `TRUE`.
*Required*: No
*Type*: String
*Allowed values*: `DELETE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Key`  <a name="cfn-qbusiness-datasource-documentattributetarget-key"></a>
The identifier of the target document attribute or metadata field. For example, 'Department' could be an identifier for the target attribute or metadata field that includes the department names associated with the documents.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_][a-zA-Z0-9_-]*$`
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-qbusiness-datasource-documentattributetarget-value"></a>
The value of a document attribute. You can only provide one value for a document attribute.
*Required*: No
*Type*: [DocumentAttributeValue](aws-properties-qbusiness-datasource-documentattributevalue.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-qbusiness-datasource-documentattributecondition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QBusiness::DataSource DocumentAttributeCondition
<a name="aws-properties-qbusiness-datasource-documentattributecondition"></a>

The condition used for the target document attribute or metadata field when ingesting documents into Amazon Q Business. You use this with [`DocumentAttributeTarget`](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeTarget.html) to apply the condition.

For example, you can create the 'Department' target field and have it prefill department names associated with the documents based on information in the 'Source\_URI' field. Set the condition that if the 'Source\_URI' field contains 'financial' in its URI value, then prefill the target field 'Department' with the target value 'Finance' for the document.

Amazon Q Business can't create a target field if it has not already been created as an index field. After you create your index field, you can create a document metadata field using `DocumentAttributeTarget`. Amazon Q Business then will map your newly created metadata field to your index field.

## Syntax
<a name="aws-properties-qbusiness-datasource-documentattributecondition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-qbusiness-datasource-documentattributecondition-syntax.json"></a>

```
{
  "[Key](#cfn-qbusiness-datasource-documentattributecondition-key)" : {{String}},
  "[Operator](#cfn-qbusiness-datasource-documentattributecondition-operator)" : {{String}},
  "[Value](#cfn-qbusiness-datasource-documentattributecondition-value)" : {{DocumentAttributeValue}}
}
```

### YAML
<a name="aws-properties-qbusiness-datasource-documentattributecondition-syntax.yaml"></a>

```
  [Key](#cfn-qbusiness-datasource-documentattributecondition-key): {{String}}
  [Operator](#cfn-qbusiness-datasource-documentattributecondition-operator): {{String}}
  [Value](#cfn-qbusiness-datasource-documentattributecondition-value): {{
    DocumentAttributeValue}}
```

## Properties
<a name="aws-properties-qbusiness-datasource-documentattributecondition-properties"></a>

`Key`  <a name="cfn-qbusiness-datasource-documentattributecondition-key"></a>
The identifier of the document attribute used for the condition.
For example, 'Source\_URI' could be an identifier for the attribute or metadata field that contains source URIs associated with the documents.
Amazon Q Business currently doesn't support `_document_body` as an attribute key used for the condition.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_][a-zA-Z0-9_-]*$`
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Operator`  <a name="cfn-qbusiness-datasource-documentattributecondition-operator"></a>
The identifier of the document attribute used for the condition.
For example, 'Source\_URI' could be an identifier for the attribute or metadata field that contains source URIs associated with the documents.
Amazon Q Business currently does not support `_document_body` as an attribute key used for the condition.
*Required*: Yes
*Type*: String
*Allowed values*: `GREATER_THAN | GREATER_THAN_OR_EQUALS | LESS_THAN | LESS_THAN_OR_EQUALS | EQUALS | NOT_EQUALS | CONTAINS | NOT_CONTAINS | EXISTS | NOT_EXISTS | BEGINS_WITH`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-qbusiness-datasource-documentattributecondition-value"></a>
The value of a document attribute. You can only provide one value for a document attribute.
*Required*: No
*Type*: [DocumentAttributeValue](aws-properties-qbusiness-datasource-documentattributevalue.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

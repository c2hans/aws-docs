---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kendra-datasource-documentattributecondition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Kendra::DataSource DocumentAttributeCondition
<a name="aws-properties-kendra-datasource-documentattributecondition"></a>

The condition used for the target document attribute or metadata field when ingesting documents into Amazon Kendra. You use this with [DocumentAttributeTarget to apply the condition](https://docs.aws.amazon.com/kendra/latest/dg/API_DocumentAttributeTarget.html).

For example, you can create the 'Department' target field and have it prefill department names associated with the documents based on information in the 'Source\_URI' field. Set the condition that if the 'Source\_URI' field contains 'financial' in its URI value, then prefill the target field 'Department' with the target value 'Finance' for the document.

Amazon Kendra cannot create a target field if it has not already been created as an index field. After you create your index field, you can create a document metadata field using `DocumentAttributeTarget`. Amazon Kendra then will map your newly created metadata field to your index field.

## Syntax
<a name="aws-properties-kendra-datasource-documentattributecondition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kendra-datasource-documentattributecondition-syntax.json"></a>

```
{
  "[ConditionDocumentAttributeKey](#cfn-kendra-datasource-documentattributecondition-conditiondocumentattributekey)" : {{String}},
  "[ConditionOnValue](#cfn-kendra-datasource-documentattributecondition-conditiononvalue)" : {{DocumentAttributeValue}},
  "[Operator](#cfn-kendra-datasource-documentattributecondition-operator)" : {{String}}
}
```

### YAML
<a name="aws-properties-kendra-datasource-documentattributecondition-syntax.yaml"></a>

```
  [ConditionDocumentAttributeKey](#cfn-kendra-datasource-documentattributecondition-conditiondocumentattributekey): {{String}}
  [ConditionOnValue](#cfn-kendra-datasource-documentattributecondition-conditiononvalue): {{
    DocumentAttributeValue}}
  [Operator](#cfn-kendra-datasource-documentattributecondition-operator): {{String}}
```

## Properties
<a name="aws-properties-kendra-datasource-documentattributecondition-properties"></a>

`ConditionDocumentAttributeKey`  <a name="cfn-kendra-datasource-documentattributecondition-conditiondocumentattributekey"></a>
The identifier of the document attribute used for the condition.
For example, 'Source\_URI' could be an identifier for the attribute or metadata field that contains source URIs associated with the documents.
Amazon Kendra currently does not support `_document_body` as an attribute key used for the condition.
*Required*: Yes
*Type*: String
*Pattern*: `[a-zA-Z0-9_][a-zA-Z0-9_-]*`
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConditionOnValue`  <a name="cfn-kendra-datasource-documentattributecondition-conditiononvalue"></a>
The value used by the operator.
For example, you can specify the value 'financial' for strings in the 'Source\_URI' field that partially match or contain this value.
*Required*: No
*Type*: [DocumentAttributeValue](aws-properties-kendra-datasource-documentattributevalue.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Operator`  <a name="cfn-kendra-datasource-documentattributecondition-operator"></a>
The condition operator.
For example, you can use 'Contains' to partially match a string.
*Required*: Yes
*Type*: String
*Allowed values*: `GreaterThan | GreaterThanOrEquals | LessThan | LessThanOrEquals | Equals | NotEquals | Contains | NotContains | Exists | NotExists | BeginsWith`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

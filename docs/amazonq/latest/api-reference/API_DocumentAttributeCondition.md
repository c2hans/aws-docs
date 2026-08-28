---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeCondition.html
---

# DocumentAttributeCondition
<a name="API_DocumentAttributeCondition"></a>

The condition used for the target document attribute or metadata field when ingesting documents into Amazon Q Business. You use this with [`DocumentAttributeTarget`](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeTarget.html) to apply the condition.

For example, you can create the 'Department' target field and have it prefill department names associated with the documents based on information in the 'Source\_URI' field. Set the condition that if the 'Source\_URI' field contains 'financial' in its URI value, then prefill the target field 'Department' with the target value 'Finance' for the document.

Amazon Q Business can't create a target field if it has not already been created as an index field. After you create your index field, you can create a document metadata field using `DocumentAttributeTarget`. Amazon Q Business then will map your newly created metadata field to your index field.

## Contents
<a name="API_DocumentAttributeCondition_Contents"></a>

 ** key **   <a name="qbusiness-Type-DocumentAttributeCondition-key"></a>
The identifier of the document attribute used for the condition.
For example, 'Source\_URI' could be an identifier for the attribute or metadata field that contains source URIs associated with the documents.
Amazon Q Business currently doesn't support `_document_body` as an attribute key used for the condition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9_][a-zA-Z0-9_-]*`
Required: Yes

 ** operator **   <a name="qbusiness-Type-DocumentAttributeCondition-operator"></a>
The identifier of the document attribute used for the condition.
For example, 'Source\_URI' could be an identifier for the attribute or metadata field that contains source URIs associated with the documents.
Amazon Q Business currently does not support `_document_body` as an attribute key used for the condition.
Type: String
Valid Values: `GREATER_THAN | GREATER_THAN_OR_EQUALS | LESS_THAN | LESS_THAN_OR_EQUALS | EQUALS | NOT_EQUALS | CONTAINS | NOT_CONTAINS | EXISTS | NOT_EXISTS | BEGINS_WITH`
Required: Yes

 ** value **   <a name="qbusiness-Type-DocumentAttributeCondition-value"></a>
The value of a document attribute. You can only provide one value for a document attribute.
Type: [DocumentAttributeValue](API_DocumentAttributeValue.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_DocumentAttributeCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/DocumentAttributeCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/DocumentAttributeCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/DocumentAttributeCondition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_AttributeFilter.html
---

# AttributeFilter
<a name="API_AttributeFilter"></a>

Enables filtering of responses based on document attributes or metadata fields.

## Contents
<a name="API_AttributeFilter_Contents"></a>

 ** andAllFilters **   <a name="qbusiness-Type-AttributeFilter-andAllFilters"></a>
Performs a logical `AND` operation on all supplied filters.
Type: Array of [AttributeFilter](#API_AttributeFilter) objects
Required: No

 ** containsAll **   <a name="qbusiness-Type-AttributeFilter-containsAll"></a>
Returns `true` when a document contains all the specified document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html): `stringListValue`.
Type: [DocumentAttribute](API_DocumentAttribute.md) object
Required: No

 ** containsAny **   <a name="qbusiness-Type-AttributeFilter-containsAny"></a>
Returns `true` when a document contains any of the specified document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html): `stringListValue`.
Type: [DocumentAttribute](API_DocumentAttribute.md) object
Required: No

 ** equalsTo **   <a name="qbusiness-Type-AttributeFilter-equalsTo"></a>
Performs an equals operation on two document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html): `dateValue`, `longValue`, `stringListValue` and `stringValue`.
Type: [DocumentAttribute](API_DocumentAttribute.md) object
Required: No

 ** greaterThan **   <a name="qbusiness-Type-AttributeFilter-greaterThan"></a>
Performs a greater than operation on two document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html): `dateValue` and `longValue`.
Type: [DocumentAttribute](API_DocumentAttribute.md) object
Required: No

 ** greaterThanOrEquals **   <a name="qbusiness-Type-AttributeFilter-greaterThanOrEquals"></a>
Performs a greater or equals than operation on two document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html): `dateValue` and `longValue`.
Type: [DocumentAttribute](API_DocumentAttribute.md) object
Required: No

 ** lessThan **   <a name="qbusiness-Type-AttributeFilter-lessThan"></a>
Performs a less than operation on two document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html): `dateValue` and `longValue`.
Type: [DocumentAttribute](API_DocumentAttribute.md) object
Required: No

 ** lessThanOrEquals **   <a name="qbusiness-Type-AttributeFilter-lessThanOrEquals"></a>
Performs a less than or equals operation on two document attributes or metadata fields.Supported for the following [document attribute value type](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html): `dateValue` and `longValue`.
Type: [DocumentAttribute](API_DocumentAttribute.md) object
Required: No

 ** notFilter **   <a name="qbusiness-Type-AttributeFilter-notFilter"></a>
Performs a logical `NOT` operation on all supplied filters.
Type: [AttributeFilter](#API_AttributeFilter) object
Required: No

 ** orAllFilters **   <a name="qbusiness-Type-AttributeFilter-orAllFilters"></a>
 Performs a logical `OR` operation on all supplied filters.
Type: Array of [AttributeFilter](#API_AttributeFilter) objects
Required: No

## See Also
<a name="API_AttributeFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/AttributeFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/AttributeFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/AttributeFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

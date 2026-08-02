---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_AttributeFilter.html
---

# AttributeFilter
<a name="API_qapps_AttributeFilter"></a>

The filter criteria used on responses based on document attributes or metadata fields.

## Contents
<a name="API_qapps_AttributeFilter_Contents"></a>

 ** andAllFilters **   <a name="qbusiness-Type-qapps_AttributeFilter-andAllFilters"></a>
Performs a logical `AND` operation on all supplied filters.
Type: Array of [AttributeFilter](#API_qapps_AttributeFilter) objects
Required: No

 ** containsAll **   <a name="qbusiness-Type-qapps_AttributeFilter-containsAll"></a>
Returns `true` when a document contains all the specified document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html): `stringListValue`.
Type: [DocumentAttribute](API_qapps_DocumentAttribute.md) object
Required: No

 ** containsAny **   <a name="qbusiness-Type-qapps_AttributeFilter-containsAny"></a>
Returns `true` when a document contains any of the specified document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html): `stringListValue`.
Type: [DocumentAttribute](API_qapps_DocumentAttribute.md) object
Required: No

 ** equalsTo **   <a name="qbusiness-Type-qapps_AttributeFilter-equalsTo"></a>
Performs an *equals* operation on two document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html): `dateValue`, `longValue`, `stringListValue` and `stringValue`.
Type: [DocumentAttribute](API_qapps_DocumentAttribute.md) object
Required: No

 ** greaterThan **   <a name="qbusiness-Type-qapps_AttributeFilter-greaterThan"></a>
Performs a *greater than* operation on two document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html): `dateValue` and `longValue`.
Type: [DocumentAttribute](API_qapps_DocumentAttribute.md) object
Required: No

 ** greaterThanOrEquals **   <a name="qbusiness-Type-qapps_AttributeFilter-greaterThanOrEquals"></a>
Performs a *greater than or equals* operation on two document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html): `dateValue` and `longValue`.
Type: [DocumentAttribute](API_qapps_DocumentAttribute.md) object
Required: No

 ** lessThan **   <a name="qbusiness-Type-qapps_AttributeFilter-lessThan"></a>
Performs a *less than* operation on two document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html): `dateValue` and `longValue`.
Type: [DocumentAttribute](API_qapps_DocumentAttribute.md) object
Required: No

 ** lessThanOrEquals **   <a name="qbusiness-Type-qapps_AttributeFilter-lessThanOrEquals"></a>
Performs a *less than or equals* operation on two document attributes or metadata fields.Supported for the following [document attribute value type](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html): `dateValue` and `longValue`.
Type: [DocumentAttribute](API_qapps_DocumentAttribute.md) object
Required: No

 ** notFilter **   <a name="qbusiness-Type-qapps_AttributeFilter-notFilter"></a>
Performs a logical `NOT` operation on all supplied filters.
Type: [AttributeFilter](#API_qapps_AttributeFilter) object
Required: No

 ** orAllFilters **   <a name="qbusiness-Type-qapps_AttributeFilter-orAllFilters"></a>
 Performs a logical `OR` operation on all supplied filters.
Type: Array of [AttributeFilter](#API_qapps_AttributeFilter) objects
Required: No

## See Also
<a name="API_qapps_AttributeFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qapps-2023-11-27/AttributeFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qapps-2023-11-27/AttributeFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qapps-2023-11-27/AttributeFilter)

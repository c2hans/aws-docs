---
source_url: https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_CodegenGenericDataField.html
---

# CodegenGenericDataField
<a name="API_CodegenGenericDataField"></a>

Describes a field in a generic data schema.

## Contents
<a name="API_CodegenGenericDataField_Contents"></a>

 ** dataType **   <a name="amplifyuibuilder-Type-CodegenGenericDataField-dataType"></a>
The data type for the generic data field.
Type: String
Valid Values: `ID | String | Int | Float | AWSDate | AWSTime | AWSDateTime | AWSTimestamp | AWSEmail | AWSURL | AWSIPAddress | Boolean | AWSJSON | AWSPhone | Enum | Model | NonModel`
Required: Yes

 ** dataTypeValue **   <a name="amplifyuibuilder-Type-CodegenGenericDataField-dataTypeValue"></a>
The value of the data type for the generic data field.
Type: String
Required: Yes

 ** isArray **   <a name="amplifyuibuilder-Type-CodegenGenericDataField-isArray"></a>
Specifies whether the generic data field is an array.
Type: Boolean
Required: Yes

 ** readOnly **   <a name="amplifyuibuilder-Type-CodegenGenericDataField-readOnly"></a>
Specifies whether the generic data field is read-only.
Type: Boolean
Required: Yes

 ** required **   <a name="amplifyuibuilder-Type-CodegenGenericDataField-required"></a>
Specifies whether the generic data field is required.
Type: Boolean
Required: Yes

 ** relationship **   <a name="amplifyuibuilder-Type-CodegenGenericDataField-relationship"></a>
The relationship of the generic data schema.
Type: [CodegenGenericDataRelationshipType](API_CodegenGenericDataRelationshipType.md) object
Required: No

## See Also
<a name="API_CodegenGenericDataField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplifyuibuilder-2021-08-11/CodegenGenericDataField)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplifyuibuilder-2021-08-11/CodegenGenericDataField)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplifyuibuilder-2021-08-11/CodegenGenericDataField)

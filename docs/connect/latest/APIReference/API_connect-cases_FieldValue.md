---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_FieldValue.html
---

# FieldValue
<a name="API_connect-cases_FieldValue"></a>

Object for case field values.

## Contents
<a name="API_connect-cases_FieldValue_Contents"></a>

 ** id **   <a name="connect-Type-connect-cases_FieldValue-id"></a>
Unique identifier of a field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** value **   <a name="connect-Type-connect-cases_FieldValue-value"></a>
Union of potential field value types.
Type: [FieldValueUnion](API_connect-cases_FieldValueUnion.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## See Also
<a name="API_connect-cases_FieldValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/FieldValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/FieldValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/FieldValue)

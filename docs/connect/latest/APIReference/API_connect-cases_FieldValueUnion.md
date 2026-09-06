---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_FieldValueUnion.html
---

# FieldValueUnion
<a name="API_connect-cases_FieldValueUnion"></a>

Object to store union of Field values.

**Note**
The `Summary` system field accepts up to 3000 characters, while all other fields accept up to 4100 characters. If you use multi-byte characters, the effective character limit may be lower.

## Contents
<a name="API_connect-cases_FieldValueUnion_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** booleanValue **   <a name="connect-Type-connect-cases_FieldValueUnion-booleanValue"></a>
Can be either null, or have a Boolean value type. Only one value can be provided.
Type: Boolean
Required: No

 ** doubleValue **   <a name="connect-Type-connect-cases_FieldValueUnion-doubleValue"></a>
Can be either null, or have a Double number value type. Only one value can be provided.
Type: Double
Required: No

 ** emptyValue **   <a name="connect-Type-connect-cases_FieldValueUnion-emptyValue"></a>
An empty value.
Type: [EmptyFieldValue](API_connect-cases_EmptyFieldValue.md) object
Required: No

 ** stringValue **   <a name="connect-Type-connect-cases_FieldValueUnion-stringValue"></a>
String value type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4100.
Required: No

 ** userArnValue **   <a name="connect-Type-connect-cases_FieldValueUnion-userArnValue"></a>
Represents the user that performed the audit.
Type: String
Required: No

## See Also
<a name="API_connect-cases_FieldValueUnion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/FieldValueUnion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/FieldValueUnion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/FieldValueUnion)

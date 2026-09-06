---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_AuditEventFieldValueUnion.html
---

# AuditEventFieldValueUnion
<a name="API_connect-cases_AuditEventFieldValueUnion"></a>

Object to store union of Field values.

## Contents
<a name="API_connect-cases_AuditEventFieldValueUnion_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** booleanValue **   <a name="connect-Type-connect-cases_AuditEventFieldValueUnion-booleanValue"></a>
Can be either null, or have a Boolean value type. Only one value can be provided.
Type: Boolean
Required: No

 ** doubleValue **   <a name="connect-Type-connect-cases_AuditEventFieldValueUnion-doubleValue"></a>
Can be either null, or have a Double value type. Only one value can be provided.
Type: Double
Required: No

 ** emptyValue **   <a name="connect-Type-connect-cases_AuditEventFieldValueUnion-emptyValue"></a>
An empty value. You cannot set `EmptyFieldValue` on a field that is required on a case template.
This structure will never have any data members. It signifies an empty value on a case field.
Type: [EmptyFieldValue](API_connect-cases_EmptyFieldValue.md) object
Required: No

 ** stringValue **   <a name="connect-Type-connect-cases_AuditEventFieldValueUnion-stringValue"></a>
Can be either null, or have a String value type. Only one value can be provided.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4100.
Required: No

 ** userArnValue **   <a name="connect-Type-connect-cases_AuditEventFieldValueUnion-userArnValue"></a>
Can be either null, or have a String value type formatted as an ARN. Only one value can be provided.
Type: String
Required: No

## See Also
<a name="API_connect-cases_AuditEventFieldValueUnion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/AuditEventFieldValueUnion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/AuditEventFieldValueUnion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/AuditEventFieldValueUnion)

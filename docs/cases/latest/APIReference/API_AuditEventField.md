---
source_url: https://docs.aws.amazon.com/cases/latest/APIReference/API_AuditEventField.html
---

# AuditEventField
<a name="API_connect-cases_AuditEventField"></a>

Fields for audit event.

## Contents
<a name="API_connect-cases_AuditEventField_Contents"></a>

 ** eventFieldId **   <a name="connect-Type-connect-cases_AuditEventField-eventFieldId"></a>
Unique identifier of field in an Audit History entry.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** newValue **   <a name="connect-Type-connect-cases_AuditEventField-newValue"></a>
Union of potential field value types.
Type: [AuditEventFieldValueUnion](API_connect-cases_AuditEventFieldValueUnion.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** oldValue **   <a name="connect-Type-connect-cases_AuditEventField-oldValue"></a>
Union of potential field value types.
Type: [AuditEventFieldValueUnion](API_connect-cases_AuditEventFieldValueUnion.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_connect-cases_AuditEventField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/AuditEventField)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/AuditEventField)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/AuditEventField)

---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_AuditEvent.html
---

# AuditEvent
<a name="API_connect-cases_AuditEvent"></a>

Represents the content of a particular audit event.

## Contents
<a name="API_connect-cases_AuditEvent_Contents"></a>

 ** eventId **   <a name="connect-Type-connect-cases_AuditEvent-eventId"></a>
Unique identifier of a case audit history event.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** fields **   <a name="connect-Type-connect-cases_AuditEvent-fields"></a>
A list of Case Audit History event fields.
Type: Array of [AuditEventField](API_connect-cases_AuditEventField.md) objects
Required: Yes

 ** performedTime **   <a name="connect-Type-connect-cases_AuditEvent-performedTime"></a>
Time at which an Audit History event took place.
Type: Timestamp
Required: Yes

 ** type **   <a name="connect-Type-connect-cases_AuditEvent-type"></a>
The type of audit history event.
Valid Values: `Case.Created` \| `Case.Updated` \| `RelatedItem.Created` \| `RelatedItem.Updated` \| `RelatedItem.Deleted`
Type: String
Valid Values: `Case.Created | Case.Updated | RelatedItem.Created | RelatedItem.Deleted | RelatedItem.Updated`
Required: Yes

 ** performedBy **   <a name="connect-Type-connect-cases_AuditEvent-performedBy"></a>
Information of the user which performed the audit.
Type: [AuditEventPerformedBy](API_connect-cases_AuditEventPerformedBy.md) object
Required: No

 ** relatedItemType **   <a name="connect-Type-connect-cases_AuditEvent-relatedItemType"></a>
The Type of the related item.
Type: String
Valid Values: `Contact | Comment | File | Sla | ConnectCase | Custom`
Required: No

## See Also
<a name="API_connect-cases_AuditEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/AuditEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/AuditEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/AuditEvent)

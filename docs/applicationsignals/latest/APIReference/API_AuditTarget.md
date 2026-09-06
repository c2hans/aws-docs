---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_AuditTarget.html
---

# AuditTarget
<a name="API_AuditTarget"></a>

A structure that specifies the target entity for audit analysis, such as a `service`, `SLO`, `service_operation`, or `canary`.

## Contents
<a name="API_AuditTarget_Contents"></a>

 ** Data **   <a name="applicationsignals-Type-AuditTarget-Data"></a>
The specific data identifying the audit target entity.
Type: [AuditTargetEntity](API_AuditTargetEntity.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** Type **   <a name="applicationsignals-Type-AuditTarget-Type"></a>
The type of entity being audited, such as `service`, `SLO`, `service_operation`, or `canary`.
Type: String
Required: Yes

## See Also
<a name="API_AuditTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/AuditTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/AuditTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/AuditTarget)

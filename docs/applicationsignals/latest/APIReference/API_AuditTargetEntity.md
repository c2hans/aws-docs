---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_AuditTargetEntity.html
---

# AuditTargetEntity
<a name="API_AuditTargetEntity"></a>

A union structure that contains the specific entity information for different types of audit targets.

## Contents
<a name="API_AuditTargetEntity_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** Canary **   <a name="applicationsignals-Type-AuditTargetEntity-Canary"></a>
Canary entity information when the audit target is a CloudWatch Synthetics canary.
Type: [CanaryEntity](API_CanaryEntity.md) object
Required: No

 ** Service **   <a name="applicationsignals-Type-AuditTargetEntity-Service"></a>
Service entity information when the audit target is a service.
Type: [ServiceEntity](API_ServiceEntity.md) object
Required: No

 ** ServiceOperation **   <a name="applicationsignals-Type-AuditTargetEntity-ServiceOperation"></a>
Service operation entity information when the audit target is a specific service operation.
Type: [ServiceOperationEntity](API_ServiceOperationEntity.md) object
Required: No

 ** Slo **   <a name="applicationsignals-Type-AuditTargetEntity-Slo"></a>
SLO entity information when the audit target is a service level objective.
Type: [ServiceLevelObjectiveEntity](API_ServiceLevelObjectiveEntity.md) object
Required: No

## See Also
<a name="API_AuditTargetEntity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/AuditTargetEntity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/AuditTargetEntity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/AuditTargetEntity)

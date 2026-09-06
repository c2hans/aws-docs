---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_AuditFinding.html
---

# AuditFinding
<a name="API_AuditFinding"></a>

The findings (results) of the audit.

## Contents
<a name="API_AuditFinding_Contents"></a>

 ** checkName **   <a name="iot-Type-AuditFinding-checkName"></a>
The audit check that generated this result.
Type: String
Required: No

 ** findingId **   <a name="iot-Type-AuditFinding-findingId"></a>
A unique identifier for this set of audit findings. This identifier is used to apply mitigation tasks to one or more sets of findings.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

 ** findingTime **   <a name="iot-Type-AuditFinding-findingTime"></a>
The time the result (finding) was discovered.
Type: Timestamp
Required: No

 ** isSuppressed **   <a name="iot-Type-AuditFinding-isSuppressed"></a>
 Indicates whether the audit finding was suppressed or not during reporting.
Type: Boolean
Required: No

 ** nonCompliantResource **   <a name="iot-Type-AuditFinding-nonCompliantResource"></a>
The resource that was found to be noncompliant with the audit check.
Type: [NonCompliantResource](API_NonCompliantResource.md) object
Required: No

 ** reasonForNonCompliance **   <a name="iot-Type-AuditFinding-reasonForNonCompliance"></a>
The reason the resource was noncompliant.
Type: String
Required: No

 ** reasonForNonComplianceCode **   <a name="iot-Type-AuditFinding-reasonForNonComplianceCode"></a>
A code that indicates the reason that the resource was noncompliant.
Type: String
Required: No

 ** relatedResources **   <a name="iot-Type-AuditFinding-relatedResources"></a>
The list of related resources.
Type: Array of [RelatedResource](API_RelatedResource.md) objects
Required: No

 ** severity **   <a name="iot-Type-AuditFinding-severity"></a>
The severity of the result (finding).
Type: String
Valid Values: `CRITICAL | HIGH | MEDIUM | LOW`
Required: No

 ** taskId **   <a name="iot-Type-AuditFinding-taskId"></a>
The ID of the audit that generated this result (finding).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 40.
Pattern: `[a-zA-Z0-9\-]+`
Required: No

 ** taskStartTime **   <a name="iot-Type-AuditFinding-taskStartTime"></a>
The time the audit started.
Type: Timestamp
Required: No

## See Also
<a name="API_AuditFinding_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/AuditFinding)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/AuditFinding)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/AuditFinding)

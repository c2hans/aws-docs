---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_AuditCheckDetails.html
---

# AuditCheckDetails
<a name="API_AuditCheckDetails"></a>

Information about the audit check.

## Contents
<a name="API_AuditCheckDetails_Contents"></a>

 ** checkCompliant **   <a name="iot-Type-AuditCheckDetails-checkCompliant"></a>
True if the check is complete and found all resources compliant.
Type: Boolean
Required: No

 ** checkRunStatus **   <a name="iot-Type-AuditCheckDetails-checkRunStatus"></a>
The completion status of this check. One of "IN\_PROGRESS", "WAITING\_FOR\_DATA\_COLLECTION", "CANCELED", "COMPLETED\_COMPLIANT", "COMPLETED\_NON\_COMPLIANT", or "FAILED".
Type: String
Valid Values: `IN_PROGRESS | WAITING_FOR_DATA_COLLECTION | CANCELED | COMPLETED_COMPLIANT | COMPLETED_NON_COMPLIANT | FAILED`
Required: No

 ** errorCode **   <a name="iot-Type-AuditCheckDetails-errorCode"></a>
The code of any error encountered when this check is performed during this audit. One of "INSUFFICIENT\_PERMISSIONS" or "AUDIT\_CHECK\_DISABLED".
Type: String
Required: No

 ** message **   <a name="iot-Type-AuditCheckDetails-message"></a>
The message associated with any error encountered when this check is performed during this audit.
Type: String
Length Constraints: Maximum length of 2048.
Required: No

 ** nonCompliantResourcesCount **   <a name="iot-Type-AuditCheckDetails-nonCompliantResourcesCount"></a>
The number of resources that were found noncompliant during the check.
Type: Long
Required: No

 ** suppressedNonCompliantResourcesCount **   <a name="iot-Type-AuditCheckDetails-suppressedNonCompliantResourcesCount"></a>
 Describes how many of the non-compliant resources created during the evaluation of an audit check were marked as suppressed.
Type: Long
Required: No

 ** totalResourcesCount **   <a name="iot-Type-AuditCheckDetails-totalResourcesCount"></a>
The number of resources on which the check was performed.
Type: Long
Required: No

## See Also
<a name="API_AuditCheckDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/AuditCheckDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/AuditCheckDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/AuditCheckDetails)

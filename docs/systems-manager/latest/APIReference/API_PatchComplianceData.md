---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_PatchComplianceData.html
---

# PatchComplianceData
<a name="API_PatchComplianceData"></a>

Information about the state of a patch on a particular managed node as it relates to the patch baseline used to patch the node.

## Contents
<a name="API_PatchComplianceData_Contents"></a>

 ** Classification **   <a name="systemsmanager-Type-PatchComplianceData-Classification"></a>
The classification of the patch, such as `SecurityUpdates`, `Updates`, and `CriticalUpdates`.
Type: String
Required: Yes

 ** InstalledTime **   <a name="systemsmanager-Type-PatchComplianceData-InstalledTime"></a>
The date/time the patch was installed on the managed node. Not all operating systems provide this level of information.
Type: Timestamp
Required: Yes

 ** KBId **   <a name="systemsmanager-Type-PatchComplianceData-KBId"></a>
The operating system-specific ID of the patch.
Type: String
Required: Yes

 ** Severity **   <a name="systemsmanager-Type-PatchComplianceData-Severity"></a>
The severity of the patch such as `Critical`, `Important`, and `Moderate`.
Type: String
Required: Yes

 ** State **   <a name="systemsmanager-Type-PatchComplianceData-State"></a>
The state of the patch on the managed node, such as INSTALLED or FAILED.
For descriptions of each patch state, see [About patch compliance](https://docs.aws.amazon.com/systems-manager/latest/userguide/compliance-about.html#compliance-monitor-patch) in the * AWS Systems Manager User Guide*.
Type: String
Valid Values: `INSTALLED | INSTALLED_OTHER | INSTALLED_PENDING_REBOOT | INSTALLED_REJECTED | MISSING | NOT_APPLICABLE | FAILED | AVAILABLE_SECURITY_UPDATE`
Required: Yes

 ** Title **   <a name="systemsmanager-Type-PatchComplianceData-Title"></a>
The title of the patch.
Type: String
Required: Yes

 ** CVEIds **   <a name="systemsmanager-Type-PatchComplianceData-CVEIds"></a>
The IDs of one or more Common Vulnerabilities and Exposure (CVE) issues that are resolved by the patch.
Currently, CVE ID values are reported only for patches with a status of `Missing` or `Failed`.
Type: String
Required: No

## See Also
<a name="API_PatchComplianceData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/PatchComplianceData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/PatchComplianceData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/PatchComplianceData)

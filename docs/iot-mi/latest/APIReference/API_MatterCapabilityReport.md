---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_MatterCapabilityReport.html
---

# MatterCapabilityReport
<a name="API_MatterCapabilityReport"></a>

Matter based capability report.

## Contents
<a name="API_MatterCapabilityReport_Contents"></a>

 ** endpoints **   <a name="managedintegrations-Type-MatterCapabilityReport-endpoints"></a>
The endpoints used in the capability report.
Type: Array of [MatterCapabilityReportEndpoint](API_MatterCapabilityReportEndpoint.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: Yes

 ** version **   <a name="managedintegrations-Type-MatterCapabilityReport-version"></a>
The version of the capability report.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `1\.0\.0`
Required: Yes

 ** nodeId **   <a name="managedintegrations-Type-MatterCapabilityReport-nodeId"></a>
The numeric identifier of the node.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9=_.,@\+\-/]+`
Required: No

## See Also
<a name="API_MatterCapabilityReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/MatterCapabilityReport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/MatterCapabilityReport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/MatterCapabilityReport)

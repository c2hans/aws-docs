---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_CapabilityReport.html
---

# CapabilityReport
<a name="API_CapabilityReport"></a>

Report of all capabilities supported by the device.

## Contents
<a name="API_CapabilityReport_Contents"></a>

 ** endpoints **   <a name="managedintegrations-Type-CapabilityReport-endpoints"></a>
The endpoints used in the capability report.
Type: Array of [CapabilityReportEndpoint](API_CapabilityReportEndpoint.md) objects
Array Members: Minimum number of 0 items. Maximum number of 40 items.
Required: Yes

 ** version **   <a name="managedintegrations-Type-CapabilityReport-version"></a>
The version of the capability report.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `1\.0\.0`
Required: Yes

 ** nodeId **   <a name="managedintegrations-Type-CapabilityReport-nodeId"></a>
The numeric identifier of the node.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9=_.,@\+\-/]+`
Required: No

## See Also
<a name="API_CapabilityReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/CapabilityReport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/CapabilityReport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/CapabilityReport)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

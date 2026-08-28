---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_CapabilityReportCapability.html
---

# CapabilityReportCapability
<a name="API_CapabilityReportCapability"></a>

The capability used in capability report.

## Contents
<a name="API_CapabilityReportCapability_Contents"></a>

 ** actions **   <a name="managedintegrations-Type-CapabilityReportCapability-actions"></a>
The capability actions used in the capability report.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[/a-zA-Z0-9\._ -]+`
Required: Yes

 ** events **   <a name="managedintegrations-Type-CapabilityReportCapability-events"></a>
The capability events used in the capability report.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[/a-zA-Z0-9\._ -]+`
Required: Yes

 ** id **   <a name="managedintegrations-Type-CapabilityReportCapability-id"></a>
The id of the schema version.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 128.
Pattern: `[a-zA-Z0-9.]+@(\d+\.\d+(\.\d+)?|\$latest)`
Required: Yes

 ** name **   <a name="managedintegrations-Type-CapabilityReportCapability-name"></a>
The name of the capability.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[/a-zA-Z0-9\._ -]+`
Required: Yes

 ** properties **   <a name="managedintegrations-Type-CapabilityReportCapability-properties"></a>
The capability properties used in the capability report.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[/a-zA-Z0-9\._ -]+`
Required: Yes

 ** version **   <a name="managedintegrations-Type-CapabilityReportCapability-version"></a>
The version of the capability.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(0|[1-9][0-9]*)`
Required: Yes

## See Also
<a name="API_CapabilityReportCapability_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/CapabilityReportCapability)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/CapabilityReportCapability)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/CapabilityReportCapability)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_CapabilityReportEndpoint.html
---

# CapabilityReportEndpoint
<a name="API_CapabilityReportEndpoint"></a>

The endpoint used in the capability report.

## Contents
<a name="API_CapabilityReportEndpoint_Contents"></a>

 ** capabilities **   <a name="managedintegrations-Type-CapabilityReportEndpoint-capabilities"></a>
The capabilities used in the capability report.
Type: Array of [CapabilityReportCapability](API_CapabilityReportCapability.md) objects
Array Members: Minimum number of 0 items. Maximum number of 40 items.
Required: Yes

 ** deviceTypes **   <a name="managedintegrations-Type-CapabilityReportEndpoint-deviceTypes"></a>
The type of device.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[a-zA-Z0-9=_. ,@\+\-/]+`
Required: Yes

 ** id **   <a name="managedintegrations-Type-CapabilityReportEndpoint-id"></a>
The id of the endpoint used in the capability report.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-zA-Z]+`
Required: Yes

## See Also
<a name="API_CapabilityReportEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/CapabilityReportEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/CapabilityReportEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/CapabilityReportEndpoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

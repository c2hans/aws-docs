---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_MatterCapabilityReportEndpoint.html
---

# MatterCapabilityReportEndpoint
<a name="API_MatterCapabilityReportEndpoint"></a>

Matter endpoint used in capability report.

## Contents
<a name="API_MatterCapabilityReportEndpoint_Contents"></a>

 ** clusters **   <a name="managedintegrations-Type-MatterCapabilityReportEndpoint-clusters"></a>
Matter clusters used in capability report.
Type: Array of [MatterCapabilityReportCluster](API_MatterCapabilityReportCluster.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: Yes

 ** deviceTypes **   <a name="managedintegrations-Type-MatterCapabilityReportEndpoint-deviceTypes"></a>
The type of device.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[a-zA-Z0-9=_. ,@\+\-/]+`
Required: Yes

 ** id **   <a name="managedintegrations-Type-MatterCapabilityReportEndpoint-id"></a>
The id of the AWS Matter capability report endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-zA-Z]+`
Required: Yes

 ** clientClusters **   <a name="managedintegrations-Type-MatterCapabilityReportEndpoint-clientClusters"></a>
Semantic information related to endpoint.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 32 items.
Length Constraints: Minimum length of 1. Maximum length of 24.
Pattern: `0[xX][0-9a-fA-F]+$|^[0-9]+`
Required: No

 ** parts **   <a name="managedintegrations-Type-MatterCapabilityReportEndpoint-parts"></a>
Heirachy of child endpoints contained in the given endpoint.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 32 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-zA-Z]+`
Required: No

 ** semanticTags **   <a name="managedintegrations-Type-MatterCapabilityReportEndpoint-semanticTags"></a>
Semantic information related to endpoint.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 32 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[0-9a-zA-Z._-]+`
Required: No

## See Also
<a name="API_MatterCapabilityReportEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/MatterCapabilityReportEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/MatterCapabilityReportEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/MatterCapabilityReportEndpoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

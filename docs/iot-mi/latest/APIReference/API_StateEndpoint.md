---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_StateEndpoint.html
---

# StateEndpoint
<a name="API_StateEndpoint"></a>

Describe the endpoint with an Id, a name, and the relevant capabilities for reporting state

## Contents
<a name="API_StateEndpoint_Contents"></a>

 ** capabilities **   <a name="managedintegrations-Type-StateEndpoint-capabilities"></a>
Describe the endpoint with an id, a name, and the relevant capabilities for the reporting state.
Type: Array of [StateCapability](API_StateCapability.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: Yes

 ** endpointId **   <a name="managedintegrations-Type-StateEndpoint-endpointId"></a>
Numeric identifier of the endpoint
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-zA-Z]+`
Required: Yes

## See Also
<a name="API_StateEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/StateEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/StateEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/StateEndpoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

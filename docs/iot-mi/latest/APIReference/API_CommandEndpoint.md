---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_CommandEndpoint.html
---

# CommandEndpoint
<a name="API_CommandEndpoint"></a>

The endpoint for a managed thing when sending a command.

## Contents
<a name="API_CommandEndpoint_Contents"></a>

 ** capabilities **   <a name="managedintegrations-Type-CommandEndpoint-capabilities"></a>
Describe the endpoint with an id, a name, and the relevant capabilities for sending commands.
Type: Array of [CommandCapability](API_CommandCapability.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: Yes

 ** endpointId **   <a name="managedintegrations-Type-CommandEndpoint-endpointId"></a>
The id of the endpoint for a managed thing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-zA-Z]+`
Required: Yes

## See Also
<a name="API_CommandEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/CommandEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/CommandEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/CommandEndpoint)

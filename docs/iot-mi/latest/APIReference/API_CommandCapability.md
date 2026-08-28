---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_CommandCapability.html
---

# CommandCapability
<a name="API_CommandCapability"></a>

The command capabilities added for the managed thing

## Contents
<a name="API_CommandCapability_Contents"></a>

 ** actions **   <a name="managedintegrations-Type-CommandCapability-actions"></a>
Describe the command capability with the actions it supports.
Type: Array of [CapabilityAction](API_CapabilityAction.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: Yes

 ** id **   <a name="managedintegrations-Type-CommandCapability-id"></a>
Describe the capability with an id.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 128.
Pattern: `[a-zA-Z0-9.]+@(\d+\.\d+(\.\d+)?|\$latest)`
Required: Yes

 ** name **   <a name="managedintegrations-Type-CommandCapability-name"></a>
Describe the capability with an name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[/a-zA-Z0-9\._ -]+`
Required: Yes

 ** version **   <a name="managedintegrations-Type-CommandCapability-version"></a>
Describe the capability with a version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(0|[1-9][0-9]*)`
Required: Yes

## See Also
<a name="API_CommandCapability_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/CommandCapability)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/CommandCapability)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/CommandCapability)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

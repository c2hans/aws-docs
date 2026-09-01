---
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_UpdatedAutoDetectionConfiguration.html
---

# UpdatedAutoDetectionConfiguration
<a name="API_UpdatedAutoDetectionConfiguration"></a>

A wrapper for updating the auto-detection configuration of a registry with PATCH semantics. Include this wrapper to replace the auto-detection configuration with the specified value. Omit it to leave the auto-detection configuration unchanged. To clear the configuration, include the wrapper with a null `optionalValue`.

## Contents
<a name="API_UpdatedAutoDetectionConfiguration_Contents"></a>

 ** optionalValue **   <a name="agentregistrycontrol-Type-UpdatedAutoDetectionConfiguration-optionalValue"></a>
The value to set for this field. Omit the wrapper to leave the field unchanged.
Type: [AutoDetectionConfiguration](API_AutoDetectionConfiguration.md) object
Required: No

## See Also
<a name="API_UpdatedAutoDetectionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/UpdatedAutoDetectionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/UpdatedAutoDetectionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/UpdatedAutoDetectionConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AgentRegistry Control Plane API Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agent-registry-control` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

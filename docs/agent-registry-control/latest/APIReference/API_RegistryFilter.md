---
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_RegistryFilter.html
---

# RegistryFilter
<a name="API_RegistryFilter"></a>

A single filter applied to a ListRegistries request.

## Contents
<a name="API_RegistryFilter_Contents"></a>

 ** name **   <a name="agentregistrycontrol-Type-RegistryFilter-name"></a>
The attribute to filter on
Type: String
Valid Values: `status | discoveryConfiguration.authorizerType`
Required: Yes

 ** values **   <a name="agentregistrycontrol-Type-RegistryFilter-values"></a>
The values to match for the attribute
Type: Array of strings
Array Members: Fixed number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## See Also
<a name="API_RegistryFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/RegistryFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/RegistryFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/RegistryFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AgentRegistry Control Plane API Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agent-registry-control` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_AuthorizerConfiguration.html
---

# AuthorizerConfiguration
<a name="API_AuthorizerConfiguration"></a>

The authorizer configuration for a registry. Exactly one member is set.

## Contents
<a name="API_AuthorizerConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** customJWTAuthorizer **   <a name="agentregistrycontrol-Type-AuthorizerConfiguration-customJWTAuthorizer"></a>
Configuration for a custom JWT authorizer.
Type: [CustomJWTAuthorizerConfiguration](API_CustomJWTAuthorizerConfiguration.md) object
Required: No

## See Also
<a name="API_AuthorizerConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/AuthorizerConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/AuthorizerConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/AuthorizerConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AgentRegistry Control Plane API Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agent-registry-control` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

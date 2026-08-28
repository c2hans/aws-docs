---
source_url: https://docs.aws.amazon.com/grafana/latest/APIReference/API_SamlAuthentication.html
---

# SamlAuthentication
<a name="API_SamlAuthentication"></a>

A structure containing information about how this workspace works with SAML.

## Contents
<a name="API_SamlAuthentication_Contents"></a>

 ** status **   <a name="ManagedGrafana-Type-SamlAuthentication-status"></a>
Specifies whether the workspace's SAML configuration is complete.
Type: String
Valid Values: `CONFIGURED | NOT_CONFIGURED`
Required: Yes

 ** configuration **   <a name="ManagedGrafana-Type-SamlAuthentication-configuration"></a>
A structure containing details about how this workspace works with SAML.
Type: [SamlConfiguration](API_SamlConfiguration.md) object
Required: No

## See Also
<a name="API_SamlAuthentication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/grafana-2020-08-18/SamlAuthentication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/grafana-2020-08-18/SamlAuthentication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/grafana-2020-08-18/SamlAuthentication)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Grafana. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query grafana` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

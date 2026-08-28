---
source_url: https://docs.aws.amazon.com/grafana/latest/APIReference/API_RoleValues.html
---

# RoleValues
<a name="API_RoleValues"></a>

This structure defines which groups defined in the SAML assertion attribute are to be mapped to the Grafana `Admin` and `Editor` roles in the workspace. SAML authenticated users not part of `Admin` or `Editor` role groups have `Viewer` permission over the workspace.

## Contents
<a name="API_RoleValues_Contents"></a>

 ** admin **   <a name="ManagedGrafana-Type-RoleValues-admin"></a>
A list of groups from the SAML assertion attribute to grant the Grafana `Admin` role to.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** editor **   <a name="ManagedGrafana-Type-RoleValues-editor"></a>
A list of groups from the SAML assertion attribute to grant the Grafana `Editor` role to.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_RoleValues_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/grafana-2020-08-18/RoleValues)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/grafana-2020-08-18/RoleValues)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/grafana-2020-08-18/RoleValues)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Grafana. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query grafana` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

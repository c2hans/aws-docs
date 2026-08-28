---
source_url: https://docs.aws.amazon.com/grafana/latest/APIReference/API_AuthenticationSummary.html
---

# AuthenticationSummary
<a name="API_AuthenticationSummary"></a>

A structure that describes whether the workspace uses SAML, IAM Identity Center, or both methods for user authentication, and whether that authentication is fully configured.

## Contents
<a name="API_AuthenticationSummary_Contents"></a>

 ** providers **   <a name="ManagedGrafana-Type-AuthenticationSummary-providers"></a>
Specifies whether the workspace uses SAML, IAM Identity Center, or both methods for user authentication.
Type: Array of strings
Valid Values: `AWS_SSO | SAML`
Required: Yes

 ** samlConfigurationStatus **   <a name="ManagedGrafana-Type-AuthenticationSummary-samlConfigurationStatus"></a>
Specifies whether the workplace's user authentication method is fully configured.
Type: String
Valid Values: `CONFIGURED | NOT_CONFIGURED`
Required: No

## See Also
<a name="API_AuthenticationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/grafana-2020-08-18/AuthenticationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/grafana-2020-08-18/AuthenticationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/grafana-2020-08-18/AuthenticationSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Grafana. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query grafana` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

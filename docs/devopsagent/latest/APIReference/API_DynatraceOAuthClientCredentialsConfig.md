---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_DynatraceOAuthClientCredentialsConfig.html
---

# DynatraceOAuthClientCredentialsConfig
<a name="API_DynatraceOAuthClientCredentialsConfig"></a>

OAuth client credentials configuration for Dynatrace.

## Contents
<a name="API_DynatraceOAuthClientCredentialsConfig_Contents"></a>

 ** clientId **   <a name="devopsagent-Type-DynatraceOAuthClientCredentialsConfig-clientId"></a>
OAuth client ID for authenticating with the service.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\u007E]+`
Required: Yes

 ** clientSecret **   <a name="devopsagent-Type-DynatraceOAuthClientCredentialsConfig-clientSecret"></a>
OAuth client secret for authenticating with the service.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\S]+`
Required: Yes

 ** clientName **   <a name="devopsagent-Type-DynatraceOAuthClientCredentialsConfig-clientName"></a>
User friendly OAuth client name specified by end user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\p{L}\p{N}\p{Z}._-]+`
Required: No

 ** exchangeParameters **   <a name="devopsagent-Type-DynatraceOAuthClientCredentialsConfig-exchangeParameters"></a>
OAuth token exchange parameters for authenticating with the service.
Type: String to string map
Required: No

## See Also
<a name="API_DynatraceOAuthClientCredentialsConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/DynatraceOAuthClientCredentialsConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/DynatraceOAuthClientCredentialsConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/DynatraceOAuthClientCredentialsConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS DevOps Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devopsagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

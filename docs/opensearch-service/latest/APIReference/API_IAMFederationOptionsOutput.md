---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_IAMFederationOptionsOutput.html
---

# IAMFederationOptionsOutput
<a name="API_IAMFederationOptionsOutput"></a>

Output parameters showing the current IAM identity federation configuration.

## Contents
<a name="API_IAMFederationOptionsOutput_Contents"></a>

 ** Enabled **   <a name="opensearchservice-Type-IAMFederationOptionsOutput-Enabled"></a>
Indicates whether IAM identity federation is currently enabled for the domain.
Type: Boolean
Required: No

 ** RolesKey **   <a name="opensearchservice-Type-IAMFederationOptionsOutput-RolesKey"></a>
The configured key in the SAML assertion for the user's role information.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^(null|[A-Za-z][A-Za-z0-9_.:/=+\-@]*)$`
Required: No

 ** SubjectKey **   <a name="opensearchservice-Type-IAMFederationOptionsOutput-SubjectKey"></a>
The configured key in the SAML assertion for the user's subject identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^(null|[A-Za-z][A-Za-z0-9_.:/=+\-@]*)$`
Required: No

## See Also
<a name="API_IAMFederationOptionsOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/IAMFederationOptionsOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/IAMFederationOptionsOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/IAMFederationOptionsOutput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

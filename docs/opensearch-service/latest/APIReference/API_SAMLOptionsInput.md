---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_SAMLOptionsInput.html
---

# SAMLOptionsInput
<a name="API_SAMLOptionsInput"></a>

The SAML authentication configuration for an Amazon OpenSearch Service domain.

## Contents
<a name="API_SAMLOptionsInput_Contents"></a>

 ** Enabled **   <a name="opensearchservice-Type-SAMLOptionsInput-Enabled"></a>
True to enable SAML authentication for a domain.
Type: Boolean
Required: No

 ** Idp **   <a name="opensearchservice-Type-SAMLOptionsInput-Idp"></a>
The SAML Identity Provider's information.
Type: [SAMLIdp](API_SAMLIdp.md) object
Required: No

 ** MasterBackendRole **   <a name="opensearchservice-Type-SAMLOptionsInput-MasterBackendRole"></a>
The backend role that the SAML master user is mapped to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** MasterUserName **   <a name="opensearchservice-Type-SAMLOptionsInput-MasterUserName"></a>
The SAML master user name, which is stored in the domain's internal user database.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*`
Required: No

 ** RolesKey **   <a name="opensearchservice-Type-SAMLOptionsInput-RolesKey"></a>
Element of the SAML assertion to use for backend roles. Default is `roles`.
Type: String
Required: No

 ** SessionTimeoutMinutes **   <a name="opensearchservice-Type-SAMLOptionsInput-SessionTimeoutMinutes"></a>
The duration, in minutes, after which a user session becomes inactive. Acceptable values are between 1 and 1440, and the default value is 60.
Type: Integer
Required: No

 ** SubjectKey **   <a name="opensearchservice-Type-SAMLOptionsInput-SubjectKey"></a>
Element of the SAML assertion to use for the user name. Default is `NameID`.
Type: String
Required: No

## See Also
<a name="API_SAMLOptionsInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/SAMLOptionsInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/SAMLOptionsInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/SAMLOptionsInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_AdvancedSecurityOptions.html
---

# AdvancedSecurityOptions
<a name="API_AdvancedSecurityOptions"></a>

Container for fine-grained access control settings.

## Contents
<a name="API_AdvancedSecurityOptions_Contents"></a>

 ** AnonymousAuthDisableDate **   <a name="opensearchservice-Type-AdvancedSecurityOptions-AnonymousAuthDisableDate"></a>
Date and time when the migration period will be disabled. Only necessary when [enabling fine-grained access control on an existing domain](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/fgac.html#fgac-enabling-existing).
Type: Timestamp
Required: No

 ** AnonymousAuthEnabled **   <a name="opensearchservice-Type-AdvancedSecurityOptions-AnonymousAuthEnabled"></a>
True if a 30-day migration period is enabled, during which administrators can create role mappings. Only necessary when [enabling fine-grained access control on an existing domain](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/fgac.html#fgac-enabling-existing).
Type: Boolean
Required: No

 ** Enabled **   <a name="opensearchservice-Type-AdvancedSecurityOptions-Enabled"></a>
True if fine-grained access control is enabled.
Type: Boolean
Required: No

 ** IAMFederationOptions **   <a name="opensearchservice-Type-AdvancedSecurityOptions-IAMFederationOptions"></a>
Configuration options for IAM identity federation in advanced security settings.
Type: [IAMFederationOptionsOutput](API_IAMFederationOptionsOutput.md) object
Required: No

 ** InternalUserDatabaseEnabled **   <a name="opensearchservice-Type-AdvancedSecurityOptions-InternalUserDatabaseEnabled"></a>
True if the internal user database is enabled.
Type: Boolean
Required: No

 ** JWTOptions **   <a name="opensearchservice-Type-AdvancedSecurityOptions-JWTOptions"></a>
Container for information about the JWT configuration of the Amazon OpenSearch Service.
Type: [JWTOptionsOutput](API_JWTOptionsOutput.md) object
Required: No

 ** SAMLOptions **   <a name="opensearchservice-Type-AdvancedSecurityOptions-SAMLOptions"></a>
Container for information about the SAML configuration for OpenSearch Dashboards.
Type: [SAMLOptionsOutput](API_SAMLOptionsOutput.md) object
Required: No

## See Also
<a name="API_AdvancedSecurityOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/AdvancedSecurityOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/AdvancedSecurityOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/AdvancedSecurityOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

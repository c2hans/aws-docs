---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_AdvancedSecurityOptionsInput.html
---

# AdvancedSecurityOptionsInput
<a name="API_AdvancedSecurityOptionsInput"></a>

Options for enabling and configuring fine-grained access control. For more information, see [Fine-grained access control in Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/fgac.html).

## Contents
<a name="API_AdvancedSecurityOptionsInput_Contents"></a>

 ** AnonymousAuthEnabled **   <a name="opensearchservice-Type-AdvancedSecurityOptionsInput-AnonymousAuthEnabled"></a>
True to enable a 30-day migration period during which administrators can create role mappings. Only necessary when [enabling fine-grained access control on an existing domain](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/fgac.html#fgac-enabling-existing).
Type: Boolean
Required: No

 ** Enabled **   <a name="opensearchservice-Type-AdvancedSecurityOptionsInput-Enabled"></a>
True to enable fine-grained access control.
Type: Boolean
Required: No

 ** IAMFederationOptions **   <a name="opensearchservice-Type-AdvancedSecurityOptionsInput-IAMFederationOptions"></a>
Input configuration for IAM identity federation within advanced security options.
Type: [IAMFederationOptionsInput](API_IAMFederationOptionsInput.md) object
Required: No

 ** InternalUserDatabaseEnabled **   <a name="opensearchservice-Type-AdvancedSecurityOptionsInput-InternalUserDatabaseEnabled"></a>
True to enable the internal user database.
Type: Boolean
Required: No

 ** JWTOptions **   <a name="opensearchservice-Type-AdvancedSecurityOptionsInput-JWTOptions"></a>
Container for information about the JWT configuration of the Amazon OpenSearch Service.
Type: [JWTOptionsInput](API_JWTOptionsInput.md) object
Required: No

 ** MasterUserOptions **   <a name="opensearchservice-Type-AdvancedSecurityOptionsInput-MasterUserOptions"></a>
Container for information about the master user.
Type: [MasterUserOptions](API_MasterUserOptions.md) object
Required: No

 ** SAMLOptions **   <a name="opensearchservice-Type-AdvancedSecurityOptionsInput-SAMLOptions"></a>
Container for information about the SAML configuration for OpenSearch Dashboards.
Type: [SAMLOptionsInput](API_SAMLOptionsInput.md) object
Required: No

## See Also
<a name="API_AdvancedSecurityOptionsInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/AdvancedSecurityOptionsInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/AdvancedSecurityOptionsInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/AdvancedSecurityOptionsInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

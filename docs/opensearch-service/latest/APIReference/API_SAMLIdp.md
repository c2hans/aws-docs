---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_SAMLIdp.html
---

# SAMLIdp
<a name="API_SAMLIdp"></a>

The SAML identity povider information.

## Contents
<a name="API_SAMLIdp_Contents"></a>

 ** EntityId **   <a name="opensearchservice-Type-SAMLIdp-EntityId"></a>
The unique entity ID of the application in the SAML identity provider.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 512.
Required: Yes

 ** MetadataContent **   <a name="opensearchservice-Type-SAMLIdp-MetadataContent"></a>
The metadata of the SAML application, in XML format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1048576.
Required: Yes

## See Also
<a name="API_SAMLIdp_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/SAMLIdp)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/SAMLIdp)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/SAMLIdp)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

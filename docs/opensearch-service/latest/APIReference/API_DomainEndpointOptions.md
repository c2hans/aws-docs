---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DomainEndpointOptions.html
---

# DomainEndpointOptions
<a name="API_DomainEndpointOptions"></a>

Options to configure a custom endpoint for an OpenSearch Service domain.

## Contents
<a name="API_DomainEndpointOptions_Contents"></a>

 ** CustomEndpoint **   <a name="opensearchservice-Type-DomainEndpointOptions-CustomEndpoint"></a>
The fully qualified URL for the custom endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^(((?!-)[A-Za-z0-9-]{0,62}[A-Za-z0-9])\.)+((?!-)[A-Za-z0-9-]{1,62}[A-Za-z0-9])$`
Required: No

 ** CustomEndpointCertificateArn **   <a name="opensearchservice-Type-DomainEndpointOptions-CustomEndpointCertificateArn"></a>
The ARN for your security certificate, managed in AWS Certificate Manager (ACM).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*`
Required: No

 ** CustomEndpointEnabled **   <a name="opensearchservice-Type-DomainEndpointOptions-CustomEndpointEnabled"></a>
Whether to enable a custom endpoint for the domain.
Type: Boolean
Required: No

 ** EnforceHTTPS **   <a name="opensearchservice-Type-DomainEndpointOptions-EnforceHTTPS"></a>
True to require that all traffic to the domain arrive over HTTPS.
Type: Boolean
Required: No

 ** TLSSecurityPolicy **   <a name="opensearchservice-Type-DomainEndpointOptions-TLSSecurityPolicy"></a>
Specify the TLS security policy to apply to the HTTPS endpoint of the domain. The policy can be one of the following values:
+  **Policy-Min-TLS-1-0-2019-07:** TLS security policy that supports TLS version 1.0 to TLS version 1.2
+  **Policy-Min-TLS-1-2-2019-07:** TLS security policy that supports only TLS version 1.2
+  **Policy-Min-TLS-1-2-PFS-2023-10:** TLS security policy that supports TLS version 1.2 to TLS version 1.3 with perfect forward secrecy cipher suites
+  **Policy-Min-TLS-1-2-RFC9151-FIPS-2024-08:** TLS security policy that supports TLS version 1.3 with FIPS
Type: String
Valid Values: `Policy-Min-TLS-1-0-2019-07 | Policy-Min-TLS-1-2-2019-07 | Policy-Min-TLS-1-2-PFS-2023-10 | Policy-Min-TLS-1-2-RFC9151-FIPS-2024-08`
Required: No

## See Also
<a name="API_DomainEndpointOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/DomainEndpointOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/DomainEndpointOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/DomainEndpointOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

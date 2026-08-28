---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsElasticsearchDomainDomainEndpointOptions.html
---

# AwsElasticsearchDomainDomainEndpointOptions
<a name="API_AwsElasticsearchDomainDomainEndpointOptions"></a>

Additional options for the domain endpoint, such as whether to require HTTPS for all traffic.

## Contents
<a name="API_AwsElasticsearchDomainDomainEndpointOptions_Contents"></a>

 ** EnforceHTTPS **   <a name="securityhub-Type-AwsElasticsearchDomainDomainEndpointOptions-EnforceHTTPS"></a>
Whether to require that all traffic to the domain arrive over HTTPS.
Type: Boolean
Required: No

 ** TLSSecurityPolicy **   <a name="securityhub-Type-AwsElasticsearchDomainDomainEndpointOptions-TLSSecurityPolicy"></a>
The TLS security policy to apply to the HTTPS endpoint of the OpenSearch domain.
Valid values:
+  `Policy-Min-TLS-1-0-2019-07`, which supports TLSv1.0 and higher
+  `Policy-Min-TLS-1-2-2019-07`, which only supports TLSv1.2
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsElasticsearchDomainDomainEndpointOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsElasticsearchDomainDomainEndpointOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsElasticsearchDomainDomainEndpointOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsElasticsearchDomainDomainEndpointOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

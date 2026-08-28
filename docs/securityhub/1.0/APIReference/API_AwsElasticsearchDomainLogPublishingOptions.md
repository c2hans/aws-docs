---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsElasticsearchDomainLogPublishingOptions.html
---

# AwsElasticsearchDomainLogPublishingOptions
<a name="API_AwsElasticsearchDomainLogPublishingOptions"></a>

configures the CloudWatch Logs to publish for the Elasticsearch domain.

## Contents
<a name="API_AwsElasticsearchDomainLogPublishingOptions_Contents"></a>

 ** AuditLogs **   <a name="securityhub-Type-AwsElasticsearchDomainLogPublishingOptions-AuditLogs"></a>
The log configuration.
Type: [AwsElasticsearchDomainLogPublishingOptionsLogConfig](API_AwsElasticsearchDomainLogPublishingOptionsLogConfig.md) object
Required: No

 ** IndexSlowLogs **   <a name="securityhub-Type-AwsElasticsearchDomainLogPublishingOptions-IndexSlowLogs"></a>
Configures the OpenSearch index logs publishing.
Type: [AwsElasticsearchDomainLogPublishingOptionsLogConfig](API_AwsElasticsearchDomainLogPublishingOptionsLogConfig.md) object
Required: No

 ** SearchSlowLogs **   <a name="securityhub-Type-AwsElasticsearchDomainLogPublishingOptions-SearchSlowLogs"></a>
Configures the OpenSearch search slow log publishing.
Type: [AwsElasticsearchDomainLogPublishingOptionsLogConfig](API_AwsElasticsearchDomainLogPublishingOptionsLogConfig.md) object
Required: No

## See Also
<a name="API_AwsElasticsearchDomainLogPublishingOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsElasticsearchDomainLogPublishingOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsElasticsearchDomainLogPublishingOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsElasticsearchDomainLogPublishingOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

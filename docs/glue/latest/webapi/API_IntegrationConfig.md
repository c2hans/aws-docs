---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_IntegrationConfig.html
---

# IntegrationConfig
<a name="API_IntegrationConfig"></a>

Properties associated with the integration.

## Contents
<a name="API_IntegrationConfig_Contents"></a>

 ** ContinuousSync **   <a name="Glue-Type-IntegrationConfig-ContinuousSync"></a>
Enables continuous synchronization for on-demand data extractions from SaaS applications to AWS data services like Amazon Redshift and Amazon S3.
Type: Boolean
Required: No

 ** RefreshInterval **   <a name="Glue-Type-IntegrationConfig-RefreshInterval"></a>
Specifies the frequency at which CDC (Change Data Capture) pulls or incremental loads should occur. This parameter provides flexibility to align the refresh rate with your specific data update patterns, system load considerations, and performance optimization goals. Time increment can be set from 15 minutes to 8640 minutes (six days).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** SourceProperties **   <a name="Glue-Type-IntegrationConfig-SourceProperties"></a>
 A collection of key-value pairs that specify additional properties for the integration source. These properties provide configuration options that can be used to customize the behavior of the ODB source during data integration operations.
Type: String to string map
Required: No

## See Also
<a name="API_IntegrationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/IntegrationConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/IntegrationConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/IntegrationConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

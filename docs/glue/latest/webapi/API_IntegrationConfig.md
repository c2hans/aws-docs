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

 ** TargetNamespace **   <a name="Glue-Type-IntegrationConfig-TargetNamespace"></a>
An optional custom namespace for the integration's target. Supply this parameter only when the target is an Amazon S3 Tables table bucket; it is not accepted for other target types. The integration replicates data into the namespace you specify, reusing it if it already exists. If you omit this parameter, the target namespace defaults to `zetl_` followed by the integration ID, with hyphens converted to underscores.
The value is immutable after the integration is created; `ModifyIntegration` rejects changes to it. It must be a valid Amazon S3 Tables namespace name: 1 to 255 characters using lowercase letters, numbers, and underscores, with no leading or trailing underscore and no reserved `aws` prefix.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-z0-9]([a-z0-9_]*[a-z0-9])?`
Required: No

## See Also
<a name="API_IntegrationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/IntegrationConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/IntegrationConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/IntegrationConfig)

---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_SourceTlsConfiguration.html
---

# SourceTlsConfiguration
<a name="API_SourceTlsConfiguration"></a>

The TLS configuration for connecting to the source during migration.

## Contents
<a name="API_SourceTlsConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** SourceTlsCertificate **
The TLS certificate used to verify the identity of the source during migration.
Type: String
Required: No

 ** SourceTlsMode **
The TLS mode to use when connecting to the source. Valid values are `none` and `verify-ca`.
Type: String
Valid Values: `none | verify-ca`
Required: No

## See Also
<a name="API_SourceTlsConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/SourceTlsConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/SourceTlsConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/SourceTlsConfiguration)

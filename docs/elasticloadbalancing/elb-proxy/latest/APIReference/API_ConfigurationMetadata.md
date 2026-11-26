---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/elb-proxy/latest/APIReference/API_ConfigurationMetadata.html
---

# ConfigurationMetadata

The configuration metadata for a proxy.

## Contents
<a name="API_ConfigurationMetadata_Contents"></a>

 ** configArchiveHash **   <a name="elasticloadbalancing-Type-ConfigurationMetadata-configArchiveHash"></a>
The SHA-256 hash of the configuration archive. This value is absent when the proxy does not have a configuration archive.
Type: String
Required: No

 ** configArchiveLastUpdatedAt **   <a name="elasticloadbalancing-Type-ConfigurationMetadata-configArchiveLastUpdatedAt"></a>
The date and time that the configuration archive was last updated.
Type: Timestamp
Required: No

 ** configFileHash **   <a name="elasticloadbalancing-Type-ConfigurationMetadata-configFileHash"></a>
The SHA-256 hash of the configuration file.
Type: String
Required: No

 ** configFileLastUpdatedAt **   <a name="elasticloadbalancing-Type-ConfigurationMetadata-configFileLastUpdatedAt"></a>
The date and time that the configuration file was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_ConfigurationMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elb-proxy-2026-11-20/ConfigurationMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elb-proxy-2026-11-20/ConfigurationMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elb-proxy-2026-11-20/ConfigurationMetadata)

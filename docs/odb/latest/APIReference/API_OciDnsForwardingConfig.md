---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_OciDnsForwardingConfig.html
---

# OciDnsForwardingConfig
<a name="API_OciDnsForwardingConfig"></a>

DNS configuration to forward DNS resolver endpoints to your OCI Private Zone.

## Contents
<a name="API_OciDnsForwardingConfig_Contents"></a>

 ** domainName **   <a name="odb-Type-OciDnsForwardingConfig-domainName"></a>
Domain name to which DNS resolver forwards to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** ociDnsListenerIp **   <a name="odb-Type-OciDnsForwardingConfig-ociDnsListenerIp"></a>
OCI DNS listener IP for custom DNS setup.
Type: String
Required: No

## See Also
<a name="API_OciDnsForwardingConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/OciDnsForwardingConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/OciDnsForwardingConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/OciDnsForwardingConfig)

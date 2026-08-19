---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_FabricConfiguration.html
---

# FabricConfiguration
<a name="API_FabricConfiguration"></a>

The fabric configuration settings for the router output.

## Contents
<a name="API_FabricConfiguration_Contents"></a>

 ** recoveryLatencyMode **   <a name="mediaconnect-Type-FabricConfiguration-recoveryLatencyMode"></a>
The recovery latency mode for the router fabric connection. Valid values include the following:
+  `BALANCED` (default) – Optimizes for stream quality.
+  `LOW_LATENCY` – Reduces latency at the potential cost of stream quality under adverse network conditions.
Type: String
Valid Values: `BALANCED | LOW_LATENCY`
Required: Yes

## See Also
<a name="API_FabricConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/FabricConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/FabricConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/FabricConfiguration)

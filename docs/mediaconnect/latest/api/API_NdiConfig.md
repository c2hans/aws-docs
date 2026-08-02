---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_NdiConfig.html
---

# NdiConfig
<a name="API_NdiConfig"></a>

Specifies the configuration settings for NDI sources and outputs.

## Contents
<a name="API_NdiConfig_Contents"></a>

 ** machineName **   <a name="mediaconnect-Type-NdiConfig-machineName"></a>
A prefix for the names of the NDI sources that the flow creates. If a custom name isn't specified, MediaConnect generates a unique 12-character ID as the prefix.
Type: String
Required: No

 ** ndiDiscoveryServers **   <a name="mediaconnect-Type-NdiConfig-ndiDiscoveryServers"></a>
A list of up to three NDI discovery server configurations. While not required by the API, this configuration is necessary for NDI functionality to work properly.
Type: Array of [NdiDiscoveryServerConfig](API_NdiDiscoveryServerConfig.md) objects
Required: No

 ** ndiState **   <a name="mediaconnect-Type-NdiConfig-ndiState"></a>
A setting that controls whether NDI® sources or outputs can be used in the flow.
 The default value is `DISABLED`. This value must be set as `ENABLED` for your flow to support NDI sources or outputs.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## See Also
<a name="API_NdiConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/NdiConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/NdiConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/NdiConfig)

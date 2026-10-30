---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ServiceConnectContainerConfiguration.html
---

# ServiceConnectContainerConfiguration
<a name="API_ServiceConnectContainerConfiguration"></a>

Contains a configuration setting for the Service Connect proxy container, such as the log level. Specify exactly one member in each object.

## Contents
<a name="API_ServiceConnectContainerConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** logLevel **   <a name="ECS-Type-ServiceConnectContainerConfiguration-logLevel"></a>
The log level of the Service Connect proxy container. Set the log level to `debug` to collect more detailed proxy logs when you troubleshoot connectivity issues between services, and set it back to `info` when you finish. Debug logging increases the volume of logs that the proxy container writes. If you don't specify a log level, the default is `info`.
Type: String
Valid Values: `debug | info`
Required: No

## See Also
<a name="API_ServiceConnectContainerConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ServiceConnectContainerConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ServiceConnectContainerConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ServiceConnectContainerConfiguration)

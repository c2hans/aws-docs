---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ProxyConfiguration.html
---

# ProxyConfiguration
<a name="API_ProxyConfiguration"></a>

The configuration details for the App Mesh proxy.

For tasks that use the EC2 launch type, the container instances require at least version 1.26.0 of the container agent and at least version 1.26.0-1 of the `ecs-init` package to use a proxy configuration. If your container instances are launched from the Amazon ECS optimized AMI version `20190301` or later, then they contain the required versions of the container agent and `ecs-init`. For more information, see [Amazon ECS-optimized Linux AMI](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html)

## Contents
<a name="API_ProxyConfiguration_Contents"></a>

 ** containerName **   <a name="ECS-Type-ProxyConfiguration-containerName"></a>
The name of the container that will serve as the App Mesh proxy.
Type: String
Required: Yes

 ** properties **   <a name="ECS-Type-ProxyConfiguration-properties"></a>
The set of network configuration parameters to provide the Container Network Interface (CNI) plugin, specified as key-value pairs.
+  `IgnoredUID` - (Required) The user ID (UID) of the proxy container as defined by the `user` parameter in a container definition. This is used to ensure the proxy ignores its own traffic. If `IgnoredGID` is specified, this field can be empty.
+  `IgnoredGID` - (Required) The group ID (GID) of the proxy container as defined by the `user` parameter in a container definition. This is used to ensure the proxy ignores its own traffic. If `IgnoredUID` is specified, this field can be empty.
+  `AppPorts` - (Required) The list of ports that the application uses. Network traffic to these ports is forwarded to the `ProxyIngressPort` and `ProxyEgressPort`.
+  `ProxyIngressPort` - (Required) Specifies the port that incoming traffic to the `AppPorts` is directed to.
+  `ProxyEgressPort` - (Required) Specifies the port that outgoing traffic from the `AppPorts` is directed to.
+  `EgressIgnoredPorts` - (Required) The egress traffic going to the specified ports is ignored and not redirected to the `ProxyEgressPort`. It can be an empty list.
+  `EgressIgnoredIPs` - (Required) The egress traffic going to the specified IP addresses is ignored and not redirected to the `ProxyEgressPort`. It can be an empty list.
Type: Array of [KeyValuePair](API_KeyValuePair.md) objects
Required: No

 ** type **   <a name="ECS-Type-ProxyConfiguration-type"></a>
The proxy type. The only supported value is `APPMESH`.
Type: String
Valid Values: `APPMESH`
Required: No

## See Also
<a name="API_ProxyConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ProxyConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ProxyConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ProxyConfiguration)

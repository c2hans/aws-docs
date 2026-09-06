---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_HostEntry.html
---

# HostEntry
<a name="API_HostEntry"></a>

Hostnames and IP address entries that are added to the `/etc/hosts` file of a container via the `extraHosts` parameter of its [ContainerDefinition](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerDefinition.html).

## Contents
<a name="API_HostEntry_Contents"></a>

 ** hostname **   <a name="ECS-Type-HostEntry-hostname"></a>
The hostname to use in the `/etc/hosts` entry.
Type: String
Required: Yes

 ** ipAddress **   <a name="ECS-Type-HostEntry-ipAddress"></a>
The IP address to use in the `/etc/hosts` entry.
Type: String
Required: Yes

## See Also
<a name="API_HostEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/HostEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/HostEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/HostEntry)

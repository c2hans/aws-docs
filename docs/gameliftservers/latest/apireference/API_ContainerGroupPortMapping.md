---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_ContainerGroupPortMapping.html
---

# ContainerGroupPortMapping
<a name="API_ContainerGroupPortMapping"></a>

Describes the port mappings for a single container in a container group. Each mapping shows how a container port maps to a connection port on the fleet instance.

 **Returned by:** [DescribeContainerGroupPortMappings](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeContainerGroupPortMappings.html)

## Contents
<a name="API_ContainerGroupPortMapping_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ContainerName **   <a name="gameliftservers-Type-ContainerGroupPortMapping-ContainerName"></a>
The name of the container, as defined in the container group definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9\-]+$`
Required: No

 ** ContainerPortMappings **   <a name="gameliftservers-Type-ContainerGroupPortMapping-ContainerPortMappings"></a>
A list of `ContainerPortMapping` objects that describe the port mappings for this container.
Type: Array of [ContainerPortMapping](API_ContainerPortMapping.md) objects
Required: No

 ** ContainerRuntimeId **   <a name="gameliftservers-Type-ContainerGroupPortMapping-ContainerRuntimeId"></a>
The runtime ID for the container that's running in a compute. This value is unique within the compute.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_ContainerGroupPortMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/ContainerGroupPortMapping)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/ContainerGroupPortMapping)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/ContainerGroupPortMapping)

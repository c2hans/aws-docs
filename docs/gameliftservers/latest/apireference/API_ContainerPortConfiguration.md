---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_ContainerPortConfiguration.html
---

# ContainerPortConfiguration
<a name="API_ContainerPortConfiguration"></a>

A set of port ranges that can be opened on the container. A process that's running in the container can bind to a port number, making it accessible to inbound traffic when it's mapped to a container fleet's connection port.

Each container port range specifies a network protocol. When the configuration supports more than one protocol, we recommend that you use a different range for each protocol. If your ranges have overlapping port numbers, Amazon GameLift Servers maps a duplicated container port number to different connection ports. For example, if you include 1935 in port ranges for both TCP and UDP, it might result in the following mappings:
+ container port 1935 (tcp) => connection port 2001
+ container port 1935 (udp) => connection port 2002

 **Part of:** [GameServerContainerDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinition.html), [GameServerContainerDefinitionInput](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinitionInput.html), [SupportContainerDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinition.html), [SupportContainerDefinitionInput](https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinitionInput.html)

## Contents
<a name="API_ContainerPortConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ContainerPortRanges **   <a name="gameliftservers-Type-ContainerPortConfiguration-ContainerPortRanges"></a>
A set of one or more container port number ranges. The ranges can't overlap if the ranges' network protocols are the same. Overlapping ranges with different protocols is allowed but not recommended.
Type: Array of [ContainerPortRange](API_ContainerPortRange.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: Yes

## See Also
<a name="API_ContainerPortConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/ContainerPortConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/ContainerPortConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/ContainerPortConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_ContainerDependency.html
---

# ContainerDependency
<a name="API_ContainerDependency"></a>

A container's dependency on another container in the same container group. The dependency impacts how the dependent container is able to start or shut down based the status of the other container.

For example, *ContainerA* is configured with the following dependency: a `START` dependency on *ContainerB*. This means that *ContainerA* can't start until *ContainerB* has started. It also means that *ContainerA* must shut down before *ContainerB*.

 **Part of:** [GameServerContainerDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinition.html), [GameServerContainerDefinitionInput](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinitionInput.html), [SupportContainerDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinition.html), [SupportContainerDefinitionInput](https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinitionInput.html)

## Contents
<a name="API_ContainerDependency_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Condition **   <a name="gameliftservers-Type-ContainerDependency-Condition"></a>
The condition that the dependency container must reach before the dependent container can start. Valid conditions include:
+ START - The dependency container must have started.
+ COMPLETE - The dependency container has run to completion (exits). Use this condition with nonessential containers, such as those that run a script and then exit. The dependency container can't be an essential container.
+ SUCCESS - The dependency container has run to completion and exited with a zero status. The dependency container can't be an essential container.
+ HEALTHY - The dependency container has passed its Docker health check. Use this condition with dependency containers that have health checks configured. This condition is confirmed at container group startup only.
Type: String
Valid Values: `START | COMPLETE | SUCCESS | HEALTHY`
Required: Yes

 ** ContainerName **   <a name="gameliftservers-Type-ContainerDependency-ContainerName"></a>
A descriptive label for the container definition that this container depends on.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9\-]+$`
Required: Yes

## See Also
<a name="API_ContainerDependency_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/ContainerDependency)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/ContainerDependency)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/ContainerDependency)

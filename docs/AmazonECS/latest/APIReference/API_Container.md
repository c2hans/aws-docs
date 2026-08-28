---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_Container.html
---

# Container
<a name="API_Container"></a>

A Docker container that's part of a task.

## Contents
<a name="API_Container_Contents"></a>

 ** containerArn **   <a name="ECS-Type-Container-containerArn"></a>
The Amazon Resource Name (ARN) of the container.
Type: String
Required: No

 ** cpu **   <a name="ECS-Type-Container-cpu"></a>
The number of CPU units set for the container. The value is `0` if no value was specified in the container definition when the task definition was registered.
Type: String
Required: No

 ** exitCode **   <a name="ECS-Type-Container-exitCode"></a>
The exit code returned from the container.
Type: Integer
Required: No

 ** gpuIds **   <a name="ECS-Type-Container-gpuIds"></a>
The IDs of each GPU assigned to the container.
Type: Array of strings
Required: No

 ** healthStatus **   <a name="ECS-Type-Container-healthStatus"></a>
The health status of the container. If health checks aren't configured for this container in its task definition, then it reports the health status as `UNKNOWN`.
Type: String
Valid Values: `HEALTHY | UNHEALTHY | UNKNOWN`
Required: No

 ** image **   <a name="ECS-Type-Container-image"></a>
The image used for the container.
Type: String
Required: No

 ** imageDigest **   <a name="ECS-Type-Container-imageDigest"></a>
The container image manifest digest.
Type: String
Required: No

 ** lastStatus **   <a name="ECS-Type-Container-lastStatus"></a>
The last known status of the container.
Type: String
Required: No

 ** managedAgents **   <a name="ECS-Type-Container-managedAgents"></a>
The details of any Amazon ECS managed agents associated with the container.
Type: Array of [ManagedAgent](API_ManagedAgent.md) objects
Required: No

 ** memory **   <a name="ECS-Type-Container-memory"></a>
The hard limit (in MiB) of memory set for the container.
Type: String
Required: No

 ** memoryReservation **   <a name="ECS-Type-Container-memoryReservation"></a>
The soft limit (in MiB) of memory set for the container.
Type: String
Required: No

 ** name **   <a name="ECS-Type-Container-name"></a>
The name of the container.
Type: String
Required: No

 ** networkBindings **   <a name="ECS-Type-Container-networkBindings"></a>
The network bindings associated with the container.
Type: Array of [NetworkBinding](API_NetworkBinding.md) objects
Required: No

 ** networkInterfaces **   <a name="ECS-Type-Container-networkInterfaces"></a>
The network interfaces associated with the container.
Type: Array of [NetworkInterface](API_NetworkInterface.md) objects
Required: No

 ** neuronDeviceIds **   <a name="ECS-Type-Container-neuronDeviceIds"></a>
The IDs of each Neuron device assigned to the container.
Type: Array of strings
Required: No

 ** reason **   <a name="ECS-Type-Container-reason"></a>
A short (1024 max characters) human-readable string to provide additional details about a running or stopped container.
Type: String
Required: No

 ** runtimeId **   <a name="ECS-Type-Container-runtimeId"></a>
The ID of the Docker container.
Type: String
Required: No

 ** taskArn **   <a name="ECS-Type-Container-taskArn"></a>
The ARN of the task.
Type: String
Required: No

## See Also
<a name="API_Container_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/Container)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/Container)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/Container)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

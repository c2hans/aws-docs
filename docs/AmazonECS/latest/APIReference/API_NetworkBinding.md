---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_NetworkBinding.html
---

# NetworkBinding
<a name="API_NetworkBinding"></a>

Details on the network bindings between a container and its host container instance. After a task reaches the `RUNNING` status, manual and automatic host and container port assignments are visible in the `networkBindings` section of [DescribeTasks](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeTasks.html) API responses.

## Contents
<a name="API_NetworkBinding_Contents"></a>

 ** bindIP **   <a name="ECS-Type-NetworkBinding-bindIP"></a>
The IP address that the container is bound to on the container instance.
Type: String
Required: No

 ** containerPort **   <a name="ECS-Type-NetworkBinding-containerPort"></a>
The port number on the container that's used with the network binding.
Type: Integer
Required: No

 ** containerPortRange **   <a name="ECS-Type-NetworkBinding-containerPortRange"></a>
The port number range on the container that's bound to the dynamically mapped host port range.
The following rules apply when you specify a `containerPortRange`:
+ You must use either the `bridge` network mode or the `awsvpc` network mode.
+ This parameter is available for both the EC2 and AWS Fargate launch types.
+ This parameter is available for both the Linux and Windows operating systems.
+ The container instance must have at least version 1.67.0 of the container agent and at least version 1.67.0-1 of the `ecs-init` package
+ You can specify a maximum of 100 port ranges per container.
+ You do not specify a `hostPortRange`. The value of the `hostPortRange` is set as follows:
  + For containers in a task with the `awsvpc` network mode, the `hostPortRange` is set to the same value as the `containerPortRange`. This is a static mapping strategy.
  + For containers in a task with the `bridge` network mode, the Amazon ECS agent finds open host ports from the default ephemeral range and passes it to docker to bind them to the container ports.
+ The `containerPortRange` valid values are between 1 and 65535.
+ A port can only be included in one port mapping per container.
+ You cannot specify overlapping port ranges.
+ The first port in the range must be less than last port in the range.
+ Docker recommends that you turn off the docker-proxy in the Docker daemon config file when you have a large number of ports.

  For more information, see [ Issue \#11185](https://github.com/moby/moby/issues/11185) on the Github website.

  For information about how to turn off the docker-proxy in the Docker daemon config file, see [Docker daemon](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/bootstrap_container_instance.html#bootstrap_docker_daemon) in the *Amazon ECS Developer Guide*.
You can call [https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeTasks.html](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeTasks.html) to view the `hostPortRange` which are the host ports that are bound to the container ports.
Type: String
Required: No

 ** hostPort **   <a name="ECS-Type-NetworkBinding-hostPort"></a>
The port number on the host that's used with the network binding.
Type: Integer
Required: No

 ** hostPortRange **   <a name="ECS-Type-NetworkBinding-hostPortRange"></a>
The port number range on the host that's used with the network binding. This is assigned is assigned by Docker and delivered by the Amazon ECS agent.
Type: String
Required: No

 ** protocol **   <a name="ECS-Type-NetworkBinding-protocol"></a>
The protocol used for the network binding.
Type: String
Valid Values: `tcp | udp`
Required: No

## See Also
<a name="API_NetworkBinding_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/NetworkBinding)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/NetworkBinding)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/NetworkBinding)

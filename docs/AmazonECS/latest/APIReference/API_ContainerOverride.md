---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerOverride.html
---

# ContainerOverride
<a name="API_ContainerOverride"></a>

The overrides that are sent to a container. An empty container override can be passed in. An example of an empty container override is `{"containerOverrides": [ ] }`. If a non-empty container override is specified, the `name` parameter must be included.

You can use Secrets Manager or AWS Systems Manager Parameter Store to store the sensitive data. For more information, see [Retrieve secrets through environment variables](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/secrets-envvar.html) in the Amazon ECS Developer Guide.

## Contents
<a name="API_ContainerOverride_Contents"></a>

 ** command **   <a name="ECS-Type-ContainerOverride-command"></a>
The command to send to the container that overrides the default command from the Docker image or the task definition. You must also specify a container name.
Type: Array of strings
Required: No

 ** cpu **   <a name="ECS-Type-ContainerOverride-cpu"></a>
The number of `cpu` units reserved for the container, instead of the default value from the task definition. You must also specify a container name.
Type: Integer
Required: No

 ** environment **   <a name="ECS-Type-ContainerOverride-environment"></a>
The environment variables to send to the container. You can add new environment variables, which are added to the container at launch, or you can override the existing environment variables from the Docker image or the task definition. You must also specify a container name.
Type: Array of [KeyValuePair](API_KeyValuePair.md) objects
Required: No

 ** environmentFiles **   <a name="ECS-Type-ContainerOverride-environmentFiles"></a>
A list of files containing the environment variables to pass to a container, instead of the value from the container definition.
Type: Array of [EnvironmentFile](API_EnvironmentFile.md) objects
Required: No

 ** memory **   <a name="ECS-Type-ContainerOverride-memory"></a>
The hard limit (in MiB) of memory to present to the container, instead of the default value from the task definition. If your container attempts to exceed the memory specified here, the container is killed. You must also specify a container name.
Type: Integer
Required: No

 ** memoryReservation **   <a name="ECS-Type-ContainerOverride-memoryReservation"></a>
The soft limit (in MiB) of memory to reserve for the container, instead of the default value from the task definition. You must also specify a container name.
Type: Integer
Required: No

 ** name **   <a name="ECS-Type-ContainerOverride-name"></a>
The name of the container that receives the override. This parameter is required if any override is specified.
Type: String
Required: No

 ** resourceRequirements **   <a name="ECS-Type-ContainerOverride-resourceRequirements"></a>
The type and amount of a resource to assign to a container, instead of the default value from the task definition. The supported resources are GPUs and Neuron devices.
Type: Array of [ResourceRequirement](API_ResourceRequirement.md) objects
Required: No

## See Also
<a name="API_ContainerOverride_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ContainerOverride)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ContainerOverride)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ContainerOverride)

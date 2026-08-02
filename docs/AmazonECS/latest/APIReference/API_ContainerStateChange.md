---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerStateChange.html
---

# ContainerStateChange
<a name="API_ContainerStateChange"></a>

An object that represents a change in state for a container.

## Contents
<a name="API_ContainerStateChange_Contents"></a>

 ** containerName **   <a name="ECS-Type-ContainerStateChange-containerName"></a>
The name of the container.
Type: String
Required: No

 ** exitCode **   <a name="ECS-Type-ContainerStateChange-exitCode"></a>
The exit code for the container, if the state change is a result of the container exiting.
Type: Integer
Required: No

 ** imageDigest **   <a name="ECS-Type-ContainerStateChange-imageDigest"></a>
The container image SHA 256 digest.
Type: String
Required: No

 ** networkBindings **   <a name="ECS-Type-ContainerStateChange-networkBindings"></a>
Any network bindings that are associated with the container.
Type: Array of [NetworkBinding](API_NetworkBinding.md) objects
Required: No

 ** reason **   <a name="ECS-Type-ContainerStateChange-reason"></a>
The reason for the state change.
Type: String
Required: No

 ** runtimeId **   <a name="ECS-Type-ContainerStateChange-runtimeId"></a>
The ID of the Docker container.
Type: String
Required: No

 ** status **   <a name="ECS-Type-ContainerStateChange-status"></a>
The status of the container.
Type: String
Required: No

## See Also
<a name="API_ContainerStateChange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ContainerStateChange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ContainerStateChange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ContainerStateChange)

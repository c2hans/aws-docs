---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerImage.html
---

# ContainerImage
<a name="API_ContainerImage"></a>

The details about the container image a service revision uses.

To ensure that all tasks in a service use the same container image, Amazon ECS resolves container image names and any image tags specified in the task definition to container image digests.

After the container image digest has been established, Amazon ECS uses the digest to start any other desired tasks, and for any future service and service revision updates. This leads to all tasks in a service always running identical container images, resulting in version consistency for your software. For more information, see [Container image resolution](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-ecs.html#deployment-container-image-stability) in the Amazon ECS Developer Guide.

## Contents
<a name="API_ContainerImage_Contents"></a>

 ** containerName **   <a name="ECS-Type-ContainerImage-containerName"></a>
The name of the container.
Type: String
Required: No

 ** image **   <a name="ECS-Type-ContainerImage-image"></a>
The container image.
Type: String
Required: No

 ** imageDigest **   <a name="ECS-Type-ContainerImage-imageDigest"></a>
The container image digest.
Type: String
Required: No

## See Also
<a name="API_ContainerImage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ContainerImage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ContainerImage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ContainerImage)

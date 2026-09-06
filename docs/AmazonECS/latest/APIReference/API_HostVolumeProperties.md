---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_HostVolumeProperties.html
---

# HostVolumeProperties
<a name="API_HostVolumeProperties"></a>

Details on a container instance bind mount host volume.

## Contents
<a name="API_HostVolumeProperties_Contents"></a>

 ** sourcePath **   <a name="ECS-Type-HostVolumeProperties-sourcePath"></a>
When the `host` parameter is used, specify a `sourcePath` to declare the path on the host container instance that's presented to the container. If this parameter is empty, then the Docker daemon has assigned a host path for you. If the `host` parameter contains a `sourcePath` file location, then the data volume persists at the specified location on the host container instance until you delete it manually. If the `sourcePath` value doesn't exist on the host container instance, the Docker daemon creates it. If the location does exist, the contents of the source path folder are exported.
If you're using the Fargate launch type, the `sourcePath` parameter is not supported.
Type: String
Required: No

## See Also
<a name="API_HostVolumeProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/HostVolumeProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/HostVolumeProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/HostVolumeProperties)

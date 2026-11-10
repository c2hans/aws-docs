---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_LogDriverVolumeConfiguration.html
---

# LogDriverVolumeConfiguration
<a name="API_LogDriverVolumeConfiguration"></a>

The configuration for a log driver volume in a daemon task definition. The volume contains the log files for each container on the container instance that uses the specified log driver in its `logConfiguration`. Containers that use a different log driver don't write log files to the volume.

For the `json-file` log driver, the volume has one directory for each container, named with the container ID. Each directory contains the container's log file, `<container-id>-json.log`, and any rotated log files. After a container stops and Amazon ECS removes it, Amazon ECS deletes the container's directory. Read the log files before the container is removed.

## Contents
<a name="API_LogDriverVolumeConfiguration_Contents"></a>

 ** driver **   <a name="ECS-Type-LogDriverVolumeConfiguration-driver"></a>
The log driver whose log files the volume contains. The only supported value is `json-file`.
Type: String
Valid Values: `json-file`
Required: Yes

## See Also
<a name="API_LogDriverVolumeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/LogDriverVolumeConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/LogDriverVolumeConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/LogDriverVolumeConfiguration)

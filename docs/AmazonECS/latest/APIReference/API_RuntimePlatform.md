---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RuntimePlatform.html
---

# RuntimePlatform
<a name="API_RuntimePlatform"></a>

Information about the platform for the Amazon ECS service or task.

For more information about `RuntimePlatform`, see [RuntimePlatform](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html#runtime-platform) in the *Amazon Elastic Container Service Developer Guide*.

## Contents
<a name="API_RuntimePlatform_Contents"></a>

 ** cpuArchitecture **   <a name="ECS-Type-RuntimePlatform-cpuArchitecture"></a>
The CPU architecture.
You can run your Linux tasks on an ARM-based platform by setting the value to `ARM64`. This option is available for tasks that run on Linux Amazon EC2 instance, Amazon ECS Managed Instances, or Linux containers on Fargate.
Type: String
Valid Values: `X86_64 | ARM64`
Required: No

 ** operatingSystemFamily **   <a name="ECS-Type-RuntimePlatform-operatingSystemFamily"></a>
The operating system.
Type: String
Valid Values: `WINDOWS_SERVER_2019_FULL | WINDOWS_SERVER_2019_CORE | WINDOWS_SERVER_2016_FULL | WINDOWS_SERVER_2004_CORE | WINDOWS_SERVER_2022_CORE | WINDOWS_SERVER_2022_FULL | WINDOWS_SERVER_2025_CORE | WINDOWS_SERVER_2025_FULL | WINDOWS_SERVER_20H2_CORE | LINUX`
Required: No

## See Also
<a name="API_RuntimePlatform_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/RuntimePlatform)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/RuntimePlatform)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/RuntimePlatform)

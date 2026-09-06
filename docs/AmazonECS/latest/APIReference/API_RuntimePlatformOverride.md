---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RuntimePlatformOverride.html
---

# RuntimePlatformOverride
<a name="API_RuntimePlatformOverride"></a>

The runtime platform that Amazon ECS applies to a service revision. This value overrides the runtime platform specified in the task definition. You can't set this value.

## Contents
<a name="API_RuntimePlatformOverride_Contents"></a>

 ** cpuArchitecture **   <a name="ECS-Type-RuntimePlatformOverride-cpuArchitecture"></a>
The CPU architecture that tasks in this service revision run on. This value might differ from the architecture declared in the task definition—for example, when Amazon ECS detects an architecture mismatch during an Amazon ECS Express deployment and runs tasks on a different architecture. You can't set this value.
Valid values:
+  `X86_64` - The x86 64-bit architecture.
+  `ARM64` - The 64-bit ARM architecture.
Type: String
Required: No

## See Also
<a name="API_RuntimePlatformOverride_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/RuntimePlatformOverride)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/RuntimePlatformOverride)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/RuntimePlatformOverride)

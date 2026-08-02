---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_Ulimit.html
---

# Ulimit
<a name="API_Ulimit"></a>

The `ulimit` settings to pass to the container.

Amazon ECS tasks hosted on AWS Fargate use the default resource limit values set by the operating system with the exception of the `nofile` resource limit parameter which AWS Fargate overrides. The `nofile` resource limit sets a restriction on the number of open files that a container can use. The default `nofile` soft limit is ` 65535` and the default hard limit is `65535`.

You can specify the `ulimit` settings for a container in a task definition.

## Contents
<a name="API_Ulimit_Contents"></a>

 ** hardLimit **   <a name="ECS-Type-Ulimit-hardLimit"></a>
The hard limit for the `ulimit` type. The value can be specified in bytes, seconds, or as a count, depending on the `type` of the `ulimit`.
Type: Integer
Required: Yes

 ** name **   <a name="ECS-Type-Ulimit-name"></a>
The `type` of the `ulimit`.
Type: String
Valid Values: `core | cpu | data | fsize | locks | memlock | msgqueue | nice | nofile | nproc | rss | rtprio | rttime | sigpending | stack`
Required: Yes

 ** softLimit **   <a name="ECS-Type-Ulimit-softLimit"></a>
The soft limit for the `ulimit` type. The value can be specified in bytes, seconds, or as a count, depending on the `type` of the `ulimit`.
Type: Integer
Required: Yes

## See Also
<a name="API_Ulimit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/Ulimit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/Ulimit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/Ulimit)

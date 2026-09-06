---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ServiceRevisionOverrides.html
---

# ServiceRevisionOverrides
<a name="API_ServiceRevisionOverrides"></a>

Contains the runtime overrides that Amazon ECS automatically applies to a service revision when the effective runtime configuration differs from the task definition. This value is read-only.

## Contents
<a name="API_ServiceRevisionOverrides_Contents"></a>

 ** runtimePlatform **   <a name="ECS-Type-ServiceRevisionOverrides-runtimePlatform"></a>
The runtime platform override that Amazon ECS automatically applies to the service revision. You can't set this value.
Type: [RuntimePlatformOverride](API_RuntimePlatformOverride.md) object
Required: No

## See Also
<a name="API_ServiceRevisionOverrides_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ServiceRevisionOverrides)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ServiceRevisionOverrides)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ServiceRevisionOverrides)

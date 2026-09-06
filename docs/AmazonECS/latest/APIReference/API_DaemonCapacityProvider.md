---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DaemonCapacityProvider.html
---

# DaemonCapacityProvider
<a name="API_DaemonCapacityProvider"></a>

Information about a capacity provider associated with a daemon revision.

## Contents
<a name="API_DaemonCapacityProvider_Contents"></a>

 ** arn **   <a name="ECS-Type-DaemonCapacityProvider-arn"></a>
The Amazon Resource Name (ARN) of the capacity provider.
Type: String
Required: No

 ** runningCount **   <a name="ECS-Type-DaemonCapacityProvider-runningCount"></a>
The number of daemon tasks running on this capacity provider.
Type: Integer
Required: No

 ** withoutDaemonCount **   <a name="ECS-Type-DaemonCapacityProvider-withoutDaemonCount"></a>
The number of instances on this capacity provider that are running without the daemon task. This applies to daemons that aren't critical, where the instance remains available for your other tasks even if the daemon task can't start or stops. These instances aren't included in `runningCount`.
Type: Integer
Required: No

## See Also
<a name="API_DaemonCapacityProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/DaemonCapacityProvider)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/DaemonCapacityProvider)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/DaemonCapacityProvider)

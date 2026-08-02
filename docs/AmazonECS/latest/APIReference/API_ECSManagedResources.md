---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ECSManagedResources.html
---

# ECSManagedResources
<a name="API_ECSManagedResources"></a>

Represents the AWS resources managed by Amazon ECS for an Express service, including ingress paths, auto-scaling policies, metric alarms, and security groups.

## Contents
<a name="API_ECSManagedResources_Contents"></a>

 ** autoScaling **   <a name="ECS-Type-ECSManagedResources-autoScaling"></a>
The auto-scaling configuration and policies for the Express service.
Type: [ManagedAutoScaling](API_ManagedAutoScaling.md) object
Required: No

 ** ingressPaths **   <a name="ECS-Type-ECSManagedResources-ingressPaths"></a>
The ingress paths and endpoints for the Express service.
Type: Array of [ManagedIngressPath](API_ManagedIngressPath.md) objects
Required: No

 ** logGroups **   <a name="ECS-Type-ECSManagedResources-logGroups"></a>
The log groups managed by the Express service.
Type: Array of [ManagedLogGroup](API_ManagedLogGroup.md) objects
Required: No

 ** metricAlarms **   <a name="ECS-Type-ECSManagedResources-metricAlarms"></a>
The CloudWatch metric alarms associated with the Express service.
Type: Array of [ManagedMetricAlarm](API_ManagedMetricAlarm.md) objects
Required: No

 ** serviceSecurityGroups **   <a name="ECS-Type-ECSManagedResources-serviceSecurityGroups"></a>
The security groups managed by the Express service.
Type: Array of [ManagedSecurityGroup](API_ManagedSecurityGroup.md) objects
Required: No

## See Also
<a name="API_ECSManagedResources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ECSManagedResources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ECSManagedResources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ECSManagedResources)

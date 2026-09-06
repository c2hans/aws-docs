---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ServiceRevisionSummary.html
---

# ServiceRevisionSummary
<a name="API_ServiceRevisionSummary"></a>

The information about the number of requested, pending, and running tasks for a service revision.

## Contents
<a name="API_ServiceRevisionSummary_Contents"></a>

 ** arn **   <a name="ECS-Type-ServiceRevisionSummary-arn"></a>
The ARN of the service revision.
Type: String
Required: No

 ** pendingTaskCount **   <a name="ECS-Type-ServiceRevisionSummary-pendingTaskCount"></a>
The number of pending tasks for the service revision.
Type: Integer
Required: No

 ** requestedProductionTrafficWeight **   <a name="ECS-Type-ServiceRevisionSummary-requestedProductionTrafficWeight"></a>
The percentage of production traffic that is directed to this service revision. This value represents a snapshot of the traffic distribution and may not reflect real-time changes during active deployments. Valid values are 0.0 to 100.0.
Type: Double
Required: No

 ** requestedTaskCount **   <a name="ECS-Type-ServiceRevisionSummary-requestedTaskCount"></a>
The number of requested tasks for the service revision.
Type: Integer
Required: No

 ** requestedTestTrafficWeight **   <a name="ECS-Type-ServiceRevisionSummary-requestedTestTrafficWeight"></a>
The percentage of test traffic that is directed to this service revision. This value represents a snapshot of the traffic distribution and may not reflect real-time changes during active deployments. Valid values are 0.0 to 100.0.
Type: Double
Required: No

 ** runningTaskCount **   <a name="ECS-Type-ServiceRevisionSummary-runningTaskCount"></a>
The number of running tasks for the service revision.
Type: Integer
Required: No

## See Also
<a name="API_ServiceRevisionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ServiceRevisionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ServiceRevisionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ServiceRevisionSummary)

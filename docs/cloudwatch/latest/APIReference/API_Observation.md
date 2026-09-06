---
source_url: https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_Observation.html
---

# Observation
<a name="API_Observation"></a>

Describes an anomaly or error with the application.

## Contents
<a name="API_Observation_Contents"></a>

 ** CloudWatchEventDetailType **   <a name="appinsights-Type-Observation-CloudWatchEventDetailType"></a>
 The detail type of the CloudWatch Event-based observation, for example, `EC2 Instance State-change Notification`.
Type: String
Required: No

 ** CloudWatchEventId **   <a name="appinsights-Type-Observation-CloudWatchEventId"></a>
 The ID of the CloudWatch Event-based observation related to the detected problem.
Type: String
Required: No

 ** CloudWatchEventSource **   <a name="appinsights-Type-Observation-CloudWatchEventSource"></a>
 The source of the CloudWatch Event.
Type: String
Valid Values: `EC2 | CODE_DEPLOY | HEALTH | RDS`
Required: No

 ** CodeDeployApplication **   <a name="appinsights-Type-Observation-CodeDeployApplication"></a>
 The CodeDeploy application to which the deployment belongs.
Type: String
Required: No

 ** CodeDeployDeploymentGroup **   <a name="appinsights-Type-Observation-CodeDeployDeploymentGroup"></a>
 The deployment group to which the CodeDeploy deployment belongs.
Type: String
Required: No

 ** CodeDeployDeploymentId **   <a name="appinsights-Type-Observation-CodeDeployDeploymentId"></a>
 The deployment ID of the CodeDeploy-based observation related to the detected problem.
Type: String
Required: No

 ** CodeDeployInstanceGroupId **   <a name="appinsights-Type-Observation-CodeDeployInstanceGroupId"></a>
 The instance group to which the CodeDeploy instance belongs.
Type: String
Required: No

 ** CodeDeployState **   <a name="appinsights-Type-Observation-CodeDeployState"></a>
 The status of the CodeDeploy deployment, for example `SUCCESS` or ` FAILURE`.
Type: String
Required: No

 ** EbsCause **   <a name="appinsights-Type-Observation-EbsCause"></a>
 The cause of an EBS CloudWatch event.
Type: String
Required: No

 ** EbsEvent **   <a name="appinsights-Type-Observation-EbsEvent"></a>
 The type of EBS CloudWatch event, such as `createVolume`, `deleteVolume` or `attachVolume`.
Type: String
Required: No

 ** EbsRequestId **   <a name="appinsights-Type-Observation-EbsRequestId"></a>
 The request ID of an EBS CloudWatch event.
Type: String
Required: No

 ** EbsResult **   <a name="appinsights-Type-Observation-EbsResult"></a>
 The result of an EBS CloudWatch event, such as `failed` or `succeeded`.
Type: String
Required: No

 ** Ec2State **   <a name="appinsights-Type-Observation-Ec2State"></a>
 The state of the instance, such as `STOPPING` or `TERMINATING`.
Type: String
Required: No

 ** EndTime **   <a name="appinsights-Type-Observation-EndTime"></a>
The time when the observation ended, in epoch seconds.
Type: Timestamp
Required: No

 ** HealthEventArn **   <a name="appinsights-Type-Observation-HealthEventArn"></a>
 The Amazon Resource Name (ARN) of the AWS Health Event-based observation.
Type: String
Required: No

 ** HealthEventDescription **   <a name="appinsights-Type-Observation-HealthEventDescription"></a>
 The description of the AWS Health event provided by the service, such as Amazon EC2.
Type: String
Required: No

 ** HealthEventTypeCategory **   <a name="appinsights-Type-Observation-HealthEventTypeCategory"></a>
 The category of the AWS Health event, such as `issue`.
Type: String
Required: No

 ** HealthEventTypeCode **   <a name="appinsights-Type-Observation-HealthEventTypeCode"></a>
 The type of the AWS Health event, for example, `AWS_EC2_POWER_CONNECTIVITY_ISSUE`.
Type: String
Required: No

 ** HealthService **   <a name="appinsights-Type-Observation-HealthService"></a>
 The service to which the AWS Health Event belongs, such as EC2.
Type: String
Required: No

 ** Id **   <a name="appinsights-Type-Observation-Id"></a>
The ID of the observation type.
Type: String
Length Constraints: Fixed length of 38.
Pattern: `o-[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}`
Required: No

 ** LineTime **   <a name="appinsights-Type-Observation-LineTime"></a>
The timestamp in the CloudWatch Logs that specifies when the matched line occurred.
Type: Timestamp
Required: No

 ** LogFilter **   <a name="appinsights-Type-Observation-LogFilter"></a>
The log filter of the observation.
Type: String
Valid Values: `ERROR | WARN | INFO`
Required: No

 ** LogGroup **   <a name="appinsights-Type-Observation-LogGroup"></a>
The log group name.
Type: String
Required: No

 ** LogText **   <a name="appinsights-Type-Observation-LogText"></a>
The log text of the observation.
Type: String
Required: No

 ** MetricName **   <a name="appinsights-Type-Observation-MetricName"></a>
The name of the observation metric.
Type: String
Required: No

 ** MetricNamespace **   <a name="appinsights-Type-Observation-MetricNamespace"></a>
The namespace of the observation metric.
Type: String
Required: No

 ** RdsEventCategories **   <a name="appinsights-Type-Observation-RdsEventCategories"></a>
 The category of an RDS event.
Type: String
Required: No

 ** RdsEventMessage **   <a name="appinsights-Type-Observation-RdsEventMessage"></a>
 The message of an RDS event.
Type: String
Required: No

 ** S3EventName **   <a name="appinsights-Type-Observation-S3EventName"></a>
 The name of the S3 CloudWatch Event-based observation.
Type: String
Required: No

 ** SourceARN **   <a name="appinsights-Type-Observation-SourceARN"></a>
The source resource ARN of the observation.
Type: String
Required: No

 ** SourceType **   <a name="appinsights-Type-Observation-SourceType"></a>
The source type of the observation.
Type: String
Required: No

 ** StartTime **   <a name="appinsights-Type-Observation-StartTime"></a>
The time when the observation was first detected, in epoch seconds.
Type: Timestamp
Required: No

 ** StatesArn **   <a name="appinsights-Type-Observation-StatesArn"></a>
 The Amazon Resource Name (ARN) of the step function-based observation.
Type: String
Required: No

 ** StatesExecutionArn **   <a name="appinsights-Type-Observation-StatesExecutionArn"></a>
 The Amazon Resource Name (ARN) of the step function execution-based observation.
Type: String
Required: No

 ** StatesInput **   <a name="appinsights-Type-Observation-StatesInput"></a>
 The input to the step function-based observation.
Type: String
Required: No

 ** StatesStatus **   <a name="appinsights-Type-Observation-StatesStatus"></a>
 The status of the step function-related observation.
Type: String
Required: No

 ** Unit **   <a name="appinsights-Type-Observation-Unit"></a>
The unit of the source observation metric.
Type: String
Required: No

 ** Value **   <a name="appinsights-Type-Observation-Value"></a>
The value of the source observation metric.
Type: Double
Required: No

 ** XRayErrorPercent **   <a name="appinsights-Type-Observation-XRayErrorPercent"></a>
 The X-Ray request error percentage for this node.
Type: Integer
Required: No

 ** XRayFaultPercent **   <a name="appinsights-Type-Observation-XRayFaultPercent"></a>
 The X-Ray request fault percentage for this node.
Type: Integer
Required: No

 ** XRayNodeName **   <a name="appinsights-Type-Observation-XRayNodeName"></a>
 The name of the X-Ray node.
Type: String
Required: No

 ** XRayNodeType **   <a name="appinsights-Type-Observation-XRayNodeType"></a>
 The type of the X-Ray node.
Type: String
Required: No

 ** XRayRequestAverageLatency **   <a name="appinsights-Type-Observation-XRayRequestAverageLatency"></a>
 The X-Ray node request average latency for this node.
Type: Long
Required: No

 ** XRayRequestCount **   <a name="appinsights-Type-Observation-XRayRequestCount"></a>
 The X-Ray request count for this node.
Type: Integer
Required: No

 ** XRayThrottlePercent **   <a name="appinsights-Type-Observation-XRayThrottlePercent"></a>
 The X-Ray request throttle percentage for this node.
Type: Integer
Required: No

## See Also
<a name="API_Observation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-insights-2018-11-25/Observation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-insights-2018-11-25/Observation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-insights-2018-11-25/Observation)

---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_PutScalingPolicy.html
---

# PutScalingPolicy
<a name="API_PutScalingPolicy"></a>

 **This API works with the following fleet types:** EC2, Container

Creates or updates a scaling policy for a fleet. Scaling policies are used to automatically scale a fleet's hosting capacity to meet player demand. An active scaling policy instructs Amazon GameLift Servers to track a fleet metric and automatically change the fleet's capacity when a certain threshold is reached. There are two types of scaling policies: target-based and rule-based. Use a target-based policy to quickly and efficiently manage fleet scaling; this option is the most commonly used. Use rule-based policies when you need to exert fine-grained control over auto-scaling.

Fleets can have multiple scaling policies of each type in force at the same time; you can have one target-based policy, one or multiple rule-based scaling policies, or both. We recommend caution, however, because multiple auto-scaling policies can have unintended consequences.

Learn more about how to work with auto-scaling in [Set Up Fleet Automatic Scaling](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-autoscaling.html).

 **Target-based policy**

A target-based policy tracks a single metric: PercentAvailableGameSessions. This metric tells us how much of a fleet's hosting capacity is ready to host game sessions but is not currently in use. This is the fleet's buffer; it measures the additional player demand that the fleet could handle at current capacity. With a target-based policy, you set your ideal buffer size and leave it to Amazon GameLift Servers to take whatever action is needed to maintain that target.

For example, you might choose to maintain a 10% buffer for a fleet that has the capacity to host 100 simultaneous game sessions. This policy tells Amazon GameLift Servers to take action whenever the fleet's available capacity falls below or rises above 10 game sessions. Amazon GameLift Servers will start new instances or stop unused instances in order to return to the 10% buffer.

To create or update a target-based policy, specify a fleet ID and name, and set the policy type to "TargetBased". Specify the metric to track (PercentAvailableGameSessions) and reference a `TargetConfiguration` object with your desired buffer value. Exclude all other parameters. On a successful request, the policy name is returned. The scaling policy is automatically in force as soon as it's successfully created. If the fleet's auto-scaling actions are temporarily suspended, the new policy will be in force once the fleet actions are restarted.

 **Rule-based policy**

A rule-based policy tracks specified fleet metric, sets a threshold value, and specifies the type of action to initiate when triggered. With a rule-based policy, you can select from several available fleet metrics. Each policy specifies whether to scale up or scale down (and by how much), so you need one policy for each type of action.

For example, a policy may make the following statement: "If the percentage of idle instances is greater than 20% for more than 15 minutes, then reduce the fleet capacity by 10%."

A policy's rule statement has the following structure:

If `[MetricName]` is `[ComparisonOperator]` `[Threshold]` for `[EvaluationPeriods]` minutes, then `[ScalingAdjustmentType]` to/by `[ScalingAdjustment]`.

To implement the example, the rule statement would look like this:

If `[PercentIdleInstances]` is `[GreaterThanThreshold]` `[20]` for `[15]` minutes, then `[PercentChangeInCapacity]` to/by `[10]`.

To create or update a scaling policy, specify a unique combination of name and fleet ID, and set the policy type to "RuleBased". Specify the parameter values for a policy rule statement. On a successful request, the policy name is returned. Scaling policies are automatically in force as soon as they're successfully created. If the fleet's auto-scaling actions are temporarily suspended, the new policy will be in force once the fleet actions are restarted.

## Request Syntax
<a name="API_PutScalingPolicy_RequestSyntax"></a>

```
{
   "ComparisonOperator": "{{string}}",
   "EvaluationPeriods": {{number}},
   "FleetId": "{{string}}",
   "MetricName": "{{string}}",
   "Name": "{{string}}",
   "PolicyType": "{{string}}",
   "ScalingAdjustment": {{number}},
   "ScalingAdjustmentType": "{{string}}",
   "TargetConfiguration": {
      "TargetValue": {{number}}
   },
   "Threshold": {{number}}
}
```

## Request Parameters
<a name="API_PutScalingPolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [FleetId](#API_PutScalingPolicy_RequestSyntax) **   <a name="gameliftservers-PutScalingPolicy-request-FleetId"></a>
A unique identifier for the fleet to apply this policy to. You can use either the fleet ID or ARN value. The fleet cannot be in any of the following statuses: ERROR or DELETING.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+$|^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`
Required: Yes

 ** [MetricName](#API_PutScalingPolicy_RequestSyntax) **   <a name="gameliftservers-PutScalingPolicy-request-MetricName"></a>
Name of the Amazon GameLift Servers-defined metric that is used to trigger a scaling adjustment. For detailed descriptions of fleet metrics, see [Monitor Amazon GameLift Servers with Amazon CloudWatch](https://docs.aws.amazon.com/gamelift/latest/developerguide/monitoring-cloudwatch.html).
+  **ActivatingGameSessions** -- Game sessions in the process of being created.
+  **ActiveGameSessions** -- Game sessions that are currently running.
+  **ActiveInstances** -- Fleet instances that are currently running at least one game session.
+  **AvailableGameSessions** -- Additional game sessions that fleet could host simultaneously, given current capacity.
+  **AvailablePlayerSessions** -- Empty player slots in currently active game sessions. This includes game sessions that are not currently accepting players. Reserved player slots are not included.
+  **CurrentPlayerSessions** -- Player slots in active game sessions that are being used by a player or are reserved for a player.
+  **IdleInstances** -- Active instances that are currently hosting zero game sessions.
+  **PercentAvailableGameSessions** -- Unused percentage of the total number of game sessions that a fleet could host simultaneously, given current capacity. Use this metric for a target-based scaling policy.
+  **PercentIdleInstances** -- Percentage of the total number of active instances that are hosting zero game sessions.
+  **QueueDepth** -- Pending game session placement requests, in any queue, where the current fleet is the top-priority destination.
+  **WaitTime** -- Current wait time for pending game session placement requests, in any queue, where the current fleet is the top-priority destination.
Type: String
Valid Values: `ActivatingGameSessions | ActiveGameSessions | ActiveInstances | AvailableGameSessions | AvailablePlayerSessions | CurrentPlayerSessions | IdleInstances | PercentAvailableGameSessions | PercentIdleInstances | QueueDepth | WaitTime | ConcurrentActivatableGameSessions`
Required: Yes

 ** [Name](#API_PutScalingPolicy_RequestSyntax) **   <a name="gameliftservers-PutScalingPolicy-request-Name"></a>
A descriptive label that is associated with a fleet's scaling policy. Policy names do not need to be unique. A fleet can have only one scaling policy with the same name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** [ComparisonOperator](#API_PutScalingPolicy_RequestSyntax) **   <a name="gameliftservers-PutScalingPolicy-request-ComparisonOperator"></a>
Comparison operator to use when measuring the metric against the threshold value.
Type: String
Valid Values: `GreaterThanOrEqualToThreshold | GreaterThanThreshold | LessThanThreshold | LessThanOrEqualToThreshold`
Required: No

 ** [EvaluationPeriods](#API_PutScalingPolicy_RequestSyntax) **   <a name="gameliftservers-PutScalingPolicy-request-EvaluationPeriods"></a>
Length of time (in minutes) the metric must be at or beyond the threshold before a scaling event is triggered.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [PolicyType](#API_PutScalingPolicy_RequestSyntax) **   <a name="gameliftservers-PutScalingPolicy-request-PolicyType"></a>
The type of scaling policy to create. For a target-based policy, set the parameter *MetricName* to 'PercentAvailableGameSessions' and specify a *TargetConfiguration*. For a rule-based policy set the following parameters: *MetricName*, *ComparisonOperator*, *Threshold*, *EvaluationPeriods*, *ScalingAdjustmentType*, and *ScalingAdjustment*.
Type: String
Valid Values: `RuleBased | TargetBased`
Required: No

 ** [ScalingAdjustment](#API_PutScalingPolicy_RequestSyntax) **   <a name="gameliftservers-PutScalingPolicy-request-ScalingAdjustment"></a>
Amount of adjustment to make, based on the scaling adjustment type.
Type: Integer
Required: No

 ** [ScalingAdjustmentType](#API_PutScalingPolicy_RequestSyntax) **   <a name="gameliftservers-PutScalingPolicy-request-ScalingAdjustmentType"></a>
The type of adjustment to make to a fleet's instance count:
+  **ChangeInCapacity** -- add (or subtract) the scaling adjustment value from the current instance count. Positive values scale up while negative values scale down.
+  **ExactCapacity** -- set the instance count to the scaling adjustment value.
+  **PercentChangeInCapacity** -- increase or reduce the current instance count by the scaling adjustment, read as a percentage. Positive values scale up while negative values scale down; for example, a value of "-10" scales the fleet down by 10%.
Type: String
Valid Values: `ChangeInCapacity | ExactCapacity | PercentChangeInCapacity`
Required: No

 ** [TargetConfiguration](#API_PutScalingPolicy_RequestSyntax) **   <a name="gameliftservers-PutScalingPolicy-request-TargetConfiguration"></a>
An object that contains settings for a target-based scaling policy.
Type: [TargetConfiguration](API_TargetConfiguration.md) object
Required: No

 ** [Threshold](#API_PutScalingPolicy_RequestSyntax) **   <a name="gameliftservers-PutScalingPolicy-request-Threshold"></a>
Metric value used to trigger a scaling event.
Type: Double
Required: No

## Response Syntax
<a name="API_PutScalingPolicy_ResponseSyntax"></a>

```
{
   "Name": "string"
}
```

## Response Elements
<a name="API_PutScalingPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Name](#API_PutScalingPolicy_ResponseSyntax) **   <a name="gameliftservers-PutScalingPolicy-response-Name"></a>
A descriptive label that is associated with a fleet's scaling policy. Policy names do not need to be unique.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_PutScalingPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.
HTTP Status Code: 500

 ** InvalidRequestException **
One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.
HTTP Status Code: 400

 ** NotFoundException **
The requested resource was not found. The resource was either not created yet or deleted.
HTTP Status Code: 400

 ** UnauthorizedException **
The client failed authentication. Clients should not retry such requests.
HTTP Status Code: 400

 ** UnsupportedRegionException **
The requested operation is not supported in the Region specified.
HTTP Status Code: 400

## Examples
<a name="API_PutScalingPolicy_Examples"></a>

### Create a target-based scaling policy
<a name="API_PutScalingPolicy_Example_1"></a>

This example sets up auto-scaling using a target-based scaling policy. For this fleet, we want to maintain a 15% capacity buffer for our game, so that our fleet will always be able to immediately accommodate some additional game sessions. For a target-based policy, we need to specify a fleet ID, policy name and type, metric name (set this parameter to "PercentAvailableGameSessions"), and target configuration (buffer size).

HTTP requests are authenticated using an [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) signature in the `Authorization` header field.

#### Sample Request
<a name="API_PutScalingPolicy_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: gamelift.us-west-2.amazonaws.com;
Accept-Encoding: identity
Content-Length: 338
User-Agent: aws-cli/1.11.36 Python/2.7.9 Windows/7 botocore/1.4.93
Content-Type: application/x-amz-json-1.0
Authorization: AWS4-HMAC-SHA256  Credential=AKIAIOSFODNN7EXAMPLE/20170406/us-west-2/gamelift/aws4_request, SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
X-Amz-Date: 20170406T004805Z
X-Amz-Target: GameLift.PutScalingPolicy

{
    "FleetId": "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
    "Name": "My_Target_Policy_1",
    "PolicyType": "TargetBased",
    "MetricName": "PercentAvailableGameSessions",
    "TargetConfiguration": {"TargetValue": 15}
}

CLI syntax:

$aws gamelift put-scaling-policy
--fleet-id "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa"
--name "My_Target_Policy_1"
--policy-type "TargetBased"
--metric-name "PercentAvailableGameSessions"
--target-configuration "TargetValue=5"
```

#### Sample Response
<a name="API_PutScalingPolicy_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: b34f8665-EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 607
Date: Thu, 06 Apr 2017 00:48:07 GMT

{
    "Name": "My_Target_Policy_1"
}
```

### Create a rule-based scaling policy
<a name="API_PutScalingPolicy_Example_2"></a>

This example illustrates using a rule-based policy to supplement a target-based policy. While the target policy does most of the work of ensuring that capacity tracks with player demand, a well-formed rule-based policy can handle special circumstances and edge cases. For example, the target-based approach becomes less efficient when fleets have just few instances. We can mitigate this issue by creating a rule that maintains at least one idle instance ready to host new game sessions. At low capacity, the two policies do not conflict; at higher capacity, the rule-based policy loses relevance.

HTTP requests are authenticated using an [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) signature in the `Authorization` header field.

#### Sample Request
<a name="API_PutScalingPolicy_Example_2_Request"></a>

```
POST / HTTP/1.1
Host: gamelift.us-west-2.amazonaws.com;
Accept-Encoding: identity
Content-Length: 336
User-Agent: aws-cli/1.11.36 Python/2.7.9 Windows/7 botocore/1.4.93
Content-Type: application/x-amz-json-1.0
Authorization: AWS4-HMAC-SHA256  Credential=AKIAIOSFODNN7EXAMPLE/20170406/us-west-2/gamelift/aws4_request, SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
X-Amz-Date: 20170406T004805Z
X-Amz-Target: GameLift.PutScalingPolicy

{
    "FleetId": "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
    "Name": "My_Rule_Policy_1",
    "PolicyType": "RuleBased",
    "MetricName": "IdleInstances",
    "ComparisonOperator": "LessThanThreshold",
    "Threshold": "2"
    "EvaluationPeriods": "5"
    "ScalingAdjustmentType": "ChangeInCapacity"
    "ScalingAdjustment": "1"
    }
}

CLI syntax:

$aws gamelift put-scaling-policy
--fleet-id "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa"
--name "My_Rule_Policy_1"
--policy-type "RuleBased"
--metric-name "IdleInstances"
--comparison-operator "LessThanThreshold"
--threshold "2"
--evaluation-periods "5"
--scaling-adjustment-type "ChangeInCapacity"
--scaling-adjustment "1"
```

#### Sample Response
<a name="API_PutScalingPolicy_Example_2_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: b34f8665-EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 600
Date: Thu, 06 Apr 2017 00:48:07 GMT

{
    "Name": "My_Rule_Policy_1"
}
```

## See Also
<a name="API_PutScalingPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/PutScalingPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/PutScalingPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/PutScalingPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/PutScalingPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/PutScalingPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/PutScalingPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/PutScalingPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/PutScalingPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/PutScalingPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/PutScalingPolicy)

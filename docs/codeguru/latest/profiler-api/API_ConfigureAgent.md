---
source_url: https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ConfigureAgent.html
---

# ConfigureAgent
<a name="API_ConfigureAgent"></a>

 Used by profiler agents to report their current state and to receive remote configuration updates. For example, `ConfigureAgent` can be used to tell an agent whether to profile or not and for how long to return profiling data.

## Request Syntax
<a name="API_ConfigureAgent_RequestSyntax"></a>

```
POST /profilingGroups/{{profilingGroupName}}/configureAgent HTTP/1.1
Content-type: application/json

{
   "fleetInstanceId": "{{string}}",
   "metadata": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_ConfigureAgent_RequestParameters"></a>

The request uses the following URI parameters.

 ** [profilingGroupName](#API_ConfigureAgent_RequestSyntax) **   <a name="profiler-ConfigureAgent-request-uri-profilingGroupName"></a>
 The name of the profiling group for which the configured agent is collecting profiling data.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w-]+`
Required: Yes

## Request Body
<a name="API_ConfigureAgent_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [fleetInstanceId](#API_ConfigureAgent_RequestSyntax) **   <a name="profiler-ConfigureAgent-request-fleetInstanceId"></a>
 A universally unique identifier (UUID) for a profiling instance. For example, if the profiling instance is an Amazon EC2 instance, it is the instance ID. If it is an AWS Fargate container, it is the container's task ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [metadata](#API_ConfigureAgent_RequestSyntax) **   <a name="profiler-ConfigureAgent-request-metadata"></a>
 Metadata captured about the compute platform the agent is running on. It includes information about sampling and reporting. The valid fields are:
+  `COMPUTE_PLATFORM` - The compute platform on which the agent is running
+  `AGENT_ID` - The ID for an agent instance.
+  `AWS_REQUEST_ID` - The AWS request ID of a Lambda invocation.
+  `EXECUTION_ENVIRONMENT` - The execution environment a Lambda function is running on.
+  `LAMBDA_FUNCTION_ARN` - The Amazon Resource Name (ARN) that is used to invoke a Lambda function.
+  `LAMBDA_MEMORY_LIMIT_IN_MB` - The memory allocated to a Lambda function.
+  `LAMBDA_REMAINING_TIME_IN_MILLISECONDS` - The time in milliseconds before execution of a Lambda function times out.
+  `LAMBDA_TIME_GAP_BETWEEN_INVOKES_IN_MILLISECONDS` - The time in milliseconds between two invocations of a Lambda function.
+  `LAMBDA_PREVIOUS_EXECUTION_TIME_IN_MILLISECONDS` - The time in milliseconds for the previous Lambda invocation.
Type: String to string map
Valid Keys: `ComputePlatform | AgentId | AwsRequestId | ExecutionEnvironment | LambdaFunctionArn | LambdaMemoryLimitInMB | LambdaRemainingTimeInMilliseconds | LambdaTimeGapBetweenInvokesInMilliseconds | LambdaPreviousExecutionTimeInMilliseconds`
Required: No

## Response Syntax
<a name="API_ConfigureAgent_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "agentParameters": {
      "string" : "string"
   },
   "periodInSeconds": number,
   "shouldProfile": boolean
}
```

## Response Elements
<a name="API_ConfigureAgent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [agentParameters](#API_ConfigureAgent_ResponseSyntax) **   <a name="profiler-ConfigureAgent-response-agentParameters"></a>
 Parameters used by the profiler. The valid parameters are:
+  `MaxStackDepth` - The maximum depth of the stacks in the code that is represented in the profile. For example, if CodeGuru Profiler finds a method `A`, which calls method `B`, which calls method `C`, which calls method `D`, then the depth is 4. If the `maxDepth` is set to 2, then the profiler evaluates `A` and `B`.
+  `MemoryUsageLimitPercent` - The percentage of memory that is used by the profiler.
+  `MinimumTimeForReportingInMilliseconds` - The minimum time in milliseconds between sending reports.
+  `ReportingIntervalInMilliseconds` - The reporting interval in milliseconds used to report profiles.
+  `SamplingIntervalInMilliseconds` - The sampling interval in milliseconds that is used to profile samples.
Type: String to string map
Valid Keys: `SamplingIntervalInMilliseconds | ReportingIntervalInMilliseconds | MinimumTimeForReportingInMilliseconds | MemoryUsageLimitPercent | MaxStackDepth`

 ** [periodInSeconds](#API_ConfigureAgent_ResponseSyntax) **   <a name="profiler-ConfigureAgent-response-periodInSeconds"></a>
 How long a profiling agent should send profiling data using [`ConfigureAgent`](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ConfigureAgent.html). For example, if this is set to 300, the profiling agent calls [`ConfigureAgent`](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ConfigureAgent.html) every 5 minutes to submit the profiled data collected during that period.
Type: Integer

 ** [shouldProfile](#API_ConfigureAgent_ResponseSyntax) **   <a name="profiler-ConfigureAgent-response-shouldProfile"></a>
 A `Boolean` that specifies whether the profiling agent collects profiling data or not. Set to `true` to enable profiling.
Type: Boolean

## Errors
<a name="API_ConfigureAgent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The server encountered an internal error and is unable to complete the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource specified in the request does not exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The parameter is not valid.
HTTP Status Code: 400

## See Also
<a name="API_ConfigureAgent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeguruprofiler-2019-07-18/ConfigureAgent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeguruprofiler-2019-07-18/ConfigureAgent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguruprofiler-2019-07-18/ConfigureAgent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeguruprofiler-2019-07-18/ConfigureAgent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguruprofiler-2019-07-18/ConfigureAgent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeguruprofiler-2019-07-18/ConfigureAgent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeguruprofiler-2019-07-18/ConfigureAgent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeguruprofiler-2019-07-18/ConfigureAgent)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codeguruprofiler-2019-07-18/ConfigureAgent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguruprofiler-2019-07-18/ConfigureAgent)

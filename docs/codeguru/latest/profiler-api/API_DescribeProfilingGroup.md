---
source_url: https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_DescribeProfilingGroup.html
---

# DescribeProfilingGroup
<a name="API_DescribeProfilingGroup"></a>

 Returns a [`ProfilingGroupDescription`](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ProfilingGroupDescription.html) object that contains information about the requested profiling group.

## Request Syntax
<a name="API_DescribeProfilingGroup_RequestSyntax"></a>

```
GET /profilingGroups/{{profilingGroupName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeProfilingGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [profilingGroupName](#API_DescribeProfilingGroup_RequestSyntax) **   <a name="profiler-DescribeProfilingGroup-request-uri-profilingGroupName"></a>
 The name of the profiling group to get information about.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w-]+`
Required: Yes

## Request Body
<a name="API_DescribeProfilingGroup_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeProfilingGroup_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "agentOrchestrationConfig": {
      "profilingEnabled": boolean
   },
   "arn": "string",
   "computePlatform": "string",
   "createdAt": "string",
   "name": "string",
   "profilingStatus": {
      "latestAgentOrchestratedAt": "string",
      "latestAgentProfileReportedAt": "string",
      "latestAggregatedProfile": {
         "period": "string",
         "start": "string"
      }
   },
   "tags": {
      "string" : "string"
   },
   "updatedAt": "string"
}
```

## Response Elements
<a name="API_DescribeProfilingGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [agentOrchestrationConfig](#API_DescribeProfilingGroup_ResponseSyntax) **   <a name="profiler-DescribeProfilingGroup-response-agentOrchestrationConfig"></a>
 An [`AgentOrchestrationConfig`](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_AgentOrchestrationConfig.html) object that indicates if the profiling group is enabled for profiled or not.
Type: [AgentOrchestrationConfig](API_AgentOrchestrationConfig.md) object

 ** [arn](#API_DescribeProfilingGroup_ResponseSyntax) **   <a name="profiler-DescribeProfilingGroup-response-arn"></a>
The Amazon Resource Name (ARN) identifying the profiling group resource.
Type: String

 ** [computePlatform](#API_DescribeProfilingGroup_ResponseSyntax) **   <a name="profiler-DescribeProfilingGroup-response-computePlatform"></a>
 The compute platform of the profiling group. If it is set to `AWSLambda`, then the profiled application runs on AWS Lambda. If it is set to `Default`, then the profiled application runs on a compute platform that is not AWS Lambda, such an Amazon EC2 instance, an on-premises server, or a different platform. The default is `Default`.
Type: String
Valid Values: `Default | AWSLambda`

 ** [createdAt](#API_DescribeProfilingGroup_ResponseSyntax) **   <a name="profiler-DescribeProfilingGroup-response-createdAt"></a>
The time when the profiling group was created. Specify using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.
Type: Timestamp

 ** [name](#API_DescribeProfilingGroup_ResponseSyntax) **   <a name="profiler-DescribeProfilingGroup-response-name"></a>
The name of the profiling group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w-]+`

 ** [profilingStatus](#API_DescribeProfilingGroup_ResponseSyntax) **   <a name="profiler-DescribeProfilingGroup-response-profilingStatus"></a>
 A [`ProfilingStatus`](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ProfilingStatus.html) object that includes information about the last time a profile agent pinged back, the last time a profile was received, and the aggregation period and start time for the most recent aggregated profile.
Type: [ProfilingStatus](API_ProfilingStatus.md) object

 ** [tags](#API_DescribeProfilingGroup_ResponseSyntax) **   <a name="profiler-DescribeProfilingGroup-response-tags"></a>
 A list of the tags that belong to this profiling group.
Type: String to string map

 ** [updatedAt](#API_DescribeProfilingGroup_ResponseSyntax) **   <a name="profiler-DescribeProfilingGroup-response-updatedAt"></a>
 The date and time when the profiling group was last updated. Specify using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.
Type: Timestamp

## Errors
<a name="API_DescribeProfilingGroup_Errors"></a>

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
<a name="API_DescribeProfilingGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeguruprofiler-2019-07-18/DescribeProfilingGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeguruprofiler-2019-07-18/DescribeProfilingGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguruprofiler-2019-07-18/DescribeProfilingGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeguruprofiler-2019-07-18/DescribeProfilingGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguruprofiler-2019-07-18/DescribeProfilingGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeguruprofiler-2019-07-18/DescribeProfilingGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeguruprofiler-2019-07-18/DescribeProfilingGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeguruprofiler-2019-07-18/DescribeProfilingGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codeguruprofiler-2019-07-18/DescribeProfilingGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguruprofiler-2019-07-18/DescribeProfilingGroup)

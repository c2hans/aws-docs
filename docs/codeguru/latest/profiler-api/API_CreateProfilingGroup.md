---
source_url: https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_CreateProfilingGroup.html
---

# CreateProfilingGroup
<a name="API_CreateProfilingGroup"></a>

Creates a profiling group.

## Request Syntax
<a name="API_CreateProfilingGroup_RequestSyntax"></a>

```
POST /profilingGroups?clientToken={{clientToken}} HTTP/1.1
Content-type: application/json

{
   "agentOrchestrationConfig": {
      "profilingEnabled": {{boolean}}
   },
   "computePlatform": "{{string}}",
   "profilingGroupName": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateProfilingGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [clientToken](#API_CreateProfilingGroup_RequestSyntax) **   <a name="profiler-CreateProfilingGroup-request-uri-clientToken"></a>
 Amazon CodeGuru Profiler uses this universally unique identifier (UUID) to prevent the accidental creation of duplicate profiling groups if there are failures and retries.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w-]+`
Required: Yes

## Request Body
<a name="API_CreateProfilingGroup_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [agentOrchestrationConfig](#API_CreateProfilingGroup_RequestSyntax) **   <a name="profiler-CreateProfilingGroup-request-agentOrchestrationConfig"></a>
 Specifies whether profiling is enabled or disabled for the created profiling group.
Type: [AgentOrchestrationConfig](API_AgentOrchestrationConfig.md) object
Required: No

 ** [computePlatform](#API_CreateProfilingGroup_RequestSyntax) **   <a name="profiler-CreateProfilingGroup-request-computePlatform"></a>
 The compute platform of the profiling group. Use `AWSLambda` if your application runs on AWS Lambda. Use `Default` if your application runs on a compute platform that is not AWS Lambda, such an Amazon EC2 instance, an on-premises server, or a different platform. If not specified, `Default` is used.
Type: String
Valid Values: `Default | AWSLambda`
Required: No

 ** [profilingGroupName](#API_CreateProfilingGroup_RequestSyntax) **   <a name="profiler-CreateProfilingGroup-request-profilingGroupName"></a>
The name of the profiling group to create.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w-]+`
Required: Yes

 ** [tags](#API_CreateProfilingGroup_RequestSyntax) **   <a name="profiler-CreateProfilingGroup-request-tags"></a>
 A list of tags to add to the created profiling group.
Type: String to string map
Required: No

## Response Syntax
<a name="API_CreateProfilingGroup_ResponseSyntax"></a>

```
HTTP/1.1 201
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
<a name="API_CreateProfilingGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [agentOrchestrationConfig](#API_CreateProfilingGroup_ResponseSyntax) **   <a name="profiler-CreateProfilingGroup-response-agentOrchestrationConfig"></a>
 An [`AgentOrchestrationConfig`](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_AgentOrchestrationConfig.html) object that indicates if the profiling group is enabled for profiled or not.
Type: [AgentOrchestrationConfig](API_AgentOrchestrationConfig.md) object

 ** [arn](#API_CreateProfilingGroup_ResponseSyntax) **   <a name="profiler-CreateProfilingGroup-response-arn"></a>
The Amazon Resource Name (ARN) identifying the profiling group resource.
Type: String

 ** [computePlatform](#API_CreateProfilingGroup_ResponseSyntax) **   <a name="profiler-CreateProfilingGroup-response-computePlatform"></a>
 The compute platform of the profiling group. If it is set to `AWSLambda`, then the profiled application runs on AWS Lambda. If it is set to `Default`, then the profiled application runs on a compute platform that is not AWS Lambda, such an Amazon EC2 instance, an on-premises server, or a different platform. The default is `Default`.
Type: String
Valid Values: `Default | AWSLambda`

 ** [createdAt](#API_CreateProfilingGroup_ResponseSyntax) **   <a name="profiler-CreateProfilingGroup-response-createdAt"></a>
The time when the profiling group was created. Specify using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.
Type: Timestamp

 ** [name](#API_CreateProfilingGroup_ResponseSyntax) **   <a name="profiler-CreateProfilingGroup-response-name"></a>
The name of the profiling group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w-]+`

 ** [profilingStatus](#API_CreateProfilingGroup_ResponseSyntax) **   <a name="profiler-CreateProfilingGroup-response-profilingStatus"></a>
 A [`ProfilingStatus`](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ProfilingStatus.html) object that includes information about the last time a profile agent pinged back, the last time a profile was received, and the aggregation period and start time for the most recent aggregated profile.
Type: [ProfilingStatus](API_ProfilingStatus.md) object

 ** [tags](#API_CreateProfilingGroup_ResponseSyntax) **   <a name="profiler-CreateProfilingGroup-response-tags"></a>
 A list of the tags that belong to this profiling group.
Type: String to string map

 ** [updatedAt](#API_CreateProfilingGroup_ResponseSyntax) **   <a name="profiler-CreateProfilingGroup-response-updatedAt"></a>
 The date and time when the profiling group was last updated. Specify using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.
Type: Timestamp

## Errors
<a name="API_CreateProfilingGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.
HTTP Status Code: 409

 ** InternalServerException **
The server encountered an internal error and is unable to complete the request.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
You have exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use [Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html) to request a service quota increase.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The parameter is not valid.
HTTP Status Code: 400

## See Also
<a name="API_CreateProfilingGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeguruprofiler-2019-07-18/CreateProfilingGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeguruprofiler-2019-07-18/CreateProfilingGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguruprofiler-2019-07-18/CreateProfilingGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeguruprofiler-2019-07-18/CreateProfilingGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguruprofiler-2019-07-18/CreateProfilingGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeguruprofiler-2019-07-18/CreateProfilingGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeguruprofiler-2019-07-18/CreateProfilingGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeguruprofiler-2019-07-18/CreateProfilingGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codeguruprofiler-2019-07-18/CreateProfilingGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguruprofiler-2019-07-18/CreateProfilingGroup)

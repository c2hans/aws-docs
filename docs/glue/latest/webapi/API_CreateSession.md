---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_CreateSession.html
---

# CreateSession
<a name="API_CreateSession"></a>

Creates a new session.

## Request Syntax
<a name="API_CreateSession_RequestSyntax"></a>

```
{
   "Command": {
      "Name": "{{string}}",
      "PythonVersion": "{{string}}"
   },
   "Connections": {
      "Connections": [ "{{string}}" ]
   },
   "DefaultArguments": {
      "{{string}}" : "{{string}}"
   },
   "Description": "{{string}}",
   "GlueVersion": "{{string}}",
   "Id": "{{string}}",
   "IdleTimeout": {{number}},
   "MaxCapacity": {{number}},
   "NumberOfWorkers": {{number}},
   "RequestOrigin": "{{string}}",
   "Role": "{{string}}",
   "SecurityConfiguration": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   },
   "Timeout": {{number}},
   "WorkerType": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateSession_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Command](#API_CreateSession_RequestSyntax) **   <a name="Glue-CreateSession-request-Command"></a>
The `SessionCommand` that runs the job.
Type: [SessionCommand](API_SessionCommand.md) object
Required: Yes

 ** [Connections](#API_CreateSession_RequestSyntax) **   <a name="Glue-CreateSession-request-Connections"></a>
The number of connections to use for the session.
Type: [ConnectionsList](API_ConnectionsList.md) object
Required: No

 ** [DefaultArguments](#API_CreateSession_RequestSyntax) **   <a name="Glue-CreateSession-request-DefaultArguments"></a>
A map array of key-value pairs. Max is 75 pairs.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 75 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[\.\-_A-Za-z0-9]+`
Value Length Constraints: Minimum length of 0. Maximum length of 4096.
Value Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** [Description](#API_CreateSession_RequestSyntax) **   <a name="Glue-CreateSession-request-Description"></a>
The description of the session.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** [GlueVersion](#API_CreateSession_RequestSyntax) **   <a name="Glue-CreateSession-request-GlueVersion"></a>
The AWS Glue version determines the versions of Apache Spark and Python that AWS Glue supports. The GlueVersion must be greater than 2.0.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^(\w+\.)+\w+$`
Required: No

 ** [Id](#API_CreateSession_RequestSyntax) **   <a name="Glue-CreateSession-request-Id"></a>
The ID of the session request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [IdleTimeout](#API_CreateSession_RequestSyntax) **   <a name="Glue-CreateSession-request-IdleTimeout"></a>
 The number of minutes when idle before session times out. Default for Spark ETL jobs is value of Timeout. Consult the documentation for other job types.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [MaxCapacity](#API_CreateSession_RequestSyntax) **   <a name="Glue-CreateSession-request-MaxCapacity"></a>
The number of AWS Glue data processing units (DPUs) that can be allocated when the job runs. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB memory.
Type: Double
Required: No

 ** [NumberOfWorkers](#API_CreateSession_RequestSyntax) **   <a name="Glue-CreateSession-request-NumberOfWorkers"></a>
The number of workers of a defined `WorkerType` to use for the session.
Type: Integer
Required: No

 ** [RequestOrigin](#API_CreateSession_RequestSyntax) **   <a name="Glue-CreateSession-request-RequestOrigin"></a>
The origin of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\.\-_A-Za-z0-9]+`
Required: No

 ** [Role](#API_CreateSession_RequestSyntax) **   <a name="Glue-CreateSession-request-Role"></a>
The IAM Role ARN
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[^:]*:iam::[0-9]*:role/.+`
Required: Yes

 ** [SecurityConfiguration](#API_CreateSession_RequestSyntax) **   <a name="Glue-CreateSession-request-SecurityConfiguration"></a>
The name of the SecurityConfiguration structure to be used with the session
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [Tags](#API_CreateSession_RequestSyntax) **   <a name="Glue-CreateSession-request-Tags"></a>
The map of key value pairs (tags) belonging to the session.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [Timeout](#API_CreateSession_RequestSyntax) **   <a name="Glue-CreateSession-request-Timeout"></a>
 The number of minutes before session times out. Default for Spark ETL jobs is 48 hours (2880 minutes). Consult the documentation for other job types.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [WorkerType](#API_CreateSession_RequestSyntax) **   <a name="Glue-CreateSession-request-WorkerType"></a>
The type of predefined worker that is allocated when a job runs. Accepts a value of G.1X, G.2X, G.4X, or G.8X for Spark jobs. Accepts the value Z.2X for Ray notebooks.
+ For the `G.1X` worker type, each worker maps to 1 DPU (4 vCPUs, 16 GB of memory) with 94GB disk, and provides 1 executor per worker. We recommend this worker type for workloads such as data transforms, joins, and queries, to offers a scalable and cost effective way to run most jobs.
+ For the `G.2X` worker type, each worker maps to 2 DPU (8 vCPUs, 32 GB of memory) with 138GB disk, and provides 1 executor per worker. We recommend this worker type for workloads such as data transforms, joins, and queries, to offers a scalable and cost effective way to run most jobs.
+ For the `G.4X` worker type, each worker maps to 4 DPU (16 vCPUs, 64 GB of memory) with 256GB disk, and provides 1 executor per worker. We recommend this worker type for jobs whose workloads contain your most demanding transforms, aggregations, joins, and queries. This worker type is available only for AWS Glue version 3.0 or later Spark ETL jobs in the following AWS Regions: US East (Ohio), US East (N. Virginia), US West (Oregon), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Canada (Central), Europe (Frankfurt), Europe (Ireland), and Europe (Stockholm).
+ For the `G.8X` worker type, each worker maps to 8 DPU (32 vCPUs, 128 GB of memory) with 512GB disk, and provides 1 executor per worker. We recommend this worker type for jobs whose workloads contain your most demanding transforms, aggregations, joins, and queries. This worker type is available only for AWS Glue version 3.0 or later Spark ETL jobs, in the same AWS Regions as supported for the `G.4X` worker type.
+ For the `Z.2X` worker type, each worker maps to 2 M-DPU (8vCPUs, 64 GB of memory) with 128 GB disk, and provides up to 8 Ray workers based on the autoscaler.
Type: String
Valid Values: `Standard | G.1X | G.2X | G.025X | G.4X | G.8X | Z.2X`
Required: No

## Response Syntax
<a name="API_CreateSession_ResponseSyntax"></a>

```
{
   "Session": {
      "Command": {
         "Name": "string",
         "PythonVersion": "string"
      },
      "CompletedOn": number,
      "Connections": {
         "Connections": [ "string" ]
      },
      "CreatedOn": number,
      "DefaultArguments": {
         "string" : "string"
      },
      "Description": "string",
      "DPUSeconds": number,
      "ErrorMessage": "string",
      "ExecutionTime": number,
      "GlueVersion": "string",
      "Id": "string",
      "IdleTimeout": number,
      "MaxCapacity": number,
      "NumberOfWorkers": number,
      "ProfileName": "string",
      "Progress": number,
      "Role": "string",
      "SecurityConfiguration": "string",
      "Status": "string",
      "WorkerType": "string"
   }
}
```

## Response Elements
<a name="API_CreateSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Session](#API_CreateSession_ResponseSyntax) **   <a name="Glue-CreateSession-response-Session"></a>
Returns the session object in the response.
Type: [Session](API_Session.md) object

## Errors
<a name="API_CreateSession_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** AlreadyExistsException **
A resource to be created or added already exists.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** IdempotentParameterMismatchException **
The same unique identifier was associated with two different records.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** InternalServiceException **
An internal service error occurred.
 ** Message **
A message describing the problem.
HTTP Status Code: 500

 ** InvalidInputException **
The input provided was not valid.
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** ResourceNumberLimitExceededException **
A resource numerical limit was exceeded.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** ValidationException **
A value could not be validated.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_CreateSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/CreateSession)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/CreateSession)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/CreateSession)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/CreateSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/CreateSession)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/CreateSession)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/CreateSession)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/CreateSession)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/CreateSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/CreateSession)

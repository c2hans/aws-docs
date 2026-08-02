---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_StartJobRun.html
---

# StartJobRun
<a name="API_StartJobRun"></a>

Starts a job run using a job definition.

## Request Syntax
<a name="API_StartJobRun_RequestSyntax"></a>

```
{
   "AllocatedCapacity": {{number}},
   "Arguments": {
      "{{string}}" : "{{string}}"
   },
   "ExecutionClass": "{{string}}",
   "ExecutionRoleSessionPolicy": "{{string}}",
   "JobName": "{{string}}",
   "JobRunId": "{{string}}",
   "JobRunQueuingEnabled": {{boolean}},
   "MaxCapacity": {{number}},
   "NotificationProperty": {
      "NotifyDelayAfter": {{number}}
   },
   "NumberOfWorkers": {{number}},
   "SecurityConfiguration": "{{string}}",
   "Timeout": {{number}},
   "WorkerType": "{{string}}"
}
```

## Request Parameters
<a name="API_StartJobRun_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AllocatedCapacity](#API_StartJobRun_RequestSyntax) **   <a name="Glue-StartJobRun-request-AllocatedCapacity"></a>
This field is deprecated. Use `MaxCapacity` instead.
The number of AWS Glue data processing units (DPUs) to allocate to this JobRun. You can allocate a minimum of 2 DPUs; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the [AWS Glue pricing page](https://aws.amazon.com/glue/pricing/).
Type: Integer
Required: No

 ** [Arguments](#API_StartJobRun_RequestSyntax) **   <a name="Glue-StartJobRun-request-Arguments"></a>
The job arguments associated with this run. For this job run, they replace the default arguments set in the job definition itself.
You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes.
Job arguments may be logged. Do not pass plaintext secrets as arguments. Retrieve secrets from a AWS Glue Connection, AWS Secrets Manager or other secret management mechanism if you intend to keep them within the Job.
For information about how to specify and consume your own Job arguments, see the [Calling AWS Glue APIs in Python](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html) topic in the developer guide.
For information about the arguments you can provide to this field when configuring Spark jobs, see the [Special Parameters Used by AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html) topic in the developer guide.
For information about the arguments you can provide to this field when configuring Ray jobs, see [Using job parameters in Ray jobs](https://docs.aws.amazon.com/glue/latest/dg/author-job-ray-job-parameters.html) in the developer guide.
Type: String to string map
Required: No

 ** [ExecutionClass](#API_StartJobRun_RequestSyntax) **   <a name="Glue-StartJobRun-request-ExecutionClass"></a>
Indicates whether the job is run with a standard or flexible execution class. The standard execution-class is ideal for time-sensitive workloads that require fast job startup and dedicated resources.
The flexible execution class is appropriate for time-insensitive jobs whose start and completion times may vary.
Only jobs with AWS Glue version 3.0 and above and command type `glueetl` will be allowed to set `ExecutionClass` to `FLEX`. The flexible execution class is available for Spark jobs.
Type: String
Length Constraints: Maximum length of 16.
Valid Values: `FLEX | STANDARD`
Required: No

 ** [ExecutionRoleSessionPolicy](#API_StartJobRun_RequestSyntax) **   <a name="Glue-StartJobRun-request-ExecutionRoleSessionPolicy"></a>
This inline session policy to the StartJobRun API allows you to dynamically restrict the permissions of the specified execution role for the scope of the job, without requiring the creation of additional IAM roles.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 2048.
Required: No

 ** [JobName](#API_StartJobRun_RequestSyntax) **   <a name="Glue-StartJobRun-request-JobName"></a>
The name of the job definition to use.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [JobRunId](#API_StartJobRun_RequestSyntax) **   <a name="Glue-StartJobRun-request-JobRunId"></a>
The ID of a previous `JobRun` to retry.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [JobRunQueuingEnabled](#API_StartJobRun_RequestSyntax) **   <a name="Glue-StartJobRun-request-JobRunQueuingEnabled"></a>
Specifies whether job run queuing is enabled for the job run.
A value of true means job run queuing is enabled for the job run. If false or not populated, the job run will not be considered for queueing.
Type: Boolean
Required: No

 ** [MaxCapacity](#API_StartJobRun_RequestSyntax) **   <a name="Glue-StartJobRun-request-MaxCapacity"></a>
For Glue version 1.0 or earlier jobs, using the standard worker type, the number of AWS Glue data processing units (DPUs) that can be allocated when this job runs. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the [AWS Glue pricing page](https://aws.amazon.com/glue/pricing/).
For Glue version 2.0\+ jobs, you cannot specify a `Maximum capacity`. Instead, you should specify a `Worker type` and the `Number of workers`.
Do not set `MaxCapacity` if using `WorkerType` and `NumberOfWorkers`.
The value that can be allocated for `MaxCapacity` depends on whether you are running a Python shell job, an Apache Spark ETL job, or an Apache Spark streaming ETL job:
+ When you specify a Python shell job (`JobCommand.Name`="pythonshell"), you can allocate either 0.0625 or 1 DPU. The default is 0.0625 DPU.
+ When you specify an Apache Spark ETL job (`JobCommand.Name`="glueetl") or Apache Spark streaming ETL job (`JobCommand.Name`="gluestreaming"), you can allocate from 2 to 100 DPUs. The default is 10 DPUs. This job type cannot have a fractional DPU allocation.
Type: Double
Required: No

 ** [NotificationProperty](#API_StartJobRun_RequestSyntax) **   <a name="Glue-StartJobRun-request-NotificationProperty"></a>
Specifies configuration properties of a job run notification.
Type: [NotificationProperty](API_NotificationProperty.md) object
Required: No

 ** [NumberOfWorkers](#API_StartJobRun_RequestSyntax) **   <a name="Glue-StartJobRun-request-NumberOfWorkers"></a>
The number of workers of a defined `workerType` that are allocated when a job runs.
Type: Integer
Required: No

 ** [SecurityConfiguration](#API_StartJobRun_RequestSyntax) **   <a name="Glue-StartJobRun-request-SecurityConfiguration"></a>
The name of the `SecurityConfiguration` structure to be used with this job run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [Timeout](#API_StartJobRun_RequestSyntax) **   <a name="Glue-StartJobRun-request-Timeout"></a>
The `JobRun` timeout in minutes. This is the maximum time that a job run can consume resources before it is terminated and enters `TIMEOUT` status. This value overrides the timeout value set in the parent job.
Jobs must have timeout values less than 7 days or 10080 minutes. Otherwise, the jobs will throw an exception.
When the value is left blank, the timeout is defaulted to 2,880 minutes for Glue version 4.0 and earlier, or 480 minutes for Glue version 5.0 and later.
Any existing AWS Glue jobs that had a timeout value greater than 7 days will be defaulted to 7 days. For instance if you have specified a timeout of 20 days for a batch job, it will be stopped on the 7th day.
For streaming jobs, if you have set up a maintenance window, it will be restarted during the maintenance window after 7 days.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [WorkerType](#API_StartJobRun_RequestSyntax) **   <a name="Glue-StartJobRun-request-WorkerType"></a>
The type of predefined worker that is allocated when a job runs. Accepts a value of G.1X, G.2X, G.4X, G.8X or G.025X for Spark jobs. Accepts the value Z.2X for Ray jobs.
+ For the `G.1X` worker type, each worker maps to 1 DPU (4 vCPUs, 16 GB of memory) with 94GB disk, and provides 1 executor per worker. We recommend this worker type for workloads such as data transforms, joins, and queries, to offers a scalable and cost effective way to run most jobs.
+ For the `G.2X` worker type, each worker maps to 2 DPU (8 vCPUs, 32 GB of memory) with 138GB disk, and provides 1 executor per worker. We recommend this worker type for workloads such as data transforms, joins, and queries, to offers a scalable and cost effective way to run most jobs.
+ For the `G.4X` worker type, each worker maps to 4 DPU (16 vCPUs, 64 GB of memory) with 256GB disk, and provides 1 executor per worker. We recommend this worker type for jobs whose workloads contain your most demanding transforms, aggregations, joins, and queries. This worker type is available only for AWS Glue version 3.0 or later Spark ETL jobs in the following AWS Regions: US East (Ohio), US East (N. Virginia), US West (Oregon), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Canada (Central), Europe (Frankfurt), Europe (Ireland), and Europe (Stockholm).
+ For the `G.8X` worker type, each worker maps to 8 DPU (32 vCPUs, 128 GB of memory) with 512GB disk, and provides 1 executor per worker. We recommend this worker type for jobs whose workloads contain your most demanding transforms, aggregations, joins, and queries. This worker type is available only for AWS Glue version 3.0 or later Spark ETL jobs, in the same AWS Regions as supported for the `G.4X` worker type.
+ For the `G.025X` worker type, each worker maps to 0.25 DPU (2 vCPUs, 4 GB of memory) with 84GB disk, and provides 1 executor per worker. We recommend this worker type for low volume streaming jobs. This worker type is only available for AWS Glue version 3.0 or later streaming jobs.
+ For the `Z.2X` worker type, each worker maps to 2 M-DPU (8vCPUs, 64 GB of memory) with 128 GB disk, and provides up to 8 Ray workers based on the autoscaler.
Type: String
Valid Values: `Standard | G.1X | G.2X | G.025X | G.4X | G.8X | Z.2X`
Required: No

## Response Syntax
<a name="API_StartJobRun_ResponseSyntax"></a>

```
{
   "JobRunId": "string"
}
```

## Response Elements
<a name="API_StartJobRun_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [JobRunId](#API_StartJobRun_ResponseSyntax) **   <a name="Glue-StartJobRun-response-JobRunId"></a>
The ID assigned to this job run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

## Errors
<a name="API_StartJobRun_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentRunsExceededException **
Too many jobs are being run concurrently.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** EntityNotFoundException **
A specified entity does not exist
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
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

## See Also
<a name="API_StartJobRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/StartJobRun)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/StartJobRun)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/StartJobRun)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/StartJobRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/StartJobRun)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/StartJobRun)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/StartJobRun)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/StartJobRun)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/StartJobRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/StartJobRun)

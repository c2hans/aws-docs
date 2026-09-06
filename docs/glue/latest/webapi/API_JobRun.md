---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_JobRun.html
---

# JobRun
<a name="API_JobRun"></a>

Contains information about a job run.

## Contents
<a name="API_JobRun_Contents"></a>

 ** AllocatedCapacity **   <a name="Glue-Type-JobRun-AllocatedCapacity"></a>
This field is deprecated. Use `MaxCapacity` instead.
The number of AWS Glue data processing units (DPUs) allocated to this JobRun. From 2 to 100 DPUs can be allocated; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the [AWS Glue pricing page](https://aws.amazon.com/glue/pricing/).
Type: Integer
Required: No

 ** Arguments **   <a name="Glue-Type-JobRun-Arguments"></a>
The job arguments associated with this run. For this job run, they replace the default arguments set in the job definition itself.
You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes.
Job arguments may be logged. Do not pass plaintext secrets as arguments. Retrieve secrets from a AWS Glue Connection, AWS Secrets Manager or other secret management mechanism if you intend to keep them within the Job.
For information about how to specify and consume your own Job arguments, see the [Calling AWS Glue APIs in Python](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html) topic in the developer guide.
For information about the arguments you can provide to this field when configuring Spark jobs, see the [Special Parameters Used by AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html) topic in the developer guide.
For information about the arguments you can provide to this field when configuring Ray jobs, see [Using job parameters in Ray jobs](https://docs.aws.amazon.com/glue/latest/dg/author-job-ray-job-parameters.html) in the developer guide.
Type: String to string map
Required: No

 ** Attempt **   <a name="Glue-Type-JobRun-Attempt"></a>
The number of the attempt to run this job.
Type: Integer
Required: No

 ** CompletedOn **   <a name="Glue-Type-JobRun-CompletedOn"></a>
The date and time that this job run completed.
Type: Timestamp
Required: No

 ** DPUSeconds **   <a name="Glue-Type-JobRun-DPUSeconds"></a>
This field can be set for either job runs with execution class `FLEX` or when Auto Scaling is enabled, and represents the total time each executor ran during the lifecycle of a job run in seconds, multiplied by a DPU factor (1 for `G.1X`, 2 for `G.2X`, or 0.25 for `G.025X` workers). This value may be different than the `executionEngineRuntime` \* `MaxCapacity` as in the case of Auto Scaling jobs, as the number of executors running at a given time may be less than the `MaxCapacity`. Therefore, it is possible that the value of `DPUSeconds` is less than `executionEngineRuntime` \* `MaxCapacity`.
Type: Double
Required: No

 ** ErrorMessage **   <a name="Glue-Type-JobRun-ErrorMessage"></a>
An error message associated with this job run.
Type: String
Required: No

 ** ExecutionClass **   <a name="Glue-Type-JobRun-ExecutionClass"></a>
Indicates whether the job is run with a standard or flexible execution class. The standard execution-class is ideal for time-sensitive workloads that require fast job startup and dedicated resources.
The flexible execution class is appropriate for time-insensitive jobs whose start and completion times may vary.
Only jobs with AWS Glue version 3.0 and above and command type `glueetl` will be allowed to set `ExecutionClass` to `FLEX`. The flexible execution class is available for Spark jobs.
Type: String
Length Constraints: Maximum length of 16.
Valid Values: `FLEX | STANDARD`
Required: No

 ** ExecutionRoleSessionPolicy **   <a name="Glue-Type-JobRun-ExecutionRoleSessionPolicy"></a>
This inline session policy to the StartJobRun API allows you to dynamically restrict the permissions of the specified execution role for the scope of the job, without requiring the creation of additional IAM roles.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 2048.
Required: No

 ** ExecutionTime **   <a name="Glue-Type-JobRun-ExecutionTime"></a>
The amount of time (in seconds) that the job run consumed resources.
Type: Integer
Required: No

 ** GlueVersion **   <a name="Glue-Type-JobRun-GlueVersion"></a>
In Spark jobs, `GlueVersion` determines the versions of Apache Spark and Python that AWS Glue available in a job. The Python version indicates the version supported for jobs of type Spark.
Ray jobs should set `GlueVersion` to `4.0` or greater. However, the versions of Ray, Python and additional libraries available in your Ray job are determined by the `Runtime` parameter of the Job command.
For more information about the available AWS Glue versions and corresponding Spark and Python versions, see [Glue version](https://docs.aws.amazon.com/glue/latest/dg/add-job.html) in the developer guide.
Jobs that are created without specifying a Glue version default to Glue 5.1.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^(\w+\.)+\w+$`
Required: No

 ** Id **   <a name="Glue-Type-JobRun-Id"></a>
The ID of this job run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** JobMode **   <a name="Glue-Type-JobRun-JobMode"></a>
A mode that describes how a job was created. Valid values are:
+  `SCRIPT` - The job was created using the AWS Glue Studio script editor.
+  `VISUAL` - The job was created using the AWS Glue Studio visual editor.
+  `NOTEBOOK` - The job was created using an interactive sessions notebook.
When the `JobMode` field is missing or null, `SCRIPT` is assigned as the default value.
Type: String
Valid Values: `SCRIPT | VISUAL | NOTEBOOK`
Required: No

 ** JobName **   <a name="Glue-Type-JobRun-JobName"></a>
The name of the job definition being used in this run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** JobRunQueuingEnabled **   <a name="Glue-Type-JobRun-JobRunQueuingEnabled"></a>
Specifies whether job run queuing is enabled for the job run.
A value of true means job run queuing is enabled for the job run. If false or not populated, the job run will not be considered for queueing.
Type: Boolean
Required: No

 ** JobRunState **   <a name="Glue-Type-JobRun-JobRunState"></a>
The current state of the job run. For more information about the statuses of jobs that have terminated abnormally, see [AWS Glue Job Run Statuses](https://docs.aws.amazon.com/glue/latest/dg/job-run-statuses.html).
Type: String
Valid Values: `STARTING | RUNNING | STOPPING | STOPPED | SUCCEEDED | FAILED | TIMEOUT | ERROR | WAITING | EXPIRED`
Required: No

 ** LastModifiedOn **   <a name="Glue-Type-JobRun-LastModifiedOn"></a>
The last time that this job run was modified.
Type: Timestamp
Required: No

 ** LogGroupName **   <a name="Glue-Type-JobRun-LogGroupName"></a>
The name of the log group for secure logging that can be server-side encrypted in Amazon CloudWatch using AWS KMS. This name can be `/aws-glue/jobs/`, in which case the default encryption is `NONE`. If you add a role name and `SecurityConfiguration` name (in other words, `/aws-glue/jobs-yourRoleName-yourSecurityConfigurationName/`), then that security configuration is used to encrypt the log group.
Type: String
Required: No

 ** MaintenanceWindow **   <a name="Glue-Type-JobRun-MaintenanceWindow"></a>
This field specifies a day of the week and hour for a maintenance window for streaming jobs. AWS Glue periodically performs maintenance activities. During these maintenance windows, AWS Glue will need to restart your streaming jobs.
 AWS Glue will restart the job within 3 hours of the specified maintenance window. For instance, if you set up the maintenance window for Monday at 10:00AM GMT, your jobs will be restarted between 10:00AM GMT to 1:00PM GMT.
Type: String
Pattern: `^(Sun|Mon|Tue|Wed|Thu|Fri|Sat):([01]?[0-9]|2[0-3])$`
Required: No

 ** MaxCapacity **   <a name="Glue-Type-JobRun-MaxCapacity"></a>
For Glue version 1.0 or earlier jobs, using the standard worker type, the number of AWS Glue data processing units (DPUs) that can be allocated when this job runs. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the [AWS Glue pricing page](https://aws.amazon.com/glue/pricing/).
For Glue version 2.0\+ jobs, you cannot specify a `Maximum capacity`. Instead, you should specify a `Worker type` and the `Number of workers`.
Do not set `MaxCapacity` if using `WorkerType` and `NumberOfWorkers`.
The value that can be allocated for `MaxCapacity` depends on whether you are running a Python shell job, an Apache Spark ETL job, or an Apache Spark streaming ETL job:
+ When you specify a Python shell job (`JobCommand.Name`="pythonshell"), you can allocate either 0.0625 or 1 DPU. The default is 0.0625 DPU.
+ When you specify an Apache Spark ETL job (`JobCommand.Name`="glueetl") or Apache Spark streaming ETL job (`JobCommand.Name`="gluestreaming"), you can allocate from 2 to 100 DPUs. The default is 10 DPUs. This job type cannot have a fractional DPU allocation.
Type: Double
Required: No

 ** NotificationProperty **   <a name="Glue-Type-JobRun-NotificationProperty"></a>
Specifies configuration properties of a job run notification.
Type: [NotificationProperty](API_NotificationProperty.md) object
Required: No

 ** NumberOfWorkers **   <a name="Glue-Type-JobRun-NumberOfWorkers"></a>
The number of workers of a defined `workerType` that are allocated when a job runs.
Type: Integer
Required: No

 ** PredecessorRuns **   <a name="Glue-Type-JobRun-PredecessorRuns"></a>
A list of predecessors to this job run.
Type: Array of [Predecessor](API_Predecessor.md) objects
Required: No

 ** PreviousRunId **   <a name="Glue-Type-JobRun-PreviousRunId"></a>
The ID of the previous run of this job. For example, the `JobRunId` specified in the `StartJobRun` action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** ProfileName **   <a name="Glue-Type-JobRun-ProfileName"></a>
The name of an AWS Glue usage profile associated with the job run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** SecurityConfiguration **   <a name="Glue-Type-JobRun-SecurityConfiguration"></a>
The name of the `SecurityConfiguration` structure to be used with this job run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** StartedOn **   <a name="Glue-Type-JobRun-StartedOn"></a>
The date and time at which this job run was started.
Type: Timestamp
Required: No

 ** StateDetail **   <a name="Glue-Type-JobRun-StateDetail"></a>
This field holds details that pertain to the state of a job run. The field is nullable.
For example, when a job run is in a WAITING state as a result of job run queuing, the field has the reason why the job run is in that state.
Type: String
Length Constraints: Maximum length of 400000.
Required: No

 ** Timeout **   <a name="Glue-Type-JobRun-Timeout"></a>
The `JobRun` timeout in minutes. This is the maximum time that a job run can consume resources before it is terminated and enters `TIMEOUT` status. This value overrides the timeout value set in the parent job.
Jobs must have timeout values less than 7 days or 10080 minutes. Otherwise, the jobs will throw an exception.
When the value is left blank, the timeout is defaulted to 2,880 minutes for Glue version 4.0 and earlier, or 480 minutes for Glue version 5.0 and later.
Any existing AWS Glue jobs that had a timeout value greater than 7 days will be defaulted to 7 days. For instance if you have specified a timeout of 20 days for a batch job, it will be stopped on the 7th day.
For streaming jobs, if you have set up a maintenance window, it will be restarted during the maintenance window after 7 days.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** TriggerName **   <a name="Glue-Type-JobRun-TriggerName"></a>
The name of the trigger that started this job run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** WorkerType **   <a name="Glue-Type-JobRun-WorkerType"></a>
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

## See Also
<a name="API_JobRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/JobRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/JobRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/JobRun)

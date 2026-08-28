---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_Job.html
---

# Job
<a name="API_Job"></a>

Specifies a job definition.

## Contents
<a name="API_Job_Contents"></a>

 ** AllocatedCapacity **   <a name="Glue-Type-Job-AllocatedCapacity"></a>
This field is deprecated. Use `MaxCapacity` instead.
The number of AWS Glue data processing units (DPUs) allocated to runs of this job. You can allocate a minimum of 2 DPUs; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the [AWS Glue pricing page](https://aws.amazon.com/glue/pricing/).

Type: Integer
Required: No

 ** CodeGenConfigurationNodes **   <a name="Glue-Type-Job-CodeGenConfigurationNodes"></a>
The representation of a directed acyclic graph on which both the Glue Studio visual component and Glue Studio code generation is based.
Type: String to [CodeGenConfigurationNode](API_CodeGenConfigurationNode.md) object map
Key Pattern: `[A-Za-z0-9_-]*`
Required: No

 ** Command **   <a name="Glue-Type-Job-Command"></a>
The `JobCommand` that runs this job.
Type: [JobCommand](API_JobCommand.md) object
Required: No

 ** Connections **   <a name="Glue-Type-Job-Connections"></a>
The connections used for this job.
Type: [ConnectionsList](API_ConnectionsList.md) object
Required: No

 ** CreatedOn **   <a name="Glue-Type-Job-CreatedOn"></a>
The time and date that this job definition was created.
Type: Timestamp
Required: No

 ** DefaultArguments **   <a name="Glue-Type-Job-DefaultArguments"></a>
The default arguments for every run of this job, specified as name-value pairs.
You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes.
Job arguments may be logged. Do not pass plaintext secrets as arguments. Retrieve secrets from a AWS Glue Connection, AWS Secrets Manager or other secret management mechanism if you intend to keep them within the Job.
For information about how to specify and consume your own Job arguments, see the [Calling AWS Glue APIs in Python](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html) topic in the developer guide.
For information about the arguments you can provide to this field when configuring Spark jobs, see the [Special Parameters Used by AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html) topic in the developer guide.
For information about the arguments you can provide to this field when configuring Ray jobs, see [Using job parameters in Ray jobs](https://docs.aws.amazon.com/glue/latest/dg/author-job-ray-job-parameters.html) in the developer guide.
Type: String to string map
Required: No

 ** Description **   <a name="Glue-Type-Job-Description"></a>
A description of the job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** ExecutionClass **   <a name="Glue-Type-Job-ExecutionClass"></a>
Indicates whether the job is run with a standard or flexible execution class. The standard execution class is ideal for time-sensitive workloads that require fast job startup and dedicated resources.
The flexible execution class is appropriate for time-insensitive jobs whose start and completion times may vary.
Only jobs with AWS Glue version 3.0 and above and command type `glueetl` will be allowed to set `ExecutionClass` to `FLEX`. The flexible execution class is available for Spark jobs.
Type: String
Length Constraints: Maximum length of 16.
Valid Values: `FLEX | STANDARD`
Required: No

 ** ExecutionProperty **   <a name="Glue-Type-Job-ExecutionProperty"></a>
An `ExecutionProperty` specifying the maximum number of concurrent runs allowed for this job.
Type: [ExecutionProperty](API_ExecutionProperty.md) object
Required: No

 ** GlueVersion **   <a name="Glue-Type-Job-GlueVersion"></a>
In Spark jobs, `GlueVersion` determines the versions of Apache Spark and Python that AWS Glue available in a job. The Python version indicates the version supported for jobs of type Spark.
Ray jobs should set `GlueVersion` to `4.0` or greater. However, the versions of Ray, Python and additional libraries available in your Ray job are determined by the `Runtime` parameter of the Job command.
For more information about the available AWS Glue versions and corresponding Spark and Python versions, see [Glue version](https://docs.aws.amazon.com/glue/latest/dg/add-job.html) in the developer guide.
Jobs that are created without specifying a Glue version default to Glue 5.1.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^(\w+\.)+\w+$`
Required: No

 ** JobMode **   <a name="Glue-Type-Job-JobMode"></a>
A mode that describes how a job was created. Valid values are:
+  `SCRIPT` - The job was created using the AWS Glue Studio script editor.
+  `VISUAL` - The job was created using the AWS Glue Studio visual editor.
+  `NOTEBOOK` - The job was created using an interactive sessions notebook.
When the `JobMode` field is missing or null, `SCRIPT` is assigned as the default value.
Type: String
Valid Values: `SCRIPT | VISUAL | NOTEBOOK`
Required: No

 ** JobRunQueuingEnabled **   <a name="Glue-Type-Job-JobRunQueuingEnabled"></a>
Specifies whether job run queuing is enabled for the job runs for this job.
A value of true means job run queuing is enabled for the job runs. If false or not populated, the job runs will not be considered for queueing.
If this field does not match the value set in the job run, then the value from the job run field will be used.
Type: Boolean
Required: No

 ** LastModifiedOn **   <a name="Glue-Type-Job-LastModifiedOn"></a>
The last point in time when this job definition was modified.
Type: Timestamp
Required: No

 ** LogUri **   <a name="Glue-Type-Job-LogUri"></a>
This field is reserved for future use.
Type: String
Required: No

 ** MaintenanceWindow **   <a name="Glue-Type-Job-MaintenanceWindow"></a>
This field specifies a day of the week and hour for a maintenance window for streaming jobs. AWS Glue periodically performs maintenance activities. During these maintenance windows, AWS Glue will need to restart your streaming jobs.
 AWS Glue will restart the job within 3 hours of the specified maintenance window. For instance, if you set up the maintenance window for Monday at 10:00AM GMT, your jobs will be restarted between 10:00AM GMT to 1:00PM GMT.
Type: String
Pattern: `^(Sun|Mon|Tue|Wed|Thu|Fri|Sat):([01]?[0-9]|2[0-3])$`
Required: No

 ** MaxCapacity **   <a name="Glue-Type-Job-MaxCapacity"></a>
For Glue version 1.0 or earlier jobs, using the standard worker type, the number of AWS Glue data processing units (DPUs) that can be allocated when this job runs. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the [AWS Glue pricing page](https://aws.amazon.com/glue/pricing/).
For Glue version 2.0 or later jobs, you cannot specify a `Maximum capacity`. Instead, you should specify a `Worker type` and the `Number of workers`.
Do not set `MaxCapacity` if using `WorkerType` and `NumberOfWorkers`.
The value that can be allocated for `MaxCapacity` depends on whether you are running a Python shell job, an Apache Spark ETL job, or an Apache Spark streaming ETL job:
+ When you specify a Python shell job (`JobCommand.Name`="pythonshell"), you can allocate either 0.0625 or 1 DPU. The default is 0.0625 DPU.
+ When you specify an Apache Spark ETL job (`JobCommand.Name`="glueetl") or Apache Spark streaming ETL job (`JobCommand.Name`="gluestreaming"), you can allocate from 2 to 100 DPUs. The default is 10 DPUs. This job type cannot have a fractional DPU allocation.
Type: Double
Required: No

 ** MaxRetries **   <a name="Glue-Type-Job-MaxRetries"></a>
The maximum number of times to retry this job after a JobRun fails.
Type: Integer
Required: No

 ** Name **   <a name="Glue-Type-Job-Name"></a>
The name you assign to this job definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** NonOverridableArguments **   <a name="Glue-Type-Job-NonOverridableArguments"></a>
Arguments for this job that are not overridden when providing job arguments in a job run, specified as name-value pairs.
Type: String to string map
Required: No

 ** NotificationProperty **   <a name="Glue-Type-Job-NotificationProperty"></a>
Specifies configuration properties of a job notification.
Type: [NotificationProperty](API_NotificationProperty.md) object
Required: No

 ** NumberOfWorkers **   <a name="Glue-Type-Job-NumberOfWorkers"></a>
The number of workers of a defined `workerType` that are allocated when a job runs.
Type: Integer
Required: No

 ** ProfileName **   <a name="Glue-Type-Job-ProfileName"></a>
The name of an AWS Glue usage profile associated with the job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** Role **   <a name="Glue-Type-Job-Role"></a>
The name or Amazon Resource Name (ARN) of the IAM role associated with this job.
Type: String
Required: No

 ** SecurityConfiguration **   <a name="Glue-Type-Job-SecurityConfiguration"></a>
The name of the `SecurityConfiguration` structure to be used with this job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** SourceControlDetails **   <a name="Glue-Type-Job-SourceControlDetails"></a>
The details for a source control configuration for a job, allowing synchronization of job artifacts to or from a remote repository.
Type: [SourceControlDetails](API_SourceControlDetails.md) object
Required: No

 ** Timeout **   <a name="Glue-Type-Job-Timeout"></a>
The job timeout in minutes. This is the maximum time that a job run can consume resources before it is terminated and enters `TIMEOUT` status.
Jobs must have timeout values less than 7 days or 10080 minutes. Otherwise, the jobs will throw an exception.
When the value is left blank, the timeout is defaulted to 2,880 minutes for Glue version 4.0 and earlier, or 480 minutes for Glue version 5.0 and later.
Any existing AWS Glue jobs that had a timeout value greater than 7 days will be defaulted to 7 days. For instance if you have specified a timeout of 20 days for a batch job, it will be stopped on the 7th day.
For streaming jobs, if you have set up a maintenance window, it will be restarted during the maintenance window after 7 days.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** WorkerType **   <a name="Glue-Type-Job-WorkerType"></a>
The type of predefined worker that is allocated when a job runs.
 AWS Glue provides multiple worker types to accommodate different workload requirements:
G Worker Types (General-purpose compute workers):
+ G.1X: 1 DPU (4 vCPUs, 16 GB memory, 94GB disk)
+ G.2X: 2 DPU (8 vCPUs, 32 GB memory, 138GB disk)
+ G.4X: 4 DPU (16 vCPUs, 64 GB memory, 256GB disk)
+ G.8X: 8 DPU (32 vCPUs, 128 GB memory, 512GB disk)
+ G.12X: 12 DPU (48 vCPUs, 192 GB memory, 768GB disk)
+ G.16X: 16 DPU (64 vCPUs, 256 GB memory, 1024GB disk)
R Worker Types (Memory-optimized workers):
+ R.1X: 1 M-DPU (4 vCPUs, 32 GB memory)
+ R.2X: 2 M-DPU (8 vCPUs, 64 GB memory)
+ R.4X: 4 M-DPU (16 vCPUs, 128 GB memory)
+ R.8X: 8 M-DPU (32 vCPUs, 256 GB memory)
Type: String
Valid Values: `Standard | G.1X | G.2X | G.025X | G.4X | G.8X | Z.2X`
Required: No

## See Also
<a name="API_Job_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/Job)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/Job)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/Job)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

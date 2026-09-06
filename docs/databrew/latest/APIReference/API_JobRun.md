---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_JobRun.html
---

# JobRun
<a name="API_JobRun"></a>

Represents one run of a DataBrew job.

## Contents
<a name="API_JobRun_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Attempt **   <a name="databrew-Type-JobRun-Attempt"></a>
The number of times that DataBrew has attempted to run the job.
Type: Integer
Required: No

 ** CompletedOn **   <a name="databrew-Type-JobRun-CompletedOn"></a>
The date and time when the job completed processing.
Type: Timestamp
Required: No

 ** DatabaseOutputs **   <a name="databrew-Type-JobRun-DatabaseOutputs"></a>
Represents a list of JDBC database output objects which defines the output destination for a DataBrew recipe job to write into.
Type: Array of [DatabaseOutput](API_DatabaseOutput.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** DataCatalogOutputs **   <a name="databrew-Type-JobRun-DataCatalogOutputs"></a>
One or more artifacts that represent the AWS Glue Data Catalog output from running the job.
Type: Array of [DataCatalogOutput](API_DataCatalogOutput.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** DatasetName **   <a name="databrew-Type-JobRun-DatasetName"></a>
The name of the dataset for the job to process.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** ErrorMessage **   <a name="databrew-Type-JobRun-ErrorMessage"></a>
A message indicating an error (if any) that was encountered when the job ran.
Type: String
Required: No

 ** ExecutionTime **   <a name="databrew-Type-JobRun-ExecutionTime"></a>
The amount of time, in seconds, during which a job run consumed resources.
Type: Integer
Required: No

 ** JobName **   <a name="databrew-Type-JobRun-JobName"></a>
The name of the job being processed during this run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 240.
Required: No

 ** JobSample **   <a name="databrew-Type-JobRun-JobSample"></a>
A sample configuration for profile jobs only, which determines the number of rows on which the profile job is run. If a `JobSample` value isn't provided, the default is used. The default value is CUSTOM\_ROWS for the mode parameter and 20,000 for the size parameter.
Type: [JobSample](API_JobSample.md) object
Required: No

 ** LogGroupName **   <a name="databrew-Type-JobRun-LogGroupName"></a>
The name of an Amazon CloudWatch log group, where the job writes diagnostic messages when it runs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** LogSubscription **   <a name="databrew-Type-JobRun-LogSubscription"></a>
The current status of Amazon CloudWatch logging for the job run.
Type: String
Valid Values: `ENABLE | DISABLE`
Required: No

 ** Outputs **   <a name="databrew-Type-JobRun-Outputs"></a>
One or more output artifacts from a job run.
Type: Array of [Output](API_Output.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** RecipeReference **   <a name="databrew-Type-JobRun-RecipeReference"></a>
The set of steps processed by the job.
Type: [RecipeReference](API_RecipeReference.md) object
Required: No

 ** RunId **   <a name="databrew-Type-JobRun-RunId"></a>
The unique identifier of the job run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** StartedBy **   <a name="databrew-Type-JobRun-StartedBy"></a>
The Amazon Resource Name (ARN) of the user who initiated the job run.
Type: String
Required: No

 ** StartedOn **   <a name="databrew-Type-JobRun-StartedOn"></a>
The date and time when the job run began.
Type: Timestamp
Required: No

 ** State **   <a name="databrew-Type-JobRun-State"></a>
The current state of the job run entity itself.
Type: String
Valid Values: `STARTING | RUNNING | STOPPING | STOPPED | SUCCEEDED | FAILED | TIMEOUT`
Required: No

 ** ValidationConfigurations **   <a name="databrew-Type-JobRun-ValidationConfigurations"></a>
List of validation configurations that are applied to the profile job run.
Type: Array of [ValidationConfiguration](API_ValidationConfiguration.md) objects
Array Members: Minimum number of 1 item.
Required: No

## See Also
<a name="API_JobRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/JobRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/JobRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/JobRun)

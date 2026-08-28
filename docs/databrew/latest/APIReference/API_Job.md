---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_Job.html
---

# Job
<a name="API_Job"></a>

Represents all of the attributes of a DataBrew job.

## Contents
<a name="API_Job_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Name **   <a name="databrew-Type-Job-Name"></a>
The unique name of the job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 240.
Required: Yes

 ** AccountId **   <a name="databrew-Type-Job-AccountId"></a>
The ID of the AWS account that owns the job.
Type: String
Length Constraints: Maximum length of 255.
Required: No

 ** CreateDate **   <a name="databrew-Type-Job-CreateDate"></a>
The date and time that the job was created.
Type: Timestamp
Required: No

 ** CreatedBy **   <a name="databrew-Type-Job-CreatedBy"></a>
The Amazon Resource Name (ARN) of the user who created the job.
Type: String
Required: No

 ** DatabaseOutputs **   <a name="databrew-Type-Job-DatabaseOutputs"></a>
Represents a list of JDBC database output objects which defines the output destination for a DataBrew recipe job to write into.
Type: Array of [DatabaseOutput](API_DatabaseOutput.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** DataCatalogOutputs **   <a name="databrew-Type-Job-DataCatalogOutputs"></a>
One or more artifacts that represent the AWS Glue Data Catalog output from running the job.
Type: Array of [DataCatalogOutput](API_DataCatalogOutput.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** DatasetName **   <a name="databrew-Type-Job-DatasetName"></a>
A dataset that the job is to process.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** EncryptionKeyArn **   <a name="databrew-Type-Job-EncryptionKeyArn"></a>
The Amazon Resource Name (ARN) of an encryption key that is used to protect the job output. For more information, see [Encrypting data written by DataBrew jobs](https://docs.aws.amazon.com/databrew/latest/dg/encryption-security-configuration.html)
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** EncryptionMode **   <a name="databrew-Type-Job-EncryptionMode"></a>
The encryption mode for the job, which can be one of the following:
+  `SSE-KMS` - Server-side encryption with keys managed by AWS KMS.
+  `SSE-S3` - Server-side encryption with keys managed by Amazon S3.
Type: String
Valid Values: `SSE-KMS | SSE-S3`
Required: No

 ** JobSample **   <a name="databrew-Type-Job-JobSample"></a>
A sample configuration for profile jobs only, which determines the number of rows on which the profile job is run. If a `JobSample` value isn't provided, the default value is used. The default value is CUSTOM\_ROWS for the mode parameter and 20,000 for the size parameter.
Type: [JobSample](API_JobSample.md) object
Required: No

 ** LastModifiedBy **   <a name="databrew-Type-Job-LastModifiedBy"></a>
The Amazon Resource Name (ARN) of the user who last modified the job.
Type: String
Required: No

 ** LastModifiedDate **   <a name="databrew-Type-Job-LastModifiedDate"></a>
The modification date and time of the job.
Type: Timestamp
Required: No

 ** LogSubscription **   <a name="databrew-Type-Job-LogSubscription"></a>
The current status of Amazon CloudWatch logging for the job.
Type: String
Valid Values: `ENABLE | DISABLE`
Required: No

 ** MaxCapacity **   <a name="databrew-Type-Job-MaxCapacity"></a>
The maximum number of nodes that can be consumed when the job processes data.
Type: Integer
Required: No

 ** MaxRetries **   <a name="databrew-Type-Job-MaxRetries"></a>
The maximum number of times to retry the job after a job run fails.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** Outputs **   <a name="databrew-Type-Job-Outputs"></a>
One or more artifacts that represent output from running the job.
Type: Array of [Output](API_Output.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** ProjectName **   <a name="databrew-Type-Job-ProjectName"></a>
The name of the project that the job is associated with.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** RecipeReference **   <a name="databrew-Type-Job-RecipeReference"></a>
A set of steps that the job runs.
Type: [RecipeReference](API_RecipeReference.md) object
Required: No

 ** ResourceArn **   <a name="databrew-Type-Job-ResourceArn"></a>
The unique Amazon Resource Name (ARN) for the job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** RoleArn **   <a name="databrew-Type-Job-RoleArn"></a>
The Amazon Resource Name (ARN) of the role to be assumed for this job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** Tags **   <a name="databrew-Type-Job-Tags"></a>
Metadata tags that have been applied to the job.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Maximum length of 256.
Required: No

 ** Timeout **   <a name="databrew-Type-Job-Timeout"></a>
The job's timeout in minutes. A job that attempts to run longer than this timeout period ends with a status of `TIMEOUT`.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** Type **   <a name="databrew-Type-Job-Type"></a>
The job type of the job, which must be one of the following:
+  `PROFILE` - A job to analyze a dataset, to determine its size, data types, data distribution, and more.
+  `RECIPE` - A job to apply one or more transformations to a dataset.
Type: String
Valid Values: `PROFILE | RECIPE`
Required: No

 ** ValidationConfigurations **   <a name="databrew-Type-Job-ValidationConfigurations"></a>
List of validation configurations that are applied to the profile job.
Type: Array of [ValidationConfiguration](API_ValidationConfiguration.md) objects
Array Members: Minimum number of 1 item.
Required: No

## See Also
<a name="API_Job_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/Job)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/Job)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/Job)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

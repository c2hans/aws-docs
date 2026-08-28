---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_CreateRecipeJob.html
---

# CreateRecipeJob
<a name="API_CreateRecipeJob"></a>

Creates a new job to transform input data, using steps defined in an existing AWS Glue DataBrew recipe

## Request Syntax
<a name="API_CreateRecipeJob_RequestSyntax"></a>

```
POST /recipeJobs HTTP/1.1
Content-type: application/json

{
   "DatabaseOutputs": [
      {
         "DatabaseOptions": {
            "TableName": "{{string}}",
            "TempDirectory": {
               "Bucket": "{{string}}",
               "BucketOwner": "{{string}}",
               "Key": "{{string}}"
            }
         },
         "DatabaseOutputMode": "{{string}}",
         "GlueConnectionName": "{{string}}"
      }
   ],
   "DataCatalogOutputs": [
      {
         "CatalogId": "{{string}}",
         "DatabaseName": "{{string}}",
         "DatabaseOptions": {
            "TableName": "{{string}}",
            "TempDirectory": {
               "Bucket": "{{string}}",
               "BucketOwner": "{{string}}",
               "Key": "{{string}}"
            }
         },
         "Overwrite": {{boolean}},
         "S3Options": {
            "Location": {
               "Bucket": "{{string}}",
               "BucketOwner": "{{string}}",
               "Key": "{{string}}"
            }
         },
         "TableName": "{{string}}"
      }
   ],
   "DatasetName": "{{string}}",
   "EncryptionKeyArn": "{{string}}",
   "EncryptionMode": "{{string}}",
   "LogSubscription": "{{string}}",
   "MaxCapacity": {{number}},
   "MaxRetries": {{number}},
   "Name": "{{string}}",
   "Outputs": [
      {
         "CompressionFormat": "{{string}}",
         "Format": "{{string}}",
         "FormatOptions": {
            "Csv": {
               "Delimiter": "{{string}}"
            }
         },
         "Location": {
            "Bucket": "{{string}}",
            "BucketOwner": "{{string}}",
            "Key": "{{string}}"
         },
         "MaxOutputFiles": {{number}},
         "Overwrite": {{boolean}},
         "PartitionColumns": [ "{{string}}" ]
      }
   ],
   "ProjectName": "{{string}}",
   "RecipeReference": {
      "Name": "{{string}}",
      "RecipeVersion": "{{string}}"
   },
   "RoleArn": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   },
   "Timeout": {{number}}
}
```

## URI Request Parameters
<a name="API_CreateRecipeJob_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateRecipeJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Name](#API_CreateRecipeJob_RequestSyntax) **   <a name="databrew-CreateRecipeJob-request-Name"></a>
A unique name for the job. Valid characters are alphanumeric (A-Z, a-z, 0-9), hyphen (-), period (.), and space.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 240.
Required: Yes

 ** [RoleArn](#API_CreateRecipeJob_RequestSyntax) **   <a name="databrew-CreateRecipeJob-request-RoleArn"></a>
The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role to be assumed when DataBrew runs the job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: Yes

 ** [DatabaseOutputs](#API_CreateRecipeJob_RequestSyntax) **   <a name="databrew-CreateRecipeJob-request-DatabaseOutputs"></a>
Represents a list of JDBC database output objects which defines the output destination for a DataBrew recipe job to write to.
Type: Array of [DatabaseOutput](API_DatabaseOutput.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** [DataCatalogOutputs](#API_CreateRecipeJob_RequestSyntax) **   <a name="databrew-CreateRecipeJob-request-DataCatalogOutputs"></a>
One or more artifacts that represent the AWS Glue Data Catalog output from running the job.
Type: Array of [DataCatalogOutput](API_DataCatalogOutput.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** [DatasetName](#API_CreateRecipeJob_RequestSyntax) **   <a name="databrew-CreateRecipeJob-request-DatasetName"></a>
The name of the dataset that this job processes.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [EncryptionKeyArn](#API_CreateRecipeJob_RequestSyntax) **   <a name="databrew-CreateRecipeJob-request-EncryptionKeyArn"></a>
The Amazon Resource Name (ARN) of an encryption key that is used to protect the job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** [EncryptionMode](#API_CreateRecipeJob_RequestSyntax) **   <a name="databrew-CreateRecipeJob-request-EncryptionMode"></a>
The encryption mode for the job, which can be one of the following:
+  `SSE-KMS` - Server-side encryption with keys managed by AWS KMS.
+  `SSE-S3` - Server-side encryption with keys managed by Amazon S3.
Type: String
Valid Values: `SSE-KMS | SSE-S3`
Required: No

 ** [LogSubscription](#API_CreateRecipeJob_RequestSyntax) **   <a name="databrew-CreateRecipeJob-request-LogSubscription"></a>
Enables or disables Amazon CloudWatch logging for the job. If logging is enabled, CloudWatch writes one log stream for each job run.
Type: String
Valid Values: `ENABLE | DISABLE`
Required: No

 ** [MaxCapacity](#API_CreateRecipeJob_RequestSyntax) **   <a name="databrew-CreateRecipeJob-request-MaxCapacity"></a>
The maximum number of nodes that DataBrew can consume when the job processes data.
Type: Integer
Required: No

 ** [MaxRetries](#API_CreateRecipeJob_RequestSyntax) **   <a name="databrew-CreateRecipeJob-request-MaxRetries"></a>
The maximum number of times to retry the job after a job run fails.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** [Outputs](#API_CreateRecipeJob_RequestSyntax) **   <a name="databrew-CreateRecipeJob-request-Outputs"></a>
One or more artifacts that represent the output from running the job.
Type: Array of [Output](API_Output.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** [ProjectName](#API_CreateRecipeJob_RequestSyntax) **   <a name="databrew-CreateRecipeJob-request-ProjectName"></a>
Either the name of an existing project, or a combination of a recipe and a dataset to associate with the recipe.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [RecipeReference](#API_CreateRecipeJob_RequestSyntax) **   <a name="databrew-CreateRecipeJob-request-RecipeReference"></a>
Represents the name and version of a DataBrew recipe.
Type: [RecipeReference](API_RecipeReference.md) object
Required: No

 ** [Tags](#API_CreateRecipeJob_RequestSyntax) **   <a name="databrew-CreateRecipeJob-request-Tags"></a>
Metadata tags to apply to this job.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Maximum length of 256.
Required: No

 ** [Timeout](#API_CreateRecipeJob_RequestSyntax) **   <a name="databrew-CreateRecipeJob-request-Timeout"></a>
The job's timeout in minutes. A job that attempts to run longer than this timeout period ends with a status of `TIMEOUT`.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## Response Syntax
<a name="API_CreateRecipeJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Name": "string"
}
```

## Response Elements
<a name="API_CreateRecipeJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Name](#API_CreateRecipeJob_ResponseSyntax) **   <a name="databrew-CreateRecipeJob-response-Name"></a>
The name of the job that you created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 240.

## Errors
<a name="API_CreateRecipeJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to the specified resource was denied.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
HTTP Status Code: 409

 ** ResourceNotFoundException **
One or more resources can't be found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
A service quota is exceeded.
HTTP Status Code: 402

 ** ValidationException **
The input parameters for this request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_CreateRecipeJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/databrew-2017-07-25/CreateRecipeJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/databrew-2017-07-25/CreateRecipeJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/CreateRecipeJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/databrew-2017-07-25/CreateRecipeJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/CreateRecipeJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/databrew-2017-07-25/CreateRecipeJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/databrew-2017-07-25/CreateRecipeJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/databrew-2017-07-25/CreateRecipeJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/databrew-2017-07-25/CreateRecipeJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/CreateRecipeJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

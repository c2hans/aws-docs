---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_UpdateRecipeJob.html
---

# UpdateRecipeJob
<a name="API_UpdateRecipeJob"></a>

Modifies the definition of an existing DataBrew recipe job.

## Request Syntax
<a name="API_UpdateRecipeJob_RequestSyntax"></a>

```
PUT /recipeJobs/{{name}} HTTP/1.1
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
   "EncryptionKeyArn": "{{string}}",
   "EncryptionMode": "{{string}}",
   "LogSubscription": "{{string}}",
   "MaxCapacity": {{number}},
   "MaxRetries": {{number}},
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
   "RoleArn": "{{string}}",
   "Timeout": {{number}}
}
```

## URI Request Parameters
<a name="API_UpdateRecipeJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_UpdateRecipeJob_RequestSyntax) **   <a name="databrew-UpdateRecipeJob-request-uri-Name"></a>
The name of the job to update.
Length Constraints: Minimum length of 1. Maximum length of 240.
Required: Yes

## Request Body
<a name="API_UpdateRecipeJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [RoleArn](#API_UpdateRecipeJob_RequestSyntax) **   <a name="databrew-UpdateRecipeJob-request-RoleArn"></a>
The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role to be assumed when DataBrew runs the job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: Yes

 ** [DatabaseOutputs](#API_UpdateRecipeJob_RequestSyntax) **   <a name="databrew-UpdateRecipeJob-request-DatabaseOutputs"></a>
Represents a list of JDBC database output objects which defines the output destination for a DataBrew recipe job to write into.
Type: Array of [DatabaseOutput](API_DatabaseOutput.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** [DataCatalogOutputs](#API_UpdateRecipeJob_RequestSyntax) **   <a name="databrew-UpdateRecipeJob-request-DataCatalogOutputs"></a>
One or more artifacts that represent the AWS Glue Data Catalog output from running the job.
Type: Array of [DataCatalogOutput](API_DataCatalogOutput.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** [EncryptionKeyArn](#API_UpdateRecipeJob_RequestSyntax) **   <a name="databrew-UpdateRecipeJob-request-EncryptionKeyArn"></a>
The Amazon Resource Name (ARN) of an encryption key that is used to protect the job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** [EncryptionMode](#API_UpdateRecipeJob_RequestSyntax) **   <a name="databrew-UpdateRecipeJob-request-EncryptionMode"></a>
The encryption mode for the job, which can be one of the following:
+  `SSE-KMS` - Server-side encryption with keys managed by AWS KMS.
+  `SSE-S3` - Server-side encryption with keys managed by Amazon S3.
Type: String
Valid Values: `SSE-KMS | SSE-S3`
Required: No

 ** [LogSubscription](#API_UpdateRecipeJob_RequestSyntax) **   <a name="databrew-UpdateRecipeJob-request-LogSubscription"></a>
Enables or disables Amazon CloudWatch logging for the job. If logging is enabled, CloudWatch writes one log stream for each job run.
Type: String
Valid Values: `ENABLE | DISABLE`
Required: No

 ** [MaxCapacity](#API_UpdateRecipeJob_RequestSyntax) **   <a name="databrew-UpdateRecipeJob-request-MaxCapacity"></a>
The maximum number of nodes that DataBrew can consume when the job processes data.
Type: Integer
Required: No

 ** [MaxRetries](#API_UpdateRecipeJob_RequestSyntax) **   <a name="databrew-UpdateRecipeJob-request-MaxRetries"></a>
The maximum number of times to retry the job after a job run fails.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** [Outputs](#API_UpdateRecipeJob_RequestSyntax) **   <a name="databrew-UpdateRecipeJob-request-Outputs"></a>
One or more artifacts that represent the output from running the job.
Type: Array of [Output](API_Output.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** [Timeout](#API_UpdateRecipeJob_RequestSyntax) **   <a name="databrew-UpdateRecipeJob-request-Timeout"></a>
The job's timeout in minutes. A job that attempts to run longer than this timeout period ends with a status of `TIMEOUT`.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## Response Syntax
<a name="API_UpdateRecipeJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Name": "string"
}
```

## Response Elements
<a name="API_UpdateRecipeJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Name](#API_UpdateRecipeJob_ResponseSyntax) **   <a name="databrew-UpdateRecipeJob-response-Name"></a>
The name of the job that you updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 240.

## Errors
<a name="API_UpdateRecipeJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to the specified resource was denied.
HTTP Status Code: 403

 ** ResourceNotFoundException **
One or more resources can't be found.
HTTP Status Code: 404

 ** ValidationException **
The input parameters for this request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_UpdateRecipeJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/databrew-2017-07-25/UpdateRecipeJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/databrew-2017-07-25/UpdateRecipeJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/UpdateRecipeJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/databrew-2017-07-25/UpdateRecipeJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/UpdateRecipeJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/databrew-2017-07-25/UpdateRecipeJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/databrew-2017-07-25/UpdateRecipeJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/databrew-2017-07-25/UpdateRecipeJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/databrew-2017-07-25/UpdateRecipeJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/UpdateRecipeJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

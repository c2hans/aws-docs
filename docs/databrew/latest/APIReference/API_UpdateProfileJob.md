---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_UpdateProfileJob.html
---

# UpdateProfileJob
<a name="API_UpdateProfileJob"></a>

Modifies the definition of an existing profile job.

## Request Syntax
<a name="API_UpdateProfileJob_RequestSyntax"></a>

```
PUT /profileJobs/{{name}} HTTP/1.1
Content-type: application/json

{
   "Configuration": {
      "ColumnStatisticsConfigurations": [
         {
            "Selectors": [
               {
                  "Name": "{{string}}",
                  "Regex": "{{string}}"
               }
            ],
            "Statistics": {
               "IncludedStatistics": [ "{{string}}" ],
               "Overrides": [
                  {
                     "Parameters": {
                        "{{string}}" : "{{string}}"
                     },
                     "Statistic": "{{string}}"
                  }
               ]
            }
         }
      ],
      "DatasetStatisticsConfiguration": {
         "IncludedStatistics": [ "{{string}}" ],
         "Overrides": [
            {
               "Parameters": {
                  "{{string}}" : "{{string}}"
               },
               "Statistic": "{{string}}"
            }
         ]
      },
      "EntityDetectorConfiguration": {
         "AllowedStatistics": [
            {
               "Statistics": [ "{{string}}" ]
            }
         ],
         "EntityTypes": [ "{{string}}" ]
      },
      "ProfileColumns": [
         {
            "Name": "{{string}}",
            "Regex": "{{string}}"
         }
      ]
   },
   "EncryptionKeyArn": "{{string}}",
   "EncryptionMode": "{{string}}",
   "JobSample": {
      "Mode": "{{string}}",
      "Size": {{number}}
   },
   "LogSubscription": "{{string}}",
   "MaxCapacity": {{number}},
   "MaxRetries": {{number}},
   "OutputLocation": {
      "Bucket": "{{string}}",
      "BucketOwner": "{{string}}",
      "Key": "{{string}}"
   },
   "RoleArn": "{{string}}",
   "Timeout": {{number}},
   "ValidationConfigurations": [
      {
         "RulesetArn": "{{string}}",
         "ValidationMode": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_UpdateProfileJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_UpdateProfileJob_RequestSyntax) **   <a name="databrew-UpdateProfileJob-request-uri-Name"></a>
The name of the job to be updated.
Length Constraints: Minimum length of 1. Maximum length of 240.
Required: Yes

## Request Body
<a name="API_UpdateProfileJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [OutputLocation](#API_UpdateProfileJob_RequestSyntax) **   <a name="databrew-UpdateProfileJob-request-OutputLocation"></a>
Represents an Amazon S3 location (bucket name, bucket owner, and object key) where DataBrew can read input data, or write output from a job.
Type: [S3Location](API_S3Location.md) object
Required: Yes

 ** [RoleArn](#API_UpdateProfileJob_RequestSyntax) **   <a name="databrew-UpdateProfileJob-request-RoleArn"></a>
The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role to be assumed when DataBrew runs the job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: Yes

 ** [Configuration](#API_UpdateProfileJob_RequestSyntax) **   <a name="databrew-UpdateProfileJob-request-Configuration"></a>
Configuration for profile jobs. Used to select columns, do evaluations, and override default parameters of evaluations. When configuration is null, the profile job will run with default settings.
Type: [ProfileConfiguration](API_ProfileConfiguration.md) object
Required: No

 ** [EncryptionKeyArn](#API_UpdateProfileJob_RequestSyntax) **   <a name="databrew-UpdateProfileJob-request-EncryptionKeyArn"></a>
The Amazon Resource Name (ARN) of an encryption key that is used to protect the job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** [EncryptionMode](#API_UpdateProfileJob_RequestSyntax) **   <a name="databrew-UpdateProfileJob-request-EncryptionMode"></a>
The encryption mode for the job, which can be one of the following:
+  `SSE-KMS` - Server-side encryption with keys managed by AWS KMS.
+  `SSE-S3` - Server-side encryption with keys managed by Amazon S3.
Type: String
Valid Values: `SSE-KMS | SSE-S3`
Required: No

 ** [JobSample](#API_UpdateProfileJob_RequestSyntax) **   <a name="databrew-UpdateProfileJob-request-JobSample"></a>
Sample configuration for Profile Jobs only. Determines the number of rows on which the Profile job will be executed. If a JobSample value is not provided for profile jobs, the default value will be used. The default value is CUSTOM\_ROWS for the mode parameter and 20000 for the size parameter.
Type: [JobSample](API_JobSample.md) object
Required: No

 ** [LogSubscription](#API_UpdateProfileJob_RequestSyntax) **   <a name="databrew-UpdateProfileJob-request-LogSubscription"></a>
Enables or disables Amazon CloudWatch logging for the job. If logging is enabled, CloudWatch writes one log stream for each job run.
Type: String
Valid Values: `ENABLE | DISABLE`
Required: No

 ** [MaxCapacity](#API_UpdateProfileJob_RequestSyntax) **   <a name="databrew-UpdateProfileJob-request-MaxCapacity"></a>
The maximum number of compute nodes that DataBrew can use when the job processes data.
Type: Integer
Required: No

 ** [MaxRetries](#API_UpdateProfileJob_RequestSyntax) **   <a name="databrew-UpdateProfileJob-request-MaxRetries"></a>
The maximum number of times to retry the job after a job run fails.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** [Timeout](#API_UpdateProfileJob_RequestSyntax) **   <a name="databrew-UpdateProfileJob-request-Timeout"></a>
The job's timeout in minutes. A job that attempts to run longer than this timeout period ends with a status of `TIMEOUT`.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** [ValidationConfigurations](#API_UpdateProfileJob_RequestSyntax) **   <a name="databrew-UpdateProfileJob-request-ValidationConfigurations"></a>
List of validation configurations that are applied to the profile job.
Type: Array of [ValidationConfiguration](API_ValidationConfiguration.md) objects
Array Members: Minimum number of 1 item.
Required: No

## Response Syntax
<a name="API_UpdateProfileJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Name": "string"
}
```

## Response Elements
<a name="API_UpdateProfileJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Name](#API_UpdateProfileJob_ResponseSyntax) **   <a name="databrew-UpdateProfileJob-response-Name"></a>
The name of the job that was updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 240.

## Errors
<a name="API_UpdateProfileJob_Errors"></a>

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
<a name="API_UpdateProfileJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/databrew-2017-07-25/UpdateProfileJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/databrew-2017-07-25/UpdateProfileJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/UpdateProfileJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/databrew-2017-07-25/UpdateProfileJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/UpdateProfileJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/databrew-2017-07-25/UpdateProfileJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/databrew-2017-07-25/UpdateProfileJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/databrew-2017-07-25/UpdateProfileJob)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/databrew-2017-07-25/UpdateProfileJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/UpdateProfileJob)

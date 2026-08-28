---
source_url: https://docs.aws.amazon.com/healthlake/latest/APIReference/API_DescribeDataTransformationJob.html
---

# DescribeDataTransformationJob
<a name="API_DescribeDataTransformationJob"></a>

Describes a data transformation job, including its current status, configuration, and progress information.

## Request Syntax
<a name="API_DescribeDataTransformationJob_RequestSyntax"></a>

```
{
   "JobId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeDataTransformationJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [JobId](#API_DescribeDataTransformationJob_RequestSyntax) **   <a name="HealthLake-DescribeDataTransformationJob-request-JobId"></a>
The unique identifier of the data transformation job to describe.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

## Response Syntax
<a name="API_DescribeDataTransformationJob_ResponseSyntax"></a>

```
{
   "TransformationJobProperties": {
      "DataAccessRoleArn": "string",
      "DriftDetectionEnabled": boolean,
      "EndTime": number,
      "InputDataConfig": {
         "S3Uri": "string",
         "SourceFormat": "string"
      },
      "JobId": "string",
      "JobName": "string",
      "JobProgressReport": {
         "TotalFilesConverted": number,
         "TotalFilesFailed": number,
         "TotalFilesScanned": number,
         "TotalResourcesGenerated": number
      },
      "JobStatus": "string",
      "Message": "string",
      "OutputDataConfig": {
         "S3Configuration": {
            "KmsKeyId": "string",
            "S3Uri": "string"
         }
      },
      "ProfileId": "string",
      "ProfileName": "string",
      "ProfileVersion": number,
      "ProvenanceEnabled": boolean,
      "SubmitTime": number
   }
}
```

## Response Elements
<a name="API_DescribeDataTransformationJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TransformationJobProperties](#API_DescribeDataTransformationJob_ResponseSyntax) **   <a name="HealthLake-DescribeDataTransformationJob-response-TransformationJobProperties"></a>
The properties of the data transformation job, including status, configuration, and progress information.
Type: [TransformationJobProperties](API_TransformationJobProperties.md) object

## Errors
<a name="API_DescribeDataTransformationJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied. Your account is not authorized to perform this operation.
HTTP Status Code: 400

 ** InternalServerException **
An unknown internal error occurred in the service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested data store was not found.
HTTP Status Code: 400

 ** ThrottlingException **
The user has exceeded their maximum number of allowed calls to the given API.
HTTP Status Code: 400

 ** ValidationException **
The user input parameter was invalid.
HTTP Status Code: 400

## See Also
<a name="API_DescribeDataTransformationJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/healthlake-2017-07-01/DescribeDataTransformationJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/healthlake-2017-07-01/DescribeDataTransformationJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/healthlake-2017-07-01/DescribeDataTransformationJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/healthlake-2017-07-01/DescribeDataTransformationJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/healthlake-2017-07-01/DescribeDataTransformationJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/healthlake-2017-07-01/DescribeDataTransformationJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/healthlake-2017-07-01/DescribeDataTransformationJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/healthlake-2017-07-01/DescribeDataTransformationJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/healthlake-2017-07-01/DescribeDataTransformationJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/healthlake-2017-07-01/DescribeDataTransformationJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthLake. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query healthlake` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

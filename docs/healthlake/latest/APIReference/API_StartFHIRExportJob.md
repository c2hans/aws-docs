---
source_url: https://docs.aws.amazon.com/healthlake/latest/APIReference/API_StartFHIRExportJob.html
---

# StartFHIRExportJob
<a name="API_StartFHIRExportJob"></a>

Start a FHIR export job.

## Request Syntax
<a name="API_StartFHIRExportJob_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "DataAccessRoleArn": "{{string}}",
   "DatastoreId": "{{string}}",
   "JobName": "{{string}}",
   "OutputDataConfig": { ... }
}
```

## Request Parameters
<a name="API_StartFHIRExportJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientToken](#API_StartFHIRExportJob_RequestSyntax) **   <a name="HealthLake-StartFHIRExportJob-request-ClientToken"></a>
An optional user provided token used for ensuring API idempotency.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`
Required: No

 ** [DataAccessRoleArn](#API_StartFHIRExportJob_RequestSyntax) **   <a name="HealthLake-StartFHIRExportJob-request-DataAccessRoleArn"></a>
The Amazon Resource Name (ARN) used during initiation of the export job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+`
Required: Yes

 ** [DatastoreId](#API_StartFHIRExportJob_RequestSyntax) **   <a name="HealthLake-StartFHIRExportJob-request-DatastoreId"></a>
The data store identifier from which files are being exported.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)`
Required: Yes

 ** [JobName](#API_StartFHIRExportJob_RequestSyntax) **   <a name="HealthLake-StartFHIRExportJob-request-JobName"></a>
The export job name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)`
Required: No

 ** [OutputDataConfig](#API_StartFHIRExportJob_RequestSyntax) **   <a name="HealthLake-StartFHIRExportJob-request-OutputDataConfig"></a>
The output data configuration supplied when the export job was started.
Type: [OutputDataConfig](API_OutputDataConfig.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## Response Syntax
<a name="API_StartFHIRExportJob_ResponseSyntax"></a>

```
{
   "DatastoreId": "string",
   "JobId": "string",
   "JobStatus": "string"
}
```

## Response Elements
<a name="API_StartFHIRExportJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DatastoreId](#API_StartFHIRExportJob_ResponseSyntax) **   <a name="HealthLake-StartFHIRExportJob-response-DatastoreId"></a>
The data store identifier from which files are being exported.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)`

 ** [JobId](#API_StartFHIRExportJob_ResponseSyntax) **   <a name="HealthLake-StartFHIRExportJob-response-JobId"></a>
The export job identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)`

 ** [JobStatus](#API_StartFHIRExportJob_ResponseSyntax) **   <a name="HealthLake-StartFHIRExportJob-response-JobStatus"></a>
The export job status.
Type: String
Valid Values: `SUBMITTED | QUEUED | IN_PROGRESS | COMPLETED_WITH_ERRORS | COMPLETED | FAILED | CANCEL_SUBMITTED | CANCEL_IN_PROGRESS | CANCEL_COMPLETED | CANCEL_FAILED`

## Errors
<a name="API_StartFHIRExportJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied. Your account is not authorized to perform this operation.
HTTP Status Code: 400

 ** FailedDependencyException **
A dependent service failed to fulfill the request.
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
<a name="API_StartFHIRExportJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/healthlake-2017-07-01/StartFHIRExportJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/healthlake-2017-07-01/StartFHIRExportJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/healthlake-2017-07-01/StartFHIRExportJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/healthlake-2017-07-01/StartFHIRExportJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/healthlake-2017-07-01/StartFHIRExportJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/healthlake-2017-07-01/StartFHIRExportJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/healthlake-2017-07-01/StartFHIRExportJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/healthlake-2017-07-01/StartFHIRExportJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/healthlake-2017-07-01/StartFHIRExportJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/healthlake-2017-07-01/StartFHIRExportJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthLake. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query healthlake` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

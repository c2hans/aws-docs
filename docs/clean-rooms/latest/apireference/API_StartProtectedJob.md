---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_StartProtectedJob.html
---

# StartProtectedJob
<a name="API_StartProtectedJob"></a>

Creates a protected job that is started by AWS Clean Rooms.

## Request Syntax
<a name="API_StartProtectedJob_RequestSyntax"></a>

```
POST /memberships/{{membershipIdentifier}}/protectedJobs HTTP/1.1
Content-type: application/json

{
   "computeConfiguration": { ... },
   "jobComputePayerAccountId": "{{string}}",
   "jobParameters": {
      "analysisTemplateArn": "{{string}}",
      "parameters": {
         "{{string}}" : "{{string}}"
      }
   },
   "resultConfiguration": {
      "outputConfiguration": { ... }
   },
   "type": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StartProtectedJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [membershipIdentifier](#API_StartProtectedJob_RequestSyntax) **   <a name="API-StartProtectedJob-request-uri-membershipIdentifier"></a>
A unique identifier for the membership to run this job against. Currently accepts a membership ID.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Request Body
<a name="API_StartProtectedJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [computeConfiguration](#API_StartProtectedJob_RequestSyntax) **   <a name="API-StartProtectedJob-request-computeConfiguration"></a>
The compute configuration for the protected job.
Type: [ProtectedJobComputeConfiguration](API_ProtectedJobComputeConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [jobComputePayerAccountId](#API_StartProtectedJob_RequestSyntax) **   <a name="API-StartProtectedJob-request-jobComputePayerAccountId"></a>
The account ID of the member that pays for the job compute costs.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d+`
Required: No

 ** [jobParameters](#API_StartProtectedJob_RequestSyntax) **   <a name="API-StartProtectedJob-request-jobParameters"></a>
 The job parameters.
Type: [ProtectedJobParameters](API_ProtectedJobParameters.md) object
Required: Yes

 ** [resultConfiguration](#API_StartProtectedJob_RequestSyntax) **   <a name="API-StartProtectedJob-request-resultConfiguration"></a>
The details needed to write the job results.
Type: [ProtectedJobResultConfigurationInput](API_ProtectedJobResultConfigurationInput.md) object
Required: No

 ** [type](#API_StartProtectedJob_RequestSyntax) **   <a name="API-StartProtectedJob-request-type"></a>
 The type of protected job to start.
Type: String
Valid Values: `PYSPARK`
Required: Yes

## Response Syntax
<a name="API_StartProtectedJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "protectedJob": {
      "computeConfiguration": { ... },
      "createTime": number,
      "error": {
         "code": "string",
         "message": "string"
      },
      "id": "string",
      "jobComputePayerAccountId": "string",
      "jobParameters": {
         "analysisTemplateArn": "string",
         "parameters": {
            "string" : "string"
         }
      },
      "membershipArn": "string",
      "membershipId": "string",
      "result": {
         "output": { ... }
      },
      "resultConfiguration": {
         "outputConfiguration": { ... }
      },
      "statistics": {
         "billedResourceUtilization": {
            "units": number
         },
         "totalDurationInMillis": number
      },
      "status": "string"
   }
}
```

## Response Elements
<a name="API_StartProtectedJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [protectedJob](#API_StartProtectedJob_ResponseSyntax) **   <a name="API-StartProtectedJob-response-protectedJob"></a>
 The protected job.
Type: [ProtectedJob](API_ProtectedJob.md) object

## Errors
<a name="API_StartProtectedJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Caller does not have sufficient access to perform this action.
 ** reason **
A reason code for the exception.
HTTP Status Code: 403

 ** InternalServerException **
Unexpected error during processing of request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Request references a resource which does not exist.
 ** resourceId **
The Id of the missing resource.
 ** resourceType **
The type of the missing resource.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
Request denied because service quota has been exceeded.
 ** quotaName **
The name of the quota.
 ** quotaValue **
The value of the quota.
HTTP Status Code: 402

 ** ThrottlingException **
Request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the specified constraints.
 ** fieldList **
Validation errors for specific input parameters.
 ** reason **
A reason code for the exception.
HTTP Status Code: 400

## See Also
<a name="API_StartProtectedJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanrooms-2022-02-17/StartProtectedJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanrooms-2022-02-17/StartProtectedJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/StartProtectedJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanrooms-2022-02-17/StartProtectedJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/StartProtectedJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanrooms-2022-02-17/StartProtectedJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanrooms-2022-02-17/StartProtectedJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanrooms-2022-02-17/StartProtectedJob)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cleanrooms-2022-02-17/StartProtectedJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/StartProtectedJob)

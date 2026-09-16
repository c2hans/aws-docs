---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_GetProtectedJob.html
---

# GetProtectedJob
<a name="API_GetProtectedJob"></a>

Returns job processing metadata.

## Request Syntax
<a name="API_GetProtectedJob_RequestSyntax"></a>

```
GET /memberships/{{membershipIdentifier}}/protectedJobs/{{protectedJobIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetProtectedJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [membershipIdentifier](#API_GetProtectedJob_RequestSyntax) **   <a name="API-GetProtectedJob-request-uri-membershipIdentifier"></a>
 The identifier for a membership in a protected job instance.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [protectedJobIdentifier](#API_GetProtectedJob_RequestSyntax) **   <a name="API-GetProtectedJob-request-uri-protectedJobIdentifier"></a>
 The identifier for the protected job instance.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Request Body
<a name="API_GetProtectedJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetProtectedJob_ResponseSyntax"></a>

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
<a name="API_GetProtectedJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [protectedJob](#API_GetProtectedJob_ResponseSyntax) **   <a name="API-GetProtectedJob-response-protectedJob"></a>
 The protected job metadata.
Type: [ProtectedJob](API_ProtectedJob.md) object

## Errors
<a name="API_GetProtectedJob_Errors"></a>

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
<a name="API_GetProtectedJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanrooms-2022-02-17/GetProtectedJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanrooms-2022-02-17/GetProtectedJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/GetProtectedJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanrooms-2022-02-17/GetProtectedJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/GetProtectedJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanrooms-2022-02-17/GetProtectedJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanrooms-2022-02-17/GetProtectedJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanrooms-2022-02-17/GetProtectedJob)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cleanrooms-2022-02-17/GetProtectedJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/GetProtectedJob)

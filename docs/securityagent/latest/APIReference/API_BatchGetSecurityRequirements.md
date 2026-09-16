---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_BatchGetSecurityRequirements.html
---

# BatchGetSecurityRequirements
<a name="API_BatchGetSecurityRequirements"></a>

Batch retrieves security requirements from a pack.

## Request Syntax
<a name="API_BatchGetSecurityRequirements_RequestSyntax"></a>

```
POST /BatchGetSecurityRequirements HTTP/1.1
Content-type: application/json

{
   "packId": "{{string}}",
   "securityRequirementNames": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_BatchGetSecurityRequirements_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchGetSecurityRequirements_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [packId](#API_BatchGetSecurityRequirements_RequestSyntax) **   <a name="securityagent-BatchGetSecurityRequirements-request-packId"></a>
The unique identifier of the security requirement pack to retrieve requirements from.
Type: String
Required: Yes

 ** [securityRequirementNames](#API_BatchGetSecurityRequirements_RequestSyntax) **   <a name="securityagent-BatchGetSecurityRequirements-request-securityRequirementNames"></a>
The list of security requirement names to retrieve.
Type: Array of strings
Required: Yes

## Response Syntax
<a name="API_BatchGetSecurityRequirements_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "errors": [
      {
         "code": "string",
         "message": "string",
         "securityRequirementName": "string"
      }
   ],
   "securityRequirements": [
      {
         "createdAt": "string",
         "description": "string",
         "domain": "string",
         "evaluation": "string",
         "name": "string",
         "packId": "string",
         "remediation": "string",
         "updatedAt": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchGetSecurityRequirements_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errors](#API_BatchGetSecurityRequirements_ResponseSyntax) **   <a name="securityagent-BatchGetSecurityRequirements-response-errors"></a>
The list of errors for security requirements that failed to be retrieved.
Type: Array of [BatchSecurityRequirementError](API_BatchSecurityRequirementError.md) objects

 ** [securityRequirements](#API_BatchGetSecurityRequirements_ResponseSyntax) **   <a name="securityagent-BatchGetSecurityRequirements-response-securityRequirements"></a>
The list of security requirements that were successfully retrieved.
Type: Array of [BatchGetSecurityRequirementResult](API_BatchGetSecurityRequirementResult.md) objects

## Errors
<a name="API_BatchGetSecurityRequirements_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 ** message **
Error description.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred during the processing of your request.
 ** message **
Error description.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found. Verify that the resource identifier is correct and that the resource exists in the specified agent space or account.
 ** message **
Error description.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
 ** message **
Error description.
 ** quotaCode **
Quota code for throttling limit.
 ** serviceCode **
Service code for throttling limit.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by the service.
 ** fieldList **
A list of specific failures encountered during validation.
 ** message **
A summary of the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_BatchGetSecurityRequirements_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/BatchGetSecurityRequirements)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/BatchGetSecurityRequirements)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/BatchGetSecurityRequirements)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/BatchGetSecurityRequirements)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/BatchGetSecurityRequirements)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/BatchGetSecurityRequirements)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/BatchGetSecurityRequirements)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/BatchGetSecurityRequirements)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/BatchGetSecurityRequirements)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/BatchGetSecurityRequirements)

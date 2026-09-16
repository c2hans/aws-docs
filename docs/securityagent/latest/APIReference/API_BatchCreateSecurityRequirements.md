---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_BatchCreateSecurityRequirements.html
---

# BatchCreateSecurityRequirements
<a name="API_BatchCreateSecurityRequirements"></a>

Batch creates security requirements in a customer managed pack.

## Request Syntax
<a name="API_BatchCreateSecurityRequirements_RequestSyntax"></a>

```
POST /BatchCreateSecurityRequirements HTTP/1.1
Content-type: application/json

{
   "packId": "{{string}}",
   "securityRequirements": [
      {
         "description": "{{string}}",
         "domain": "{{string}}",
         "evaluation": "{{string}}",
         "name": "{{string}}",
         "remediation": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_BatchCreateSecurityRequirements_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchCreateSecurityRequirements_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [packId](#API_BatchCreateSecurityRequirements_RequestSyntax) **   <a name="securityagent-BatchCreateSecurityRequirements-request-packId"></a>
The unique identifier of the security requirement pack to add requirements to.
Type: String
Required: Yes

 ** [securityRequirements](#API_BatchCreateSecurityRequirements_RequestSyntax) **   <a name="securityagent-BatchCreateSecurityRequirements-request-securityRequirements"></a>
The list of security requirements to create.
Type: Array of [CreateSecurityRequirementEntry](API_CreateSecurityRequirementEntry.md) objects
Required: Yes

## Response Syntax
<a name="API_BatchCreateSecurityRequirements_ResponseSyntax"></a>

```
HTTP/1.1 201
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
<a name="API_BatchCreateSecurityRequirements_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [errors](#API_BatchCreateSecurityRequirements_ResponseSyntax) **   <a name="securityagent-BatchCreateSecurityRequirements-response-errors"></a>
The list of errors for security requirements that failed to be created.
Type: Array of [BatchSecurityRequirementError](API_BatchSecurityRequirementError.md) objects

 ** [securityRequirements](#API_BatchCreateSecurityRequirements_ResponseSyntax) **   <a name="securityagent-BatchCreateSecurityRequirements-response-securityRequirements"></a>
The list of security requirements that were successfully created.
Type: Array of [BatchCreateSecurityRequirementResult](API_BatchCreateSecurityRequirementResult.md) objects

## Errors
<a name="API_BatchCreateSecurityRequirements_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 ** message **
Error description.
HTTP Status Code: 403

 ** ConflictException **
The request could not be completed due to a conflict with the current state of the resource.
 ** message **
Error description.
HTTP Status Code: 409

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

 ** ServiceQuotaExceededException **
The request exceeds a service quota. Review your current usage and request a quota increase if needed.
HTTP Status Code: 402

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
<a name="API_BatchCreateSecurityRequirements_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/BatchCreateSecurityRequirements)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/BatchCreateSecurityRequirements)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/BatchCreateSecurityRequirements)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/BatchCreateSecurityRequirements)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/BatchCreateSecurityRequirements)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/BatchCreateSecurityRequirements)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/BatchCreateSecurityRequirements)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/BatchCreateSecurityRequirements)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/BatchCreateSecurityRequirements)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/BatchCreateSecurityRequirements)

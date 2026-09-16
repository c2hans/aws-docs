---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_UpdateSecurityRequirementPack.html
---

# UpdateSecurityRequirementPack
<a name="API_UpdateSecurityRequirementPack"></a>

Updates a security requirement pack. For customer managed packs, both metadata and status can be updated. For AWS managed packs, only status can be updated.

## Request Syntax
<a name="API_UpdateSecurityRequirementPack_RequestSyntax"></a>

```
POST /UpdateSecurityRequirementPack HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "name": "{{string}}",
   "packId": "{{string}}",
   "status": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateSecurityRequirementPack_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateSecurityRequirementPack_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_UpdateSecurityRequirementPack_RequestSyntax) **   <a name="securityagent-UpdateSecurityRequirementPack-request-description"></a>
The updated description of the security requirement pack.
Type: String
Required: No

 ** [name](#API_UpdateSecurityRequirementPack_RequestSyntax) **   <a name="securityagent-UpdateSecurityRequirementPack-request-name"></a>
The updated name of the security requirement pack.
Type: String
Required: No

 ** [packId](#API_UpdateSecurityRequirementPack_RequestSyntax) **   <a name="securityagent-UpdateSecurityRequirementPack-request-packId"></a>
The unique identifier of the security requirement pack to update.
Type: String
Required: Yes

 ** [status](#API_UpdateSecurityRequirementPack_RequestSyntax) **   <a name="securityagent-UpdateSecurityRequirementPack-request-status"></a>
The updated status of the security requirement pack.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## Response Syntax
<a name="API_UpdateSecurityRequirementPack_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "description": "string",
   "name": "string",
   "packId": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_UpdateSecurityRequirementPack_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [description](#API_UpdateSecurityRequirementPack_ResponseSyntax) **   <a name="securityagent-UpdateSecurityRequirementPack-response-description"></a>
The description of the security requirement pack.
Type: String

 ** [name](#API_UpdateSecurityRequirementPack_ResponseSyntax) **   <a name="securityagent-UpdateSecurityRequirementPack-response-name"></a>
The name of the security requirement pack.
Type: String

 ** [packId](#API_UpdateSecurityRequirementPack_ResponseSyntax) **   <a name="securityagent-UpdateSecurityRequirementPack-response-packId"></a>
The unique identifier of the security requirement pack.
Type: String

 ** [status](#API_UpdateSecurityRequirementPack_ResponseSyntax) **   <a name="securityagent-UpdateSecurityRequirementPack-response-status"></a>
The status of the security requirement pack.
Type: String
Valid Values: `ENABLED | DISABLED`

## Errors
<a name="API_UpdateSecurityRequirementPack_Errors"></a>

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
<a name="API_UpdateSecurityRequirementPack_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/UpdateSecurityRequirementPack)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/UpdateSecurityRequirementPack)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/UpdateSecurityRequirementPack)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/UpdateSecurityRequirementPack)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/UpdateSecurityRequirementPack)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/UpdateSecurityRequirementPack)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/UpdateSecurityRequirementPack)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/UpdateSecurityRequirementPack)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/UpdateSecurityRequirementPack)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/UpdateSecurityRequirementPack)

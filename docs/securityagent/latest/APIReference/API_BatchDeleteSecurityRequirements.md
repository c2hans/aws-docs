---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_BatchDeleteSecurityRequirements.html
---

# BatchDeleteSecurityRequirements
<a name="API_BatchDeleteSecurityRequirements"></a>

Batch deletes security requirements from a customer managed pack.

## Request Syntax
<a name="API_BatchDeleteSecurityRequirements_RequestSyntax"></a>

```
POST /BatchDeleteSecurityRequirements HTTP/1.1
Content-type: application/json

{
   "packId": "{{string}}",
   "securityRequirementNames": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_BatchDeleteSecurityRequirements_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchDeleteSecurityRequirements_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [packId](#API_BatchDeleteSecurityRequirements_RequestSyntax) **   <a name="securityagent-BatchDeleteSecurityRequirements-request-packId"></a>
The unique identifier of the security requirement pack to remove requirements from.
Type: String
Required: Yes

 ** [securityRequirementNames](#API_BatchDeleteSecurityRequirements_RequestSyntax) **   <a name="securityagent-BatchDeleteSecurityRequirements-request-securityRequirementNames"></a>
The list of security requirement names to delete.
Type: Array of strings
Required: Yes

## Response Syntax
<a name="API_BatchDeleteSecurityRequirements_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "deletedSecurityRequirementNames": [ "string" ],
   "errors": [
      {
         "code": "string",
         "message": "string",
         "securityRequirementName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchDeleteSecurityRequirements_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [deletedSecurityRequirementNames](#API_BatchDeleteSecurityRequirements_ResponseSyntax) **   <a name="securityagent-BatchDeleteSecurityRequirements-response-deletedSecurityRequirementNames"></a>
The list of security requirement names that were successfully deleted.
Type: Array of strings

 ** [errors](#API_BatchDeleteSecurityRequirements_ResponseSyntax) **   <a name="securityagent-BatchDeleteSecurityRequirements-response-errors"></a>
The list of errors for security requirements that failed to be deleted.
Type: Array of [BatchSecurityRequirementError](API_BatchSecurityRequirementError.md) objects

## Errors
<a name="API_BatchDeleteSecurityRequirements_Errors"></a>

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
<a name="API_BatchDeleteSecurityRequirements_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/BatchDeleteSecurityRequirements)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/BatchDeleteSecurityRequirements)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/BatchDeleteSecurityRequirements)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/BatchDeleteSecurityRequirements)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/BatchDeleteSecurityRequirements)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/BatchDeleteSecurityRequirements)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/BatchDeleteSecurityRequirements)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/BatchDeleteSecurityRequirements)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/BatchDeleteSecurityRequirements)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/BatchDeleteSecurityRequirements)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

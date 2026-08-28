---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_BatchUpdateSecurityRequirements.html
---

# BatchUpdateSecurityRequirements
<a name="API_BatchUpdateSecurityRequirements"></a>

Batch updates security requirements within a customer managed pack.

## Request Syntax
<a name="API_BatchUpdateSecurityRequirements_RequestSyntax"></a>

```
POST /BatchUpdateSecurityRequirements HTTP/1.1
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
<a name="API_BatchUpdateSecurityRequirements_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchUpdateSecurityRequirements_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [packId](#API_BatchUpdateSecurityRequirements_RequestSyntax) **   <a name="securityagent-BatchUpdateSecurityRequirements-request-packId"></a>
The unique identifier of the security requirement pack containing the requirements to update.
Type: String
Required: Yes

 ** [securityRequirements](#API_BatchUpdateSecurityRequirements_RequestSyntax) **   <a name="securityagent-BatchUpdateSecurityRequirements-request-securityRequirements"></a>
The list of security requirement updates to apply.
Type: Array of [UpdateSecurityRequirementEntry](API_UpdateSecurityRequirementEntry.md) objects
Required: Yes

## Response Syntax
<a name="API_BatchUpdateSecurityRequirements_ResponseSyntax"></a>

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
   "updatedSecurityRequirementNames": [ "string" ]
}
```

## Response Elements
<a name="API_BatchUpdateSecurityRequirements_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errors](#API_BatchUpdateSecurityRequirements_ResponseSyntax) **   <a name="securityagent-BatchUpdateSecurityRequirements-response-errors"></a>
The list of errors for security requirements that failed to be updated.
Type: Array of [BatchSecurityRequirementError](API_BatchSecurityRequirementError.md) objects

 ** [updatedSecurityRequirementNames](#API_BatchUpdateSecurityRequirements_ResponseSyntax) **   <a name="securityagent-BatchUpdateSecurityRequirements-response-updatedSecurityRequirementNames"></a>
The list of security requirement names that were successfully updated.
Type: Array of strings

## Errors
<a name="API_BatchUpdateSecurityRequirements_Errors"></a>

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
<a name="API_BatchUpdateSecurityRequirements_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/BatchUpdateSecurityRequirements)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/BatchUpdateSecurityRequirements)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/BatchUpdateSecurityRequirements)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/BatchUpdateSecurityRequirements)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/BatchUpdateSecurityRequirements)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/BatchUpdateSecurityRequirements)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/BatchUpdateSecurityRequirements)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/BatchUpdateSecurityRequirements)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/BatchUpdateSecurityRequirements)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/BatchUpdateSecurityRequirements)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

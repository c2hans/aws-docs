---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_CreateSecurityRequirementPack.html
---

# CreateSecurityRequirementPack
<a name="API_CreateSecurityRequirementPack"></a>

Creates a customer managed security requirement pack.

## Request Syntax
<a name="API_CreateSecurityRequirementPack_RequestSyntax"></a>

```
POST /CreateSecurityRequirementPack HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "kmsKeyId": "{{string}}",
   "name": "{{string}}",
   "status": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateSecurityRequirementPack_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateSecurityRequirementPack_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_CreateSecurityRequirementPack_RequestSyntax) **   <a name="securityagent-CreateSecurityRequirementPack-request-description"></a>
A description of the security requirement pack.
Type: String
Required: No

 ** [kmsKeyId](#API_CreateSecurityRequirementPack_RequestSyntax) **   <a name="securityagent-CreateSecurityRequirementPack-request-kmsKeyId"></a>
The identifier of the AWS KMS key used to encrypt pack contents.
Type: String
Required: No

 ** [name](#API_CreateSecurityRequirementPack_RequestSyntax) **   <a name="securityagent-CreateSecurityRequirementPack-request-name"></a>
The name of the security requirement pack.
Type: String
Required: Yes

 ** [status](#API_CreateSecurityRequirementPack_RequestSyntax) **   <a name="securityagent-CreateSecurityRequirementPack-request-status"></a>
The status of the pack. Defaults to ENABLED if not provided.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [tags](#API_CreateSecurityRequirementPack_RequestSyntax) **   <a name="securityagent-CreateSecurityRequirementPack-request-tags"></a>
The tags to associate with the security requirement pack.
Type: String to string map
Required: No

## Response Syntax
<a name="API_CreateSecurityRequirementPack_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "kmsKeyId": "string",
   "packId": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_CreateSecurityRequirementPack_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [kmsKeyId](#API_CreateSecurityRequirementPack_ResponseSyntax) **   <a name="securityagent-CreateSecurityRequirementPack-response-kmsKeyId"></a>
The identifier of the AWS KMS key used to encrypt pack contents.
Type: String

 ** [packId](#API_CreateSecurityRequirementPack_ResponseSyntax) **   <a name="securityagent-CreateSecurityRequirementPack-response-packId"></a>
The unique identifier of the created security requirement pack.
Type: String

 ** [status](#API_CreateSecurityRequirementPack_ResponseSyntax) **   <a name="securityagent-CreateSecurityRequirementPack-response-status"></a>
The status of the created security requirement pack.
Type: String
Valid Values: `ENABLED | DISABLED`

## Errors
<a name="API_CreateSecurityRequirementPack_Errors"></a>

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
<a name="API_CreateSecurityRequirementPack_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/CreateSecurityRequirementPack)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/CreateSecurityRequirementPack)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/CreateSecurityRequirementPack)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/CreateSecurityRequirementPack)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/CreateSecurityRequirementPack)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/CreateSecurityRequirementPack)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/CreateSecurityRequirementPack)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/CreateSecurityRequirementPack)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/CreateSecurityRequirementPack)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/CreateSecurityRequirementPack)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

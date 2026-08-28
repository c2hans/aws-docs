---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_GetSecurityRequirementPack.html
---

# GetSecurityRequirementPack
<a name="API_GetSecurityRequirementPack"></a>

Retrieves information about a security requirement pack.

## Request Syntax
<a name="API_GetSecurityRequirementPack_RequestSyntax"></a>

```
POST /GetSecurityRequirementPack HTTP/1.1
Content-type: application/json

{
   "packId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetSecurityRequirementPack_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetSecurityRequirementPack_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [packId](#API_GetSecurityRequirementPack_RequestSyntax) **   <a name="securityagent-GetSecurityRequirementPack-request-packId"></a>
The unique identifier of the security requirement pack to retrieve.
Type: String
Required: Yes

## Response Syntax
<a name="API_GetSecurityRequirementPack_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": "string",
   "description": "string",
   "importStatus": "string",
   "kmsKeyId": "string",
   "managementType": "string",
   "name": "string",
   "packId": "string",
   "status": "string",
   "updatedAt": "string",
   "vendorName": "string"
}
```

## Response Elements
<a name="API_GetSecurityRequirementPack_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_GetSecurityRequirementPack_ResponseSyntax) **   <a name="securityagent-GetSecurityRequirementPack-response-createdAt"></a>
The date and time the security requirement pack was created, in UTC format.
Type: Timestamp

 ** [description](#API_GetSecurityRequirementPack_ResponseSyntax) **   <a name="securityagent-GetSecurityRequirementPack-response-description"></a>
A description of the security requirement pack.
Type: String

 ** [importStatus](#API_GetSecurityRequirementPack_ResponseSyntax) **   <a name="securityagent-GetSecurityRequirementPack-response-importStatus"></a>
The status of the security requirements import workflow for this pack.
Type: String
Valid Values: `PENDING | IN_PROGRESS | FAILED | COMPLETED`

 ** [kmsKeyId](#API_GetSecurityRequirementPack_ResponseSyntax) **   <a name="securityagent-GetSecurityRequirementPack-response-kmsKeyId"></a>
The identifier of the AWS KMS key used to encrypt pack contents.
Type: String

 ** [managementType](#API_GetSecurityRequirementPack_ResponseSyntax) **   <a name="securityagent-GetSecurityRequirementPack-response-managementType"></a>
The management type of the pack. Valid values are AWS\_MANAGED and CUSTOMER\_MANAGED.
Type: String
Valid Values: `AWS_MANAGED | CUSTOMER_MANAGED`

 ** [name](#API_GetSecurityRequirementPack_ResponseSyntax) **   <a name="securityagent-GetSecurityRequirementPack-response-name"></a>
The name of the security requirement pack.
Type: String

 ** [packId](#API_GetSecurityRequirementPack_ResponseSyntax) **   <a name="securityagent-GetSecurityRequirementPack-response-packId"></a>
The unique identifier of the security requirement pack.
Type: String

 ** [status](#API_GetSecurityRequirementPack_ResponseSyntax) **   <a name="securityagent-GetSecurityRequirementPack-response-status"></a>
The status of the security requirement pack.
Type: String
Valid Values: `ENABLED | DISABLED`

 ** [updatedAt](#API_GetSecurityRequirementPack_ResponseSyntax) **   <a name="securityagent-GetSecurityRequirementPack-response-updatedAt"></a>
The date and time the security requirement pack was last updated, in UTC format.
Type: Timestamp

 ** [vendorName](#API_GetSecurityRequirementPack_ResponseSyntax) **   <a name="securityagent-GetSecurityRequirementPack-response-vendorName"></a>
The vendor name for AWS managed packs, such as ISO or NIST.
Type: String

## Errors
<a name="API_GetSecurityRequirementPack_Errors"></a>

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
<a name="API_GetSecurityRequirementPack_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/GetSecurityRequirementPack)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/GetSecurityRequirementPack)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/GetSecurityRequirementPack)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/GetSecurityRequirementPack)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/GetSecurityRequirementPack)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/GetSecurityRequirementPack)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/GetSecurityRequirementPack)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/GetSecurityRequirementPack)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/GetSecurityRequirementPack)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/GetSecurityRequirementPack)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

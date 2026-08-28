---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_channel_DeleteProgramManagementAccount.html
---

# DeleteProgramManagementAccount
<a name="API_channel_DeleteProgramManagementAccount"></a>

Deletes a program management account.

## Request Syntax
<a name="API_channel_DeleteProgramManagementAccount_RequestSyntax"></a>

```
{
   "catalog": "{{string}}",
   "clientToken": "{{string}}",
   "identifier": "{{string}}"
}
```

## Request Parameters
<a name="API_channel_DeleteProgramManagementAccount_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [catalog](#API_channel_DeleteProgramManagementAccount_RequestSyntax) **   <a name="AWSPartnerCentral-channel_DeleteProgramManagementAccount-request-catalog"></a>
The catalog identifier for the program management account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z]*`
Required: Yes

 ** [identifier](#API_channel_DeleteProgramManagementAccount_RequestSyntax) **   <a name="AWSPartnerCentral-channel_DeleteProgramManagementAccount-request-identifier"></a>
The unique identifier of the program management account to delete.
Type: String
Length Constraints: Minimum length of 17. Maximum length of 1011.
Pattern: `(arn:[a-z-]+:partnercentral:[a-z0-9-]+:[0-9]{12}:catalog/[a-zA-Z]+/program-management-account/)?pma-[a-z0-9]{13}`
Required: Yes

 ** [clientToken](#API_channel_DeleteProgramManagementAccount_RequestSyntax) **   <a name="AWSPartnerCentral-channel_DeleteProgramManagementAccount-request-clientToken"></a>
A unique, case-sensitive identifier to ensure idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[!-~]*`
Required: No

## Response Elements
<a name="API_channel_DeleteProgramManagementAccount_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_channel_DeleteProgramManagementAccount_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request was denied due to insufficient permissions.
 ** message **
A message describing the access denial.
 ** reason **
The reason for the access denial.
HTTP Status Code: 400

 ** ConflictException **
The request could not be completed due to a conflict with the current state of the resource.
 ** message **
A message describing the conflict.
 ** resourceId **
The identifier of the resource that caused the conflict.
 ** resourceType **
The type of the resource that caused the conflict.
HTTP Status Code: 400

 ** InternalServerException **
An internal server error occurred while processing the request.
 ** message **
A message describing the internal server error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found.
 ** message **
A message describing the resource not found error.
 ** resourceId **
The identifier of the resource that was not found.
 ** resourceType **
The type of the resource that was not found.
HTTP Status Code: 400

 ** ThrottlingException **
The request was throttled due to too many requests being sent in a short period.
 ** message **
A message describing the throttling error.
 ** quotaCode **
The quota code associated with the throttling error.
 ** serviceCode **
The service code associated with the throttling error.
HTTP Status Code: 400

 ** ValidationException **
The request failed validation due to invalid input parameters.
 ** fieldList **
A list of fields that failed validation.
 ** message **
A message describing the validation error.
 ** reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_channel_DeleteProgramManagementAccount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-channel-2024-03-18/DeleteProgramManagementAccount)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-channel-2024-03-18/DeleteProgramManagementAccount)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-channel-2024-03-18/DeleteProgramManagementAccount)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-channel-2024-03-18/DeleteProgramManagementAccount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-channel-2024-03-18/DeleteProgramManagementAccount)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-channel-2024-03-18/DeleteProgramManagementAccount)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-channel-2024-03-18/DeleteProgramManagementAccount)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-channel-2024-03-18/DeleteProgramManagementAccount)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/partnercentral-channel-2024-03-18/DeleteProgramManagementAccount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-channel-2024-03-18/DeleteProgramManagementAccount)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

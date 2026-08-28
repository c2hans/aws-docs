---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_UpdateExascaleDbStorageVault.html
---

# UpdateExascaleDbStorageVault
<a name="API_UpdateExascaleDbStorageVault"></a>

Updates the specified Exascale storage vault.

## Request Syntax
<a name="API_UpdateExascaleDbStorageVault_RequestSyntax"></a>

```
{
   "additionalFlashCacheInPercent": {{number}},
   "autoscaleLimitInGBs": {{number}},
   "description": "{{string}}",
   "displayName": "{{string}}",
   "exascaleDbStorageVaultId": "{{string}}",
   "highCapacityDatabaseStorageTotalSizeInGBs": {{number}},
   "isAutoscaleEnabled": {{boolean}}
}
```

## Request Parameters
<a name="API_UpdateExascaleDbStorageVault_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [additionalFlashCacheInPercent](#API_UpdateExascaleDbStorageVault_RequestSyntax) **   <a name="odb-UpdateExascaleDbStorageVault-request-additionalFlashCacheInPercent"></a>
The additional flash cache percentage for the Exascale storage vault.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** [autoscaleLimitInGBs](#API_UpdateExascaleDbStorageVault_RequestSyntax) **   <a name="odb-UpdateExascaleDbStorageVault-request-autoscaleLimitInGBs"></a>
The autoscale limit in gigabytes (GB) for the Exascale storage vault.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** [description](#API_UpdateExascaleDbStorageVault_RequestSyntax) **   <a name="odb-UpdateExascaleDbStorageVault-request-description"></a>
A new description for the Exascale storage vault.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 400.
Required: No

 ** [displayName](#API_UpdateExascaleDbStorageVault_RequestSyntax) **   <a name="odb-UpdateExascaleDbStorageVault-request-displayName"></a>
A new user-friendly name for the Exascale storage vault.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z_](?!.*--)[a-zA-Z0-9_-]*`
Required: No

 ** [exascaleDbStorageVaultId](#API_UpdateExascaleDbStorageVault_RequestSyntax) **   <a name="odb-UpdateExascaleDbStorageVault-request-exascaleDbStorageVaultId"></a>
The unique identifier of the Exascale storage vault to update.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 2048.
Pattern: `(arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-zA-Z0-9_~.-]{6,64}|[a-zA-Z0-9_~.-]{6,64})`
Required: Yes

 ** [highCapacityDatabaseStorageTotalSizeInGBs](#API_UpdateExascaleDbStorageVault_RequestSyntax) **   <a name="odb-UpdateExascaleDbStorageVault-request-highCapacityDatabaseStorageTotalSizeInGBs"></a>
The total size of the high-capacity database storage, in gigabytes (GB), for the Exascale storage vault.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** [isAutoscaleEnabled](#API_UpdateExascaleDbStorageVault_RequestSyntax) **   <a name="odb-UpdateExascaleDbStorageVault-request-isAutoscaleEnabled"></a>
Specifies whether autoscaling is enabled for the Exascale storage vault.
Type: Boolean
Required: No

## Response Syntax
<a name="API_UpdateExascaleDbStorageVault_ResponseSyntax"></a>

```
{
   "displayName": "string",
   "exascaleDbStorageVaultId": "string",
   "status": "string",
   "statusReason": "string"
}
```

## Response Elements
<a name="API_UpdateExascaleDbStorageVault_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [displayName](#API_UpdateExascaleDbStorageVault_ResponseSyntax) **   <a name="odb-UpdateExascaleDbStorageVault-response-displayName"></a>
The user-friendly name for the Exascale storage vault.
Type: String

 ** [exascaleDbStorageVaultId](#API_UpdateExascaleDbStorageVault_ResponseSyntax) **   <a name="odb-UpdateExascaleDbStorageVault-response-exascaleDbStorageVaultId"></a>
The unique identifier of the Exascale storage vault.
Type: String

 ** [status](#API_UpdateExascaleDbStorageVault_ResponseSyntax) **   <a name="odb-UpdateExascaleDbStorageVault-response-status"></a>
The current status of the Exascale storage vault.
Type: String
Valid Values: `AVAILABLE | FAILED | PROVISIONING | TERMINATED | TERMINATING | UPDATING | MAINTENANCE_IN_PROGRESS`

 ** [statusReason](#API_UpdateExascaleDbStorageVault_ResponseSyntax) **   <a name="odb-UpdateExascaleDbStorageVault-response-statusReason"></a>
Additional information about the status of the Exascale storage vault.
Type: String

## Errors
<a name="API_UpdateExascaleDbStorageVault_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.
HTTP Status Code: 400

 ** ConflictException **
Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.
 ** resourceId **
The identifier of the resource that caused the conflict.
 ** resourceType **
The type of resource that caused the conflict.
HTTP Status Code: 400

 ** InternalServerException **
Occurs when there is an internal failure in the Oracle Database@AWS service. Wait and try again.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request after an internal server error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.
 ** resourceId **
The identifier of the resource that was not found.
 ** resourceType **
The type of resource that was not found.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request after being throttled.
HTTP Status Code: 400

 ** ValidationException **
The request has failed validation because it is missing required fields or has invalid inputs.
 ** fieldList **
A list of fields that failed validation.
 ** reason **
The reason why the validation failed.
HTTP Status Code: 400

## See Also
<a name="API_UpdateExascaleDbStorageVault_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/odb-2024-08-20/UpdateExascaleDbStorageVault)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/odb-2024-08-20/UpdateExascaleDbStorageVault)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/UpdateExascaleDbStorageVault)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/odb-2024-08-20/UpdateExascaleDbStorageVault)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/UpdateExascaleDbStorageVault)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/odb-2024-08-20/UpdateExascaleDbStorageVault)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/odb-2024-08-20/UpdateExascaleDbStorageVault)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/odb-2024-08-20/UpdateExascaleDbStorageVault)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/odb-2024-08-20/UpdateExascaleDbStorageVault)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/UpdateExascaleDbStorageVault)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Oracle Database@AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query odb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_CreateAutonomousDatabaseBackup.html
---

# CreateAutonomousDatabaseBackup
<a name="API_CreateAutonomousDatabaseBackup"></a>

Creates a new backup of the specified Autonomous Database.

## Request Syntax
<a name="API_CreateAutonomousDatabaseBackup_RequestSyntax"></a>

```
{
   "autonomousDatabaseId": "{{string}}",
   "clientToken": "{{string}}",
   "displayName": "{{string}}",
   "retentionPeriodInDays": {{number}},
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreateAutonomousDatabaseBackup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [autonomousDatabaseId](#API_CreateAutonomousDatabaseBackup_RequestSyntax) **   <a name="odb-CreateAutonomousDatabaseBackup-request-autonomousDatabaseId"></a>
The unique identifier of the Autonomous Database to back up.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 2048.
Pattern: `(arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-zA-Z0-9_~.-]{6,64}|[a-zA-Z0-9_~.-]{6,64})`
Required: Yes

 ** [clientToken](#API_CreateAutonomousDatabaseBackup_RequestSyntax) **   <a name="odb-CreateAutonomousDatabaseBackup-request-clientToken"></a>
A client-provided token to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 64.
Pattern: `[a-zA-Z0-9_\/.=-]+`
Required: No

 ** [displayName](#API_CreateAutonomousDatabaseBackup_RequestSyntax) **   <a name="odb-CreateAutonomousDatabaseBackup-request-displayName"></a>
The user-friendly name for the Autonomous Database backup.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z_](?!.*--)[a-zA-Z0-9_-]*`
Required: No

 ** [retentionPeriodInDays](#API_CreateAutonomousDatabaseBackup_RequestSyntax) **   <a name="odb-CreateAutonomousDatabaseBackup-request-retentionPeriodInDays"></a>
The retention period, in days, for the Autonomous Database backup.
Type: Integer
Valid Range: Minimum value of 90. Maximum value of 3650.
Required: No

 ** [tags](#API_CreateAutonomousDatabaseBackup_RequestSyntax) **   <a name="odb-CreateAutonomousDatabaseBackup-request-tags"></a>
The list of resource tags to apply to the Autonomous Database backup. Each tag is a key-value pair with no predefined name, type, or namespace.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateAutonomousDatabaseBackup_ResponseSyntax"></a>

```
{
   "autonomousDatabaseBackupId": "string",
   "displayName": "string",
   "status": "string",
   "statusReason": "string"
}
```

## Response Elements
<a name="API_CreateAutonomousDatabaseBackup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [autonomousDatabaseBackupId](#API_CreateAutonomousDatabaseBackup_ResponseSyntax) **   <a name="odb-CreateAutonomousDatabaseBackup-response-autonomousDatabaseBackupId"></a>
The unique identifier of the Autonomous Database backup that was created.
Type: String

 ** [displayName](#API_CreateAutonomousDatabaseBackup_ResponseSyntax) **   <a name="odb-CreateAutonomousDatabaseBackup-response-displayName"></a>
The user-friendly name of the Autonomous Database backup that was created.
Type: String

 ** [status](#API_CreateAutonomousDatabaseBackup_ResponseSyntax) **   <a name="odb-CreateAutonomousDatabaseBackup-response-status"></a>
The current status of the Autonomous Database backup.
Type: String
Valid Values: `AVAILABLE | FAILED | PROVISIONING | TERMINATED | TERMINATING | UPDATING | MAINTENANCE_IN_PROGRESS`

 ** [statusReason](#API_CreateAutonomousDatabaseBackup_ResponseSyntax) **   <a name="odb-CreateAutonomousDatabaseBackup-response-statusReason"></a>
Additional information about the current status of the Autonomous Database backup, if applicable.
Type: String

## Errors
<a name="API_CreateAutonomousDatabaseBackup_Errors"></a>

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

 ** ServiceQuotaExceededException **
You have exceeded the service quota.
 ** quotaCode **
The unqiue identifier of the service quota that was exceeded.
 ** resourceId **
The identifier of the resource that exceeded the service quota.
 ** resourceType **
The type of resource that exceeded the service quota.
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
<a name="API_CreateAutonomousDatabaseBackup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/odb-2024-08-20/CreateAutonomousDatabaseBackup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/odb-2024-08-20/CreateAutonomousDatabaseBackup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/CreateAutonomousDatabaseBackup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/odb-2024-08-20/CreateAutonomousDatabaseBackup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/CreateAutonomousDatabaseBackup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/odb-2024-08-20/CreateAutonomousDatabaseBackup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/odb-2024-08-20/CreateAutonomousDatabaseBackup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/odb-2024-08-20/CreateAutonomousDatabaseBackup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/odb-2024-08-20/CreateAutonomousDatabaseBackup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/CreateAutonomousDatabaseBackup)

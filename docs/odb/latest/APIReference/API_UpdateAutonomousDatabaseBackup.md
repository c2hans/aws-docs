---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_UpdateAutonomousDatabaseBackup.html
---

# UpdateAutonomousDatabaseBackup
<a name="API_UpdateAutonomousDatabaseBackup"></a>

Updates the properties of an Autonomous Database backup.

## Request Syntax
<a name="API_UpdateAutonomousDatabaseBackup_RequestSyntax"></a>

```
{
   "autonomousDatabaseBackupId": "{{string}}",
   "retentionPeriodInDays": {{number}}
}
```

## Request Parameters
<a name="API_UpdateAutonomousDatabaseBackup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [autonomousDatabaseBackupId](#API_UpdateAutonomousDatabaseBackup_RequestSyntax) **   <a name="odb-UpdateAutonomousDatabaseBackup-request-autonomousDatabaseBackupId"></a>
The unique identifier of the Autonomous Database backup to update.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 64.
Pattern: `[a-zA-Z0-9_~.-]+`
Required: Yes

 ** [retentionPeriodInDays](#API_UpdateAutonomousDatabaseBackup_RequestSyntax) **   <a name="odb-UpdateAutonomousDatabaseBackup-request-retentionPeriodInDays"></a>
The retention period, in days, for the Autonomous Database backup.
Type: Integer
Valid Range: Minimum value of 90. Maximum value of 3650.
Required: No

## Response Syntax
<a name="API_UpdateAutonomousDatabaseBackup_ResponseSyntax"></a>

```
{
   "autonomousDatabaseBackupId": "string",
   "displayName": "string",
   "status": "string",
   "statusReason": "string"
}
```

## Response Elements
<a name="API_UpdateAutonomousDatabaseBackup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [autonomousDatabaseBackupId](#API_UpdateAutonomousDatabaseBackup_ResponseSyntax) **   <a name="odb-UpdateAutonomousDatabaseBackup-response-autonomousDatabaseBackupId"></a>
The unique identifier of the Autonomous Database backup that was updated.
Type: String

 ** [displayName](#API_UpdateAutonomousDatabaseBackup_ResponseSyntax) **   <a name="odb-UpdateAutonomousDatabaseBackup-response-displayName"></a>
The user-friendly name of the Autonomous Database backup.
Type: String

 ** [status](#API_UpdateAutonomousDatabaseBackup_ResponseSyntax) **   <a name="odb-UpdateAutonomousDatabaseBackup-response-status"></a>
The current status of the Autonomous Database backup.
Type: String
Valid Values: `AVAILABLE | FAILED | PROVISIONING | TERMINATED | TERMINATING | UPDATING | MAINTENANCE_IN_PROGRESS`

 ** [statusReason](#API_UpdateAutonomousDatabaseBackup_ResponseSyntax) **   <a name="odb-UpdateAutonomousDatabaseBackup-response-statusReason"></a>
Additional information about the current status of the Autonomous Database backup, if applicable.
Type: String

## Errors
<a name="API_UpdateAutonomousDatabaseBackup_Errors"></a>

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
<a name="API_UpdateAutonomousDatabaseBackup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/odb-2024-08-20/UpdateAutonomousDatabaseBackup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/odb-2024-08-20/UpdateAutonomousDatabaseBackup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/UpdateAutonomousDatabaseBackup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/odb-2024-08-20/UpdateAutonomousDatabaseBackup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/UpdateAutonomousDatabaseBackup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/odb-2024-08-20/UpdateAutonomousDatabaseBackup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/odb-2024-08-20/UpdateAutonomousDatabaseBackup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/odb-2024-08-20/UpdateAutonomousDatabaseBackup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/odb-2024-08-20/UpdateAutonomousDatabaseBackup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/UpdateAutonomousDatabaseBackup)

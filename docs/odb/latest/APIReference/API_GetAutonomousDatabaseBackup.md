---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_GetAutonomousDatabaseBackup.html
---

# GetAutonomousDatabaseBackup
<a name="API_GetAutonomousDatabaseBackup"></a>

Gets information about a specific Autonomous Database backup.

## Request Syntax
<a name="API_GetAutonomousDatabaseBackup_RequestSyntax"></a>

```
{
   "autonomousDatabaseBackupId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetAutonomousDatabaseBackup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [autonomousDatabaseBackupId](#API_GetAutonomousDatabaseBackup_RequestSyntax) **   <a name="odb-GetAutonomousDatabaseBackup-request-autonomousDatabaseBackupId"></a>
The unique identifier of the Autonomous Database backup to retrieve information about.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 64.
Pattern: `[a-zA-Z0-9_~.-]+`
Required: Yes

## Response Syntax
<a name="API_GetAutonomousDatabaseBackup_ResponseSyntax"></a>

```
{
   "autonomousDatabaseBackup": {
      "autonomousDatabaseBackupArn": "string",
      "autonomousDatabaseBackupId": "string",
      "autonomousDatabaseId": "string",
      "dbVersion": "string",
      "displayName": "string",
      "isAutomatic": boolean,
      "ocid": "string",
      "retentionPeriodInDays": number,
      "sizeInTBs": number,
      "status": "string",
      "statusReason": "string",
      "timeAvailableTill": "string",
      "timeEnded": "string",
      "timeStarted": "string",
      "type": "string"
   }
}
```

## Response Elements
<a name="API_GetAutonomousDatabaseBackup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [autonomousDatabaseBackup](#API_GetAutonomousDatabaseBackup_ResponseSyntax) **   <a name="odb-GetAutonomousDatabaseBackup-response-autonomousDatabaseBackup"></a>
The details of the requested Autonomous Database backup.
Type: [AutonomousDatabaseBackup](API_AutonomousDatabaseBackup.md) object

## Errors
<a name="API_GetAutonomousDatabaseBackup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.
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
<a name="API_GetAutonomousDatabaseBackup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/odb-2024-08-20/GetAutonomousDatabaseBackup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/odb-2024-08-20/GetAutonomousDatabaseBackup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/GetAutonomousDatabaseBackup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/odb-2024-08-20/GetAutonomousDatabaseBackup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/GetAutonomousDatabaseBackup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/odb-2024-08-20/GetAutonomousDatabaseBackup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/odb-2024-08-20/GetAutonomousDatabaseBackup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/odb-2024-08-20/GetAutonomousDatabaseBackup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/odb-2024-08-20/GetAutonomousDatabaseBackup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/GetAutonomousDatabaseBackup)

---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_StartAutonomousDatabaseRefresh.html
---

# StartAutonomousDatabaseRefresh

Starts a refresh of the specified refreshable clone Autonomous Database with data from its source database. The refresh runs asynchronously. To track its progress, check the `refreshableStatus` of the Autonomous Database.

## Request Syntax
<a name="API_StartAutonomousDatabaseRefresh_RequestSyntax"></a>

```
{
   "autonomousDatabaseId": "{{string}}",
   "timeOfRefreshCutoff": "{{string}}"
}
```

## Request Parameters
<a name="API_StartAutonomousDatabaseRefresh_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [autonomousDatabaseId](#API_StartAutonomousDatabaseRefresh_RequestSyntax) **   <a name="odb-StartAutonomousDatabaseRefresh-request-autonomousDatabaseId"></a>
The unique identifier of the refreshable clone Autonomous Database to refresh.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 2048.
Pattern: `(arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-zA-Z0-9_~.-]{6,64}|[a-zA-Z0-9_~.-]{6,64})`
Required: Yes

 ** [timeOfRefreshCutoff](#API_StartAutonomousDatabaseRefresh_RequestSyntax) **   <a name="odb-StartAutonomousDatabaseRefresh-request-timeOfRefreshCutoff"></a>
The date and time up to which the refreshable clone Autonomous Database is refreshed from its source database. Data committed on the source database after this time isn't applied to the refreshable clone. The time must be at least 1 minute and at most 7 days in the past, and later than the clone's last refresh point.
Type: Timestamp
Required: No

## Response Syntax
<a name="API_StartAutonomousDatabaseRefresh_ResponseSyntax"></a>

```
{
   "autonomousDatabaseId": "string",
   "displayName": "string",
   "refreshableStatus": "string",
   "status": "string",
   "statusReason": "string"
}
```

## Response Elements
<a name="API_StartAutonomousDatabaseRefresh_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [autonomousDatabaseId](#API_StartAutonomousDatabaseRefresh_ResponseSyntax) **   <a name="odb-StartAutonomousDatabaseRefresh-response-autonomousDatabaseId"></a>
The unique identifier of the refreshable clone Autonomous Database that is being refreshed.
Type: String

 ** [displayName](#API_StartAutonomousDatabaseRefresh_ResponseSyntax) **   <a name="odb-StartAutonomousDatabaseRefresh-response-displayName"></a>
The user-friendly name of the Autonomous Database.
Type: String

 ** [refreshableStatus](#API_StartAutonomousDatabaseRefresh_ResponseSyntax) **   <a name="odb-StartAutonomousDatabaseRefresh-response-refreshableStatus"></a>
The refresh status of the refreshable clone Autonomous Database.
Type: String
Valid Values: `REFRESHING | NOT_REFRESHING`

 ** [status](#API_StartAutonomousDatabaseRefresh_ResponseSyntax) **   <a name="odb-StartAutonomousDatabaseRefresh-response-status"></a>
The current status of the Autonomous Database.
Type: String
Valid Values: `AVAILABLE | FAILED | PROVISIONING | TERMINATED | TERMINATING | UPDATING | MAINTENANCE_IN_PROGRESS | STOPPING | STOPPED | STARTING | UNAVAILABLE | RESTORE_IN_PROGRESS | RESTORE_FAILED | BACKUP_IN_PROGRESS | SCALE_IN_PROGRESS | AVAILABLE_NEEDS_ATTENTION | RESTARTING | RECREATING | ROLE_CHANGE_IN_PROGRESS | UPGRADING | INACCESSIBLE | STANDBY`

 ** [statusReason](#API_StartAutonomousDatabaseRefresh_ResponseSyntax) **   <a name="odb-StartAutonomousDatabaseRefresh-response-statusReason"></a>
Additional information about the current status of the Autonomous Database.
Type: String

## Errors
<a name="API_StartAutonomousDatabaseRefresh_Errors"></a>

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
<a name="API_StartAutonomousDatabaseRefresh_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/odb-2024-08-20/StartAutonomousDatabaseRefresh)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/odb-2024-08-20/StartAutonomousDatabaseRefresh)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/StartAutonomousDatabaseRefresh)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/odb-2024-08-20/StartAutonomousDatabaseRefresh)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/StartAutonomousDatabaseRefresh)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/odb-2024-08-20/StartAutonomousDatabaseRefresh)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/odb-2024-08-20/StartAutonomousDatabaseRefresh)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/odb-2024-08-20/StartAutonomousDatabaseRefresh)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/odb-2024-08-20/StartAutonomousDatabaseRefresh)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/StartAutonomousDatabaseRefresh)

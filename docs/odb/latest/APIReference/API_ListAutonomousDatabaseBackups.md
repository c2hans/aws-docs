---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_ListAutonomousDatabaseBackups.html
---

# ListAutonomousDatabaseBackups
<a name="API_ListAutonomousDatabaseBackups"></a>

Lists the backups of the specified Autonomous Database.

## Request Syntax
<a name="API_ListAutonomousDatabaseBackups_RequestSyntax"></a>

```
{
   "autonomousDatabaseId": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "status": "{{string}}",
   "type": "{{string}}"
}
```

## Request Parameters
<a name="API_ListAutonomousDatabaseBackups_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [autonomousDatabaseId](#API_ListAutonomousDatabaseBackups_RequestSyntax) **   <a name="odb-ListAutonomousDatabaseBackups-request-autonomousDatabaseId"></a>
The unique identifier of the Autonomous Database whose backups you want to list.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 64.
Pattern: `[a-zA-Z0-9_~.-]+`
Required: Yes

 ** [maxResults](#API_ListAutonomousDatabaseBackups_RequestSyntax) **   <a name="odb-ListAutonomousDatabaseBackups-request-maxResults"></a>
The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_ListAutonomousDatabaseBackups_RequestSyntax) **   <a name="odb-ListAutonomousDatabaseBackups-request-nextToken"></a>
The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Required: No

 ** [status](#API_ListAutonomousDatabaseBackups_RequestSyntax) **   <a name="odb-ListAutonomousDatabaseBackups-request-status"></a>
The status of the Autonomous Database backups to return results for.
Type: String
Valid Values: `ACTIVE | CREATING | UPDATING | DELETING | FAILED`
Required: No

 ** [type](#API_ListAutonomousDatabaseBackups_RequestSyntax) **   <a name="odb-ListAutonomousDatabaseBackups-request-type"></a>
The type of the Autonomous Database backups to return results for.
Type: String
Valid Values: `INCREMENTAL | FULL | LONGTERM | VIRTUAL_FULL | CUMULATIVE_INCREMENTAL | ROLL_FORWARD_IMAGE_COPY`
Required: No

## Response Syntax
<a name="API_ListAutonomousDatabaseBackups_ResponseSyntax"></a>

```
{
   "autonomousDatabaseBackups": [
      {
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
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAutonomousDatabaseBackups_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [autonomousDatabaseBackups](#API_ListAutonomousDatabaseBackups_ResponseSyntax) **   <a name="odb-ListAutonomousDatabaseBackups-response-autonomousDatabaseBackups"></a>
The list of Autonomous Database backups along with their properties.
Type: Array of [AutonomousDatabaseBackupSummary](API_AutonomousDatabaseBackupSummary.md) objects

 ** [nextToken](#API_ListAutonomousDatabaseBackups_ResponseSyntax) **   <a name="odb-ListAutonomousDatabaseBackups-response-nextToken"></a>
The token to include in another request to get the next page of items. This value is `null` when there are no more items to return.
Type: String

## Errors
<a name="API_ListAutonomousDatabaseBackups_Errors"></a>

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
<a name="API_ListAutonomousDatabaseBackups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/odb-2024-08-20/ListAutonomousDatabaseBackups)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/odb-2024-08-20/ListAutonomousDatabaseBackups)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/ListAutonomousDatabaseBackups)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/odb-2024-08-20/ListAutonomousDatabaseBackups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/ListAutonomousDatabaseBackups)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/odb-2024-08-20/ListAutonomousDatabaseBackups)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/odb-2024-08-20/ListAutonomousDatabaseBackups)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/odb-2024-08-20/ListAutonomousDatabaseBackups)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/odb-2024-08-20/ListAutonomousDatabaseBackups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/ListAutonomousDatabaseBackups)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Oracle Database@AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query odb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

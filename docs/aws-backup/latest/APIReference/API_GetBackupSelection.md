---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_GetBackupSelection.html
---

# GetBackupSelection
<a name="API_GetBackupSelection"></a>

Returns selection metadata and a document in JSON format that specifies a list of resources that are associated with a backup plan.

## Request Syntax
<a name="API_GetBackupSelection_RequestSyntax"></a>

```
GET /backup/plans/{{backupPlanId}}/selections/{{selectionId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetBackupSelection_RequestParameters"></a>

The request uses the following URI parameters.

 ** [backupPlanId](#API_GetBackupSelection_RequestSyntax) **   <a name="Backup-GetBackupSelection-request-uri-BackupPlanId"></a>
Uniquely identifies a backup plan.
Required: Yes

 ** [selectionId](#API_GetBackupSelection_RequestSyntax) **   <a name="Backup-GetBackupSelection-request-uri-SelectionId"></a>
Uniquely identifies the body of a request to assign a set of resources to a backup plan.
Required: Yes

## Request Body
<a name="API_GetBackupSelection_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetBackupSelection_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "BackupPlanId": "string",
   "BackupSelection": {
      "Conditions": {
         "StringEquals": [
            {
               "ConditionKey": "string",
               "ConditionValue": "string"
            }
         ],
         "StringLike": [
            {
               "ConditionKey": "string",
               "ConditionValue": "string"
            }
         ],
         "StringNotEquals": [
            {
               "ConditionKey": "string",
               "ConditionValue": "string"
            }
         ],
         "StringNotLike": [
            {
               "ConditionKey": "string",
               "ConditionValue": "string"
            }
         ]
      },
      "IamRoleArn": "string",
      "ListOfTags": [
         {
            "ConditionKey": "string",
            "ConditionType": "string",
            "ConditionValue": "string"
         }
      ],
      "NotResources": [ "string" ],
      "Resources": [ "string" ],
      "SelectionName": "string"
   },
   "CreationDate": number,
   "CreatorRequestId": "string",
   "SelectionId": "string"
}
```

## Response Elements
<a name="API_GetBackupSelection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BackupPlanId](#API_GetBackupSelection_ResponseSyntax) **   <a name="Backup-GetBackupSelection-response-BackupPlanId"></a>
Uniquely identifies a backup plan.
Type: String

 ** [BackupSelection](#API_GetBackupSelection_ResponseSyntax) **   <a name="Backup-GetBackupSelection-response-BackupSelection"></a>
Specifies the body of a request to assign a set of resources to a backup plan.
Type: [BackupSelection](API_BackupSelection.md) object

 ** [CreationDate](#API_GetBackupSelection_ResponseSyntax) **   <a name="Backup-GetBackupSelection-response-CreationDate"></a>
The date and time a backup selection is created, in Unix format and Coordinated Universal Time (UTC). The value of `CreationDate` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
Type: Timestamp

 ** [CreatorRequestId](#API_GetBackupSelection_ResponseSyntax) **   <a name="Backup-GetBackupSelection-response-CreatorRequestId"></a>
A unique string that identifies the request and allows failed requests to be retried without the risk of running the operation twice.
Type: String

 ** [SelectionId](#API_GetBackupSelection_ResponseSyntax) **   <a name="Backup-GetBackupSelection-response-SelectionId"></a>
Uniquely identifies the body of a request to assign a set of resources to a backup plan.
Type: String

## Errors
<a name="API_GetBackupSelection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **
Indicates that something is wrong with a parameter's value. For example, the value is out of range.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** MissingParameterValueException **
Indicates that a required parameter is missing.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** ResourceNotFoundException **
A resource that is required for the action doesn't exist.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** ServiceUnavailableException **
The request failed due to a temporary failure of the server.
 ** Context **

 ** Type **

HTTP Status Code: 500

## See Also
<a name="API_GetBackupSelection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/GetBackupSelection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/GetBackupSelection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/GetBackupSelection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/GetBackupSelection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/GetBackupSelection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/GetBackupSelection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/GetBackupSelection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/GetBackupSelection)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/GetBackupSelection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/GetBackupSelection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

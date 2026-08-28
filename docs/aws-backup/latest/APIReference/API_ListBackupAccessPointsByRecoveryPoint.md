---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_ListBackupAccessPointsByRecoveryPoint.html
---

# ListBackupAccessPointsByRecoveryPoint
<a name="API_ListBackupAccessPointsByRecoveryPoint"></a>

Returns the backup access points associated with the specified recovery point.

If you own the recovery point and have shared it with other accounts, the response includes backup access points created by those accounts.

## Request Syntax
<a name="API_ListBackupAccessPointsByRecoveryPoint_RequestSyntax"></a>

```
POST /backup-access-point/recovery-point/{{RecoveryPointArn}}?MaxResults={{MaxResults}}&NextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListBackupAccessPointsByRecoveryPoint_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListBackupAccessPointsByRecoveryPoint_RequestSyntax) **   <a name="Backup-ListBackupAccessPointsByRecoveryPoint-request-uri-MaxResults"></a>
The maximum number of items to be returned.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListBackupAccessPointsByRecoveryPoint_RequestSyntax) **   <a name="Backup-ListBackupAccessPointsByRecoveryPoint-request-uri-NextToken"></a>
The next item following a partial list of returned items. For example, if a request is made to return `MaxResults` number of items, `NextToken` allows you to return more items in your list starting at the location pointed to by the next token.

 ** [RecoveryPointArn](#API_ListBackupAccessPointsByRecoveryPoint_RequestSyntax) **   <a name="Backup-ListBackupAccessPointsByRecoveryPoint-request-uri-RecoveryPointArn"></a>
The Amazon Resource Name (ARN) of the recovery point whose backup access points you want to list.
Pattern: `(arn:aws[a-z-]*:[a-z-\d]+:[a-z-\d]+:).+`
Required: Yes

## Request Body
<a name="API_ListBackupAccessPointsByRecoveryPoint_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListBackupAccessPointsByRecoveryPoint_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "BackupAccessPoints": [
      {
         "AccessPointArn": "string",
         "AccessPointMetadata": {
            "string" : "string"
         },
         "BackupVaultArn": "string",
         "BackupVaultName": "string",
         "CreationTime": number,
         "Name": "string",
         "RecoveryPointArn": "string",
         "ResourceArn": "string",
         "ResourceType": "string",
         "Status": "string",
         "StatusMessage": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListBackupAccessPointsByRecoveryPoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BackupAccessPoints](#API_ListBackupAccessPointsByRecoveryPoint_ResponseSyntax) **   <a name="Backup-ListBackupAccessPointsByRecoveryPoint-response-BackupAccessPoints"></a>
A list of backup access points, each containing metadata such as its name, ARN, status, and associated recovery point.
Type: Array of [ListAccessPointsMember](API_ListAccessPointsMember.md) objects

 ** [NextToken](#API_ListBackupAccessPointsByRecoveryPoint_ResponseSyntax) **   <a name="Backup-ListBackupAccessPointsByRecoveryPoint-response-NextToken"></a>
The next item following a partial list of returned items. For example, if a request is made to return `MaxResults` number of items, `NextToken` allows you to return more items in your list starting at the location pointed to by the next token.
Type: String

## Errors
<a name="API_ListBackupAccessPointsByRecoveryPoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **
Indicates that something is wrong with a parameter's value. For example, the value is out of range.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** ServiceUnavailableException **
The request failed due to a temporary failure of the server.
 ** Context **

 ** Type **

HTTP Status Code: 500

## See Also
<a name="API_ListBackupAccessPointsByRecoveryPoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/ListBackupAccessPointsByRecoveryPoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/ListBackupAccessPointsByRecoveryPoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/ListBackupAccessPointsByRecoveryPoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/ListBackupAccessPointsByRecoveryPoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/ListBackupAccessPointsByRecoveryPoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/ListBackupAccessPointsByRecoveryPoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/ListBackupAccessPointsByRecoveryPoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/ListBackupAccessPointsByRecoveryPoint)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/ListBackupAccessPointsByRecoveryPoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/ListBackupAccessPointsByRecoveryPoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

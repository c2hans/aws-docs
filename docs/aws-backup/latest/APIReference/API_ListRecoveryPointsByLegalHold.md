---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_ListRecoveryPointsByLegalHold.html
---

# ListRecoveryPointsByLegalHold
<a name="API_ListRecoveryPointsByLegalHold"></a>

This action returns recovery point ARNs (Amazon Resource Names) of the specified legal hold.

## Request Syntax
<a name="API_ListRecoveryPointsByLegalHold_RequestSyntax"></a>

```
GET /legal-holds/{{legalHoldId}}/recovery-points?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListRecoveryPointsByLegalHold_RequestParameters"></a>

The request uses the following URI parameters.

 ** [legalHoldId](#API_ListRecoveryPointsByLegalHold_RequestSyntax) **   <a name="Backup-ListRecoveryPointsByLegalHold-request-uri-LegalHoldId"></a>
The ID of the legal hold.
Required: Yes

 ** [MaxResults](#API_ListRecoveryPointsByLegalHold_RequestSyntax) **   <a name="Backup-ListRecoveryPointsByLegalHold-request-uri-MaxResults"></a>
The maximum number of resource list items to be returned.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [NextToken](#API_ListRecoveryPointsByLegalHold_RequestSyntax) **   <a name="Backup-ListRecoveryPointsByLegalHold-request-uri-NextToken"></a>
The next item following a partial list of returned resources. For example, if a request is made to return `MaxResults` number of resources, `NextToken` allows you to return more items in your list starting at the location pointed to by the next token.

## Request Body
<a name="API_ListRecoveryPointsByLegalHold_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListRecoveryPointsByLegalHold_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "RecoveryPoints": [
      {
         "BackupVaultName": "string",
         "RecoveryPointArn": "string",
         "ResourceArn": "string",
         "ResourceType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListRecoveryPointsByLegalHold_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListRecoveryPointsByLegalHold_ResponseSyntax) **   <a name="Backup-ListRecoveryPointsByLegalHold-response-NextToken"></a>
The next item following a partial list of returned resources.
Type: String

 ** [RecoveryPoints](#API_ListRecoveryPointsByLegalHold_ResponseSyntax) **   <a name="Backup-ListRecoveryPointsByLegalHold-response-RecoveryPoints"></a>
The recovery points.
Type: Array of [RecoveryPointMember](API_RecoveryPointMember.md) objects

## Errors
<a name="API_ListRecoveryPointsByLegalHold_Errors"></a>

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

 ** ServiceUnavailableException **
The request failed due to a temporary failure of the server.
 ** Context **

 ** Type **

HTTP Status Code: 500

## See Also
<a name="API_ListRecoveryPointsByLegalHold_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/ListRecoveryPointsByLegalHold)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/ListRecoveryPointsByLegalHold)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/ListRecoveryPointsByLegalHold)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/ListRecoveryPointsByLegalHold)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/ListRecoveryPointsByLegalHold)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/ListRecoveryPointsByLegalHold)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/ListRecoveryPointsByLegalHold)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/ListRecoveryPointsByLegalHold)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/ListRecoveryPointsByLegalHold)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/ListRecoveryPointsByLegalHold)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

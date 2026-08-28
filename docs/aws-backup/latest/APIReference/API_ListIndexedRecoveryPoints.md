---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_ListIndexedRecoveryPoints.html
---

# ListIndexedRecoveryPoints
<a name="API_ListIndexedRecoveryPoints"></a>

This operation returns a list of recovery points that have an associated index, belonging to the specified account.

Optional parameters you can include are: MaxResults; NextToken; SourceResourceArns; CreatedBefore; CreatedAfter; and ResourceType.

## Request Syntax
<a name="API_ListIndexedRecoveryPoints_RequestSyntax"></a>

```
GET /indexes/recovery-point/?createdAfter={{CreatedAfter}}&createdBefore={{CreatedBefore}}&indexStatus={{IndexStatus}}&maxResults={{MaxResults}}&nextToken={{NextToken}}&resourceType={{ResourceType}}&sourceResourceArn={{SourceResourceArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListIndexedRecoveryPoints_RequestParameters"></a>

The request uses the following URI parameters.

 ** [CreatedAfter](#API_ListIndexedRecoveryPoints_RequestSyntax) **   <a name="Backup-ListIndexedRecoveryPoints-request-uri-CreatedAfter"></a>
Returns only indexed recovery points that were created after the specified date.

 ** [CreatedBefore](#API_ListIndexedRecoveryPoints_RequestSyntax) **   <a name="Backup-ListIndexedRecoveryPoints-request-uri-CreatedBefore"></a>
Returns only indexed recovery points that were created before the specified date.

 ** [IndexStatus](#API_ListIndexedRecoveryPoints_RequestSyntax) **   <a name="Backup-ListIndexedRecoveryPoints-request-uri-IndexStatus"></a>
Include this parameter to filter the returned list by the indicated statuses.
Accepted values: `PENDING` \| `ACTIVE` \| `FAILED` \| `DELETING`
A recovery point with an index that has the status of `ACTIVE` can be included in a search.
Valid Values: `PENDING | ACTIVE | FAILED | DELETING`

 ** [MaxResults](#API_ListIndexedRecoveryPoints_RequestSyntax) **   <a name="Backup-ListIndexedRecoveryPoints-request-uri-MaxResults"></a>
The maximum number of resource list items to be returned.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [NextToken](#API_ListIndexedRecoveryPoints_RequestSyntax) **   <a name="Backup-ListIndexedRecoveryPoints-request-uri-NextToken"></a>
The next item following a partial list of returned recovery points.
For example, if a request is made to return `MaxResults` number of indexed recovery points, `NextToken` allows you to return more items in your list starting at the location pointed to by the next token.

 ** [ResourceType](#API_ListIndexedRecoveryPoints_RequestSyntax) **   <a name="Backup-ListIndexedRecoveryPoints-request-uri-ResourceType"></a>
Returns a list of indexed recovery points for the specified resource type(s).
Accepted values include:
+  `EBS` for Amazon Elastic Block Store
+  `S3` for Amazon Simple Storage Service (Amazon S3)
Pattern: `^[a-zA-Z0-9\-\_\.]{1,50}$`

 ** [SourceResourceArn](#API_ListIndexedRecoveryPoints_RequestSyntax) **   <a name="Backup-ListIndexedRecoveryPoints-request-uri-SourceResourceArn"></a>
A string of the Amazon Resource Name (ARN) that uniquely identifies the source resource.

## Request Body
<a name="API_ListIndexedRecoveryPoints_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListIndexedRecoveryPoints_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "IndexedRecoveryPoints": [
      {
         "BackupCreationDate": number,
         "BackupVaultArn": "string",
         "IamRoleArn": "string",
         "IndexCreationDate": number,
         "IndexStatus": "string",
         "IndexStatusMessage": "string",
         "RecoveryPointArn": "string",
         "ResourceType": "string",
         "SourceResourceArn": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListIndexedRecoveryPoints_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [IndexedRecoveryPoints](#API_ListIndexedRecoveryPoints_ResponseSyntax) **   <a name="Backup-ListIndexedRecoveryPoints-response-IndexedRecoveryPoints"></a>
This is a list of recovery points that have an associated index, belonging to the specified account.
Type: Array of [IndexedRecoveryPoint](API_IndexedRecoveryPoint.md) objects

 ** [NextToken](#API_ListIndexedRecoveryPoints_ResponseSyntax) **   <a name="Backup-ListIndexedRecoveryPoints-response-NextToken"></a>
The next item following a partial list of returned recovery points.
For example, if a request is made to return `MaxResults` number of indexed recovery points, `NextToken` allows you to return more items in your list starting at the location pointed to by the next token.
Type: String

## Errors
<a name="API_ListIndexedRecoveryPoints_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **
Indicates that something is wrong with a parameter's value. For example, the value is out of range.
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
<a name="API_ListIndexedRecoveryPoints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/ListIndexedRecoveryPoints)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/ListIndexedRecoveryPoints)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/ListIndexedRecoveryPoints)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/ListIndexedRecoveryPoints)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/ListIndexedRecoveryPoints)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/ListIndexedRecoveryPoints)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/ListIndexedRecoveryPoints)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/ListIndexedRecoveryPoints)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/ListIndexedRecoveryPoints)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/ListIndexedRecoveryPoints)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

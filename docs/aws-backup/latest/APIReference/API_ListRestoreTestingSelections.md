---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_ListRestoreTestingSelections.html
---

# ListRestoreTestingSelections
<a name="API_ListRestoreTestingSelections"></a>

Returns a list of restore testing selections. Can be filtered by `MaxResults` and `RestoreTestingPlanName`.

## Request Syntax
<a name="API_ListRestoreTestingSelections_RequestSyntax"></a>

```
GET /restore-testing/plans/{{RestoreTestingPlanName}}/selections?MaxResults={{MaxResults}}&NextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListRestoreTestingSelections_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListRestoreTestingSelections_RequestSyntax) **   <a name="Backup-ListRestoreTestingSelections-request-uri-MaxResults"></a>
The maximum number of items to be returned.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [NextToken](#API_ListRestoreTestingSelections_RequestSyntax) **   <a name="Backup-ListRestoreTestingSelections-request-uri-NextToken"></a>
The next item following a partial list of returned items. For example, if a request is made to return `MaxResults` number of items, `NextToken` allows you to return more items in your list starting at the location pointed to by the nexttoken.

 ** [RestoreTestingPlanName](#API_ListRestoreTestingSelections_RequestSyntax) **   <a name="Backup-ListRestoreTestingSelections-request-uri-RestoreTestingPlanName"></a>
Returns restore testing selections by the specified restore testing plan name.
Required: Yes

## Request Body
<a name="API_ListRestoreTestingSelections_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListRestoreTestingSelections_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "RestoreTestingSelections": [
      {
         "CreationTime": number,
         "IamRoleArn": "string",
         "ProtectedResourceType": "string",
         "RestoreTestingPlanName": "string",
         "RestoreTestingSelectionName": "string",
         "ValidationWindowHours": number
      }
   ]
}
```

## Response Elements
<a name="API_ListRestoreTestingSelections_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListRestoreTestingSelections_ResponseSyntax) **   <a name="Backup-ListRestoreTestingSelections-response-NextToken"></a>
The next item following a partial list of returned items. For example, if a request is made to return `MaxResults` number of items, `NextToken` allows you to return more items in your list starting at the location pointed to by the nexttoken.
Type: String

 ** [RestoreTestingSelections](#API_ListRestoreTestingSelections_ResponseSyntax) **   <a name="Backup-ListRestoreTestingSelections-response-RestoreTestingSelections"></a>
The returned restore testing selections associated with the restore testing plan.
Type: Array of [RestoreTestingSelectionForList](API_RestoreTestingSelectionForList.md) objects

## Errors
<a name="API_ListRestoreTestingSelections_Errors"></a>

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
<a name="API_ListRestoreTestingSelections_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/ListRestoreTestingSelections)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/ListRestoreTestingSelections)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/ListRestoreTestingSelections)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/ListRestoreTestingSelections)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/ListRestoreTestingSelections)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/ListRestoreTestingSelections)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/ListRestoreTestingSelections)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/ListRestoreTestingSelections)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/ListRestoreTestingSelections)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/ListRestoreTestingSelections)

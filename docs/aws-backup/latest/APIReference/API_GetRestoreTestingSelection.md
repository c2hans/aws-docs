---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_GetRestoreTestingSelection.html
---

# GetRestoreTestingSelection
<a name="API_GetRestoreTestingSelection"></a>

Returns RestoreTestingSelection, which displays resources and elements of the restore testing plan.

## Request Syntax
<a name="API_GetRestoreTestingSelection_RequestSyntax"></a>

```
GET /restore-testing/plans/{{RestoreTestingPlanName}}/selections/{{RestoreTestingSelectionName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetRestoreTestingSelection_RequestParameters"></a>

The request uses the following URI parameters.

 ** [RestoreTestingPlanName](#API_GetRestoreTestingSelection_RequestSyntax) **   <a name="Backup-GetRestoreTestingSelection-request-uri-RestoreTestingPlanName"></a>
Required unique name of the restore testing plan.
Required: Yes

 ** [RestoreTestingSelectionName](#API_GetRestoreTestingSelection_RequestSyntax) **   <a name="Backup-GetRestoreTestingSelection-request-uri-RestoreTestingSelectionName"></a>
Required unique name of the restore testing selection.
Required: Yes

## Request Body
<a name="API_GetRestoreTestingSelection_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetRestoreTestingSelection_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "RestoreTestingSelection": {
      "CreationTime": number,
      "CreatorRequestId": "string",
      "IamRoleArn": "string",
      "ProtectedResourceArns": [ "string" ],
      "ProtectedResourceConditions": {
         "StringEquals": [
            {
               "Key": "string",
               "Value": "string"
            }
         ],
         "StringNotEquals": [
            {
               "Key": "string",
               "Value": "string"
            }
         ]
      },
      "ProtectedResourceType": "string",
      "RestoreMetadataOverrides": {
         "string" : "string"
      },
      "RestoreTestingPlanName": "string",
      "RestoreTestingSelectionName": "string",
      "ValidationWindowHours": number
   }
}
```

## Response Elements
<a name="API_GetRestoreTestingSelection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RestoreTestingSelection](#API_GetRestoreTestingSelection_ResponseSyntax) **   <a name="Backup-GetRestoreTestingSelection-response-RestoreTestingSelection"></a>
Unique name of the restore testing selection.
Type: [RestoreTestingSelectionForGet](API_RestoreTestingSelectionForGet.md) object

## Errors
<a name="API_GetRestoreTestingSelection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_GetRestoreTestingSelection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/GetRestoreTestingSelection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/GetRestoreTestingSelection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/GetRestoreTestingSelection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/GetRestoreTestingSelection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/GetRestoreTestingSelection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/GetRestoreTestingSelection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/GetRestoreTestingSelection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/GetRestoreTestingSelection)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/GetRestoreTestingSelection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/GetRestoreTestingSelection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_DeleteRestoreTestingSelection.html
---

# DeleteRestoreTestingSelection
<a name="API_DeleteRestoreTestingSelection"></a>

Input the Restore Testing Plan name and Restore Testing Selection name.

All testing selections associated with a restore testing plan must be deleted before the restore testing plan can be deleted.

## Request Syntax
<a name="API_DeleteRestoreTestingSelection_RequestSyntax"></a>

```
DELETE /restore-testing/plans/{{RestoreTestingPlanName}}/selections/{{RestoreTestingSelectionName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteRestoreTestingSelection_RequestParameters"></a>

The request uses the following URI parameters.

 ** [RestoreTestingPlanName](#API_DeleteRestoreTestingSelection_RequestSyntax) **   <a name="Backup-DeleteRestoreTestingSelection-request-uri-RestoreTestingPlanName"></a>
Required unique name of the restore testing plan that contains the restore testing selection you wish to delete.
Required: Yes

 ** [RestoreTestingSelectionName](#API_DeleteRestoreTestingSelection_RequestSyntax) **   <a name="Backup-DeleteRestoreTestingSelection-request-uri-RestoreTestingSelectionName"></a>
Required unique name of the restore testing selection you wish to delete.
Required: Yes

## Request Body
<a name="API_DeleteRestoreTestingSelection_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteRestoreTestingSelection_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteRestoreTestingSelection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteRestoreTestingSelection_Errors"></a>

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
<a name="API_DeleteRestoreTestingSelection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/DeleteRestoreTestingSelection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/DeleteRestoreTestingSelection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/DeleteRestoreTestingSelection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/DeleteRestoreTestingSelection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/DeleteRestoreTestingSelection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/DeleteRestoreTestingSelection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/DeleteRestoreTestingSelection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/DeleteRestoreTestingSelection)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/DeleteRestoreTestingSelection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/DeleteRestoreTestingSelection)

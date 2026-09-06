---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_DeleteRestoreTestingPlan.html
---

# DeleteRestoreTestingPlan
<a name="API_DeleteRestoreTestingPlan"></a>

This request deletes the specified restore testing plan.

Deletion can only successfully occur if all associated restore testing selections are deleted first.

## Request Syntax
<a name="API_DeleteRestoreTestingPlan_RequestSyntax"></a>

```
DELETE /restore-testing/plans/{{RestoreTestingPlanName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteRestoreTestingPlan_RequestParameters"></a>

The request uses the following URI parameters.

 ** [RestoreTestingPlanName](#API_DeleteRestoreTestingPlan_RequestSyntax) **   <a name="Backup-DeleteRestoreTestingPlan-request-uri-RestoreTestingPlanName"></a>
Required unique name of the restore testing plan you wish to delete.
Required: Yes

## Request Body
<a name="API_DeleteRestoreTestingPlan_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteRestoreTestingPlan_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteRestoreTestingPlan_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteRestoreTestingPlan_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidRequestException **
Indicates that something is wrong with the input to the request. For example, a parameter is of the wrong type.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** ServiceUnavailableException **
The request failed due to a temporary failure of the server.
 ** Context **

 ** Type **

HTTP Status Code: 500

## See Also
<a name="API_DeleteRestoreTestingPlan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/DeleteRestoreTestingPlan)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/DeleteRestoreTestingPlan)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/DeleteRestoreTestingPlan)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/DeleteRestoreTestingPlan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/DeleteRestoreTestingPlan)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/DeleteRestoreTestingPlan)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/DeleteRestoreTestingPlan)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/DeleteRestoreTestingPlan)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/DeleteRestoreTestingPlan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/DeleteRestoreTestingPlan)

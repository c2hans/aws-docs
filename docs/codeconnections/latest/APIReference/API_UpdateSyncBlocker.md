---
source_url: https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_UpdateSyncBlocker.html
---

# UpdateSyncBlocker
<a name="API_UpdateSyncBlocker"></a>

Allows you to update the status of a sync blocker, resolving the blocker and allowing syncing to continue.

## Request Syntax
<a name="API_UpdateSyncBlocker_RequestSyntax"></a>

```
{
   "Id": "{{string}}",
   "ResolvedReason": "{{string}}",
   "ResourceName": "{{string}}",
   "SyncType": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateSyncBlocker_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Id](#API_UpdateSyncBlocker_RequestSyntax) **   <a name="codeconnections-UpdateSyncBlocker-request-Id"></a>
The ID of the sync blocker to be updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: Yes

 ** [ResolvedReason](#API_UpdateSyncBlocker_RequestSyntax) **   <a name="codeconnections-UpdateSyncBlocker-request-ResolvedReason"></a>
The reason for resolving the sync blocker.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 250.
Required: Yes

 ** [ResourceName](#API_UpdateSyncBlocker_RequestSyntax) **   <a name="codeconnections-UpdateSyncBlocker-request-ResourceName"></a>
The name of the resource for the sync blocker to be updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[0-9A-Za-z]+[0-9A-Za-z_\\-]*$`
Required: Yes

 ** [SyncType](#API_UpdateSyncBlocker_RequestSyntax) **   <a name="codeconnections-UpdateSyncBlocker-request-SyncType"></a>
The sync type of the sync blocker to be updated.
Type: String
Valid Values: `CFN_STACK_SYNC`
Required: Yes

## Response Syntax
<a name="API_UpdateSyncBlocker_ResponseSyntax"></a>

```
{
   "ParentResourceName": "string",
   "ResourceName": "string",
   "SyncBlocker": {
      "Contexts": [
         {
            "Key": "string",
            "Value": "string"
         }
      ],
      "CreatedAt": number,
      "CreatedReason": "string",
      "Id": "string",
      "ResolvedAt": number,
      "ResolvedReason": "string",
      "Status": "string",
      "Type": "string"
   }
}
```

## Response Elements
<a name="API_UpdateSyncBlocker_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ParentResourceName](#API_UpdateSyncBlocker_ResponseSyntax) **   <a name="codeconnections-UpdateSyncBlocker-response-ParentResourceName"></a>
The parent resource name for the sync blocker.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[0-9A-Za-z]+[0-9A-Za-z_\\-]*$`

 ** [ResourceName](#API_UpdateSyncBlocker_ResponseSyntax) **   <a name="codeconnections-UpdateSyncBlocker-response-ResourceName"></a>
The resource name for the sync blocker.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[0-9A-Za-z]+[0-9A-Za-z_\\-]*$`

 ** [SyncBlocker](#API_UpdateSyncBlocker_ResponseSyntax) **   <a name="codeconnections-UpdateSyncBlocker-response-SyncBlocker"></a>
Information about the sync blocker to be updated.
Type: [SyncBlocker](API_SyncBlocker.md) object

## Errors
<a name="API_UpdateSyncBlocker_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
Received an internal server exception. Try again later.
HTTP Status Code: 400

 ** InvalidInputException **
The input is not valid. Verify that the action is typed correctly.
HTTP Status Code: 400

 ** ResourceNotFoundException **
Resource not found. Verify the connection resource ARN and try again.
HTTP Status Code: 400

 ** RetryLatestCommitFailedException **
Retrying the latest commit failed. Try again later.
HTTP Status Code: 400

 ** SyncBlockerDoesNotExistException **
Unable to continue. The sync blocker does not exist.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

## See Also
<a name="API_UpdateSyncBlocker_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeconnections-2023-12-01/UpdateSyncBlocker)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeconnections-2023-12-01/UpdateSyncBlocker)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeconnections-2023-12-01/UpdateSyncBlocker)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeconnections-2023-12-01/UpdateSyncBlocker)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeconnections-2023-12-01/UpdateSyncBlocker)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeconnections-2023-12-01/UpdateSyncBlocker)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeconnections-2023-12-01/UpdateSyncBlocker)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeconnections-2023-12-01/UpdateSyncBlocker)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codeconnections-2023-12-01/UpdateSyncBlocker)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeconnections-2023-12-01/UpdateSyncBlocker)

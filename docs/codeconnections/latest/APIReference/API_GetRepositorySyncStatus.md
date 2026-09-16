---
source_url: https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_GetRepositorySyncStatus.html
---

# GetRepositorySyncStatus
<a name="API_GetRepositorySyncStatus"></a>

Returns details about the sync status for a repository. A repository sync uses Git sync to push and pull changes from your remote repository.

## Request Syntax
<a name="API_GetRepositorySyncStatus_RequestSyntax"></a>

```
{
   "Branch": "{{string}}",
   "RepositoryLinkId": "{{string}}",
   "SyncType": "{{string}}"
}
```

## Request Parameters
<a name="API_GetRepositorySyncStatus_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Branch](#API_GetRepositorySyncStatus_RequestSyntax) **   <a name="codeconnections-GetRepositorySyncStatus-request-Branch"></a>
The branch of the repository link for the requested repository sync status.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^.*$`
Required: Yes

 ** [RepositoryLinkId](#API_GetRepositorySyncStatus_RequestSyntax) **   <a name="codeconnections-GetRepositorySyncStatus-request-RepositoryLinkId"></a>
The repository link ID for the requested repository sync status.
Type: String
Pattern: `^[0-9a-fA-F]{8}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{12}$`
Required: Yes

 ** [SyncType](#API_GetRepositorySyncStatus_RequestSyntax) **   <a name="codeconnections-GetRepositorySyncStatus-request-SyncType"></a>
The sync type of the requested sync status.
Type: String
Valid Values: `CFN_STACK_SYNC`
Required: Yes

## Response Syntax
<a name="API_GetRepositorySyncStatus_ResponseSyntax"></a>

```
{
   "LatestSync": {
      "Events": [
         {
            "Event": "string",
            "ExternalId": "string",
            "Time": number,
            "Type": "string"
         }
      ],
      "StartedAt": number,
      "Status": "string"
   }
}
```

## Response Elements
<a name="API_GetRepositorySyncStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LatestSync](#API_GetRepositorySyncStatus_ResponseSyntax) **   <a name="codeconnections-GetRepositorySyncStatus-response-LatestSync"></a>
The status of the latest sync returned for a specified repository and branch.
Type: [RepositorySyncAttempt](API_RepositorySyncAttempt.md) object

## Errors
<a name="API_GetRepositorySyncStatus_Errors"></a>

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

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

## See Also
<a name="API_GetRepositorySyncStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeconnections-2023-12-01/GetRepositorySyncStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeconnections-2023-12-01/GetRepositorySyncStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeconnections-2023-12-01/GetRepositorySyncStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeconnections-2023-12-01/GetRepositorySyncStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeconnections-2023-12-01/GetRepositorySyncStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeconnections-2023-12-01/GetRepositorySyncStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeconnections-2023-12-01/GetRepositorySyncStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeconnections-2023-12-01/GetRepositorySyncStatus)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codeconnections-2023-12-01/GetRepositorySyncStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeconnections-2023-12-01/GetRepositorySyncStatus)

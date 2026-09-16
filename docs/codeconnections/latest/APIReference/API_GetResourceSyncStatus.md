---
source_url: https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_GetResourceSyncStatus.html
---

# GetResourceSyncStatus
<a name="API_GetResourceSyncStatus"></a>

Returns the status of the sync with the Git repository for a specific AWS resource.

## Request Syntax
<a name="API_GetResourceSyncStatus_RequestSyntax"></a>

```
{
   "ResourceName": "{{string}}",
   "SyncType": "{{string}}"
}
```

## Request Parameters
<a name="API_GetResourceSyncStatus_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceName](#API_GetResourceSyncStatus_RequestSyntax) **   <a name="codeconnections-GetResourceSyncStatus-request-ResourceName"></a>
The name of the AWS resource for the sync status with the Git repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[0-9A-Za-z]+[0-9A-Za-z_\\-]*$`
Required: Yes

 ** [SyncType](#API_GetResourceSyncStatus_RequestSyntax) **   <a name="codeconnections-GetResourceSyncStatus-request-SyncType"></a>
The sync type for the sync status with the Git repository.
Type: String
Valid Values: `CFN_STACK_SYNC`
Required: Yes

## Response Syntax
<a name="API_GetResourceSyncStatus_ResponseSyntax"></a>

```
{
   "DesiredState": {
      "Branch": "string",
      "Directory": "string",
      "OwnerId": "string",
      "ProviderType": "string",
      "RepositoryName": "string",
      "Sha": "string"
   },
   "LatestSuccessfulSync": {
      "Events": [
         {
            "Event": "string",
            "ExternalId": "string",
            "Time": number,
            "Type": "string"
         }
      ],
      "InitialRevision": {
         "Branch": "string",
         "Directory": "string",
         "OwnerId": "string",
         "ProviderType": "string",
         "RepositoryName": "string",
         "Sha": "string"
      },
      "StartedAt": number,
      "Status": "string",
      "Target": "string",
      "TargetRevision": {
         "Branch": "string",
         "Directory": "string",
         "OwnerId": "string",
         "ProviderType": "string",
         "RepositoryName": "string",
         "Sha": "string"
      }
   },
   "LatestSync": {
      "Events": [
         {
            "Event": "string",
            "ExternalId": "string",
            "Time": number,
            "Type": "string"
         }
      ],
      "InitialRevision": {
         "Branch": "string",
         "Directory": "string",
         "OwnerId": "string",
         "ProviderType": "string",
         "RepositoryName": "string",
         "Sha": "string"
      },
      "StartedAt": number,
      "Status": "string",
      "Target": "string",
      "TargetRevision": {
         "Branch": "string",
         "Directory": "string",
         "OwnerId": "string",
         "ProviderType": "string",
         "RepositoryName": "string",
         "Sha": "string"
      }
   }
}
```

## Response Elements
<a name="API_GetResourceSyncStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DesiredState](#API_GetResourceSyncStatus_ResponseSyntax) **   <a name="codeconnections-GetResourceSyncStatus-response-DesiredState"></a>
The desired state of the AWS resource for the sync status with the Git repository.
Type: [Revision](API_Revision.md) object

 ** [LatestSuccessfulSync](#API_GetResourceSyncStatus_ResponseSyntax) **   <a name="codeconnections-GetResourceSyncStatus-response-LatestSuccessfulSync"></a>
The latest successful sync for the sync status with the Git repository.
Type: [ResourceSyncAttempt](API_ResourceSyncAttempt.md) object

 ** [LatestSync](#API_GetResourceSyncStatus_ResponseSyntax) **   <a name="codeconnections-GetResourceSyncStatus-response-LatestSync"></a>
The latest sync for the sync status with the Git repository, whether successful or not.
Type: [ResourceSyncAttempt](API_ResourceSyncAttempt.md) object

## Errors
<a name="API_GetResourceSyncStatus_Errors"></a>

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
<a name="API_GetResourceSyncStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeconnections-2023-12-01/GetResourceSyncStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeconnections-2023-12-01/GetResourceSyncStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeconnections-2023-12-01/GetResourceSyncStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeconnections-2023-12-01/GetResourceSyncStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeconnections-2023-12-01/GetResourceSyncStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeconnections-2023-12-01/GetResourceSyncStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeconnections-2023-12-01/GetResourceSyncStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeconnections-2023-12-01/GetResourceSyncStatus)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codeconnections-2023-12-01/GetResourceSyncStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeconnections-2023-12-01/GetResourceSyncStatus)

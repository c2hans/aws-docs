---
source_url: https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_GetSyncConfiguration.html
---

# GetSyncConfiguration
<a name="API_GetSyncConfiguration"></a>

Returns details about a sync configuration, including the sync type and resource name. A sync configuration allows the configuration to sync (push and pull) changes from the remote repository for a specified branch in a Git repository.

## Request Syntax
<a name="API_GetSyncConfiguration_RequestSyntax"></a>

```
{
   "ResourceName": "{{string}}",
   "SyncType": "{{string}}"
}
```

## Request Parameters
<a name="API_GetSyncConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceName](#API_GetSyncConfiguration_RequestSyntax) **   <a name="codeconnections-GetSyncConfiguration-request-ResourceName"></a>
The name of the AWS resource for the sync configuration for which you want to retrieve information.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[0-9A-Za-z]+[0-9A-Za-z_\\-]*$`
Required: Yes

 ** [SyncType](#API_GetSyncConfiguration_RequestSyntax) **   <a name="codeconnections-GetSyncConfiguration-request-SyncType"></a>
The sync type for the sync configuration for which you want to retrieve information.
Type: String
Valid Values: `CFN_STACK_SYNC`
Required: Yes

## Response Syntax
<a name="API_GetSyncConfiguration_ResponseSyntax"></a>

```
{
   "SyncConfiguration": {
      "Branch": "string",
      "ConfigFile": "string",
      "OwnerId": "string",
      "ProviderType": "string",
      "PublishDeploymentStatus": "string",
      "PullRequestComment": "string",
      "RepositoryLinkId": "string",
      "RepositoryName": "string",
      "ResourceName": "string",
      "RoleArn": "string",
      "SyncType": "string",
      "TriggerResourceUpdateOn": "string"
   }
}
```

## Response Elements
<a name="API_GetSyncConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SyncConfiguration](#API_GetSyncConfiguration_ResponseSyntax) **   <a name="codeconnections-GetSyncConfiguration-response-SyncConfiguration"></a>
The details about the sync configuration for which you want to retrieve information.
Type: [SyncConfiguration](API_SyncConfiguration.md) object

## Errors
<a name="API_GetSyncConfiguration_Errors"></a>

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
<a name="API_GetSyncConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeconnections-2023-12-01/GetSyncConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeconnections-2023-12-01/GetSyncConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeconnections-2023-12-01/GetSyncConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeconnections-2023-12-01/GetSyncConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeconnections-2023-12-01/GetSyncConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeconnections-2023-12-01/GetSyncConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeconnections-2023-12-01/GetSyncConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeconnections-2023-12-01/GetSyncConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codeconnections-2023-12-01/GetSyncConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeconnections-2023-12-01/GetSyncConfiguration)

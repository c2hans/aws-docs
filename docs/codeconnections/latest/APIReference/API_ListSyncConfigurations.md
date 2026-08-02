---
source_url: https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_ListSyncConfigurations.html
---

# ListSyncConfigurations
<a name="API_ListSyncConfigurations"></a>

Returns a list of sync configurations for a specified repository.

## Request Syntax
<a name="API_ListSyncConfigurations_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "RepositoryLinkId": "{{string}}",
   "SyncType": "{{string}}"
}
```

## Request Parameters
<a name="API_ListSyncConfigurations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListSyncConfigurations_RequestSyntax) **   <a name="codeconnections-ListSyncConfigurations-request-MaxResults"></a>
A non-zero, non-negative integer used to limit the number of returned results.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListSyncConfigurations_RequestSyntax) **   <a name="codeconnections-ListSyncConfigurations-request-NextToken"></a>
An enumeration token that allows the operation to batch the results of the operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^.*$`
Required: No

 ** [RepositoryLinkId](#API_ListSyncConfigurations_RequestSyntax) **   <a name="codeconnections-ListSyncConfigurations-request-RepositoryLinkId"></a>
The ID of the repository link for the requested list of sync configurations.
Type: String
Pattern: `^[0-9a-fA-F]{8}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{12}$`
Required: Yes

 ** [SyncType](#API_ListSyncConfigurations_RequestSyntax) **   <a name="codeconnections-ListSyncConfigurations-request-SyncType"></a>
The sync type for the requested list of sync configurations.
Type: String
Valid Values: `CFN_STACK_SYNC`
Required: Yes

## Response Syntax
<a name="API_ListSyncConfigurations_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "SyncConfigurations": [
      {
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
   ]
}
```

## Response Elements
<a name="API_ListSyncConfigurations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListSyncConfigurations_ResponseSyntax) **   <a name="codeconnections-ListSyncConfigurations-response-NextToken"></a>
An enumeration token that allows the operation to batch the next results of the operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^.*$`

 ** [SyncConfigurations](#API_ListSyncConfigurations_ResponseSyntax) **   <a name="codeconnections-ListSyncConfigurations-response-SyncConfigurations"></a>
The list of repository sync definitions returned by the request.
Type: Array of [SyncConfiguration](API_SyncConfiguration.md) objects

## Errors
<a name="API_ListSyncConfigurations_Errors"></a>

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
<a name="API_ListSyncConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeconnections-2023-12-01/ListSyncConfigurations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeconnections-2023-12-01/ListSyncConfigurations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeconnections-2023-12-01/ListSyncConfigurations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeconnections-2023-12-01/ListSyncConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeconnections-2023-12-01/ListSyncConfigurations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeconnections-2023-12-01/ListSyncConfigurations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeconnections-2023-12-01/ListSyncConfigurations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeconnections-2023-12-01/ListSyncConfigurations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codeconnections-2023-12-01/ListSyncConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeconnections-2023-12-01/ListSyncConfigurations)

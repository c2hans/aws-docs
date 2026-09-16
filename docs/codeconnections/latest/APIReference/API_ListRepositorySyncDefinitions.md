---
source_url: https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_ListRepositorySyncDefinitions.html
---

# ListRepositorySyncDefinitions
<a name="API_ListRepositorySyncDefinitions"></a>

Lists the repository sync definitions for repository links in your account.

## Request Syntax
<a name="API_ListRepositorySyncDefinitions_RequestSyntax"></a>

```
{
   "RepositoryLinkId": "{{string}}",
   "SyncType": "{{string}}"
}
```

## Request Parameters
<a name="API_ListRepositorySyncDefinitions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [RepositoryLinkId](#API_ListRepositorySyncDefinitions_RequestSyntax) **   <a name="codeconnections-ListRepositorySyncDefinitions-request-RepositoryLinkId"></a>
The ID of the repository link for the sync definition for which you want to retrieve information.
Type: String
Pattern: `^[0-9a-fA-F]{8}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{12}$`
Required: Yes

 ** [SyncType](#API_ListRepositorySyncDefinitions_RequestSyntax) **   <a name="codeconnections-ListRepositorySyncDefinitions-request-SyncType"></a>
The sync type of the repository link for the the sync definition for which you want to retrieve information.
Type: String
Valid Values: `CFN_STACK_SYNC`
Required: Yes

## Response Syntax
<a name="API_ListRepositorySyncDefinitions_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "RepositorySyncDefinitions": [
      {
         "Branch": "string",
         "Directory": "string",
         "Parent": "string",
         "Target": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListRepositorySyncDefinitions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListRepositorySyncDefinitions_ResponseSyntax) **   <a name="codeconnections-ListRepositorySyncDefinitions-response-NextToken"></a>
An enumeration token that, when provided in a request, returns the next batch of the results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^.*$`

 ** [RepositorySyncDefinitions](#API_ListRepositorySyncDefinitions_ResponseSyntax) **   <a name="codeconnections-ListRepositorySyncDefinitions-response-RepositorySyncDefinitions"></a>
The list of repository sync definitions returned by the request. A `RepositorySyncDefinition` is a mapping from a repository branch to all the AWS resources that are being synced from that branch.
Type: Array of [RepositorySyncDefinition](API_RepositorySyncDefinition.md) objects

## Errors
<a name="API_ListRepositorySyncDefinitions_Errors"></a>

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
<a name="API_ListRepositorySyncDefinitions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeconnections-2023-12-01/ListRepositorySyncDefinitions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeconnections-2023-12-01/ListRepositorySyncDefinitions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeconnections-2023-12-01/ListRepositorySyncDefinitions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeconnections-2023-12-01/ListRepositorySyncDefinitions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeconnections-2023-12-01/ListRepositorySyncDefinitions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeconnections-2023-12-01/ListRepositorySyncDefinitions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeconnections-2023-12-01/ListRepositorySyncDefinitions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeconnections-2023-12-01/ListRepositorySyncDefinitions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codeconnections-2023-12-01/ListRepositorySyncDefinitions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeconnections-2023-12-01/ListRepositorySyncDefinitions)

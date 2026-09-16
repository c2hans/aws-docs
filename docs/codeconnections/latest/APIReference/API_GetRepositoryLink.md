---
source_url: https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_GetRepositoryLink.html
---

# GetRepositoryLink
<a name="API_GetRepositoryLink"></a>

Returns details about a repository link. A repository link allows Git sync to monitor and sync changes from files in a specified Git repository.

## Request Syntax
<a name="API_GetRepositoryLink_RequestSyntax"></a>

```
{
   "RepositoryLinkId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetRepositoryLink_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [RepositoryLinkId](#API_GetRepositoryLink_RequestSyntax) **   <a name="codeconnections-GetRepositoryLink-request-RepositoryLinkId"></a>
The ID of the repository link to get.
Type: String
Pattern: `^[0-9a-fA-F]{8}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{12}$`
Required: Yes

## Response Syntax
<a name="API_GetRepositoryLink_ResponseSyntax"></a>

```
{
   "RepositoryLinkInfo": {
      "ConnectionArn": "string",
      "EncryptionKeyArn": "string",
      "OwnerId": "string",
      "ProviderType": "string",
      "RepositoryLinkArn": "string",
      "RepositoryLinkId": "string",
      "RepositoryName": "string"
   }
}
```

## Response Elements
<a name="API_GetRepositoryLink_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RepositoryLinkInfo](#API_GetRepositoryLink_ResponseSyntax) **   <a name="codeconnections-GetRepositoryLink-response-RepositoryLinkInfo"></a>
The information returned for a specified repository link.
Type: [RepositoryLinkInfo](API_RepositoryLinkInfo.md) object

## Errors
<a name="API_GetRepositoryLink_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 400

 ** ConcurrentModificationException **
Exception thrown as a result of concurrent modification to an application. For example, two individuals attempting to edit the same application at the same time.
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
<a name="API_GetRepositoryLink_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeconnections-2023-12-01/GetRepositoryLink)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeconnections-2023-12-01/GetRepositoryLink)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeconnections-2023-12-01/GetRepositoryLink)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeconnections-2023-12-01/GetRepositoryLink)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeconnections-2023-12-01/GetRepositoryLink)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeconnections-2023-12-01/GetRepositoryLink)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeconnections-2023-12-01/GetRepositoryLink)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeconnections-2023-12-01/GetRepositoryLink)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codeconnections-2023-12-01/GetRepositoryLink)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeconnections-2023-12-01/GetRepositoryLink)

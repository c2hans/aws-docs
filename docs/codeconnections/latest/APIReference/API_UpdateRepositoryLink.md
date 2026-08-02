---
source_url: https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_UpdateRepositoryLink.html
---

# UpdateRepositoryLink
<a name="API_UpdateRepositoryLink"></a>

Updates the association between your connection and a specified external Git repository. A repository link allows Git sync to monitor and sync changes to files in a specified Git repository.

## Request Syntax
<a name="API_UpdateRepositoryLink_RequestSyntax"></a>

```
{
   "ConnectionArn": "{{string}}",
   "EncryptionKeyArn": "{{string}}",
   "RepositoryLinkId": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateRepositoryLink_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConnectionArn](#API_UpdateRepositoryLink_RequestSyntax) **   <a name="codeconnections-UpdateRepositoryLink-request-ConnectionArn"></a>
The Amazon Resource Name (ARN) of the connection for the repository link to be updated. The updated connection ARN must have the same providerType (such as GitHub) as the original connection ARN for the repo link.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws(-[\w]+)*:.+:.+:[0-9]{12}:.+`
Required: No

 ** [EncryptionKeyArn](#API_UpdateRepositoryLink_RequestSyntax) **   <a name="codeconnections-UpdateRepositoryLink-request-EncryptionKeyArn"></a>
The Amazon Resource Name (ARN) of the encryption key for the repository link to be updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:aws(-[\w]+)*:kms:[a-z\-0-9]+:\d{12}:key/[a-zA-Z0-9\-]+`
Required: No

 ** [RepositoryLinkId](#API_UpdateRepositoryLink_RequestSyntax) **   <a name="codeconnections-UpdateRepositoryLink-request-RepositoryLinkId"></a>
The ID of the repository link to be updated.
Type: String
Pattern: `^[0-9a-fA-F]{8}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{12}$`
Required: Yes

## Response Syntax
<a name="API_UpdateRepositoryLink_ResponseSyntax"></a>

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
<a name="API_UpdateRepositoryLink_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RepositoryLinkInfo](#API_UpdateRepositoryLink_ResponseSyntax) **   <a name="codeconnections-UpdateRepositoryLink-response-RepositoryLinkInfo"></a>
Information about the repository link to be updated.
Type: [RepositoryLinkInfo](API_RepositoryLinkInfo.md) object

## Errors
<a name="API_UpdateRepositoryLink_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 400

 ** ConditionalCheckFailedException **
The conditional check failed. Try again later.
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

 ** UpdateOutOfSyncException **
The update is out of sync. Try syncing again.
HTTP Status Code: 400

## See Also
<a name="API_UpdateRepositoryLink_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeconnections-2023-12-01/UpdateRepositoryLink)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeconnections-2023-12-01/UpdateRepositoryLink)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeconnections-2023-12-01/UpdateRepositoryLink)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeconnections-2023-12-01/UpdateRepositoryLink)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeconnections-2023-12-01/UpdateRepositoryLink)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeconnections-2023-12-01/UpdateRepositoryLink)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeconnections-2023-12-01/UpdateRepositoryLink)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeconnections-2023-12-01/UpdateRepositoryLink)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codeconnections-2023-12-01/UpdateRepositoryLink)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeconnections-2023-12-01/UpdateRepositoryLink)

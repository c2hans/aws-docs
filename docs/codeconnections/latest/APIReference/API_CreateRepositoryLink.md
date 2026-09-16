---
source_url: https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_CreateRepositoryLink.html
---

# CreateRepositoryLink
<a name="API_CreateRepositoryLink"></a>

Creates a link to a specified external Git repository. A repository link allows Git sync to monitor and sync changes to files in a specified Git repository.

## Request Syntax
<a name="API_CreateRepositoryLink_RequestSyntax"></a>

```
{
   "ConnectionArn": "{{string}}",
   "EncryptionKeyArn": "{{string}}",
   "OwnerId": "{{string}}",
   "RepositoryName": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateRepositoryLink_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConnectionArn](#API_CreateRepositoryLink_RequestSyntax) **   <a name="codeconnections-CreateRepositoryLink-request-ConnectionArn"></a>
The Amazon Resource Name (ARN) of the connection to be associated with the repository link.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws(-[\w]+)*:.+:.+:[0-9]{12}:.+`
Required: Yes

 ** [EncryptionKeyArn](#API_CreateRepositoryLink_RequestSyntax) **   <a name="codeconnections-CreateRepositoryLink-request-EncryptionKeyArn"></a>
The Amazon Resource Name (ARN) encryption key for the repository to be associated with the repository link.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:aws(-[\w]+)*:kms:[a-z\-0-9]+:\d{12}:key/[a-zA-Z0-9\-]+`
Required: No

 ** [OwnerId](#API_CreateRepositoryLink_RequestSyntax) **   <a name="codeconnections-CreateRepositoryLink-request-OwnerId"></a>
The owner ID for the repository associated with a specific sync configuration, such as the owner ID in GitHub.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^.*$`
Required: Yes

 ** [RepositoryName](#API_CreateRepositoryLink_RequestSyntax) **   <a name="codeconnections-CreateRepositoryLink-request-RepositoryName"></a>
The name of the repository to be associated with the repository link.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^.*$`
Required: Yes

 ** [Tags](#API_CreateRepositoryLink_RequestSyntax) **   <a name="codeconnections-CreateRepositoryLink-request-Tags"></a>
The tags for the repository to be associated with the repository link.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_CreateRepositoryLink_ResponseSyntax"></a>

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
<a name="API_CreateRepositoryLink_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RepositoryLinkInfo](#API_CreateRepositoryLink_ResponseSyntax) **   <a name="codeconnections-CreateRepositoryLink-response-RepositoryLinkInfo"></a>
The returned information about the created repository link.
Type: [RepositoryLinkInfo](API_RepositoryLinkInfo.md) object

## Errors
<a name="API_CreateRepositoryLink_Errors"></a>

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

 ** LimitExceededException **
Exceeded the maximum limit for connections.
HTTP Status Code: 400

 ** ResourceAlreadyExistsException **
Unable to create resource. Resource already exists.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

## See Also
<a name="API_CreateRepositoryLink_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeconnections-2023-12-01/CreateRepositoryLink)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeconnections-2023-12-01/CreateRepositoryLink)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeconnections-2023-12-01/CreateRepositoryLink)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeconnections-2023-12-01/CreateRepositoryLink)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeconnections-2023-12-01/CreateRepositoryLink)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeconnections-2023-12-01/CreateRepositoryLink)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeconnections-2023-12-01/CreateRepositoryLink)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeconnections-2023-12-01/CreateRepositoryLink)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codeconnections-2023-12-01/CreateRepositoryLink)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeconnections-2023-12-01/CreateRepositoryLink)

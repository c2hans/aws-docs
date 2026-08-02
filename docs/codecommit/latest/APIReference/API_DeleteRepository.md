---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_DeleteRepository.html
---

# DeleteRepository
<a name="API_DeleteRepository"></a>

Deletes a repository. If a specified repository was already deleted, a null repository ID is returned.

**Important**
Deleting a repository also deletes all associated objects and metadata. After a repository is deleted, all future push calls to the deleted repository fail.

## Request Syntax
<a name="API_DeleteRepository_RequestSyntax"></a>

```
{
   "repositoryName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteRepository_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [repositoryName](#API_DeleteRepository_RequestSyntax) **   <a name="CodeCommit-DeleteRepository-request-repositoryName"></a>
The name of the repository to delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\.-]+`
Required: Yes

## Response Syntax
<a name="API_DeleteRepository_ResponseSyntax"></a>

```
{
   "repositoryId": "string"
}
```

## Response Elements
<a name="API_DeleteRepository_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [repositoryId](#API_DeleteRepository_ResponseSyntax) **   <a name="CodeCommit-DeleteRepository-response-repositoryId"></a>
The ID of the repository that was deleted.
Type: String

## Errors
<a name="API_DeleteRepository_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** EncryptionIntegrityChecksFailedException **
An encryption integrity check failed.
HTTP Status Code: 500

 ** EncryptionKeyAccessDeniedException **
An encryption key could not be accessed.
HTTP Status Code: 400

 ** EncryptionKeyDisabledException **
The encryption key is disabled.
HTTP Status Code: 400

 ** EncryptionKeyNotFoundException **
No encryption key was found.
HTTP Status Code: 400

 ** EncryptionKeyUnavailableException **
The encryption key is not available.
HTTP Status Code: 400

 ** InvalidRepositoryNameException **
A specified repository name is not valid.
This exception occurs only when a specified repository name is not valid. Other exceptions occur when a required repository parameter is missing, or when a specified repository does not exist.
HTTP Status Code: 400

 ** RepositoryNameRequiredException **
A repository name is required, but was not specified.
HTTP Status Code: 400

## Examples
<a name="API_DeleteRepository_Examples"></a>

### Example
<a name="API_DeleteRepository_Example_1"></a>

This example illustrates one usage of DeleteRepository.

#### Sample Request
<a name="API_DeleteRepository_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codecommit.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 31
X-Amz-Target: CodeCommit_20150413.DeleteRepository
X-Amz-Date: 20151028T225354Z
User-Agent: aws-cli/1.7.38 Python/2.7.9 Windows/7
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20151028/us-east-1/codecommit/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
  "repositoryName": "MyDemoRepo"
}
```

#### Sample Response
<a name="API_DeleteRepository_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 0728aaa8-EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 55
Date: Wed, 28 Oct 2015 22:53:56 GMT

{
  "repositoryId": "f7579e13-b83e-4027-aaef-650c0EXAMPLE"
}
```

## See Also
<a name="API_DeleteRepository_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/DeleteRepository)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/DeleteRepository)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/DeleteRepository)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/DeleteRepository)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/DeleteRepository)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/DeleteRepository)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/DeleteRepository)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/DeleteRepository)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/DeleteRepository)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/DeleteRepository)

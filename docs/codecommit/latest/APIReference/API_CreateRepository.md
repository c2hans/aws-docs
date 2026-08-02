---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_CreateRepository.html
---

# CreateRepository
<a name="API_CreateRepository"></a>

Creates a new, empty repository.

## Request Syntax
<a name="API_CreateRepository_RequestSyntax"></a>

```
{
   "kmsKeyId": "{{string}}",
   "repositoryDescription": "{{string}}",
   "repositoryName": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreateRepository_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [kmsKeyId](#API_CreateRepository_RequestSyntax) **   <a name="CodeCommit-CreateRepository-request-kmsKeyId"></a>
The ID of the encryption key. You can view the ID of an encryption key in the AWS KMS console, or use the AWS KMS APIs to programmatically retrieve a key ID. For more information about acceptable values for kmsKeyID, see [KeyId](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html#KMS-Decrypt-request-KeyId) in the Decrypt API description in the * AWS Key Management Service API Reference*.
If no key is specified, the default `aws/codecommit` AWS managed key is used.
Type: String
Pattern: `^[a-zA-Z0-9:/_-]+$`
Required: No

 ** [repositoryDescription](#API_CreateRepository_RequestSyntax) **   <a name="CodeCommit-CreateRepository-request-repositoryDescription"></a>
A comment or description about the new repository.
The description field for a repository accepts all HTML characters and all valid Unicode characters. Applications that do not HTML-encode the description and display it in a webpage can expose users to potentially malicious code. Make sure that you HTML-encode the description field in any application that uses this API to display the repository description on a webpage.
Type: String
Length Constraints: Maximum length of 1000.
Required: No

 ** [repositoryName](#API_CreateRepository_RequestSyntax) **   <a name="CodeCommit-CreateRepository-request-repositoryName"></a>
The name of the new repository to be created.
The repository name must be unique across the calling AWS account. Repository names are limited to 100 alphanumeric, dash, and underscore characters, and cannot include certain characters. For more information about the limits on repository names, see [Quotas](https://docs.aws.amazon.com/codecommit/latest/userguide/limits.html) in the * AWS CodeCommit User Guide*. The suffix .git is prohibited.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\.-]+`
Required: Yes

 ** [tags](#API_CreateRepository_RequestSyntax) **   <a name="CodeCommit-CreateRepository-request-tags"></a>
One or more tag key-value pairs to use when tagging this repository.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateRepository_ResponseSyntax"></a>

```
{
   "repositoryMetadata": {
      "accountId": "string",
      "Arn": "string",
      "cloneUrlHttp": "string",
      "cloneUrlSsh": "string",
      "creationDate": number,
      "defaultBranch": "string",
      "kmsKeyId": "string",
      "lastModifiedDate": number,
      "repositoryDescription": "string",
      "repositoryId": "string",
      "repositoryName": "string"
   }
}
```

## Response Elements
<a name="API_CreateRepository_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [repositoryMetadata](#API_CreateRepository_ResponseSyntax) **   <a name="CodeCommit-CreateRepository-response-repositoryMetadata"></a>
Information about the newly created repository.
Type: [RepositoryMetadata](API_RepositoryMetadata.md) object

## Errors
<a name="API_CreateRepository_Errors"></a>

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

 ** EncryptionKeyInvalidIdException **
The AWS Key Management Service encryption key is not valid.
HTTP Status Code: 400

 ** EncryptionKeyInvalidUsageException **
A AWS KMS encryption key was used to try and encrypt or decrypt a repository, but either the repository or the key was not in a valid state to support the operation.
HTTP Status Code: 400

 ** EncryptionKeyNotFoundException **
No encryption key was found.
HTTP Status Code: 400

 ** EncryptionKeyUnavailableException **
The encryption key is not available.
HTTP Status Code: 400

 ** InvalidRepositoryDescriptionException **
The specified repository description is not valid.
HTTP Status Code: 400

 ** InvalidRepositoryNameException **
A specified repository name is not valid.
This exception occurs only when a specified repository name is not valid. Other exceptions occur when a required repository parameter is missing, or when a specified repository does not exist.
HTTP Status Code: 400

 ** InvalidSystemTagUsageException **
The specified tag is not valid. Key names cannot be prefixed with aws:.
HTTP Status Code: 400

 ** InvalidTagsMapException **
The map of tags is not valid.
HTTP Status Code: 400

 ** OperationNotAllowedException **
Thrown when request is denied due to other reason than lack of permission.
HTTP Status Code: 400

 ** RepositoryLimitExceededException **
A repository resource limit was exceeded.
HTTP Status Code: 400

 ** RepositoryNameExistsException **
The specified repository name already exists.
HTTP Status Code: 400

 ** RepositoryNameRequiredException **
A repository name is required, but was not specified.
HTTP Status Code: 400

 ** TagPolicyException **
The tag policy is not valid.
HTTP Status Code: 400

 ** TooManyTagsException **
The maximum number of tags for an AWS CodeCommit resource has been exceeded.
HTTP Status Code: 400

## Examples
<a name="API_CreateRepository_Examples"></a>

### Example
<a name="API_CreateRepository_Example_1"></a>

This example illustrates one usage of CreateRepository.

#### Sample Request
<a name="API_CreateRepository_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codecommit.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 88
X-Amz-Target: CodeCommit_20150413.CreateRepository
X-Amz-Date: 20151028T223339Z
User-Agent: aws-cli/1.7.38 Python/2.7.9 Windows/7
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20151028/us-east-1/codecommit/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
  "repositoryName": "MyDemoRepo",
  "repositoryDescription": "My demonstration repository",
  "tags": {
    "Team":"Saanvi"
  }
}
```

#### Sample Response
<a name="API_CreateRepository_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 0728aaa8-EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 483
Date: Wed, 28 Oct 2015 22:33:42 GMT

{
    "repositoryMetadata": {
        "repositoryName": "MyDemoRepo",
        "cloneUrlSsh": "ssh://git-codecommit.us-east-1.amazonaws.com/v1/repos/MyDemoRepo",
        "lastModifiedDate": 1446071622.494,
        "repositoryDescription": "My demonstration repository",
        "cloneUrlHttp": "https://git-codecommit.us-east-1.amazonaws.com/v1/repos/MyDemoRepo",
        "defaultBranch": main,
        "kmsKeyId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "creationDate": 1446071622.494,
        "repositoryId": "a1b2c3d4-5678-90ab-cdef-EXAMPLEbbbbb",
        "Arn": "arn:aws:codecommit:us-east-1:123456789012EXAMPLE:MyDemoRepo",
        "accountId": "123456789012"
    }
}
```

## See Also
<a name="API_CreateRepository_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/CreateRepository)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/CreateRepository)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/CreateRepository)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/CreateRepository)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/CreateRepository)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/CreateRepository)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/CreateRepository)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/CreateRepository)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/CreateRepository)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/CreateRepository)

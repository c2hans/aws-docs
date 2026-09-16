---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_UpdateRepositoryEncryptionKey.html
---

# UpdateRepositoryEncryptionKey
<a name="API_UpdateRepositoryEncryptionKey"></a>

Updates the AWS Key Management Service encryption key used to encrypt and decrypt a CodeCommit repository.

## Request Syntax
<a name="API_UpdateRepositoryEncryptionKey_RequestSyntax"></a>

```
{
   "kmsKeyId": "{{string}}",
   "repositoryName": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateRepositoryEncryptionKey_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [kmsKeyId](#API_UpdateRepositoryEncryptionKey_RequestSyntax) **   <a name="CodeCommit-UpdateRepositoryEncryptionKey-request-kmsKeyId"></a>
The ID of the encryption key. You can view the ID of an encryption key in the AWS KMS console, or use the AWS KMS APIs to programmatically retrieve a key ID. For more information about acceptable values for keyID, see [KeyId](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html#KMS-Decrypt-request-KeyId) in the Decrypt API description in the * AWS Key Management Service API Reference*.
Type: String
Pattern: `^[a-zA-Z0-9:/_-]+$`
Required: Yes

 ** [repositoryName](#API_UpdateRepositoryEncryptionKey_RequestSyntax) **   <a name="CodeCommit-UpdateRepositoryEncryptionKey-request-repositoryName"></a>
The name of the repository for which you want to update the AWS KMS encryption key used to encrypt and decrypt the repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\.-]+`
Required: Yes

## Response Syntax
<a name="API_UpdateRepositoryEncryptionKey_ResponseSyntax"></a>

```
{
   "kmsKeyId": "string",
   "originalKmsKeyId": "string",
   "repositoryId": "string"
}
```

## Response Elements
<a name="API_UpdateRepositoryEncryptionKey_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [kmsKeyId](#API_UpdateRepositoryEncryptionKey_ResponseSyntax) **   <a name="CodeCommit-UpdateRepositoryEncryptionKey-response-kmsKeyId"></a>
The ID of the encryption key.
Type: String
Pattern: `^[a-zA-Z0-9:/_-]+$`

 ** [originalKmsKeyId](#API_UpdateRepositoryEncryptionKey_ResponseSyntax) **   <a name="CodeCommit-UpdateRepositoryEncryptionKey-response-originalKmsKeyId"></a>
The ID of the encryption key formerly used to encrypt and decrypt the repository.
Type: String
Pattern: `^[a-zA-Z0-9:/_-]+$`

 ** [repositoryId](#API_UpdateRepositoryEncryptionKey_ResponseSyntax) **   <a name="CodeCommit-UpdateRepositoryEncryptionKey-response-repositoryId"></a>
The ID of the repository.
Type: String

## Errors
<a name="API_UpdateRepositoryEncryptionKey_Errors"></a>

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

 ** EncryptionKeyRequiredException **
A AWS KMS encryption key ID is required but was not specified.
HTTP Status Code: 400

 ** EncryptionKeyUnavailableException **
The encryption key is not available.
HTTP Status Code: 400

 ** InvalidRepositoryNameException **
A specified repository name is not valid.
This exception occurs only when a specified repository name is not valid. Other exceptions occur when a required repository parameter is missing, or when a specified repository does not exist.
HTTP Status Code: 400

 ** RepositoryDoesNotExistException **
The specified repository does not exist.
HTTP Status Code: 400

 ** RepositoryNameRequiredException **
A repository name is required, but was not specified.
HTTP Status Code: 400

## Examples
<a name="API_UpdateRepositoryEncryptionKey_Examples"></a>

### Example
<a name="API_UpdateRepositoryEncryptionKey_Example_1"></a>

The following example updates a repository named *MyDemoRepo* to use a AWS KMS key with the ID of *a1b2c3d4-5678-90ab-cdef-EXAMPLE11111*.

#### Sample Request
<a name="API_UpdateRepositoryEncryptionKey_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codecommit.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 79
X-Amz-Target: CodeCommit_20150413.UpdateRepositoryEncryptionKey
X-Amz-Date: 20231221T153512Z
User-Agent: aws-cli/1.32.0 Python/3.6.0 Windows/10
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20151029/us-east-1/codecommit/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
  "kmsKeyId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
  "repositoryName": "MyDemoRepo"
}
```

#### Sample Response
<a name="API_UpdateRepositoryEncryptionKey_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 0728aaa8-EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 0
Date: Thu, 21 Dec 2023 15:35:13 GMT

 {
  "kmsKeyId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
  "originalKmsKeyId": "a1b2c3d4-5678-90ab-cdef-EXAMPLEaaaaa",
  "repositoryName": "MyDemoRepo"
}
```

## See Also
<a name="API_UpdateRepositoryEncryptionKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/UpdateRepositoryEncryptionKey)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/UpdateRepositoryEncryptionKey)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/UpdateRepositoryEncryptionKey)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/UpdateRepositoryEncryptionKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/UpdateRepositoryEncryptionKey)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/UpdateRepositoryEncryptionKey)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/UpdateRepositoryEncryptionKey)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/UpdateRepositoryEncryptionKey)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/UpdateRepositoryEncryptionKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/UpdateRepositoryEncryptionKey)

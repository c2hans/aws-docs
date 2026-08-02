---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_UpdateDefaultBranch.html
---

# UpdateDefaultBranch
<a name="API_UpdateDefaultBranch"></a>

Sets or changes the default branch name for the specified repository.

**Note**
If you use this operation to change the default branch name to the current default branch name, a success message is returned even though the default branch did not change.

## Request Syntax
<a name="API_UpdateDefaultBranch_RequestSyntax"></a>

```
{
   "defaultBranchName": "{{string}}",
   "repositoryName": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateDefaultBranch_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [defaultBranchName](#API_UpdateDefaultBranch_RequestSyntax) **   <a name="CodeCommit-UpdateDefaultBranch-request-defaultBranchName"></a>
The name of the branch to set as the default branch.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [repositoryName](#API_UpdateDefaultBranch_RequestSyntax) **   <a name="CodeCommit-UpdateDefaultBranch-request-repositoryName"></a>
The name of the repository for which you want to set or change the default branch.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\.-]+`
Required: Yes

## Response Elements
<a name="API_UpdateDefaultBranch_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateDefaultBranch_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BranchDoesNotExistException **
The specified branch does not exist.
HTTP Status Code: 400

 ** BranchNameRequiredException **
A branch name is required, but was not specified.
HTTP Status Code: 400

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

 ** InvalidBranchNameException **
The specified reference name is not valid.
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
<a name="API_UpdateDefaultBranch_Examples"></a>

### Example
<a name="API_UpdateDefaultBranch_Example_1"></a>

This example illustrates one usage of UpdateDefaultBranch.

#### Sample Request
<a name="API_UpdateDefaultBranch_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codecommit.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 71
X-Amz-Target: CodeCommit_20150413.UpdateDefaultBranch
X-Amz-Date: 20151029T151143Z
User-Agent: aws-cli/1.7.38 Python/2.7.9 Windows/7
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20151029/us-east-1/codecommit/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
  "defaultBranchName": "MyNewBranch",
  "repositoryName": "MyDemoRepo"
}
```

#### Sample Response
<a name="API_UpdateDefaultBranch_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 0728aaa8-EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 0
Date: Thu, 29 Oct 2015 15:11:44 GMT
```

## See Also
<a name="API_UpdateDefaultBranch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/UpdateDefaultBranch)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/UpdateDefaultBranch)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/UpdateDefaultBranch)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/UpdateDefaultBranch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/UpdateDefaultBranch)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/UpdateDefaultBranch)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/UpdateDefaultBranch)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/UpdateDefaultBranch)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/UpdateDefaultBranch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/UpdateDefaultBranch)

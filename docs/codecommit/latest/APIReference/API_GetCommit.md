---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_GetCommit.html
---

# GetCommit
<a name="API_GetCommit"></a>

Returns information about a commit, including commit message and committer information.

## Request Syntax
<a name="API_GetCommit_RequestSyntax"></a>

```
{
   "commitId": "{{string}}",
   "repositoryName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetCommit_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [commitId](#API_GetCommit_RequestSyntax) **   <a name="CodeCommit-GetCommit-request-commitId"></a>
The commit ID. Commit IDs are the full SHA ID of the commit.
Type: String
Required: Yes

 ** [repositoryName](#API_GetCommit_RequestSyntax) **   <a name="CodeCommit-GetCommit-request-repositoryName"></a>
The name of the repository to which the commit was made.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\.-]+`
Required: Yes

## Response Syntax
<a name="API_GetCommit_ResponseSyntax"></a>

```
{
   "commit": {
      "additionalData": "string",
      "author": {
         "date": "string",
         "email": "string",
         "name": "string"
      },
      "commitId": "string",
      "committer": {
         "date": "string",
         "email": "string",
         "name": "string"
      },
      "message": "string",
      "parents": [ "string" ],
      "treeId": "string"
   }
}
```

## Response Elements
<a name="API_GetCommit_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [commit](#API_GetCommit_ResponseSyntax) **   <a name="CodeCommit-GetCommit-response-commit"></a>
A commit data type object that contains information about the specified commit.
Type: [Commit](API_Commit.md) object

## Errors
<a name="API_GetCommit_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CommitIdDoesNotExistException **
The specified commit ID does not exist.
HTTP Status Code: 400

 ** CommitIdRequiredException **
A commit ID was not specified.
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

 ** InvalidCommitIdException **
The specified commit ID is not valid.
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
<a name="API_GetCommit_Examples"></a>

### Example
<a name="API_GetCommit_Example_1"></a>

This example illustrates one usage of GetCommit.

#### Sample Request
<a name="API_GetCommit_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codecommit.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 57
X-Amz-Target: CodeCommit_20150413.GetCommit
X-Amz-Date: 20170111T224311Z
User-Agent: aws-cli/1.11.187 Python/2.7.9 Windows/7
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20151028/us-east-1/codecommit/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
  "repositoryName": "MyDemoRepo",
  "commitId": "12345678EXAMPLE"
}
```

#### Sample Response
<a name="API_GetCommit_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 0728aaa8-EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 720
Date: Wed, 11 Jan 2017 22:43:13 GMT

{
    "commit": {
        "commitId": "12345678EXAMPLE",
        "additionalData": "",
        "committer": {
            "date": "1484167798 -0800",
            "name": "Mary Major",
            "email": "mary_major@example.com"
        },
        "author": {
            "date": "1484167798 -0800",
            "name": "Mary Major",
            "email": "mary_major@example.com"
        },
        "treeId": "347a3408EXAMPLE",
        "parents": [
            "7aa87a0EXAMPLE"
        ],
        "message": "Fix incorrect variable name\n"
    }
}
```

## See Also
<a name="API_GetCommit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/GetCommit)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/GetCommit)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/GetCommit)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/GetCommit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/GetCommit)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/GetCommit)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/GetCommit)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/GetCommit)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/GetCommit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/GetCommit)

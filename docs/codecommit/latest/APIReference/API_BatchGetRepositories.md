---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_BatchGetRepositories.html
---

# BatchGetRepositories
<a name="API_BatchGetRepositories"></a>

Returns information about one or more repositories.

**Note**
The description field for a repository accepts all HTML characters and all valid Unicode characters. Applications that do not HTML-encode the description and display it in a webpage can expose users to potentially malicious code. Make sure that you HTML-encode the description field in any application that uses this API to display the repository description on a webpage.

## Request Syntax
<a name="API_BatchGetRepositories_RequestSyntax"></a>

```
{
   "repositoryNames": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_BatchGetRepositories_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [repositoryNames](#API_BatchGetRepositories_RequestSyntax) **   <a name="CodeCommit-BatchGetRepositories-request-repositoryNames"></a>
The names of the repositories to get information about.
The length constraint limit is for each string in the array. The array itself can be empty.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\.-]+`
Required: Yes

## Response Syntax
<a name="API_BatchGetRepositories_ResponseSyntax"></a>

```
{
   "errors": [
      {
         "errorCode": "string",
         "errorMessage": "string",
         "repositoryId": "string",
         "repositoryName": "string"
      }
   ],
   "repositories": [
      {
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
   ],
   "repositoriesNotFound": [ "string" ]
}
```

## Response Elements
<a name="API_BatchGetRepositories_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errors](#API_BatchGetRepositories_ResponseSyntax) **   <a name="CodeCommit-BatchGetRepositories-response-errors"></a>
Returns information about any errors returned when attempting to retrieve information about the repositories.
Type: Array of [BatchGetRepositoriesError](API_BatchGetRepositoriesError.md) objects

 ** [repositories](#API_BatchGetRepositories_ResponseSyntax) **   <a name="CodeCommit-BatchGetRepositories-response-repositories"></a>
A list of repositories returned by the batch get repositories operation.
Type: Array of [RepositoryMetadata](API_RepositoryMetadata.md) objects

 ** [repositoriesNotFound](#API_BatchGetRepositories_ResponseSyntax) **   <a name="CodeCommit-BatchGetRepositories-response-repositoriesNotFound"></a>
Returns a list of repository names for which information could not be found.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\.-]+`

## Errors
<a name="API_BatchGetRepositories_Errors"></a>

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

 ** MaximumRepositoryNamesExceededException **
The maximum number of allowed repository names was exceeded. Currently, this number is 100.
HTTP Status Code: 400

 ** RepositoryNamesRequiredException **
At least one repository name object is required, but was not specified.
HTTP Status Code: 400

## Examples
<a name="API_BatchGetRepositories_Examples"></a>

### Example
<a name="API_BatchGetRepositories_Example_1"></a>

This example illustrates one usage of BatchGetRepositories.

#### Sample Request
<a name="API_BatchGetRepositories_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codecommit.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 50
X-Amz-Target: CodeCommit_20150413.BatchGetRepositories
X-Amz-Date: 20151028T213222Z
User-Agent: aws-cli/1.7.38 Python/2.7.9 Windows/7
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20151028/us-east-1/codecommit/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
  "repositoryNames": [
    "MyDemoRepo",
	"MyOtherDemoRepo"
  ]
}
```

#### Sample Response
<a name="API_BatchGetRepositories_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 0728aaa8-EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 550
Date: Wed, 28 Oct 2015 21:32:24 GMT

{
    "repositories": [
        {
            "repositoryName": "MyDemoRepo",
			"defaultBranch": "main",
            "cloneUrlSsh": "ssh://git-codecommit.us-east-1.amazonaws.com/v1/repos/MyDemoRepo",
            "lastModifiedDate": 1441725693.583,
            "repositoryDescription": "My demonstration repository",
            "cloneUrlHttp": "https://git-codecommit.us-east-1.amazonaws.com/v1/repos/MyDemoRepo",
            "defaultBranch": "main",
            "kmsKeyId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "creationDate": 1441725693.583,
            "repositoryId": "f7579e13-b83e-4027-aaef-650c0EXAMPLE",
            "Arn": "arn:aws:codecommit:us-east-1:123456789012EXAMPLE:MyDemoRepo",
            "accountId": "123456789012"
        },
        {
            "creationDate": 1431980067.669,
            "defaultBranch": "main",
            "repositoryName": "MyOtherDemoRepo",
            "cloneUrlSsh": "ssh://git-codecommit.us-east-1.amazonaws.com/v1/repos/MyOtherDemoRepo",
            "lastModifiedDate": 1444776815.847,
            "repositoryDescription": "My other demonstration repository",
            "cloneUrlHttp": "https://git-codecommit.us-east-1.amazonaws.com/v1/repos/MyOtherDemoRepo",
            "defaultBranch": "release",
            "kmsKeyId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
            "repositoryId": "cfc29ac4-b0cb-44dc-9990-f6f51EXAMPLE",
            "Arn": "arn:aws:codecommit:us-east-1:123456789012EXAMPLE:MyOtherDemoRepo",
            "accountId": "123456789012"
        }
    ],
    "repositoriesNotFound": []
}
```

## See Also
<a name="API_BatchGetRepositories_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/BatchGetRepositories)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/BatchGetRepositories)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/BatchGetRepositories)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/BatchGetRepositories)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/BatchGetRepositories)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/BatchGetRepositories)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/BatchGetRepositories)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/BatchGetRepositories)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/BatchGetRepositories)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/BatchGetRepositories)

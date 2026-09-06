---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_GetFile.html
---

# GetFile
<a name="API_GetFile"></a>

Returns the base-64 encoded contents of a specified file and its metadata.

## Request Syntax
<a name="API_GetFile_RequestSyntax"></a>

```
{
   "commitSpecifier": "{{string}}",
   "filePath": "{{string}}",
   "repositoryName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetFile_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [commitSpecifier](#API_GetFile_RequestSyntax) **   <a name="CodeCommit-GetFile-request-commitSpecifier"></a>
The fully quaified reference that identifies the commit that contains the file. For example, you can specify a full commit ID, a tag, a branch name, or a reference such as refs/heads/main. If none is provided, the head commit is used.
Type: String
Required: No

 ** [filePath](#API_GetFile_RequestSyntax) **   <a name="CodeCommit-GetFile-request-filePath"></a>
The fully qualified path to the file, including the full name and extension of the file. For example, /examples/file.md is the fully qualified path to a file named file.md in a folder named examples.
Type: String
Required: Yes

 ** [repositoryName](#API_GetFile_RequestSyntax) **   <a name="CodeCommit-GetFile-request-repositoryName"></a>
The name of the repository that contains the file.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\.-]+`
Required: Yes

## Response Syntax
<a name="API_GetFile_ResponseSyntax"></a>

```
{
   "blobId": "string",
   "commitId": "string",
   "fileContent": blob,
   "fileMode": "string",
   "filePath": "string",
   "fileSize": number
}
```

## Response Elements
<a name="API_GetFile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [blobId](#API_GetFile_ResponseSyntax) **   <a name="CodeCommit-GetFile-response-blobId"></a>
The blob ID of the object that represents the file content.
Type: String

 ** [commitId](#API_GetFile_ResponseSyntax) **   <a name="CodeCommit-GetFile-response-commitId"></a>
The full commit ID of the commit that contains the content returned by GetFile.
Type: String

 ** [fileContent](#API_GetFile_ResponseSyntax) **   <a name="CodeCommit-GetFile-response-fileContent"></a>
The base-64 encoded binary data object that represents the content of the file.
Type: Base64-encoded binary data object
Length Constraints: Maximum length of 6291456.

 ** [fileMode](#API_GetFile_ResponseSyntax) **   <a name="CodeCommit-GetFile-response-fileMode"></a>
The extrapolated file mode permissions of the blob. Valid values include strings such as EXECUTABLE and not numeric values.
The file mode permissions returned by this API are not the standard file mode permission values, such as 100644, but rather extrapolated values. See the supported return values.
Type: String
Valid Values: `EXECUTABLE | NORMAL | SYMLINK`

 ** [filePath](#API_GetFile_ResponseSyntax) **   <a name="CodeCommit-GetFile-response-filePath"></a>
The fully qualified path to the specified file. Returns the name and extension of the file.
Type: String

 ** [fileSize](#API_GetFile_ResponseSyntax) **   <a name="CodeCommit-GetFile-response-fileSize"></a>
The size of the contents of the file, in bytes.
Type: Long

## Errors
<a name="API_GetFile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CommitDoesNotExistException **
The specified commit does not exist or no commit was specified, and the specified repository has no default branch.
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

 ** FileDoesNotExistException **
The specified file does not exist. Verify that you have used the correct file name, full path, and extension.
HTTP Status Code: 400

 ** FileTooLargeException **
The specified file exceeds the file size limit for AWS CodeCommit. For more information about limits in AWS CodeCommit, see [Quotas](https://docs.aws.amazon.com/codecommit/latest/userguide/limits.html) in the * AWS CodeCommit User Guide*.
HTTP Status Code: 400

 ** InvalidCommitException **
The specified commit is not valid.
HTTP Status Code: 400

 ** InvalidPathException **
The specified path is not valid.
HTTP Status Code: 400

 ** InvalidRepositoryNameException **
A specified repository name is not valid.
This exception occurs only when a specified repository name is not valid. Other exceptions occur when a required repository parameter is missing, or when a specified repository does not exist.
HTTP Status Code: 400

 ** PathRequiredException **
The folderPath for a location cannot be null.
HTTP Status Code: 400

 ** RepositoryDoesNotExistException **
The specified repository does not exist.
HTTP Status Code: 400

 ** RepositoryNameRequiredException **
A repository name is required, but was not specified.
HTTP Status Code: 400

## Examples
<a name="API_GetFile_Examples"></a>

### Example
<a name="API_GetFile_Example_1"></a>

This example illustrates one usage of GetFile.

#### Sample Request
<a name="API_GetFile_Example_1_Request"></a>

```
POST / HTTP/1.1
    Host: codecommit.us-east-1.amazonaws.com
    Accept-Encoding: identity
    Content-Length: 124
    X-Amz-Target: CodeCommit_20150413.GetFile
    X-Amz-Date: 20180914T223055Z
    User-Agent: aws-cli/1.15.9 Python/2.7.11 Darwin/16.7.0 botocore/1.10.9
    Content-Type: application/x-amz-json-1.1
    Authorization: AWS4-HMAC-SHA256 Credential=AKIAEXAMPLE/20180914/us-east-1/codecommit/aws4_request, SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature==8d9b5998EXAMPLE
{
   "commitSpecifier": "main",
   "repositoryName": "MyDemoRepo",
   "filePath": "README.md"
}
```

#### Sample Response
<a name="API_GetFile_Example_1_Response"></a>

```
HTTP/1.1 200 OK
    x-amzn-RequestId: d8ad1d21-EXAMPLE
    Content-Type: application/x-amz-json-1.1
    Content-Length: 2267
    Date: Fri, 14 Sep 2018 22:30:56 GMT
    Connection: keep-alive

{
    "blobId":"559b44fEXAMPLE",
    "commitId":"c5709475EXAMPLE",
    "fileContent":"IyBQaHVzEXAMPLE",
    "filePath":"README.md",
    "fileSize":1563
    "fileMode":"NORMAL"
}
```

## See Also
<a name="API_GetFile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/GetFile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/GetFile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/GetFile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/GetFile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/GetFile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/GetFile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/GetFile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/GetFile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/GetFile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/GetFile)

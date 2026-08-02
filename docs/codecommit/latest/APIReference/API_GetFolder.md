---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_GetFolder.html
---

# GetFolder
<a name="API_GetFolder"></a>

Returns the contents of a specified folder in a repository.

## Request Syntax
<a name="API_GetFolder_RequestSyntax"></a>

```
{
   "commitSpecifier": "{{string}}",
   "folderPath": "{{string}}",
   "repositoryName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetFolder_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [commitSpecifier](#API_GetFolder_RequestSyntax) **   <a name="CodeCommit-GetFolder-request-commitSpecifier"></a>
A fully qualified reference used to identify a commit that contains the version of the folder's content to return. A fully qualified reference can be a commit ID, branch name, tag, or reference such as HEAD. If no specifier is provided, the folder content is returned as it exists in the HEAD commit.
Type: String
Required: No

 ** [folderPath](#API_GetFolder_RequestSyntax) **   <a name="CodeCommit-GetFolder-request-folderPath"></a>
The fully qualified path to the folder whose contents are returned, including the folder name. For example, /examples is a fully-qualified path to a folder named examples that was created off of the root directory (/) of a repository.
Type: String
Required: Yes

 ** [repositoryName](#API_GetFolder_RequestSyntax) **   <a name="CodeCommit-GetFolder-request-repositoryName"></a>
The name of the repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\.-]+`
Required: Yes

## Response Syntax
<a name="API_GetFolder_ResponseSyntax"></a>

```
{
   "commitId": "string",
   "files": [
      {
         "absolutePath": "string",
         "blobId": "string",
         "fileMode": "string",
         "relativePath": "string"
      }
   ],
   "folderPath": "string",
   "subFolders": [
      {
         "absolutePath": "string",
         "relativePath": "string",
         "treeId": "string"
      }
   ],
   "subModules": [
      {
         "absolutePath": "string",
         "commitId": "string",
         "relativePath": "string"
      }
   ],
   "symbolicLinks": [
      {
         "absolutePath": "string",
         "blobId": "string",
         "fileMode": "string",
         "relativePath": "string"
      }
   ],
   "treeId": "string"
}
```

## Response Elements
<a name="API_GetFolder_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [commitId](#API_GetFolder_ResponseSyntax) **   <a name="CodeCommit-GetFolder-response-commitId"></a>
The full commit ID used as a reference for the returned version of the folder content.
Type: String

 ** [files](#API_GetFolder_ResponseSyntax) **   <a name="CodeCommit-GetFolder-response-files"></a>
The list of files in the specified folder, if any.
Type: Array of [File](API_File.md) objects

 ** [folderPath](#API_GetFolder_ResponseSyntax) **   <a name="CodeCommit-GetFolder-response-folderPath"></a>
The fully qualified path of the folder whose contents are returned.
Type: String

 ** [subFolders](#API_GetFolder_ResponseSyntax) **   <a name="CodeCommit-GetFolder-response-subFolders"></a>
The list of folders that exist under the specified folder, if any.
Type: Array of [Folder](API_Folder.md) objects

 ** [subModules](#API_GetFolder_ResponseSyntax) **   <a name="CodeCommit-GetFolder-response-subModules"></a>
The list of submodules in the specified folder, if any.
Type: Array of [SubModule](API_SubModule.md) objects

 ** [symbolicLinks](#API_GetFolder_ResponseSyntax) **   <a name="CodeCommit-GetFolder-response-symbolicLinks"></a>
The list of symbolic links to other files and folders in the specified folder, if any.
Type: Array of [SymbolicLink](API_SymbolicLink.md) objects

 ** [treeId](#API_GetFolder_ResponseSyntax) **   <a name="CodeCommit-GetFolder-response-treeId"></a>
The full SHA-1 pointer of the tree information for the commit that contains the folder.
Type: String

## Errors
<a name="API_GetFolder_Errors"></a>

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

 ** FolderDoesNotExistException **
The specified folder does not exist. Either the folder name is not correct, or you did not enter the full path to the folder.
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
<a name="API_GetFolder_Examples"></a>

### Example
<a name="API_GetFolder_Example_1"></a>

This example illustrates one usage of GetFolder.

#### Sample Request
<a name="API_GetFolder_Example_1_Request"></a>

```
POST / HTTP/1.1
    Host: codecommit.us-east-1.amazonaws.com
    Accept-Encoding: identity
    Content-Length: 88
    X-Amz-Target: CodeCommit_20150413.GetFolder
    X-Amz-Date: 20180914T222143Z
    User-Agent: aws-cli/1.15.9 Python/2.7.11 Darwin/16.7.0 botocore/1.10.9
    Content-Type: application/x-amz-json-1.1
    Authorization: AWS4-HMAC-SHA256 Credential=AKIAEXAMPLE/20180914/us-east-1/codecommit/aws4_request, SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=0bcf747dEXAMPLE

{
    "folderPath": "",
    "repositoryName": "MyDemoRepo"
}
```

#### Sample Response
<a name="API_GetFolder_Example_1_Response"></a>

```
HTTP/1.1 200 OK
    x-amzn-RequestId: 8f9d4f13-EXAMPLE
    Content-Type: application/x-amz-json-1.1
    Content-Length: 1157
    Date: Fri, 14 Sep 2018 22:21:44 GMT
    Connection: keep-alive

{
    "commitId":"c5709475EXAMPLE",
    "files":[
        {
          "absolutePath":".gitignore",
          "blobId":"74094e8bEXAMPLE",
          "fileMode":"NORMAL",
          "relativePath":".gitignore"
        },
        {
          "absolutePath":"Gemfile",
          "blobId":"9ceb72f6EXAMPLE",
          "fileMode":"NORMAL",
          "relativePath":"Gemfile"
        },
        {
          "absolutePath":"Gemfile.lock",
          "blobId":"795c4a2aEXAMPLE",
          "fileMode":"NORMAL",
          "relativePath":"Gemfile.lock"
        },
        {
          "absolutePath":"LICENSE.txt",
          "blobId":"0c7932c8EXAMPLE",
          "fileMode":"NORMAL",
          "relativePath":"LICENSE.txt"
        },
        {
          "absolutePath":"README.md",
          "blobId":"559b44feEXAMPLE",
          "fileMode":"NORMAL",
          "relativePath":"README.md"
        }
    ],
    "folderPath":"",
    "subFolders":[
        {
          "absolutePath":"public",
          "relativePath":"public",
          "treeId":"d5e92ae3aEXAMPLE"
        },
        {
          "absolutePath":"tmp",
          "relativePath":"tmp",
          "treeId":"d564d0bcEXAMPLE"
        }
    ],
    "subModules":[],
    "symbolicLinks":[],
    "treeId":"7b3c4dadEXAMPLE"
}
```

## See Also
<a name="API_GetFolder_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/GetFolder)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/GetFolder)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/GetFolder)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/GetFolder)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/GetFolder)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/GetFolder)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/GetFolder)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/GetFolder)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/GetFolder)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/GetFolder)

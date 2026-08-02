---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_UpdateRepositoryName.html
---

# UpdateRepositoryName
<a name="API_UpdateRepositoryName"></a>

Renames a repository. The repository name must be unique across the calling AWS account. Repository names are limited to 100 alphanumeric, dash, and underscore characters, and cannot include certain characters. The suffix .git is prohibited. For more information about the limits on repository names, see [Quotas](https://docs.aws.amazon.com/codecommit/latest/userguide/limits.html) in the AWS CodeCommit User Guide.

## Request Syntax
<a name="API_UpdateRepositoryName_RequestSyntax"></a>

```
{
   "newName": "{{string}}",
   "oldName": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateRepositoryName_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [newName](#API_UpdateRepositoryName_RequestSyntax) **   <a name="CodeCommit-UpdateRepositoryName-request-newName"></a>
The new name for the repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\.-]+`
Required: Yes

 ** [oldName](#API_UpdateRepositoryName_RequestSyntax) **   <a name="CodeCommit-UpdateRepositoryName-request-oldName"></a>
The current name of the repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\.-]+`
Required: Yes

## Response Elements
<a name="API_UpdateRepositoryName_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateRepositoryName_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidRepositoryNameException **
A specified repository name is not valid.
This exception occurs only when a specified repository name is not valid. Other exceptions occur when a required repository parameter is missing, or when a specified repository does not exist.
HTTP Status Code: 400

 ** RepositoryDoesNotExistException **
The specified repository does not exist.
HTTP Status Code: 400

 ** RepositoryNameExistsException **
The specified repository name already exists.
HTTP Status Code: 400

 ** RepositoryNameRequiredException **
A repository name is required, but was not specified.
HTTP Status Code: 400

## Examples
<a name="API_UpdateRepositoryName_Examples"></a>

### Example
<a name="API_UpdateRepositoryName_Example_1"></a>

This example illustrates one usage of UpdateRepositoryName.

#### Sample Request
<a name="API_UpdateRepositoryName_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codecommit.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 62
X-Amz-Target: CodeCommit_20150413.UpdateRepositoryName
X-Amz-Date: 20151029T153512Z
User-Agent: aws-cli/1.7.38 Python/2.7.9 Windows/7
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20151029/us-east-1/codecommit/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
  "newName": "MyRenamedDemoRepo",
  "oldName": "MyDemoRepo"
}
```

#### Sample Response
<a name="API_UpdateRepositoryName_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 0728aaa8-EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 0
Date: Thu, 29 Oct 2015 15:35:13 GMT
```

## See Also
<a name="API_UpdateRepositoryName_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/UpdateRepositoryName)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/UpdateRepositoryName)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/UpdateRepositoryName)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/UpdateRepositoryName)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/UpdateRepositoryName)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/UpdateRepositoryName)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/UpdateRepositoryName)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/UpdateRepositoryName)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/UpdateRepositoryName)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/UpdateRepositoryName)

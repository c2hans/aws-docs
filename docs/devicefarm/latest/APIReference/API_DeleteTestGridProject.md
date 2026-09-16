---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_DeleteTestGridProject.html
---

# DeleteTestGridProject
<a name="API_DeleteTestGridProject"></a>

 Deletes a Selenium testing project and all content generated under it. You cannot delete a project if it has active sessions.

**Important**
You cannot undo this operation.

## Request Syntax
<a name="API_DeleteTestGridProject_RequestSyntax"></a>

```
{
   "projectArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteTestGridProject_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [projectArn](#API_DeleteTestGridProject_RequestSyntax) **   <a name="devicefarm-DeleteTestGridProject-request-projectArn"></a>
The ARN of the project to delete, from [CreateTestGridProject](API_CreateTestGridProject.md) or [ListTestGridProjects](API_ListTestGridProjects.md).
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: Yes

## Response Elements
<a name="API_DeleteTestGridProject_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteTestGridProject_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ArgumentException **
An invalid argument was specified.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

 ** CannotDeleteException **
The requested object could not be deleted.
HTTP Status Code: 400

 ** InternalServiceException **
An internal exception was raised in the service. Contact [aws-devicefarm-support@amazon.com](mailto:aws-devicefarm-support@amazon.com) if you see this error.
HTTP Status Code: 500

 ** NotFoundException **
The specified entity was not found.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

## See Also
<a name="API_DeleteTestGridProject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devicefarm-2015-06-23/DeleteTestGridProject)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devicefarm-2015-06-23/DeleteTestGridProject)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/DeleteTestGridProject)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devicefarm-2015-06-23/DeleteTestGridProject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/DeleteTestGridProject)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devicefarm-2015-06-23/DeleteTestGridProject)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devicefarm-2015-06-23/DeleteTestGridProject)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devicefarm-2015-06-23/DeleteTestGridProject)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/devicefarm-2015-06-23/DeleteTestGridProject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/DeleteTestGridProject)

---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteProject.html
---

# DeleteProject
<a name="API_DeleteProject"></a>

Delete the specified project.

## Request Syntax
<a name="API_DeleteProject_RequestSyntax"></a>

```
{
   "ProjectName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteProject_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ProjectName](#API_DeleteProject_RequestSyntax) **   <a name="sagemaker-DeleteProject-request-ProjectName"></a>
The name of the project to delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,31}`
Required: Yes

## Response Elements
<a name="API_DeleteProject_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteProject_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
There was a conflict when you attempted to modify a SageMaker entity such as an `Experiment` or `Artifact`.
HTTP Status Code: 400

## See Also
<a name="API_DeleteProject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DeleteProject)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DeleteProject)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DeleteProject)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DeleteProject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DeleteProject)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DeleteProject)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DeleteProject)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DeleteProject)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DeleteProject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DeleteProject)

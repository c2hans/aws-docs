---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_DeleteBuildBatch.html
---

# DeleteBuildBatch
<a name="API_DeleteBuildBatch"></a>

Deletes a batch build.

## Request Syntax
<a name="API_DeleteBuildBatch_RequestSyntax"></a>

```
{
   "id": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteBuildBatch_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [id](#API_DeleteBuildBatch_RequestSyntax) **   <a name="CodeBuild-DeleteBuildBatch-request-id"></a>
The identifier of the batch build to delete.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

## Response Syntax
<a name="API_DeleteBuildBatch_ResponseSyntax"></a>

```
{
   "buildsDeleted": [ "string" ],
   "buildsNotDeleted": [
      {
         "id": "string",
         "statusCode": "string"
      }
   ],
   "statusCode": "string"
}
```

## Response Elements
<a name="API_DeleteBuildBatch_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [buildsDeleted](#API_DeleteBuildBatch_ResponseSyntax) **   <a name="CodeBuild-DeleteBuildBatch-response-buildsDeleted"></a>
An array of strings that contain the identifiers of the builds that were deleted.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1.

 ** [buildsNotDeleted](#API_DeleteBuildBatch_ResponseSyntax) **   <a name="CodeBuild-DeleteBuildBatch-response-buildsNotDeleted"></a>
An array of `BuildNotDeleted` objects that specify the builds that could not be deleted.
Type: Array of [BuildNotDeleted](API_BuildNotDeleted.md) objects

 ** [statusCode](#API_DeleteBuildBatch_ResponseSyntax) **   <a name="CodeBuild-DeleteBuildBatch-response-statusCode"></a>
The status code.
Type: String

## Errors
<a name="API_DeleteBuildBatch_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInputException **
The input value that was provided is not valid.
HTTP Status Code: 400

## See Also
<a name="API_DeleteBuildBatch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codebuild-2016-10-06/DeleteBuildBatch)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codebuild-2016-10-06/DeleteBuildBatch)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/DeleteBuildBatch)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codebuild-2016-10-06/DeleteBuildBatch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/DeleteBuildBatch)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codebuild-2016-10-06/DeleteBuildBatch)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codebuild-2016-10-06/DeleteBuildBatch)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codebuild-2016-10-06/DeleteBuildBatch)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codebuild-2016-10-06/DeleteBuildBatch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/DeleteBuildBatch)

---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_DeleteWebhook.html
---

# DeleteWebhook
<a name="API_DeleteWebhook"></a>

For an existing AWS CodeBuild build project that has its source code stored in a GitHub or Bitbucket repository, stops AWS CodeBuild from rebuilding the source code every time a code change is pushed to the repository.

## Request Syntax
<a name="API_DeleteWebhook_RequestSyntax"></a>

```
{
   "projectName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteWebhook_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [projectName](#API_DeleteWebhook_RequestSyntax) **   <a name="CodeBuild-DeleteWebhook-request-projectName"></a>
The name of the AWS CodeBuild project.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 150.
Pattern: `[A-Za-z0-9][A-Za-z0-9\-_]{1,149}`
Required: Yes

## Response Elements
<a name="API_DeleteWebhook_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteWebhook_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInputException **
The input value that was provided is not valid.
HTTP Status Code: 400

 ** OAuthProviderException **
There was a problem with the underlying OAuth provider.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified AWS resource cannot be found.
HTTP Status Code: 400

## See Also
<a name="API_DeleteWebhook_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codebuild-2016-10-06/DeleteWebhook)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codebuild-2016-10-06/DeleteWebhook)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/DeleteWebhook)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codebuild-2016-10-06/DeleteWebhook)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/DeleteWebhook)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codebuild-2016-10-06/DeleteWebhook)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codebuild-2016-10-06/DeleteWebhook)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codebuild-2016-10-06/DeleteWebhook)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codebuild-2016-10-06/DeleteWebhook)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/DeleteWebhook)

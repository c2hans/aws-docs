---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_DeleteSourceCredentials.html
---

# DeleteSourceCredentials
<a name="API_DeleteSourceCredentials"></a>

 Deletes a set of GitHub, GitHub Enterprise, or Bitbucket source credentials.

## Request Syntax
<a name="API_DeleteSourceCredentials_RequestSyntax"></a>

```
{
   "arn": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteSourceCredentials_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [arn](#API_DeleteSourceCredentials_RequestSyntax) **   <a name="CodeBuild-DeleteSourceCredentials-request-arn"></a>
 The Amazon Resource Name (ARN) of the token.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

## Response Syntax
<a name="API_DeleteSourceCredentials_ResponseSyntax"></a>

```
{
   "arn": "string"
}
```

## Response Elements
<a name="API_DeleteSourceCredentials_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_DeleteSourceCredentials_ResponseSyntax) **   <a name="CodeBuild-DeleteSourceCredentials-response-arn"></a>
 The Amazon Resource Name (ARN) of the token.
Type: String
Length Constraints: Minimum length of 1.

## Errors
<a name="API_DeleteSourceCredentials_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInputException **
The input value that was provided is not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified AWS resource cannot be found.
HTTP Status Code: 400

## See Also
<a name="API_DeleteSourceCredentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codebuild-2016-10-06/DeleteSourceCredentials)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codebuild-2016-10-06/DeleteSourceCredentials)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/DeleteSourceCredentials)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codebuild-2016-10-06/DeleteSourceCredentials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/DeleteSourceCredentials)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codebuild-2016-10-06/DeleteSourceCredentials)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codebuild-2016-10-06/DeleteSourceCredentials)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codebuild-2016-10-06/DeleteSourceCredentials)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codebuild-2016-10-06/DeleteSourceCredentials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/DeleteSourceCredentials)

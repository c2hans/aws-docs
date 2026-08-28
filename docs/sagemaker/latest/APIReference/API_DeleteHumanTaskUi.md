---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteHumanTaskUi.html
---

# DeleteHumanTaskUi
<a name="API_DeleteHumanTaskUi"></a>

Use this operation to delete a human task user interface (worker task template).

 To see a list of human task user interfaces (work task templates) in your account, use [ListHumanTaskUis](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListHumanTaskUis.html). When you delete a worker task template, it no longer appears when you call `ListHumanTaskUis`.

## Request Syntax
<a name="API_DeleteHumanTaskUi_RequestSyntax"></a>

```
{
   "HumanTaskUiName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteHumanTaskUi_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [HumanTaskUiName](#API_DeleteHumanTaskUi_RequestSyntax) **   <a name="sagemaker-DeleteHumanTaskUi-request-HumanTaskUiName"></a>
The name of the human task user interface (work task template) you want to delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-z0-9](-*[a-z0-9])*`
Required: Yes

## Response Elements
<a name="API_DeleteHumanTaskUi_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteHumanTaskUi_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DeleteHumanTaskUi_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DeleteHumanTaskUi)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DeleteHumanTaskUi)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DeleteHumanTaskUi)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DeleteHumanTaskUi)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DeleteHumanTaskUi)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DeleteHumanTaskUi)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DeleteHumanTaskUi)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DeleteHumanTaskUi)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DeleteHumanTaskUi)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DeleteHumanTaskUi)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

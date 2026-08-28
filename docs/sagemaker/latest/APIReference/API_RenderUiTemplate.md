---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_RenderUiTemplate.html
---

# RenderUiTemplate
<a name="API_RenderUiTemplate"></a>

Renders the UI template so that you can preview the worker's experience.

## Request Syntax
<a name="API_RenderUiTemplate_RequestSyntax"></a>

```
{
   "HumanTaskUiArn": "{{string}}",
   "RoleArn": "{{string}}",
   "Task": {
      "Input": "{{string}}"
   },
   "UiTemplate": {
      "Content": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_RenderUiTemplate_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [HumanTaskUiArn](#API_RenderUiTemplate_RequestSyntax) **   <a name="sagemaker-RenderUiTemplate-request-HumanTaskUiArn"></a>
The `HumanTaskUiArn` of the worker UI that you want to render. Do not provide a `HumanTaskUiArn` if you use the `UiTemplate` parameter.
See a list of available Human Ui Amazon Resource Names (ARNs) in [UiConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UiConfig.html).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]+:[0-9]{12}:human-task-ui/.*`
Required: No

 ** [RoleArn](#API_RenderUiTemplate_RequestSyntax) **   <a name="sagemaker-RenderUiTemplate-request-RoleArn"></a>
The Amazon Resource Name (ARN) that has access to the S3 objects that are used by the template.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** [Task](#API_RenderUiTemplate_RequestSyntax) **   <a name="sagemaker-RenderUiTemplate-request-Task"></a>
A `RenderableTask` object containing a representative task to render.
Type: [RenderableTask](API_RenderableTask.md) object
Required: Yes

 ** [UiTemplate](#API_RenderUiTemplate_RequestSyntax) **   <a name="sagemaker-RenderUiTemplate-request-UiTemplate"></a>
A `Template` object containing the worker UI template to render.
Type: [UiTemplate](API_UiTemplate.md) object
Required: No

## Response Syntax
<a name="API_RenderUiTemplate_ResponseSyntax"></a>

```
{
   "Errors": [
      {
         "Code": "string",
         "Message": "string"
      }
   ],
   "RenderedContent": "string"
}
```

## Response Elements
<a name="API_RenderUiTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Errors](#API_RenderUiTemplate_ResponseSyntax) **   <a name="sagemaker-RenderUiTemplate-response-Errors"></a>
A list of one or more `RenderingError` objects if any were encountered while rendering the template. If there were no errors, the list is empty.
Type: Array of [RenderingError](API_RenderingError.md) objects

 ** [RenderedContent](#API_RenderUiTemplate_ResponseSyntax) **   <a name="sagemaker-RenderUiTemplate-response-RenderedContent"></a>
A Liquid template that renders the HTML for the worker UI.
Type: String

## Errors
<a name="API_RenderUiTemplate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_RenderUiTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/RenderUiTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/RenderUiTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/RenderUiTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/RenderUiTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/RenderUiTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/RenderUiTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/RenderUiTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/RenderUiTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/RenderUiTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/RenderUiTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

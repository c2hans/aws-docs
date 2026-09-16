---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeHumanTaskUi.html
---

# DescribeHumanTaskUi
<a name="API_DescribeHumanTaskUi"></a>

Returns information about the requested human task user interface (worker task template).

## Request Syntax
<a name="API_DescribeHumanTaskUi_RequestSyntax"></a>

```
{
   "HumanTaskUiName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeHumanTaskUi_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [HumanTaskUiName](#API_DescribeHumanTaskUi_RequestSyntax) **   <a name="sagemaker-DescribeHumanTaskUi-request-HumanTaskUiName"></a>
The name of the human task user interface (worker task template) you want information about.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-z0-9](-*[a-z0-9])*`
Required: Yes

## Response Syntax
<a name="API_DescribeHumanTaskUi_ResponseSyntax"></a>

```
{
   "HumanTaskUiArn": "string",
   "HumanTaskUiName": "string",
   "HumanTaskUiStatus": "string",
   "UiTemplate": {
      "ContentSha256": "string",
      "Url": "string"
   }
}
```

## Response Elements
<a name="API_DescribeHumanTaskUi_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [HumanTaskUiArn](#API_DescribeHumanTaskUi_ResponseSyntax) **   <a name="sagemaker-DescribeHumanTaskUi-response-HumanTaskUiArn"></a>
The Amazon Resource Name (ARN) of the human task user interface (worker task template).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]+:[0-9]{12}:human-task-ui/.*`

 ** [HumanTaskUiName](#API_DescribeHumanTaskUi_ResponseSyntax) **   <a name="sagemaker-DescribeHumanTaskUi-response-HumanTaskUiName"></a>
The name of the human task user interface (worker task template).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-z0-9](-*[a-z0-9])*`

 ** [HumanTaskUiStatus](#API_DescribeHumanTaskUi_ResponseSyntax) **   <a name="sagemaker-DescribeHumanTaskUi-response-HumanTaskUiStatus"></a>
The status of the human task user interface (worker task template). Valid values are listed below.
Type: String
Valid Values: `Active | Deleting`

 ** [UiTemplate](#API_DescribeHumanTaskUi_ResponseSyntax) **   <a name="sagemaker-DescribeHumanTaskUi-response-UiTemplate"></a>
Container for user interface template information.
Type: [UiTemplateInfo](API_UiTemplateInfo.md) object

## Errors
<a name="API_DescribeHumanTaskUi_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeHumanTaskUi_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeHumanTaskUi)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeHumanTaskUi)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeHumanTaskUi)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeHumanTaskUi)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeHumanTaskUi)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeHumanTaskUi)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeHumanTaskUi)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeHumanTaskUi)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeHumanTaskUi)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeHumanTaskUi)

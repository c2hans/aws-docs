---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateHumanTaskUi.html
---

# CreateHumanTaskUi
<a name="API_CreateHumanTaskUi"></a>

Defines the settings you will use for the human review workflow user interface. Reviewers will see a three-panel interface with an instruction area, the item to review, and an input area.

## Request Syntax
<a name="API_CreateHumanTaskUi_RequestSyntax"></a>

```
{
   "HumanTaskUiName": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "UiTemplate": {
      "Content": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreateHumanTaskUi_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [HumanTaskUiName](#API_CreateHumanTaskUi_RequestSyntax) **   <a name="sagemaker-CreateHumanTaskUi-request-HumanTaskUiName"></a>
The name of the user interface you are creating.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-z0-9](-*[a-z0-9])*`
Required: Yes

 ** [Tags](#API_CreateHumanTaskUi_RequestSyntax) **   <a name="sagemaker-CreateHumanTaskUi-request-Tags"></a>
An array of key-value pairs that contain metadata to help you categorize and organize a human review workflow user interface. Each tag consists of a key and a value, both of which you define.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [UiTemplate](#API_CreateHumanTaskUi_RequestSyntax) **   <a name="sagemaker-CreateHumanTaskUi-request-UiTemplate"></a>
The Liquid template for the worker user interface.
Type: [UiTemplate](API_UiTemplate.md) object
Required: Yes

## Response Syntax
<a name="API_CreateHumanTaskUi_ResponseSyntax"></a>

```
{
   "HumanTaskUiArn": "string"
}
```

## Response Elements
<a name="API_CreateHumanTaskUi_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [HumanTaskUiArn](#API_CreateHumanTaskUi_ResponseSyntax) **   <a name="sagemaker-CreateHumanTaskUi-response-HumanTaskUiArn"></a>
The Amazon Resource Name (ARN) of the human review workflow user interface you create.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]+:[0-9]{12}:human-task-ui/.*`

## Errors
<a name="API_CreateHumanTaskUi_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceInUse **
Resource being accessed is in use.
HTTP Status Code: 400

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

## See Also
<a name="API_CreateHumanTaskUi_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateHumanTaskUi)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateHumanTaskUi)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateHumanTaskUi)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateHumanTaskUi)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateHumanTaskUi)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateHumanTaskUi)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateHumanTaskUi)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateHumanTaskUi)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateHumanTaskUi)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateHumanTaskUi)

---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteTrialComponent.html
---

# DeleteTrialComponent
<a name="API_DeleteTrialComponent"></a>

Deletes the specified trial component. A trial component must be disassociated from all trials before the trial component can be deleted. To disassociate a trial component from a trial, call the [DisassociateTrialComponent](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DisassociateTrialComponent.html) API.

## Request Syntax
<a name="API_DeleteTrialComponent_RequestSyntax"></a>

```
{
   "TrialComponentName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteTrialComponent_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [TrialComponentName](#API_DeleteTrialComponent_RequestSyntax) **   <a name="sagemaker-DeleteTrialComponent-request-TrialComponentName"></a>
The name of the component to delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`
Required: Yes

## Response Syntax
<a name="API_DeleteTrialComponent_ResponseSyntax"></a>

```
{
   "TrialComponentArn": "string"
}
```

## Response Elements
<a name="API_DeleteTrialComponent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TrialComponentArn](#API_DeleteTrialComponent_ResponseSyntax) **   <a name="sagemaker-DeleteTrialComponent-response-TrialComponentArn"></a>
The Amazon Resource Name (ARN) of the component is being deleted.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:experiment-trial-component/.*`

## Errors
<a name="API_DeleteTrialComponent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DeleteTrialComponent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DeleteTrialComponent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DeleteTrialComponent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DeleteTrialComponent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DeleteTrialComponent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DeleteTrialComponent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DeleteTrialComponent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DeleteTrialComponent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DeleteTrialComponent)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DeleteTrialComponent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DeleteTrialComponent)

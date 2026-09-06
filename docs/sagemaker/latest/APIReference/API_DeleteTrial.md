---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteTrial.html
---

# DeleteTrial
<a name="API_DeleteTrial"></a>

Deletes the specified trial. All trial components that make up the trial must be deleted first. Use the [DescribeTrialComponent](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeTrialComponent.html) API to get the list of trial components.

## Request Syntax
<a name="API_DeleteTrial_RequestSyntax"></a>

```
{
   "TrialName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteTrial_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [TrialName](#API_DeleteTrial_RequestSyntax) **   <a name="sagemaker-DeleteTrial-request-TrialName"></a>
The name of the trial to delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`
Required: Yes

## Response Syntax
<a name="API_DeleteTrial_ResponseSyntax"></a>

```
{
   "TrialArn": "string"
}
```

## Response Elements
<a name="API_DeleteTrial_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TrialArn](#API_DeleteTrial_ResponseSyntax) **   <a name="sagemaker-DeleteTrial-response-TrialArn"></a>
The Amazon Resource Name (ARN) of the trial that is being deleted.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:experiment-trial/.*`

## Errors
<a name="API_DeleteTrial_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DeleteTrial_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DeleteTrial)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DeleteTrial)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DeleteTrial)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DeleteTrial)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DeleteTrial)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DeleteTrial)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DeleteTrial)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DeleteTrial)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DeleteTrial)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DeleteTrial)

---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeletePartnerApp.html
---

# DeletePartnerApp
<a name="API_DeletePartnerApp"></a>

Deletes a SageMaker Partner AI App.

## Request Syntax
<a name="API_DeletePartnerApp_RequestSyntax"></a>

```
{
   "Arn": "{{string}}",
   "ClientToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DeletePartnerApp_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Arn](#API_DeletePartnerApp_RequestSyntax) **   <a name="sagemaker-DeletePartnerApp-request-Arn"></a>
The ARN of the SageMaker Partner AI App to delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:partner-app\/app-[A-Z0-9]{12}`
Required: Yes

 ** [ClientToken](#API_DeletePartnerApp_RequestSyntax) **   <a name="sagemaker-DeletePartnerApp-request-ClientToken"></a>
A unique token that guarantees that the call to this API is idempotent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `[a-zA-Z0-9-]+`
Required: No

## Response Syntax
<a name="API_DeletePartnerApp_ResponseSyntax"></a>

```
{
   "Arn": "string"
}
```

## Response Elements
<a name="API_DeletePartnerApp_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_DeletePartnerApp_ResponseSyntax) **   <a name="sagemaker-DeletePartnerApp-response-Arn"></a>
The ARN of the SageMaker Partner AI App that was deleted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:partner-app\/app-[A-Z0-9]{12}`

## Errors
<a name="API_DeletePartnerApp_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
There was a conflict when you attempted to modify a SageMaker entity such as an `Experiment` or `Artifact`.
HTTP Status Code: 400

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DeletePartnerApp_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DeletePartnerApp)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DeletePartnerApp)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DeletePartnerApp)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DeletePartnerApp)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DeletePartnerApp)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DeletePartnerApp)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DeletePartnerApp)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DeletePartnerApp)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DeletePartnerApp)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DeletePartnerApp)

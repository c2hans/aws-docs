---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteHubContentReference.html
---

# DeleteHubContentReference
<a name="API_DeleteHubContentReference"></a>

Delete a hub content reference in order to remove a model from a private hub.

## Request Syntax
<a name="API_DeleteHubContentReference_RequestSyntax"></a>

```
{
   "HubContentName": "{{string}}",
   "HubContentType": "{{string}}",
   "HubName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteHubContentReference_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [HubContentName](#API_DeleteHubContentReference_RequestSyntax) **   <a name="sagemaker-DeleteHubContentReference-request-HubContentName"></a>
The name of the hub content to delete.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [HubContentType](#API_DeleteHubContentReference_RequestSyntax) **   <a name="sagemaker-DeleteHubContentReference-request-HubContentType"></a>
The type of hub content reference to delete. The only supported type of hub content reference to delete is `ModelReference`.
Type: String
Valid Values: `Model | Notebook | ModelReference | DataSet | JsonDoc`
Required: Yes

 ** [HubName](#API_DeleteHubContentReference_RequestSyntax) **   <a name="sagemaker-DeleteHubContentReference-request-HubName"></a>
The name of the hub to delete the hub content reference from.
Type: String
Pattern: `(arn:[a-z0-9-\.]{1,63}:sagemaker:\w+(?:-\w+)+:(\d{12}|aws):hub\/)?[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

## Response Elements
<a name="API_DeleteHubContentReference_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteHubContentReference_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DeleteHubContentReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DeleteHubContentReference)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DeleteHubContentReference)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DeleteHubContentReference)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DeleteHubContentReference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DeleteHubContentReference)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DeleteHubContentReference)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DeleteHubContentReference)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DeleteHubContentReference)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DeleteHubContentReference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DeleteHubContentReference)

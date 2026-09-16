---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateHubContentReference.html
---

# UpdateHubContentReference
<a name="API_UpdateHubContentReference"></a>

Updates the contents of a SageMaker hub for a `ModelReference` resource. A `ModelReference` allows you to access public SageMaker JumpStart models from within your private hub.

When using this API, you can update the `MinVersion` field for additional flexibility in the model version. You shouldn't update any additional fields when using this API, because the metadata in your private hub should match the public JumpStart model's metadata.

**Note**
If you want to update a `Model` or `Notebook` resource in your hub, use the `UpdateHubContent` API instead.

For more information about adding model references to your hub, see [ Add models to a private hub](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-curated-hubs-admin-guide-add-models.html).

## Request Syntax
<a name="API_UpdateHubContentReference_RequestSyntax"></a>

```
{
   "HubContentName": "{{string}}",
   "HubContentType": "{{string}}",
   "HubName": "{{string}}",
   "MinVersion": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateHubContentReference_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [HubContentName](#API_UpdateHubContentReference_RequestSyntax) **   <a name="sagemaker-UpdateHubContentReference-request-HubContentName"></a>
The name of the hub content resource that you want to update.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [HubContentType](#API_UpdateHubContentReference_RequestSyntax) **   <a name="sagemaker-UpdateHubContentReference-request-HubContentType"></a>
The content type of the resource that you want to update. Only specify a `ModelReference` resource for this API. To update a `Model` or `Notebook` resource, use the `UpdateHubContent` API instead.
Type: String
Valid Values: `Model | Notebook | ModelReference | DataSet | JsonDoc`
Required: Yes

 ** [HubName](#API_UpdateHubContentReference_RequestSyntax) **   <a name="sagemaker-UpdateHubContentReference-request-HubName"></a>
The name of the SageMaker hub that contains the hub content you want to update. You can optionally use the hub ARN instead.
Type: String
Pattern: `(arn:[a-z0-9-\.]{1,63}:sagemaker:\w+(?:-\w+)+:(\d{12}|aws):hub\/)?[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [MinVersion](#API_UpdateHubContentReference_RequestSyntax) **   <a name="sagemaker-UpdateHubContentReference-request-MinVersion"></a>
The minimum hub content version of the referenced model that you want to use. The minimum version must be older than the latest available version of the referenced model. To support all versions of a model, set the value to `1.0.0`.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 14.
Pattern: `\d{1,4}.\d{1,4}.\d{1,4}`
Required: No

## Response Syntax
<a name="API_UpdateHubContentReference_ResponseSyntax"></a>

```
{
   "HubArn": "string",
   "HubContentArn": "string"
}
```

## Response Elements
<a name="API_UpdateHubContentReference_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [HubArn](#API_UpdateHubContentReference_ResponseSyntax) **   <a name="sagemaker-UpdateHubContentReference-response-HubArn"></a>
The ARN of the private model hub that contains the updated hub content.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `.*`

 ** [HubContentArn](#API_UpdateHubContentReference_ResponseSyntax) **   <a name="sagemaker-UpdateHubContentReference-response-HubContentArn"></a>
The ARN of the hub content resource that was updated.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `.*`

## Errors
<a name="API_UpdateHubContentReference_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceInUse **
Resource being accessed is in use.
HTTP Status Code: 400

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_UpdateHubContentReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/UpdateHubContentReference)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/UpdateHubContentReference)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/UpdateHubContentReference)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/UpdateHubContentReference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/UpdateHubContentReference)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/UpdateHubContentReference)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/UpdateHubContentReference)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/UpdateHubContentReference)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/UpdateHubContentReference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/UpdateHubContentReference)

---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateHubContentPresignedUrls.html
---

# CreateHubContentPresignedUrls
<a name="API_CreateHubContentPresignedUrls"></a>

Creates presigned URLs for accessing hub content artifacts. This operation generates time-limited, secure URLs that allow direct download of model artifacts and associated files from Amazon SageMaker hub content, including gated models that require end-user license agreement acceptance.

## Request Syntax
<a name="API_CreateHubContentPresignedUrls_RequestSyntax"></a>

```
{
   "AccessConfig": {
      "AcceptEula": {{boolean}},
      "ExpectedS3Url": "{{string}}"
   },
   "HubContentName": "{{string}}",
   "HubContentType": "{{string}}",
   "HubContentVersion": "{{string}}",
   "HubName": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateHubContentPresignedUrls_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccessConfig](#API_CreateHubContentPresignedUrls_RequestSyntax) **   <a name="sagemaker-CreateHubContentPresignedUrls-request-AccessConfig"></a>
Configuration settings for accessing the hub content, including end-user license agreement acceptance for gated models and expected S3 URL validation.
Type: [PresignedUrlAccessConfig](API_PresignedUrlAccessConfig.md) object
Required: No

 ** [HubContentName](#API_CreateHubContentPresignedUrls_RequestSyntax) **   <a name="sagemaker-CreateHubContentPresignedUrls-request-HubContentName"></a>
The name of the hub content for which to generate presigned URLs. This identifies the specific model or content within the hub.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [HubContentType](#API_CreateHubContentPresignedUrls_RequestSyntax) **   <a name="sagemaker-CreateHubContentPresignedUrls-request-HubContentType"></a>
The type of hub content to access. Valid values include `Model`, `Notebook`, and `ModelReference`.
Type: String
Valid Values: `Model | Notebook | ModelReference | DataSet | JsonDoc`
Required: Yes

 ** [HubContentVersion](#API_CreateHubContentPresignedUrls_RequestSyntax) **   <a name="sagemaker-CreateHubContentPresignedUrls-request-HubContentVersion"></a>
The version of the hub content. If not specified, the latest version is used.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 14.
Pattern: `\d{1,4}.\d{1,4}.\d{1,4}`
Required: No

 ** [HubName](#API_CreateHubContentPresignedUrls_RequestSyntax) **   <a name="sagemaker-CreateHubContentPresignedUrls-request-HubName"></a>
The name or Amazon Resource Name (ARN) of the hub that contains the content. For public content, use `SageMakerPublicHub`.
Type: String
Pattern: `(arn:[a-z0-9-\.]{1,63}:sagemaker:\w+(?:-\w+)+:(\d{12}|aws):hub\/)?[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [MaxResults](#API_CreateHubContentPresignedUrls_RequestSyntax) **   <a name="sagemaker-CreateHubContentPresignedUrls-request-MaxResults"></a>
The maximum number of presigned URLs to return in the response. Default value is 100. Large models may contain hundreds of files, requiring pagination to retrieve all URLs.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_CreateHubContentPresignedUrls_RequestSyntax) **   <a name="sagemaker-CreateHubContentPresignedUrls-request-NextToken"></a>
 A token for pagination. Use this token to retrieve the next set of presigned URLs when the response is truncated.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

## Response Syntax
<a name="API_CreateHubContentPresignedUrls_ResponseSyntax"></a>

```
{
   "AuthorizedUrlConfigs": [
      {
         "LocalPath": "string",
         "Url": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_CreateHubContentPresignedUrls_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AuthorizedUrlConfigs](#API_CreateHubContentPresignedUrls_ResponseSyntax) **   <a name="sagemaker-CreateHubContentPresignedUrls-response-AuthorizedUrlConfigs"></a>
An array of authorized URL configurations, each containing a presigned URL and its corresponding local file path for proper file organization during download.
Type: Array of [AuthorizedUrl](API_AuthorizedUrl.md) objects

 ** [NextToken](#API_CreateHubContentPresignedUrls_ResponseSyntax) **   <a name="sagemaker-CreateHubContentPresignedUrls-response-NextToken"></a>
A token for pagination. If present, indicates that more presigned URLs are available. Use this token in a subsequent request to retrieve additional URLs.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_CreateHubContentPresignedUrls_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_CreateHubContentPresignedUrls_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateHubContentPresignedUrls)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateHubContentPresignedUrls)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateHubContentPresignedUrls)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateHubContentPresignedUrls)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateHubContentPresignedUrls)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateHubContentPresignedUrls)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateHubContentPresignedUrls)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateHubContentPresignedUrls)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateHubContentPresignedUrls)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateHubContentPresignedUrls)

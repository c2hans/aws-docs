---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateHubContent.html
---

# UpdateHubContent
<a name="API_UpdateHubContent"></a>

Updates SageMaker hub content (either a `Model` or `Notebook` resource).

You can update the metadata that describes the resource. In addition to the required request fields, specify at least one of the following fields to update:
+  `HubContentDescription`
+  `HubContentDisplayName`
+  `HubContentMarkdown`
+  `HubContentSearchKeywords`
+  `SupportStatus`

For more information about hubs, see [Private curated hubs for foundation model access control in JumpStart](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-curated-hubs.html).

**Note**
If you want to update a `ModelReference` resource in your hub, use the `UpdateHubContentResource` API instead.

## Request Syntax
<a name="API_UpdateHubContent_RequestSyntax"></a>

```
{
   "HubContentDescription": "{{string}}",
   "HubContentDisplayName": "{{string}}",
   "HubContentMarkdown": "{{string}}",
   "HubContentName": "{{string}}",
   "HubContentSearchKeywords": [ "{{string}}" ],
   "HubContentType": "{{string}}",
   "HubContentVersion": "{{string}}",
   "HubName": "{{string}}",
   "SupportStatus": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateHubContent_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [HubContentDescription](#API_UpdateHubContent_RequestSyntax) **   <a name="sagemaker-UpdateHubContent-request-HubContentDescription"></a>
The description of the hub content.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1023.
Pattern: `.*`
Required: No

 ** [HubContentDisplayName](#API_UpdateHubContent_RequestSyntax) **   <a name="sagemaker-UpdateHubContent-request-HubContentDisplayName"></a>
The display name of the hub content.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `.*`
Required: No

 ** [HubContentMarkdown](#API_UpdateHubContent_RequestSyntax) **   <a name="sagemaker-UpdateHubContent-request-HubContentMarkdown"></a>
A string that provides a description of the hub content. This string can include links, tables, and standard markdown formatting.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 170391.
Required: No

 ** [HubContentName](#API_UpdateHubContent_RequestSyntax) **   <a name="sagemaker-UpdateHubContent-request-HubContentName"></a>
The name of the hub content resource that you want to update.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [HubContentSearchKeywords](#API_UpdateHubContent_RequestSyntax) **   <a name="sagemaker-UpdateHubContent-request-HubContentSearchKeywords"></a>
The searchable keywords of the hub content.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `.*`
Required: No

 ** [HubContentType](#API_UpdateHubContent_RequestSyntax) **   <a name="sagemaker-UpdateHubContent-request-HubContentType"></a>
The content type of the resource that you want to update. Only specify a `Model` or `Notebook` resource for this API. To update a `ModelReference`, use the `UpdateHubContentReference` API instead.
Type: String
Valid Values: `Model | Notebook | ModelReference | DataSet | JsonDoc`
Required: Yes

 ** [HubContentVersion](#API_UpdateHubContent_RequestSyntax) **   <a name="sagemaker-UpdateHubContent-request-HubContentVersion"></a>
The hub content version that you want to update. For example, if you have two versions of a resource in your hub, you can update the second version.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 14.
Pattern: `\d{1,4}.\d{1,4}.\d{1,4}`
Required: Yes

 ** [HubName](#API_UpdateHubContent_RequestSyntax) **   <a name="sagemaker-UpdateHubContent-request-HubName"></a>
The name of the SageMaker hub that contains the hub content you want to update. You can optionally use the hub ARN instead.
Type: String
Pattern: `(arn:[a-z0-9-\.]{1,63}:sagemaker:\w+(?:-\w+)+:(\d{12}|aws):hub\/)?[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [SupportStatus](#API_UpdateHubContent_RequestSyntax) **   <a name="sagemaker-UpdateHubContent-request-SupportStatus"></a>
Indicates the current status of the hub content resource.
Type: String
Valid Values: `Supported | Deprecated | Restricted`
Required: No

## Response Syntax
<a name="API_UpdateHubContent_ResponseSyntax"></a>

```
{
   "HubArn": "string",
   "HubContentArn": "string"
}
```

## Response Elements
<a name="API_UpdateHubContent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [HubArn](#API_UpdateHubContent_ResponseSyntax) **   <a name="sagemaker-UpdateHubContent-response-HubArn"></a>
The ARN of the private model hub that contains the updated hub content.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `.*`

 ** [HubContentArn](#API_UpdateHubContent_ResponseSyntax) **   <a name="sagemaker-UpdateHubContent-response-HubContentArn"></a>
The ARN of the hub content resource that was updated.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `.*`

## Errors
<a name="API_UpdateHubContent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceInUse **
Resource being accessed is in use.
HTTP Status Code: 400

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_UpdateHubContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/UpdateHubContent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/UpdateHubContent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/UpdateHubContent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/UpdateHubContent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/UpdateHubContent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/UpdateHubContent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/UpdateHubContent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/UpdateHubContent)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/UpdateHubContent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/UpdateHubContent)

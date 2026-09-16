---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ImportHubContent.html
---

# ImportHubContent
<a name="API_ImportHubContent"></a>

Import hub content.

## Request Syntax
<a name="API_ImportHubContent_RequestSyntax"></a>

```
{
   "DocumentSchemaVersion": "{{string}}",
   "HubContentDescription": "{{string}}",
   "HubContentDisplayName": "{{string}}",
   "HubContentDocument": "{{string}}",
   "HubContentMarkdown": "{{string}}",
   "HubContentName": "{{string}}",
   "HubContentSearchKeywords": [ "{{string}}" ],
   "HubContentType": "{{string}}",
   "HubContentVersion": "{{string}}",
   "HubName": "{{string}}",
   "SupportStatus": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_ImportHubContent_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DocumentSchemaVersion](#API_ImportHubContent_RequestSyntax) **   <a name="sagemaker-ImportHubContent-request-DocumentSchemaVersion"></a>
The version of the hub content schema to import.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 14.
Pattern: `\d{1,4}.\d{1,4}.\d{1,4}`
Required: Yes

 ** [HubContentDescription](#API_ImportHubContent_RequestSyntax) **   <a name="sagemaker-ImportHubContent-request-HubContentDescription"></a>
A description of the hub content to import.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1023.
Pattern: `.*`
Required: No

 ** [HubContentDisplayName](#API_ImportHubContent_RequestSyntax) **   <a name="sagemaker-ImportHubContent-request-HubContentDisplayName"></a>
The display name of the hub content to import.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `.*`
Required: No

 ** [HubContentDocument](#API_ImportHubContent_RequestSyntax) **   <a name="sagemaker-ImportHubContent-request-HubContentDocument"></a>
The hub content document that describes information about the hub content such as type, associated containers, scripts, and more.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 327680.
Pattern: `.*`
Required: Yes

 ** [HubContentMarkdown](#API_ImportHubContent_RequestSyntax) **   <a name="sagemaker-ImportHubContent-request-HubContentMarkdown"></a>
A string that provides a description of the hub content. This string can include links, tables, and standard markdown formating.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 170391.
Required: No

 ** [HubContentName](#API_ImportHubContent_RequestSyntax) **   <a name="sagemaker-ImportHubContent-request-HubContentName"></a>
The name of the hub content to import.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [HubContentSearchKeywords](#API_ImportHubContent_RequestSyntax) **   <a name="sagemaker-ImportHubContent-request-HubContentSearchKeywords"></a>
The searchable keywords of the hub content.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `.*`
Required: No

 ** [HubContentType](#API_ImportHubContent_RequestSyntax) **   <a name="sagemaker-ImportHubContent-request-HubContentType"></a>
The type of hub content to import.
Type: String
Valid Values: `Model | Notebook | ModelReference | DataSet | JsonDoc`
Required: Yes

 ** [HubContentVersion](#API_ImportHubContent_RequestSyntax) **   <a name="sagemaker-ImportHubContent-request-HubContentVersion"></a>
The version of the hub content to import.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 14.
Pattern: `\d{1,4}.\d{1,4}.\d{1,4}`
Required: No

 ** [HubName](#API_ImportHubContent_RequestSyntax) **   <a name="sagemaker-ImportHubContent-request-HubName"></a>
The name of the hub to import content into.
Type: String
Pattern: `(arn:[a-z0-9-\.]{1,63}:sagemaker:\w+(?:-\w+)+:(\d{12}|aws):hub\/)?[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [SupportStatus](#API_ImportHubContent_RequestSyntax) **   <a name="sagemaker-ImportHubContent-request-SupportStatus"></a>
The status of the hub content resource.
Type: String
Valid Values: `Supported | Deprecated | Restricted`
Required: No

 ** [Tags](#API_ImportHubContent_RequestSyntax) **   <a name="sagemaker-ImportHubContent-request-Tags"></a>
Any tags associated with the hub content.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_ImportHubContent_ResponseSyntax"></a>

```
{
   "HubArn": "string",
   "HubContentArn": "string"
}
```

## Response Elements
<a name="API_ImportHubContent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [HubArn](#API_ImportHubContent_ResponseSyntax) **   <a name="sagemaker-ImportHubContent-response-HubArn"></a>
The ARN of the hub that the content was imported into.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `.*`

 ** [HubContentArn](#API_ImportHubContent_ResponseSyntax) **   <a name="sagemaker-ImportHubContent-response-HubContentArn"></a>
The ARN of the hub content that was imported.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `.*`

## Errors
<a name="API_ImportHubContent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceInUse **
Resource being accessed is in use.
HTTP Status Code: 400

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_ImportHubContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ImportHubContent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ImportHubContent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ImportHubContent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ImportHubContent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ImportHubContent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ImportHubContent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ImportHubContent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ImportHubContent)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ImportHubContent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ImportHubContent)

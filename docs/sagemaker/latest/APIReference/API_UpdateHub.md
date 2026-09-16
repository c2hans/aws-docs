---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateHub.html
---

# UpdateHub
<a name="API_UpdateHub"></a>

Update a hub.

## Request Syntax
<a name="API_UpdateHub_RequestSyntax"></a>

```
{
   "HubDescription": "{{string}}",
   "HubDisplayName": "{{string}}",
   "HubName": "{{string}}",
   "HubSearchKeywords": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_UpdateHub_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [HubDescription](#API_UpdateHub_RequestSyntax) **   <a name="sagemaker-UpdateHub-request-HubDescription"></a>
A description of the updated hub.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1023.
Pattern: `.*`
Required: No

 ** [HubDisplayName](#API_UpdateHub_RequestSyntax) **   <a name="sagemaker-UpdateHub-request-HubDisplayName"></a>
The display name of the hub.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `.*`
Required: No

 ** [HubName](#API_UpdateHub_RequestSyntax) **   <a name="sagemaker-UpdateHub-request-HubName"></a>
The name of the hub to update.
Type: String
Pattern: `(arn:[a-z0-9-\.]{1,63}:sagemaker:\w+(?:-\w+)+:(\d{12}|aws):hub\/)?[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [HubSearchKeywords](#API_UpdateHub_RequestSyntax) **   <a name="sagemaker-UpdateHub-request-HubSearchKeywords"></a>
The searchable keywords for the hub.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[^A-Z]*`
Required: No

## Response Syntax
<a name="API_UpdateHub_ResponseSyntax"></a>

```
{
   "HubArn": "string"
}
```

## Response Elements
<a name="API_UpdateHub_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [HubArn](#API_UpdateHub_ResponseSyntax) **   <a name="sagemaker-UpdateHub-response-HubArn"></a>
The Amazon Resource Name (ARN) of the updated hub.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `.*`

## Errors
<a name="API_UpdateHub_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_UpdateHub_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/UpdateHub)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/UpdateHub)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/UpdateHub)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/UpdateHub)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/UpdateHub)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/UpdateHub)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/UpdateHub)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/UpdateHub)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/UpdateHub)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/UpdateHub)

---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateHubContentReference.html
---

# CreateHubContentReference
<a name="API_CreateHubContentReference"></a>

Create a hub content reference in order to add a model in the JumpStart public hub to a private hub.

## Request Syntax
<a name="API_CreateHubContentReference_RequestSyntax"></a>

```
{
   "HubContentName": "{{string}}",
   "HubName": "{{string}}",
   "MinVersion": "{{string}}",
   "SageMakerPublicHubContentArn": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateHubContentReference_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [HubContentName](#API_CreateHubContentReference_RequestSyntax) **   <a name="sagemaker-CreateHubContentReference-request-HubContentName"></a>
The name of the hub content to reference.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** [HubName](#API_CreateHubContentReference_RequestSyntax) **   <a name="sagemaker-CreateHubContentReference-request-HubName"></a>
The name of the hub to add the hub content reference to.
Type: String
Pattern: `(arn:[a-z0-9-\.]{1,63}:sagemaker:\w+(?:-\w+)+:(\d{12}|aws):hub\/)?[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [MinVersion](#API_CreateHubContentReference_RequestSyntax) **   <a name="sagemaker-CreateHubContentReference-request-MinVersion"></a>
The minimum version of the hub content to reference.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 14.
Pattern: `\d{1,4}.\d{1,4}.\d{1,4}`
Required: No

 ** [SageMakerPublicHubContentArn](#API_CreateHubContentReference_RequestSyntax) **   <a name="sagemaker-CreateHubContentReference-request-SageMakerPublicHubContentArn"></a>
The ARN of the public hub content to reference.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `arn:[a-z0-9-\.]{1,63}:sagemaker:\w+(?:-\w+)+:aws:hub-content\/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}\/Model\/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,63}`
Required: Yes

 ** [Tags](#API_CreateHubContentReference_RequestSyntax) **   <a name="sagemaker-CreateHubContentReference-request-Tags"></a>
Any tags associated with the hub content to reference.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateHubContentReference_ResponseSyntax"></a>

```
{
   "HubArn": "string",
   "HubContentArn": "string"
}
```

## Response Elements
<a name="API_CreateHubContentReference_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [HubArn](#API_CreateHubContentReference_ResponseSyntax) **   <a name="sagemaker-CreateHubContentReference-response-HubArn"></a>
The ARN of the hub that the hub content reference was added to.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `.*`

 ** [HubContentArn](#API_CreateHubContentReference_ResponseSyntax) **   <a name="sagemaker-CreateHubContentReference-response-HubContentArn"></a>
The ARN of the hub content.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `.*`

## Errors
<a name="API_CreateHubContentReference_Errors"></a>

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
<a name="API_CreateHubContentReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateHubContentReference)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateHubContentReference)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateHubContentReference)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateHubContentReference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateHubContentReference)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateHubContentReference)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateHubContentReference)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateHubContentReference)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateHubContentReference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateHubContentReference)

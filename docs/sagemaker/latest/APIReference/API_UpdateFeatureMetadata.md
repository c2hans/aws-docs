---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateFeatureMetadata.html
---

# UpdateFeatureMetadata
<a name="API_UpdateFeatureMetadata"></a>

Updates the description and parameters of the feature group.

## Request Syntax
<a name="API_UpdateFeatureMetadata_RequestSyntax"></a>

```
{
   "Description": "{{string}}",
   "FeatureGroupName": "{{string}}",
   "FeatureName": "{{string}}",
   "ParameterAdditions": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "ParameterRemovals": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_UpdateFeatureMetadata_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Description](#API_UpdateFeatureMetadata_RequestSyntax) **   <a name="sagemaker-UpdateFeatureMetadata-request-Description"></a>
A description that you can write to better describe the feature.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `.*`
Required: No

 ** [FeatureGroupName](#API_UpdateFeatureMetadata_RequestSyntax) **   <a name="sagemaker-UpdateFeatureMetadata-request-FeatureGroupName"></a>
The name or Amazon Resource Name (ARN) of the feature group containing the feature that you're updating.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:feature-group\/)?([a-zA-Z0-9]([_-]*[a-zA-Z0-9]){0,63})`
Required: Yes

 ** [FeatureName](#API_UpdateFeatureMetadata_RequestSyntax) **   <a name="sagemaker-UpdateFeatureMetadata-request-FeatureName"></a>
The name of the feature that you're updating.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9]([-_]*[a-zA-Z0-9]){0,63}`
Required: Yes

 ** [ParameterAdditions](#API_UpdateFeatureMetadata_RequestSyntax) **   <a name="sagemaker-UpdateFeatureMetadata-request-ParameterAdditions"></a>
A list of key-value pairs that you can add to better describe the feature.
Type: Array of [FeatureParameter](API_FeatureParameter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Required: No

 ** [ParameterRemovals](#API_UpdateFeatureMetadata_RequestSyntax) **   <a name="sagemaker-UpdateFeatureMetadata-request-ParameterRemovals"></a>
A list of parameter keys that you can specify to remove parameters that describe your feature.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-]*)`
Required: No

## Response Elements
<a name="API_UpdateFeatureMetadata_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateFeatureMetadata_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_UpdateFeatureMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/UpdateFeatureMetadata)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/UpdateFeatureMetadata)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/UpdateFeatureMetadata)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/UpdateFeatureMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/UpdateFeatureMetadata)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/UpdateFeatureMetadata)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/UpdateFeatureMetadata)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/UpdateFeatureMetadata)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/UpdateFeatureMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/UpdateFeatureMetadata)

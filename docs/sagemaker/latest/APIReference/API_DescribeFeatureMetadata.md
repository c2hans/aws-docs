---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeFeatureMetadata.html
---

# DescribeFeatureMetadata
<a name="API_DescribeFeatureMetadata"></a>

Shows the metadata for a feature within a feature group.

## Request Syntax
<a name="API_DescribeFeatureMetadata_RequestSyntax"></a>

```
{
   "FeatureGroupName": "{{string}}",
   "FeatureName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeFeatureMetadata_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [FeatureGroupName](#API_DescribeFeatureMetadata_RequestSyntax) **   <a name="sagemaker-DescribeFeatureMetadata-request-FeatureGroupName"></a>
The name or Amazon Resource Name (ARN) of the feature group containing the feature.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:feature-group\/)?([a-zA-Z0-9]([_-]*[a-zA-Z0-9]){0,63})`
Required: Yes

 ** [FeatureName](#API_DescribeFeatureMetadata_RequestSyntax) **   <a name="sagemaker-DescribeFeatureMetadata-request-FeatureName"></a>
The name of the feature.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9]([-_]*[a-zA-Z0-9]){0,63}`
Required: Yes

## Response Syntax
<a name="API_DescribeFeatureMetadata_ResponseSyntax"></a>

```
{
   "CreationTime": number,
   "Description": "string",
   "FeatureGroupArn": "string",
   "FeatureGroupName": "string",
   "FeatureName": "string",
   "FeatureType": "string",
   "LastModifiedTime": number,
   "Parameters": [
      {
         "Key": "string",
         "Value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeFeatureMetadata_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreationTime](#API_DescribeFeatureMetadata_ResponseSyntax) **   <a name="sagemaker-DescribeFeatureMetadata-response-CreationTime"></a>
A timestamp indicating when the feature was created.
Type: Timestamp

 ** [Description](#API_DescribeFeatureMetadata_ResponseSyntax) **   <a name="sagemaker-DescribeFeatureMetadata-response-Description"></a>
The description you added to describe the feature.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `.*`

 ** [FeatureGroupArn](#API_DescribeFeatureMetadata_ResponseSyntax) **   <a name="sagemaker-DescribeFeatureMetadata-response-FeatureGroupArn"></a>
The Amazon Resource Number (ARN) of the feature group that contains the feature.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:feature-group/.*`

 ** [FeatureGroupName](#API_DescribeFeatureMetadata_ResponseSyntax) **   <a name="sagemaker-DescribeFeatureMetadata-response-FeatureGroupName"></a>
The name of the feature group that you've specified.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9]([_-]*[a-zA-Z0-9]){0,63}`

 ** [FeatureName](#API_DescribeFeatureMetadata_ResponseSyntax) **   <a name="sagemaker-DescribeFeatureMetadata-response-FeatureName"></a>
The name of the feature that you've specified.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9]([-_]*[a-zA-Z0-9]){0,63}`

 ** [FeatureType](#API_DescribeFeatureMetadata_ResponseSyntax) **   <a name="sagemaker-DescribeFeatureMetadata-response-FeatureType"></a>
The data type of the feature.
Type: String
Valid Values: `Integral | Fractional | String`

 ** [LastModifiedTime](#API_DescribeFeatureMetadata_ResponseSyntax) **   <a name="sagemaker-DescribeFeatureMetadata-response-LastModifiedTime"></a>
A timestamp indicating when the metadata for the feature group was modified. For example, if you add a parameter describing the feature, the timestamp changes to reflect the last time you
Type: Timestamp

 ** [Parameters](#API_DescribeFeatureMetadata_ResponseSyntax) **   <a name="sagemaker-DescribeFeatureMetadata-response-Parameters"></a>
The key-value pairs that you added to describe the feature.
Type: Array of [FeatureParameter](API_FeatureParameter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 25 items.

## Errors
<a name="API_DescribeFeatureMetadata_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeFeatureMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeFeatureMetadata)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeFeatureMetadata)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeFeatureMetadata)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeFeatureMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeFeatureMetadata)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeFeatureMetadata)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeFeatureMetadata)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeFeatureMetadata)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeFeatureMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeFeatureMetadata)

---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateClusterExtension.html
---

# UpdateClusterExtension
<a name="API_UpdateClusterExtension"></a>

Updates the configuration or the version of an extension installed on a SageMaker HyperPod cluster. SageMaker HyperPod applies the change to every node in the cluster. You can change the configuration, the version, or both in one request.
+  **Configuration:** You can change settings by sending `ConfigurationValues`. Settings that you include are changed. Settings that you omit keep their current values. A setting with the value `null` is removed and returns to its default value.
+  **Version:** You can update to a later version. You can't update to an earlier version. To use an earlier version, delete the extension and create it again with that version.

You can't update an extension while it is being deleted.

## Request Syntax
<a name="API_UpdateClusterExtension_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "ClusterArn": "{{string}}",
   "ConfigurationValues": "{{string}}",
   "ExtensionArn": "{{string}}",
   "ExtensionVersion": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateClusterExtension_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientToken](#API_UpdateClusterExtension_RequestSyntax) **   <a name="sagemaker-UpdateClusterExtension-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide so that the request is idempotent. If you send the same update more than once, SageMaker HyperPod applies it once and doesn't return an error.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[\x21-\x7E]+`
Required: No

 ** [ClusterArn](#API_UpdateClusterExtension_RequestSyntax) **   <a name="sagemaker-UpdateClusterExtension-request-ClusterArn"></a>
The Amazon Resource Name (ARN) of the SageMaker HyperPod cluster on which the extension is installed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:cluster/[a-z0-9]{12}`
Required: Yes

 ** [ConfigurationValues](#API_UpdateClusterExtension_RequestSyntax) **   <a name="sagemaker-UpdateClusterExtension-request-ConfigurationValues"></a>
The configuration changes to apply, as a JSON object serialized as a string. Settings that you include are changed, settings that you omit are unchanged, and a setting with the value `null` returns to its default value. The resulting configuration must be valid for the target extension version. If you omit `ConfigurationValues`, the configuration is unchanged.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10240.
Required: No

 ** [ExtensionArn](#API_UpdateClusterExtension_RequestSyntax) **   <a name="sagemaker-UpdateClusterExtension-request-ExtensionArn"></a>
The Amazon Resource Name (ARN) of the extension to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:extension/(sagemaker|eks|pcs)-[a-z0-9-]+/[a-z0-9-]+/[a-z0-9]+`
Required: Yes

 ** [ExtensionVersion](#API_UpdateClusterExtension_RequestSyntax) **   <a name="sagemaker-UpdateClusterExtension-request-ExtensionVersion"></a>
The version to update the extension to, in `MAJOR.MINOR.PATCH` format. The version must be later than the extension's current version. If you omit this parameter, the extension keeps its current version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9]+\.[0-9]+\.[0-9]+`
Required: No

## Response Syntax
<a name="API_UpdateClusterExtension_ResponseSyntax"></a>

```
{
   "ExtensionArn": "string"
}
```

## Response Elements
<a name="API_UpdateClusterExtension_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ExtensionArn](#API_UpdateClusterExtension_ResponseSyntax) **   <a name="sagemaker-UpdateClusterExtension-response-ExtensionArn"></a>
The Amazon Resource Name (ARN) of the extension that is being updated. To track the update, call `DescribeClusterExtension`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:extension/(sagemaker|eks|pcs)-[a-z0-9-]+/[a-z0-9-]+/[a-z0-9]+`

## Errors
<a name="API_UpdateClusterExtension_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
There was a conflict when you attempted to modify a SageMaker entity such as an `Experiment` or `Artifact`.
HTTP Status Code: 400

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_UpdateClusterExtension_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/UpdateClusterExtension)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/UpdateClusterExtension)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/UpdateClusterExtension)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/UpdateClusterExtension)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/UpdateClusterExtension)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/UpdateClusterExtension)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/UpdateClusterExtension)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/UpdateClusterExtension)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/UpdateClusterExtension)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/UpdateClusterExtension)

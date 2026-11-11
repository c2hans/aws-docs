---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateClusterExtension.html
---

# CreateClusterExtension
<a name="API_CreateClusterExtension"></a>

Installs an extension, such as `sagemaker-observability`, on a SageMaker HyperPod cluster orchestrated by Slurm. The cluster must have `NodeProvisioningMode` set to `Continuous` and can have only one extension with a given name. To track the installation, call `DescribeClusterExtension`.

## Request Syntax
<a name="API_CreateClusterExtension_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "ClusterArn": "{{string}}",
   "ConfigurationValues": "{{string}}",
   "ExtensionName": "{{string}}",
   "ExtensionVersion": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateClusterExtension_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateClusterExtension_RequestSyntax) **   <a name="sagemaker-CreateClusterExtension-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide so that the operation completes no more than one time. This token is valid for 8 hours. If you retry the request with the same client token and the same parameters within this time, the API returns the Amazon Resource Name (ARN) of the extension that the original request created, without creating a duplicate. If you use the same client token with different parameters, the request fails.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[\x21-\x7E]+`
Required: No

 ** [ClusterArn](#API_CreateClusterExtension_RequestSyntax) **   <a name="sagemaker-CreateClusterExtension-request-ClusterArn"></a>
The Amazon Resource Name (ARN) of the SageMaker HyperPod cluster on which to install the extension. The cluster must use Slurm as the orchestrator and have `NodeProvisioningMode` set to `Continuous`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:cluster/[a-z0-9]{12}`
Required: Yes

 ** [ConfigurationValues](#API_CreateClusterExtension_RequestSyntax) **   <a name="sagemaker-CreateClusterExtension-request-ConfigurationValues"></a>
The configuration settings for the extension, as a JSON object serialized as a string, for example `{"metricsProvider":{"nodeMetrics":{"level":"ADVANCED"}}}`. Each extension version defines which settings it accepts. SageMaker HyperPod validates the settings against that definition, and rejects the request if a setting is unknown or has an invalid value. Settings that you omit use the extension's default values. If you omit `ConfigurationValues`, all settings use their default values.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10240.
Required: No

 ** [ExtensionName](#API_CreateClusterExtension_RequestSyntax) **   <a name="sagemaker-CreateClusterExtension-request-ExtensionName"></a>
The name of the extension to install, for example `sagemaker-observability`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-z]([a-z0-9]|-[a-z0-9])*`
Required: Yes

 ** [ExtensionVersion](#API_CreateClusterExtension_RequestSyntax) **   <a name="sagemaker-CreateClusterExtension-request-ExtensionVersion"></a>
The version of the extension to install, in `MAJOR.MINOR.PATCH` format, for example `1.0.0`. If you don't specify a version, SageMaker HyperPod installs the latest available version of the extension.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9]+\.[0-9]+\.[0-9]+`
Required: No

 ** [Tags](#API_CreateClusterExtension_RequestSyntax) **   <a name="sagemaker-CreateClusterExtension-request-Tags"></a>
Custom tags for managing the extension as an AWS resource. You can add tags to your extension in the same way you add them in other AWS services that support tagging. To learn more about tagging AWS resources in general, see [Tagging AWS Resources User Guide](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html). To use this operation to add tags when you create an extension, you must have the `sagemaker:AddTags` permission.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateClusterExtension_ResponseSyntax"></a>

```
{
   "ExtensionArn": "string"
}
```

## Response Elements
<a name="API_CreateClusterExtension_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ExtensionArn](#API_CreateClusterExtension_ResponseSyntax) **   <a name="sagemaker-CreateClusterExtension-response-ExtensionArn"></a>
The Amazon Resource Name (ARN) of the extension that you created. Use this ARN to describe, update, or delete the extension.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:extension/(sagemaker|eks|pcs)-[a-z0-9-]+/[a-z0-9-]+/[a-z0-9]+`

## Errors
<a name="API_CreateClusterExtension_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
There was a conflict when you attempted to modify a SageMaker entity such as an `Experiment` or `Artifact`.
HTTP Status Code: 400

 ** ResourceInUse **
Resource being accessed is in use.
HTTP Status Code: 400

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_CreateClusterExtension_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateClusterExtension)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateClusterExtension)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateClusterExtension)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateClusterExtension)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateClusterExtension)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateClusterExtension)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateClusterExtension)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateClusterExtension)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateClusterExtension)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateClusterExtension)

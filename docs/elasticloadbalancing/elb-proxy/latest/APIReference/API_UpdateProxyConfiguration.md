---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/elb-proxy/latest/APIReference/API_UpdateProxyConfiguration.html
---

# UpdateProxyConfiguration

Updates the configuration for the specified proxy. You can update the configuration file, the configuration archive, or both.

## Request Parameters
<a name="API_UpdateProxyConfiguration_RequestParameters"></a>

 ** configurationArchive **
The updated configuration archive for the proxy. If you don't specify a value, the existing configuration archive is unchanged.
Type: [ConfigurationArchive](API_ConfigurationArchive.md) object
Required: No

 ** configurationFile **
The updated configuration file for the proxy. If you don't specify a value, the existing configuration file is unchanged.
Type: [ConfigurationFile](API_ConfigurationFile.md) object
Required: No

 ** customerKmsKeyArn **
The Amazon Resource Name (ARN) of the customer managed KMS key used to encrypt the proxy's configuration content. Specify a new ARN to set or rotate the key. If you don't specify a value, the existing key is unchanged.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[a-z-]+:kms:[a-z0-9-]+:[0-9]{12}:key/(mrk-)?[a-f0-9-]+`
Required: No

 ** proxyIdentifier **
The Amazon Resource Name (ARN) of the proxy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[a-z-]+:elasticloadbalancing:[a-z0-9-]+:[0-9]{12}:proxy/[a-zA-Z0-9-]+:[a-zA-Z0-9]+`
Required: Yes

 ** resetConfigurationArchive **
Indicates whether to remove the configuration archive from the proxy.
Type: Boolean
Required: No

 ** resetCustomerKmsKeyArn **
Indicates whether to remove the customer managed KMS key from the proxy and use the default service-owned key.
Type: Boolean
Required: No

## Response Elements
<a name="API_UpdateProxyConfiguration_ResponseElements"></a>

The following elements are returned by the service.

 ** configurationMetadata **
The configuration metadata for the proxy after the update.
Type: [ConfigurationMetadata](API_ConfigurationMetadata.md) object

 ** customerKmsKeyArn **
The Amazon Resource Name (ARN) of the customer managed KMS key used to encrypt the proxy's configuration content after the update. This value is absent when the proxy uses the default service-owned key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[a-z-]+:kms:[a-z0-9-]+:[0-9]{12}:key/(mrk-)?[a-f0-9-]+`

 ** updateId **
The ID of the update that was submitted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`

## Errors
<a name="API_UpdateProxyConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user does not have sufficient access to perform this action.
 ** message **
The error message.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred while processing the request.
 ** message **
The error message.
HTTP Status Code: 500

 ** PriorRequestNotCompletedException **
The request could not be completed because a prior request has not yet completed.
 ** message **
The error message.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The request references a resource that does not exist.
 ** message **
The error message.
HTTP Status Code: 404

 ** ThrottlingException **
The limit on the number of requests per second was exceeded.
 ** message **
The error message.
HTTP Status Code: 429

 ** ValidationError **
The input does not satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_UpdateProxyConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elb-proxy-2026-11-20/UpdateProxyConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elb-proxy-2026-11-20/UpdateProxyConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elb-proxy-2026-11-20/UpdateProxyConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elb-proxy-2026-11-20/UpdateProxyConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elb-proxy-2026-11-20/UpdateProxyConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elb-proxy-2026-11-20/UpdateProxyConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elb-proxy-2026-11-20/UpdateProxyConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elb-proxy-2026-11-20/UpdateProxyConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elb-proxy-2026-11-20/UpdateProxyConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elb-proxy-2026-11-20/UpdateProxyConfiguration)

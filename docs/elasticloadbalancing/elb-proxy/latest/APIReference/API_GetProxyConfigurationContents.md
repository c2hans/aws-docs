---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/elb-proxy/latest/APIReference/API_GetProxyConfigurationContents.html
---

# GetProxyConfigurationContents

Retrieves the configuration file, the configuration archive, or both for the specified proxy. This operation is separate from GetProxy so that you can grant access to proxy metadata without granting access to the configuration content.

## Request Parameters
<a name="API_GetProxyConfigurationContents_RequestParameters"></a>

 ** includeConfigArchive **
Indicates whether to include the configuration archive contents in the response. The default is `false`.
Type: Boolean
Required: No

 ** includeConfigFile **
Indicates whether to include the configuration file contents in the response. The default is `false`.
Type: Boolean
Required: No

 ** proxyIdentifier **
The Amazon Resource Name (ARN) of the proxy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[a-z-]+:elasticloadbalancing:[a-z0-9-]+:[0-9]{12}:proxy/[a-zA-Z0-9-]+:[a-zA-Z0-9]+`
Required: Yes

## Response Elements
<a name="API_GetProxyConfigurationContents_ResponseElements"></a>

The following elements are returned by the service.

 ** configurationArchiveContents **
The configuration archive contents. Populated only if `includeConfigArchive` was `true`.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 0. Maximum length of 52428800.

 ** configurationFileContents **
The configuration file contents. Populated only if `includeConfigFile` was `true`.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 0. Maximum length of 1048576.

 ** configurationMetadata **
The configuration metadata for the proxy.
Type: [ConfigurationMetadata](API_ConfigurationMetadata.md) object

 ** customerKmsKeyArn **
The Amazon Resource Name (ARN) of the customer managed KMS key used to encrypt the proxy's configuration content.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[a-z-]+:kms:[a-z0-9-]+:[0-9]{12}:key/(mrk-)?[a-f0-9-]+`

## Errors
<a name="API_GetProxyConfigurationContents_Errors"></a>

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
<a name="API_GetProxyConfigurationContents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elb-proxy-2026-11-20/GetProxyConfigurationContents)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elb-proxy-2026-11-20/GetProxyConfigurationContents)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elb-proxy-2026-11-20/GetProxyConfigurationContents)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elb-proxy-2026-11-20/GetProxyConfigurationContents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elb-proxy-2026-11-20/GetProxyConfigurationContents)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elb-proxy-2026-11-20/GetProxyConfigurationContents)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elb-proxy-2026-11-20/GetProxyConfigurationContents)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elb-proxy-2026-11-20/GetProxyConfigurationContents)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elb-proxy-2026-11-20/GetProxyConfigurationContents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elb-proxy-2026-11-20/GetProxyConfigurationContents)

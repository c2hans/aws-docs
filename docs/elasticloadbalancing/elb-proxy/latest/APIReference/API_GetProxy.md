---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/elb-proxy/latest/APIReference/API_GetProxy.html
---

# GetProxy

Retrieves information about the specified proxy.

## Request Parameters
<a name="API_GetProxy_RequestParameters"></a>

 ** proxyIdentifier **
The Amazon Resource Name (ARN) of the proxy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[a-z-]+:elasticloadbalancing:[a-z0-9-]+:[0-9]{12}:proxy/[a-zA-Z0-9-]+:[a-zA-Z0-9]+`
Required: Yes

## Response Elements
<a name="API_GetProxy_ResponseElements"></a>

The following elements are returned by the service.

 ** arn **
The Amazon Resource Name (ARN) of the proxy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** configurationMetadata **
The configuration metadata for the proxy.
Type: [ConfigurationMetadata](API_ConfigurationMetadata.md) object

 ** createdAt **
The date and time that the proxy was created.
Type: Timestamp

 ** customerKmsKeyArn **
The Amazon Resource Name (ARN) of the customer managed KMS key used to encrypt the proxy's configuration content. This value is absent when the proxy uses the default service-owned key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[a-z-]+:kms:[a-z0-9-]+:[0-9]{12}:key/(mrk-)?[a-f0-9-]+`

 ** dnsName **
The DNS name of the proxy.
Type: String

 ** name **
The name of the proxy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `.*(^[a-zA-Z0-9]+$|^[a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]$).*`

 ** networkConfiguration **
The network configuration for the proxy.
Type: [ProxyNetworkConfiguration](API_ProxyNetworkConfiguration.md) object

 ** proxyVersion **
The version of the proxy software.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `\d+\.\d+`

 ** roleArn **
The Amazon Resource Name (ARN) of the IAM role that provides permissions to the code that your Envoy configuration runs on the proxy, such as filters and extensions. These are the permissions that this code needs when it calls AWS services.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[a-z-]+:iam::[0-9]{12}:role/.+`

 ** status **
The status of the proxy.
Type: [ProxyStatus](API_ProxyStatus.md) object

 ** type **
The type of proxy.
Type: String
Valid Values: `envoy`

## Errors
<a name="API_GetProxy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_GetProxy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elb-proxy-2026-11-20/GetProxy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elb-proxy-2026-11-20/GetProxy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elb-proxy-2026-11-20/GetProxy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elb-proxy-2026-11-20/GetProxy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elb-proxy-2026-11-20/GetProxy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elb-proxy-2026-11-20/GetProxy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elb-proxy-2026-11-20/GetProxy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elb-proxy-2026-11-20/GetProxy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elb-proxy-2026-11-20/GetProxy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elb-proxy-2026-11-20/GetProxy)

---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/elb-proxy/latest/APIReference/API_CreateProxy.html
---

# CreateProxy

Creates a proxy. A proxy is a fully managed, Envoy-based proxy that runs your Envoy configuration on Amazon EC2 instances inside your own virtual private cloud (VPC). AWS provisions and scales the proxy, upgrades the Envoy version, patches the operating system, and monitors its health.

## Request Parameters
<a name="API_CreateProxy_RequestParameters"></a>

 ** attributes **
The attributes for the proxy. Attributes can be changed after creation. Attributes that you don't specify are set to their default values.
Type: Array of [Attribute](API_Attribute.md) objects
Required: No

 ** clientToken **
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[!-~]+`
Required: No

 ** configuration **
The configuration for the proxy.
Type: [ProxyConfiguration](API_ProxyConfiguration.md) object
Required: Yes

 ** customerKmsKeyArn **
The Amazon Resource Name (ARN) of the customer managed KMS key used to encrypt the proxy's configuration content. If you don't specify a key, the default service-owned key is used.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[a-z-]+:kms:[a-z0-9-]+:[0-9]{12}:key/(mrk-)?[a-f0-9-]+`
Required: No

 ** name **
The name of the proxy. The name must be unique within your account for the Region. The valid characters are a-z, A-Z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `.*(^[a-zA-Z0-9]+$|^[a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]$).*`
Required: Yes

 ** networkConfiguration **
The network configuration for the proxy.
Type: [ProxyNetworkUserConfiguration](API_ProxyNetworkUserConfiguration.md) object
Required: Yes

 ** proxyVersion **
The version of the proxy software, in `major.minor` format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `\d+\.\d+`
Required: Yes

 ** roleArn **
The Amazon Resource Name (ARN) of the IAM role that provides permissions to the code that your Envoy configuration runs on the proxy, such as filters and extensions. These are the permissions that this code needs when it calls AWS services.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[a-z-]+:iam::[0-9]{12}:role/.+`
Required: Yes

 ** tags **
The tags for the proxy.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** type **
The type of proxy.
Type: String
Valid Values: `envoy`
Required: Yes

## Response Elements
<a name="API_CreateProxy_ResponseElements"></a>

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
<a name="API_CreateProxy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user does not have sufficient access to perform this action.
 ** message **
The error message.
HTTP Status Code: 403

 ** ConflictException **
The request conflicts with the current state of the resource.
 ** message **
The error message.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error occurred while processing the request.
 ** message **
The error message.
HTTP Status Code: 500

 ** OperationNotPermittedException **
The requested operation is not permitted.
 ** message **
The error message.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
The request would cause a service quota to be exceeded.
 ** message **
The error message.
 ** quotaCode **
The ID of the service quota that was exceeded.
 ** resourceId **
The ID of the resource that caused the service quota to be exceeded.
 ** resourceType **
The type of the resource that caused the service quota to be exceeded.
 ** serviceCode **
The code of the service associated with the exceeded quota.
HTTP Status Code: 402

 ** ThrottlingException **
The limit on the number of requests per second was exceeded.
 ** message **
The error message.
HTTP Status Code: 429

 ** ValidationError **
The input does not satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_CreateProxy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elb-proxy-2026-11-20/CreateProxy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elb-proxy-2026-11-20/CreateProxy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elb-proxy-2026-11-20/CreateProxy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elb-proxy-2026-11-20/CreateProxy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elb-proxy-2026-11-20/CreateProxy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elb-proxy-2026-11-20/CreateProxy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elb-proxy-2026-11-20/CreateProxy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elb-proxy-2026-11-20/CreateProxy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elb-proxy-2026-11-20/CreateProxy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elb-proxy-2026-11-20/CreateProxy)

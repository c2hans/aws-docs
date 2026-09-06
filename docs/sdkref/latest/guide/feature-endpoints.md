---
source_url: https://docs.aws.amazon.com/sdkref/latest/guide/feature-endpoints.html
---

# Dual-stack and FIPS endpoints
<a name="feature-endpoints"></a>

**Note**
For help in understanding the layout of settings pages, or in interpreting the **Support by AWS SDKs and tools** table that follows, see [Understanding the settings pages of this guide](settings-reference.md#settingsPages).

Configure this functionality by using the following:

**`use_dualstack_endpoint` - shared AWS `config` file setting`AWS_USE_DUALSTACK_ENDPOINT` - environment variable`aws.useDualstackEndpoint` - JVM system property: Java/Kotlin only**
Turns on or off whether the SDK will send requests to dual-stack endpoints. To learn more about dual-stack endpoints, which support both IPv4 and IPv6 traffic, see [Using Amazon S3 dual-stack endpoints](https://docs.aws.amazon.com/AmazonS3/latest/userguide/dual-stack-endpoints.html) in the *Amazon Simple Storage Service User Guide*. Dual-stack endpoints are available for some services in some regions.
**Default value:** `false`
**Valid values:**
+ **`true`** – The SDK or tool will attempt to use dual-stack endpoints to make network requests. If a dual-stack endpoint does not exist for the service and/or AWS Region, the request will fail.
+ **`false`** – The SDK or tool will not use dual-stack endpoints to make network requests.

**`use_fips_endpoint` - shared AWS `config` file setting`AWS_USE_FIPS_ENDPOINT` - environment variable`aws.useFipsEndpoint` - JVM system property: Java/Kotlin only**
Turns on or off whether the SDK or tool will send requests to FIPS-compliant endpoints. The Federal Information Processing Standards (FIPS) are a set of US Government security requirements for data and its encryption. Government agencies, partners, and those wanting to do business with the federal government are required to adhere to FIPS guidelines. Unlike standard AWS endpoints, FIPS endpoints use a TLS software library that is validated against FIPS 140. If this setting is enabled and a FIPS endpoint does not exist for the service in your AWS Region, the AWS call may fail. [Service-specific endpoints](feature-ss-endpoints.md) and the `--endpoint-url` option for the AWS Command Line Interface override this setting.
To learn more about other ways to specify FIPS endpoints by AWS Region, see [FIPS Endpoints by Service](https://aws.amazon.com/compliance/fips/). For more information on Amazon Elastic Compute Cloud service endpoints, see [Dual-stack (IPv4 and IPv6) endpoints](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Using_Endpoints.html#ipv6) in the *Amazon EC2 API Reference*.
**Default value:** `false`
**Valid values:**
+ **`true`** – The SDK or tool will send requests to FIPS-compliant endpoints.
+ **`false`** – The SDK or tool will not send requests to FIPS-compliant endpoints.

## Support by AWS SDKs and tools
<a name="endpoints-sdk-compat"></a>

The following SDKs support the features and settings described in this topic. Any partial exceptions are noted. Any JVM system property settings are supported by the AWS SDK for Java and the AWS SDK for Kotlin only.

| SDK | Supported | Notes or more information |
| --- | --- | --- |
| [AWS CLI v2](https://docs.aws.amazon.com/cli/latest/userguide/) | Yes |  |
| [SDK for C\+\+](https://docs.aws.amazon.com/sdk-for-cpp/latest/developer-guide/) | Yes |  |
| [SDK for Go V2 (1.x)](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/) | Yes |  |
| [SDK for Go 1.x (V1)](https://docs.aws.amazon.com/sdk-for-go/latest/developer-guide/) | Yes | To use shared config file settings, you must turn on loading from the config file; see [Sessions](https://docs.aws.amazon.com/sdk-for-go/api/aws/session/). |
| [SDK for Java 2.x](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/) | Yes |  |
| [SDK for Java 1.x](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/) | No |  |
| [SDK for JavaScript 3.x](https://docs.aws.amazon.com/sdk-for-javascript/latest/developer-guide/) | Yes |  |
| [SDK for JavaScript 2.x](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/) | Yes |  |
| [SDK for Kotlin](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/) | Yes |  |
| [SDK for .NET 4.x](https://docs.aws.amazon.com/sdk-for-net/latest/developer-guide/) | Yes |  |
| [SDK for .NET 3.x](https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/) | Yes |  |
| [SDK for PHP 3.x](https://docs.aws.amazon.com/sdk-for-php/latest/developer-guide/) | Yes |  |
| [SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/) | Yes |  |
| [SDK for Ruby 3.x](https://docs.aws.amazon.com/sdk-for-ruby/latest/developer-guide/) | Yes |  |
| [SDK for Rust](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/) | Yes |  |
| [SDK for Swift](https://docs.aws.amazon.com/sdk-for-swift/latest/developer-guide/) | Yes |  |
| [Tools for PowerShell V5](https://docs.aws.amazon.com/powershell/latest/userguide/) | Yes |  |
| [Tools for PowerShell V4](https://docs.aws.amazon.com/powershell/v4/userguide/) | Yes |  |

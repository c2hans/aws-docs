---
source_url: https://docs.aws.amazon.com/sdkref/latest/guide/feature-imds-client.html
---

# IMDS client
<a name="feature-imds-client"></a>

**Note**
For help in understanding the layout of settings pages, or in interpreting the **Support by AWS SDKs and tools** table that follows, see [Understanding the settings pages of this guide](settings-reference.md#settingsPages).

SDKs implement an Instance Metadata Service Version 2 (IMDSv2) client using session-oriented requests. For more information on IMDSv2, see [Use IMDSv2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html) in the *Amazon EC2 User Guide*. The IMDS client is configurable via a client configuration object available in the SDK code base.

Configure this functionality by using the following:

**`retries` - client configuration object member**
The number of additional retry attempts for any failed request.
**Default value:** 3
**Valid values:** Number greater than 0.

**`port` - client configuration object member**
The port for the endpoint.
**Default value:** 80
**Valid values:** Number.

**`token_ttl` - client configuration object member**
The TTL of the token.
**Default value:** 21,600 seconds (6 hours, the maximum time allotted).
**Valid values:** Number.

**`endpoint` - client configuration object member**
The endpoint of IMDS.
**Default value:** If `endpoint_mode` equals `IPv4`, then default endpoint is `http://169.254.169.254`. If `endpoint_mode` equals `IPv6`, then default endpoint is `http://[fd00:ec2::254]`.
**Valid values:** Valid URI.

The following options are supported by most SDKs. See your specific SDK code base for details.

**`endpoint_mode` - client configuration object member**
The endpoint mode of IMDS.
**Default value:** `IPv4`
**Valid values:** `IPv4`, `IPv6`

**`http_open_timeout` - client configuration object member (name may vary)**
The number of seconds to wait for the connection to open.
**Default value:** 1 second.
**Valid values:** Number greater than 0.

**`http_read_timeout` - client configuration object member (name may vary)**
The number of seconds for one chunk of data to be read.
**Default value:** 1 second.
**Valid values:** Number greater than 0.

**`http_debug_output` - client configuration object member (name may vary)**
Sets an output stream for debugging.
**Default value:** None.
**Valid values:** A valid I/O stream, like STDOUT.

**`backoff` - client configuration object member (name may vary)**
The number of seconds to sleep in between retries or a customer provided backoff function to call. This overrides the default exponential backoff strategy.
**Default value:** Varies by SDK.
**Valid values:** Varies by SDK. Can be either a numeric value or a call out to a custom function.

## Support by AWS SDKs and tools
<a name="feature-imds-client-sdk-compat"></a>

The following SDKs support the features and settings described in this topic. Any partial exceptions are noted. Any JVM system property settings are supported by the AWS SDK for Java and the AWS SDK for Kotlin only.

| SDK | Supported | Notes or more information |
| --- | --- | --- |
| [AWS CLI v2](https://docs.aws.amazon.com/cli/latest/userguide/) | Yes |  |
| [SDK for C\+\+](https://docs.aws.amazon.com/sdk-for-cpp/latest/developer-guide/) | No |  |
| [SDK for Go V2 (1.x)](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/) | Yes |  |
| [SDK for Go 1.x (V1)](https://docs.aws.amazon.com/sdk-for-go/latest/developer-guide/) | Yes |  |
| [SDK for Java 2.x](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/) | Yes |  |
| [SDK for Java 1.x](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/) | Yes |  |
| [SDK for JavaScript 3.x](https://docs.aws.amazon.com/sdk-for-javascript/latest/developer-guide/) | Yes |  |
| [SDK for JavaScript 2.x](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/) | Yes |  |
| [SDK for Kotlin](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/) | No |  |
| [SDK for .NET 4.x](https://docs.aws.amazon.com/sdk-for-net/latest/developer-guide/) | Yes |  |
| [SDK for .NET 3.x](https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/) | Yes |  |
| [SDK for PHP 3.x](https://docs.aws.amazon.com/sdk-for-php/latest/developer-guide/) | Yes |  |
| [SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/) | Yes |  |
| [SDK for Ruby 3.x](https://docs.aws.amazon.com/sdk-for-ruby/latest/developer-guide/) | Yes |  |
| [SDK for Rust](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/) | Yes |  |
| [SDK for Swift](https://docs.aws.amazon.com/sdk-for-swift/latest/developer-guide/) | Yes |  |
| [Tools for PowerShell V5](https://docs.aws.amazon.com/powershell/latest/userguide/) | Yes |  |
| [Tools for PowerShell V4](https://docs.aws.amazon.com/powershell/v4/userguide/) | Yes |  |

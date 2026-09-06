---
source_url: https://docs.aws.amazon.com/sdkref/latest/guide/feature-s3-express.html
---

# S3 Express One Zone session authentication
<a name="feature-s3-express"></a>

**Note**
For help in understanding the layout of settings pages, or in interpreting the **Support by AWS SDKs and tools** table that follows, see [Understanding the settings pages of this guide](settings-reference.md#settingsPages).

S3 Express One Zone is Amazon S3's high-performance storage class that provides single-digit millisecond latency for frequently accessed data. When you use S3 Express One Zone buckets, AWS SDKs and tools automatically use session-based authentication that is optimized for low-latency authorization of data requests. You use session tokens with Zonal (object-level) operations to distribute the latency that's associated with authorization over a number of requests in a session, reducing the authentication overhead and improving overall request performance.

S3 Express One Zone buckets use a specific naming format that includes the Availability Zone ID, such as `bucket-name--usw2-az1--x-s3`. When the SDK detects this naming pattern, it automatically routes requests to the appropriate S3 Express One Zone endpoints and applies the optimized authentication flow. The session authentication creates temporary, bucket-specific credentials that provide low-latency access to your bucket and are cached and refreshed automatically by the SDK. See [S3 Express One Zone](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-high-performance.html#s3-express-one-zone) in the *Amazon S3 User Guide* to learn more.

By default, session authentication is enabled for S3 Express One Zone buckets.

Configure this functionality by using the following:

**`s3_disable_express_session_auth` - shared AWS `config` file setting`AWS_S3_DISABLE_EXPRESS_SESSION_AUTH` - environment variable`aws.disableS3ExpressAuth` - JVM system property: Java/Kotlin only**
Controls whether S3 Express One Zone session authentication is disabled. When set to `true`, the SDK uses standard SigV4 authentication for S3 Express One Zone buckets instead of session authentication.
**Default value:** `false`
**Valid values:**
+ **`true`** – Disable S3 Express One Zone session authentication.
+ **`false`** – Enable S3 Express One Zone session authentication.

Example of setting this value in the `config` file:

```
[default]
s3_disable_express_session_auth=true
```

Linux/macOS example of setting environment variables via command line:

```
export AWS_S3_DISABLE_EXPRESS_SESSION_AUTH=true
```

Windows example of setting environment variables via command line:

```
setx AWS_S3_DISABLE_EXPRESS_SESSION_AUTH true
```

## Support by AWS SDKs and tools
<a name="s3-express-sdk-compat"></a>

The following SDKs support the features and settings described in this topic. Any partial exceptions are noted. Any JVM system property settings are supported by the AWS SDK for Java and the AWS SDK for Kotlin only.

| SDK | Supported | Notes or more information |
| --- | --- | --- |
| [AWS CLI v2](https://docs.aws.amazon.com/cli/latest/userguide/) | Yes |  |
| [AWS CLI v1](https://docs.aws.amazon.com/cli/v1/userguide/cli-chap-welcome.html) | Yes |  |
| [SDK for C\+\+](https://docs.aws.amazon.com/sdk-for-cpp/latest/developer-guide/) | Yes |  |
| [SDK for Go V2 (1.x)](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/) | Yes |  |
| [SDK for Go 1.x (V1)](https://docs.aws.amazon.com/sdk-for-go/latest/developer-guide/) | No | To use shared config file settings, you must turn on loading from the config file; see [Sessions](https://docs.aws.amazon.com/sdk-for-go/api/aws/session/). |
| [SDK for Java 2.x](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/) | Yes |  |
| [SDK for Java 1.x](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/) | No |  |
| [SDK for JavaScript 3.x](https://docs.aws.amazon.com/sdk-for-javascript/latest/developer-guide/) | Yes |  |
| [SDK for JavaScript 2.x](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/) | No |  |
| [SDK for Kotlin](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/) | Yes | The JVM system property is aws.s3DisableExpressSessionAuth. |
| [SDK for .NET 4.x](https://docs.aws.amazon.com/sdk-for-net/latest/developer-guide/) | Yes |  |
| [SDK for .NET 3.x](https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/) | Yes |  |
| [SDK for PHP 3.x](https://docs.aws.amazon.com/sdk-for-php/latest/developer-guide/) | Yes |  |
| [SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/) | Yes |  |
| [SDK for Ruby 3.x](https://docs.aws.amazon.com/sdk-for-ruby/latest/developer-guide/) | Yes |  |
| [SDK for Rust](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/) | Yes |  |
| [SDK for Swift](https://docs.aws.amazon.com/sdk-for-swift/latest/developer-guide/) | Yes |  |
| [Tools for PowerShell V5](https://docs.aws.amazon.com/powershell/latest/userguide/) | Yes |  |
| [Tools for PowerShell V4](https://docs.aws.amazon.com/powershell/v4/userguide/) | Yes |  |

---
source_url: https://docs.aws.amazon.com/sdkref/latest/guide/feature-smart-config-defaults.html
---

# Smart configuration defaults
<a name="feature-smart-config-defaults"></a>

**Note**
For help in understanding the layout of settings pages, or in interpreting the **Support by AWS SDKs and tools** table that follows, see [Understanding the settings pages of this guide](settings-reference.md#settingsPages).

With the smart configuration defaults feature, AWS SDKs can provide predefined, optimized default values for other configuration settings.

Configure this functionality by using the following:

**`defaults_mode` - shared AWS `config` file setting`AWS_DEFAULTS_MODE` - environment variable`aws.defaultsMode` - JVM system property: Java/Kotlin only**
With this setting, you can choose a mode that aligns with your application architecture, which then provides optimized default values for your application. If an AWS SDK setting has a value explicitly set, then that value always takes precedence. If an AWS SDK setting does not have a value explicitly set, and `defaults_mode` is not equal to legacy, then this feature can provide different default values for various settings optimized for your application. Settings may include the following: HTTP communication settings, retry behavior, service Regional endpoint settings, and, potentially, any SDK-related configuration. Customers who use this feature can get new configuration defaults tailored to common usage scenarios. If your `defaults_mode` is not equal to `legacy`, we recommend performing tests of your application when you upgrade the SDK, because the default values provided might change as best practices evolve.
**Default value:** `legacy`
Note: New major versions of SDKs will default to `standard`.
**Valid values:**
+ `legacy` – Provides default settings that vary by SDK and existed before establishment of `defaults_mode`.
+ `standard` – Provides the latest recommended default values that should be safe to run in most scenarios.
+ `in-region` – Builds on the standard mode and includes optimization tailored for applications that call AWS services from within the same AWS Region.
+ `cross-region` – Builds on the standard mode and includes optimization tailored for applications that call AWS services in a different Region.
+ `mobile` – Builds on the standard mode and includes optimization tailored for mobile applications.
+ `auto` – Builds on the standard mode and includes experimental features. The SDK attempts to discover the runtime environment to determine the appropriate settings automatically. The auto detection is heuristics-based and does not provide 100% accuracy. If the runtime environment can't be determined, `standard` mode is used. The auto detection might query [instance metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html), which might introduce latency. If startup latency is critical to your application, we recommend choosing an explicit `defaults_mode` instead.
 Example of setting this value in the `config` file:

```
[default]
defaults_mode = standard
```
The following parameters might be optimized based on the selection of `defaults_mode`:
+ `retryMode` – Specifies how the SDK attempts retries. See [Retry behavior](feature-retry-behavior.md).
+ `stsRegionalEndpoints` – Specifies how the SDK determines the AWS service endpoint that it uses to talk to the AWS Security Token Service (AWS STS). See [AWS STS Regional endpoints](feature-sts-regionalized-endpoints.md).
+ `s3UsEast1RegionalEndpoints` – Specifies how the SDK determines the AWS service endpoint that it uses to talk to the Amazon S3 for the `us-east-1` Region.
+ `connectTimeoutInMillis` – After making an initial connection attempt on a socket, the amount of time before timing out. If the client does not receive a completion of the connect handshake, the client gives up and fails the operation.
+ `tlsNegotiationTimeoutInMillis` – The maximum amount of time that a TLS handshake can take from the time the CLIENT HELLO message is sent to the time the client and server have fully negotiated ciphers and exchanged keys.

The default value for each setting changes depending on the `defaults_mode` selected for your application. These values are currently set as follows (subject to change):

| Parameter | `standard` mode | `in-region` mode | `cross-region` mode | `mobile` mode |
| --- | --- | --- | --- | --- |
|  retryMode  | standard | standard | standard | standard |
|  stsRegionalEndpoints  | regional | regional | regional | regional |
|  s3UsEast1RegionalEndpoints  | regional | regional | regional | regional |
|  connectTimeoutInMillis  | 3100 | 1100 | 3100 | 30000 |
|  tlsNegotiationTimeoutInMillis  | 3100 | 1100 | 3100 | 30000 |

For example, if the `defaults_mode` you selected was `standard`, then the value of `standard` would be assigned for `retry_mode` (from the valid `retry_mode` options) and the value of `regional` would be assigned for `stsRegionalEndpoints` (from the valid `stsRegionalEndpoints` options).

## Support by AWS SDKs and tools
<a name="feature-smart-config-defaults-sdk-compat"></a>

The following SDKs support the features and settings described in this topic. Any partial exceptions are noted. Any JVM system property settings are supported by the AWS SDK for Java and the AWS SDK for Kotlin only.

| SDK | Supported | Notes or more information |
| --- | --- | --- |
| [AWS CLI v2](https://docs.aws.amazon.com/cli/latest/userguide/) | No |  |
| [SDK for C\+\+](https://docs.aws.amazon.com/sdk-for-cpp/latest/developer-guide/) |  Yes | Parameters not optimized: stsRegionalEndpoints, s3UsEast1RegionalEndpoints, tlsNegotiationTimeoutInMillis. |
| [SDK for Go V2 (1.x)](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/) | Yes | Parameters not optimized: retryMode, stsRegionalEndpoints, s3UsEast1RegionalEndpoints. |
| [SDK for Go 1.x (V1)](https://docs.aws.amazon.com/sdk-for-go/latest/developer-guide/) | No |  |
| [SDK for Java 2.x](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/) | Yes | Parameters not optimized: stsRegionalEndpoints. |
| [SDK for Java 1.x](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/) | No |  |
| [SDK for JavaScript 3.x](https://docs.aws.amazon.com/sdk-for-javascript/latest/developer-guide/) | Yes | Parameters not optimized: stsRegionalEndpoints, s3UsEast1RegionalEndpoints, tlsNegotiationTimeoutInMillis. connectTimeoutInMillis is called connectionTimeout. |
| [SDK for JavaScript 2.x](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/) | No |  |
| [SDK for Kotlin](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/) | No |  |
| [SDK for .NET 4.x](https://docs.aws.amazon.com/sdk-for-net/latest/developer-guide/) | Yes | Parameters not optimized: connectTimeoutInMillis, tlsNegotiationTimeoutInMillis. |
| [SDK for .NET 3.x](https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/) | Yes | Parameters not optimized: connectTimeoutInMillis, tlsNegotiationTimeoutInMillis. |
| [SDK for PHP 3.x](https://docs.aws.amazon.com/sdk-for-php/latest/developer-guide/) | Yes | Parameters not optimized: tlsNegotiationTimeoutInMillis. |
| [SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/) | Yes | Parameters not optimized: tlsNegotiationTimeoutInMillis. |
| [SDK for Ruby 3.x](https://docs.aws.amazon.com/sdk-for-ruby/latest/developer-guide/) | Yes |   |
| [SDK for Rust](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/) | No |  |
| [SDK for Swift](https://docs.aws.amazon.com/sdk-for-swift/latest/developer-guide/) | No |  |
| [Tools for PowerShell V5](https://docs.aws.amazon.com/powershell/latest/userguide/) | Yes | Parameters not optimized: connectTimeoutInMillis, tlsNegotiationTimeoutInMillis. |
| [Tools for PowerShell V4](https://docs.aws.amazon.com/powershell/v4/userguide/) | Yes | Parameters not optimized: connectTimeoutInMillis, tlsNegotiationTimeoutInMillis. |

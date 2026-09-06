---
source_url: https://docs.aws.amazon.com/sdkref/latest/guide/feature-auth-scheme.html
---

# Authentication scheme
<a name="feature-auth-scheme"></a>

**Note**
For help in understanding the layout of settings pages, or in interpreting the **Support by AWS SDKs and tools** table that follows, see [Understanding the settings pages of this guide](settings-reference.md#settingsPages).

AWS services support multiple authentication schemes, such as AWS Signature Version 4 (SigV4) and AWS Signature Version 4a (SigV4a). By default, SDKs select authentication schemes based on service model definitions and prioritize schemes that provide the best compatibility. However, you can configure your preferred authentication scheme to optimize for specific requirements.

Unlike SigV4, requests signed with SigV4a are valid in multiple AWS Regions. SigV4a provides enhanced availability through cross-region request signing, which enables automatic failover to backup regions during regional disruptions. This is particularly beneficial for global services like AWS Identity and Access Management or Amazon CloudFront.

For more information on these two authentication schemes, see [AWS Signature Version 4 for API requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html) in the *IAM User Guide*.

Configure this functionality by using the following:

**`auth_scheme_preference` - shared AWS `config` file setting`AWS_AUTH_SCHEME_PREFERENCE` - environment variable`aws.authSchemePreference` - JVM system property: Java/Kotlin only**
Specifies a comma-separated list of preferred authentication schemes in priority order. When a service supports multiple authentication schemes, the SDK attempts to use schemes from this list in the specified order, falling back to default behavior if none of the preferred schemes are available.
**Default value:** None.
**Valid values:** A comma-separated list of one or more of the following:
+ **`sigv4`** – Signature Version 4 (fastest performance, single-region)
+ **`sigv4a`** – Signature Version 4a (enhanced availability, cross-region support, has a slower signing performance than SigV4)
+ **`httpBearerAuth`** – HTTP Bearer token authentication
Space and tab characters between scheme names are ignored.
Example of setting this value in the `config` file to prefer SigV4a:

```
[default]
auth_scheme_preference=sigv4a,sigv4
```

**`sigv4a_signing_region_set` - shared AWS `config` file setting`AWS_SIGV4A_SIGNING_REGION_SET` - environment variable**
Specifies comma-separated list of AWS Regions for SigV4a multi-region signing. This is used as the default Region set for the request if SigV4a is the selected authentication scheme.
**Default value:** Determined by the request.
**Valid values:** Comma-separated list of AWS Regions. Space and tab characters between Regions are ignored.

## Support by AWS SDKs and tools
<a name="auth-scheme-sdk-compat"></a>

The following SDKs support the features and settings described in this topic. Any partial exceptions are noted. Any JVM system property settings are supported by the AWS SDK for Java and the AWS SDK for Kotlin only.

| SDK | Supported | Notes or more information |
| --- | --- | --- |
| [AWS CLI v2](https://docs.aws.amazon.com/cli/latest/userguide/) | Yes |  |
| [SDK for C\+\+](https://docs.aws.amazon.com/sdk-for-cpp/latest/developer-guide/) | Yes |  |
| [SDK for Go V2 (1.x)](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/) | Yes |  |
| [SDK for Go 1.x (V1)](https://docs.aws.amazon.com/sdk-for-go/latest/developer-guide/) | No |  |
| [SDK for Java 2.x](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/) | Yes |  |
| [SDK for Java 1.x](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/) | No |  |
| [SDK for JavaScript 3.x](https://docs.aws.amazon.com/sdk-for-javascript/latest/developer-guide/) | Yes |  |
| [SDK for JavaScript 2.x](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/) | No |  |
| [SDK for Kotlin](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/) | Yes |  |
| [SDK for .NET 4.x](https://docs.aws.amazon.com/sdk-for-net/latest/developer-guide/) | Yes |  |
| [SDK for .NET 3.x](https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/) | No |  |
| [SDK for PHP 3.x](https://docs.aws.amazon.com/sdk-for-php/latest/developer-guide/) | Yes |  |
| [SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/) | Yes |  |
| [SDK for Ruby 3.x](https://docs.aws.amazon.com/sdk-for-ruby/latest/developer-guide/) | Yes |  |
| [SDK for Rust](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/) | Yes |  |
| [SDK for Swift](https://docs.aws.amazon.com/sdk-for-swift/latest/developer-guide/) | Yes |  |
| [Tools for PowerShell V5](https://docs.aws.amazon.com/powershell/latest/userguide/) | Yes |  |
| [Tools for PowerShell V4](https://docs.aws.amazon.com/powershell/v4/userguide/) | No |  |

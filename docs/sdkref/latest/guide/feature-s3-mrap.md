---
source_url: https://docs.aws.amazon.com/sdkref/latest/guide/feature-s3-mrap.html
---

# Amazon S3 Multi-Region Access Points
<a name="feature-s3-mrap"></a>

**Note**
For help in understanding the layout of settings pages, or in interpreting the **Support by AWS SDKs and tools** table that follows, see [Understanding the settings pages of this guide](settings-reference.md#settingsPages).

Amazon S3 Multi-Region Access Points provide a global endpoint that applications can use to fulfill requests from Amazon S3 buckets located in multiple AWS Regions. You can use Multi-Region Access Points to build multi-Region applications with the same architecture used in a single Region, and then run those applications anywhere in the world.

To learn more about Multi-Region Access Points, see [Multi-Region Access Points in Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiRegionAccessPoints.html) in the *Amazon S3 User Guide*.

To learn more about Multi-Region Access Point Amazon Resource Names (ARNs), see [Making requests using a Multi-Region Access Point](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiRegionAccessPointRequests.html) in the *Amazon S3 User Guide*.

To learn more about creating Multi-Region Access Points, see [Managing Multi-Region Access Points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ManagingMultiRegionAccessPoints.html) in the *Amazon S3 User Guide*.

The SigV4A algorithm is the signing implementation used to sign the global Region requests. This algorithm is obtained by the SDK through a dependency on the [AWS Common Runtime (CRT) libraries](common-runtime.md).

Configure this functionality by using the following:

**`s3_disable_multiregion_access_points` - shared AWS `config` file setting`AWS_S3_DISABLE_MULTIREGION_ACCESS_POINTS` - environment variable`aws.s3DisableMultiRegionAccessPoints` - JVM system property: Java/Kotlin onlyTo configure value directly in code, consult your specific SDK directly. **
This setting controls whether the SDK potentially attempts cross-Region requests. If multiply defined, the code-configured setting takes precedence, followed by the environment variable setting.
**Default value:** `false`
**Valid values:**
+ **`true`** – Stops the use of cross-Region requests.
+ **`false`** – Enables cross-Region requests using Multi-Region Access Points.

## Support by AWS SDKs and tools
<a name="s3-mrap-sdk-compat"></a>

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
| [SDK for .NET 3.x](https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/) | Yes |  |
| [SDK for PHP 3.x](https://docs.aws.amazon.com/sdk-for-php/latest/developer-guide/) | Yes |  |
| [SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/) | Yes |  |
| [SDK for Ruby 3.x](https://docs.aws.amazon.com/sdk-for-ruby/latest/developer-guide/) | Yes |  |
| [SDK for Rust](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/) | Yes |  |
| [SDK for Swift](https://docs.aws.amazon.com/sdk-for-swift/latest/developer-guide/) | No |  |
| [Tools for PowerShell V5](https://docs.aws.amazon.com/powershell/latest/userguide/) | Yes |  |
| [Tools for PowerShell V4](https://docs.aws.amazon.com/powershell/v4/userguide/) | Yes |  |

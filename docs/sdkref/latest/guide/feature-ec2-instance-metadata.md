---
source_url: https://docs.aws.amazon.com/sdkref/latest/guide/feature-ec2-instance-metadata.html
---

# Amazon EC2 instance metadata
<a name="feature-ec2-instance-metadata"></a>

**Note**
For help in understanding the layout of settings pages, or in interpreting the **Support by AWS SDKs and tools** table that follows, see [Understanding the settings pages of this guide](settings-reference.md#settingsPages).

Amazon EC2 provides a service on instances called the Instance Metadata Service (IMDS). To learn more about this service, see [Work with instance metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html) in the *Amazon EC2 User Guide*. When attempting to retrieve credentials on an Amazon EC2 instance that has been configured with an IAM role, the connection to the instance metadata service is adjustable.

Configure this functionality by using the following:

**`metadata_service_num_attempts` - shared AWS `config` file setting`AWS_METADATA_SERVICE_NUM_ATTEMPTS` - environment variable**
This setting specifies the number of total attempts to make before giving up when attempting to retrieve data from the instance metadata service.
**Default value:** 1
**Valid values:** Number greater than or equal to 1.

**`metadata_service_timeout` - shared AWS `config` file setting`AWS_METADATA_SERVICE_TIMEOUT` - environment variable**
Specifies the number of seconds before timing out when attempting to retrieve data from the instance metadata service.
**Default value:** 1
**Valid values:** Number greater than or equal to 1.

Example of setting these values in the `config` file:

```
[default]
metadata_service_num_attempts={{10}}
metadata_service_timeout={{10}}
```

Linux/macOS example of setting environment variables via command line:

```
export AWS_METADATA_SERVICE_NUM_ATTEMPTS={{10}}
export AWS_METADATA_SERVICE_TIMEOUT={{10}}
```

Windows example of setting environment variables via command line:

```
setx AWS_METADATA_SERVICE_NUM_ATTEMPTS {{10}}
setx AWS_METADATA_SERVICE_TIMEOUT {{10}}
```

## Support by AWS SDKs and tools
<a name="feature-ec2-instance-metadata-sdk-compat"></a>

The following SDKs support the features and settings described in this topic. Any partial exceptions are noted. Any JVM system property settings are supported by the AWS SDK for Java and the AWS SDK for Kotlin only.

| SDK | Supported | Notes or more information |
| --- | --- | --- |
| [AWS CLI v2](https://docs.aws.amazon.com/cli/latest/userguide/) | Yes |  |
| [SDK for C\+\+](https://docs.aws.amazon.com/sdk-for-cpp/latest/developer-guide/) | No |  |
| [SDK for Go V2 (1.x)](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/) | No |  |
| [SDK for Go 1.x (V1)](https://docs.aws.amazon.com/sdk-for-go/latest/developer-guide/) | No |  |
| [SDK for Java 2.x](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/) | Partial | Only AWS\_METADATA\_SERVICE\_TIMEOUT is supported. |
| [SDK for Java 1.x](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/) | Partial | Only AWS\_METADATA\_SERVICE\_TIMEOUT is supported. |
| [SDK for JavaScript 3.x](https://docs.aws.amazon.com/sdk-for-javascript/latest/developer-guide/) | No |  |
| [SDK for JavaScript 2.x](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/) | No |  |
| [SDK for Kotlin](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/) | No |  |
| [SDK for .NET 4.x](https://docs.aws.amazon.com/sdk-for-net/latest/developer-guide/) | No |  |
| [SDK for .NET 3.x](https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/) | No |  |
| [SDK for PHP 3.x](https://docs.aws.amazon.com/sdk-for-php/latest/developer-guide/) | Yes |  |
| [SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/) | Yes |  |
| [SDK for Ruby 3.x](https://docs.aws.amazon.com/sdk-for-ruby/latest/developer-guide/) | No |  |
| [SDK for Rust](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/) | No |  |
| [SDK for Swift](https://docs.aws.amazon.com/sdk-for-swift/latest/developer-guide/) | No |  |
| [Tools for PowerShell V5](https://docs.aws.amazon.com/powershell/latest/userguide/) | No |  |
| [Tools for PowerShell V4](https://docs.aws.amazon.com/powershell/v4/userguide/) | No |  |

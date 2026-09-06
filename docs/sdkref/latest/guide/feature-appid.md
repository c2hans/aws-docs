---
source_url: https://docs.aws.amazon.com/sdkref/latest/guide/feature-appid.html
---

# Application ID
<a name="feature-appid"></a>

**Note**
For help in understanding the layout of settings pages, or in interpreting the **Support by AWS SDKs and tools** table that follows, see [Understanding the settings pages of this guide](settings-reference.md#settingsPages).

A single AWS account can be used by multiple customer applications to make calls to AWS services. Application ID provides a way for customers to identify which source application made a set of calls using an AWS account. AWS SDKs and services don't use or interpret this value other than to surface it back in customer communications. For example, this value can be included in operational emails or in the AWS Health Dashboard to uniquely identify which of your applications is associated with the notification.

Configure this functionality by using the following:

**`sdk_ua_app_id` - shared AWS `config` file setting`AWS_SDK_UA_APP_ID` - environment variable`sdk.ua.appId` - JVM system property: Java/Kotlin only**
This setting is a unique string you assign to your application to identify which of your applications within a particular AWS account makes calls to AWS.
**Default value:** `None`
**Valid values:** String with maximum length of 50. Letters, numbers and the following special characters are allowed: `!`,`#`,`$`,`%`,`&`,`'`,`*`,`+`,`-`,`.`,`^`,`_`,```,`|`,`~`.

Example of setting this value in the `config` file:

```
[default]
sdk_ua_app_id=ABCDEF
```

Linux/macOS example of setting environment variables via command line:

```
export AWS_SDK_UA_APP_ID=ABCDEF
export AWS_SDK_UA_APP_ID="ABC DEF"
```

Windows example of setting environment variables via command line:

```
setx AWS_SDK_UA_APP_ID ABCDEF
setx AWS_SDK_UA_APP_ID="ABC DEF"
```

If you include symbols that have a special meaning to the shell being used, escape the value as appropriate.

## Support by AWS SDKs and tools
<a name="appid-sdk-compat"></a>

The following SDKs support the features and settings described in this topic. Any partial exceptions are noted. Any JVM system property settings are supported by the AWS SDK for Java and the AWS SDK for Kotlin only.

| SDK | Supported | Notes or more information |
| --- | --- | --- |
| [AWS CLI v2](https://docs.aws.amazon.com/cli/latest/userguide/) | Yes |  |
| [SDK for C\+\+](https://docs.aws.amazon.com/sdk-for-cpp/latest/developer-guide/) | Yes | shared config file not supported. |
| [SDK for Go V2 (1.x)](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/) | Yes |  |
| [SDK for Go 1.x (V1)](https://docs.aws.amazon.com/sdk-for-go/latest/developer-guide/) | No |  |
| [SDK for Java 2.x](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/) | Yes |  |
| [SDK for Java 1.x](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/) | No |  |
| [SDK for JavaScript 3.x](https://docs.aws.amazon.com/sdk-for-javascript/latest/developer-guide/) | Yes |  |
| [SDK for JavaScript 2.x](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/) | No |  |
| [SDK for Kotlin](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/) | Yes | The JVM system property is aws.userAgentAppId. |
| [SDK for .NET 4.x](https://docs.aws.amazon.com/sdk-for-net/latest/developer-guide/) | Yes |  |
| [SDK for .NET 3.x](https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/) | Yes |  |
| [SDK for PHP 3.x](https://docs.aws.amazon.com/sdk-for-php/latest/developer-guide/) | Yes |  |
| [SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/) | Yes |  |
| [SDK for Ruby 3.x](https://docs.aws.amazon.com/sdk-for-ruby/latest/developer-guide/) | Yes |  |
| [SDK for Rust](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/) | Yes |  |
| [SDK for Swift](https://docs.aws.amazon.com/sdk-for-swift/latest/developer-guide/) | Yes |  |
| [Tools for PowerShell V5](https://docs.aws.amazon.com/powershell/latest/userguide/) | Yes |  |
| [Tools for PowerShell V4](https://docs.aws.amazon.com/powershell/v4/userguide/) | Yes |  |

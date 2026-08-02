---
source_url: https://docs.aws.amazon.com/sdkref/latest/guide/feature-gen-config.html
---

# General configuration settings
<a name="feature-gen-config"></a>

**Note**
For help in understanding the layout of settings pages, or in interpreting the **Support by AWS SDKs and tools** table that follows, see [Understanding the settings pages of this guide](settings-reference.md#settingsPages).

SDKs support some general settings that configure overall SDK behaviors.

Configure this functionality by using the following:

**`api_versions` - shared AWS `config` file setting**
Some AWS services maintain multiple API versions to support backward compatibility. By default, SDK and AWS CLI operations use the latest available API version. To require a specific API version to use for your requests, include the `api_versions` setting in your profile.
**Default value:** None. (Latest API version is used by the SDK.)
**Valid values:** This is a nested setting that's followed by one or more indented lines that each identify one AWS service and the API version to use. See the documentation for the AWS service to understand which API versions are available.
 The example sets a specific API version for two AWS services in the `config` file. These API versions are used only for commands that run under the profile that contains these settings. Commands for any other service use the latest version of that service's API.

```
api_versions =
    ec2 = {{2015-03-01}}
    cloudfront = {{2015-09-017}}
```

**`ca_bundle` - shared AWS `config` file setting`AWS_CA_BUNDLE` - environment variable**
Specifies the path to a custom certificate bundle (a file with a `.pem` extension) to use when establishing SSL/TLS connections.
**Default value:** none
**Valid values:** Specify either the full path or a base file name. If there is a base file name, the system attempts to find the program within folders specified by the `PATH` environment variable.
 Example of setting this value in the `config` file:

```
[default]
ca_bundle = {{dev/apps/ca-certs/cabundle-2019mar05.pem}}
```
Due to differences in how operating systems handle paths and escaping of path characters, the following is an example of setting this value in the `config` file on Windows:

```
[default]
ca_bundle = {{C:\\Users\\username\\.aws\\aws-custom-bundle.pem}}
```
Linux/macOS example of setting environment variables via command line:

```
export AWS_CA_BUNDLE={{/dev/apps/ca-certs/cabundle-2019mar05.pem}}
```
Windows example of setting environment variables via command line:

```
setx AWS_CA_BUNDLE {{C:\dev\apps\ca-certs\cabundle-2019mar05.pem}}
```

**`output` - shared AWS `config` file setting**
Specifies how results are formatted in the AWS CLI and other AWS SDKs and tools.
**Default value:** `json`
**Valid values:**
+ **[https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-output-format.html#json-output](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-output-format.html#json-output)** – The output is formatted as a [JSON](https://json.org/) string.
+  **[https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-output-format.html#yaml-output](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-output-format.html#yaml-output)** – The output is formatted as a [YAML](https://yaml.org/) string.
+ **[https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-output-format.html#yaml-stream-output](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-output-format.html#yaml-stream-output)** – The output is streamed and formatted as a [YAML](https://yaml.org/) string. Streaming allows for faster handling of large data types.
+ **[https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-output-format.html#text-output](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-output-format.html#text-output)** – The output is formatted as multiple lines of tab-separated string values. This can be useful to pass the output to a text processor, like `grep`, `sed`, or `awk`.
+ **[https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-output-format.html#table-output](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-output-format.html#table-output)** – The output is formatted as a table using the characters \+\|- to form the cell borders. It typically presents the information in a "human-friendly" format that is much easier to read than the others, but not as programmatically useful.

**`parameter_validation` - shared AWS `config` file setting**
Specifies whether the SDK or tool attempts to validate command line parameters before sending them to the AWS service endpoint.
**Default value:** `true`
**Valid values:**
+ **`true`** – The default. The SDK or tool performs client-side validation of command line parameters. This helps the SDK or tool confirm that parameters are valid, and catches some errors. The SDK or tool can reject requests that aren't valid before sending requests to the AWS service endpoint.
+  **`false`** – The SDK or tool doesn't validate command line parameters before sending them to the AWS service endpoint. The AWS service endpoint is responsible for validating all requests and rejecting requests that aren't valid.

## Support by AWS SDKs and tools
<a name="feature-gen-config-sdk-compat"></a>

The following SDKs support the features and settings described in this topic. Any partial exceptions are noted. Any JVM system property settings are supported by the AWS SDK for Java and the AWS SDK for Kotlin only.

| SDK | Supported | Notes or more information |
| --- | --- | --- |
| [AWS CLI v2](https://docs.aws.amazon.com/cli/latest/userguide/) | Partial | api\_versions not supported. |
| [SDK for C\+\+](https://docs.aws.amazon.com/sdk-for-cpp/latest/developer-guide/) | Yes |  |
| [SDK for Go V2 (1.x)](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/) | Partial | api\_versions and parameter\_validation not supported. |
| [SDK for Go 1.x (V1)](https://docs.aws.amazon.com/sdk-for-go/latest/developer-guide/) | Partial | api\_versions and parameter\_validation not supported. To use shared config file settings, you must turn on loading from the config file; see [Sessions](https://docs.aws.amazon.com/sdk-for-go/api/aws/session/). |
| [SDK for Java 2.x](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/) | No |  |
| [SDK for Java 1.x](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/) | No |  |
| [SDK for JavaScript 3.x](https://docs.aws.amazon.com/sdk-for-javascript/latest/developer-guide/) | Yes |  |
| [SDK for JavaScript 2.x](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/) | Yes |  |
| [SDK for Kotlin](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/) | No |  |
| [SDK for .NET 4.x](https://docs.aws.amazon.com/sdk-for-net/latest/developer-guide/) | No |  |
| [SDK for .NET 3.x](https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/) | No |  |
| [SDK for PHP 3.x](https://docs.aws.amazon.com/sdk-for-php/latest/developer-guide/) | Yes |  |
| [SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/) | Yes |  |
| [SDK for Ruby 3.x](https://docs.aws.amazon.com/sdk-for-ruby/latest/developer-guide/) | Yes |  |
| [SDK for Rust](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/) | No |  |
| [SDK for Swift](https://docs.aws.amazon.com/sdk-for-swift/latest/developer-guide/) | No |  |
| [Tools for PowerShell V5](https://docs.aws.amazon.com/powershell/latest/userguide/) | No |  |
| [Tools for PowerShell V4](https://docs.aws.amazon.com/powershell/v4/userguide/) | No |  |

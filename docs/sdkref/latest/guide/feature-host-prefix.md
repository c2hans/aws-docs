---
source_url: https://docs.aws.amazon.com/sdkref/latest/guide/feature-host-prefix.html
---

# Host prefix injection
<a name="feature-host-prefix"></a>

**Note**
For help in understanding the layout of settings pages, or in interpreting the **Support by AWS SDKs and tools** table that follows, see [Understanding the settings pages of this guide](settings-reference.md#settingsPages).

Host prefix injection is a feature where AWS SDKs automatically prepend a prefix to the hostname of service endpoints for certain API operations. This prefix can be either a static string or a dynamic value that includes data from your request parameters.

For example, when using Amazon Simple Storage Service to perform actions on Amazon S3 objects or buckets, the SDK replaces your bucket name and AWS account ID in the final API endpoint.

While this behavior is required for normal AWS service endpoints, it can cause problems when using custom endpoints such as VPC endpoints or local testing tools. In these cases, you might need to disable host prefix injection.

Configure this functionality by using the following:

**`disable_host_prefix_injection` - shared AWS `config` file setting`AWS_DISABLE_HOST_PREFIX_INJECTION` - environment variable`aws.disableHostPrefixInjection` - JVM system property: Java/Kotlin only**
This setting controls whether the SDK or tool will modify the endpoint hostname by prepending a host prefix as defined in your SDK's client object or variable.
**Default value:** `false`
**Valid values:**
+ **`true`** – Disable host prefix injection. The SDK will not modify the endpoint hostname.
+ **`false`** – Enable host prefix injection. The SDK will prepend the host prefix to the endpoint hostname.

Example of setting this value in the `config` file:

```
[default]
disable_host_prefix_injection = true
```

Linux/macOS example of setting environment variables via command line:

```
export AWS_DISABLE_HOST_PREFIX_INJECTION=true
```

Windows example of setting environment variables via command line:

```
setx AWS_DISABLE_HOST_PREFIX_INJECTION true
```

## Examples of host prefix injection
<a name="hostprefix_examples"></a>

The following table of examples show how SDKs modify the final endpoint when host prefix injection is enabled and disabled.
+ **Host prefix**: The template of the host prefix property string set on the SDK's client object or variable in code.
+ **Inputs**: Additional inputs set on the SDK's client object or variable in code.
+ **Client endpoint**: The client's derived endpoint.
+ **Setting value**: Resolved value for the previous setting.
+ **Resulting endpoint**: The resulting endpoint the SDK client uses to make the API call.

| Host prefix | Inputs | Client endpoint | Setting value | Resulting endpoint |
| --- |--- |--- |--- |--- |
| "data." | {} | "https://service.us-west-2.amazonaws.com" | false | "https://data.service.us-west-2.amazonaws.com" |
| "{Bucket}-{AccountId}." | Bucket: "amzn-s3-demo-bucket1", AccountId:"123456789012" | "https://service.us-west-2.amazonaws.com" | false | "https://amzn-s3-demo-bucket1-123456789012.service.us-west-2.amazonaws.com" |
| "data." | {} | "https://override.us-west-2.amazonaws.com" (as an override endpoint) | true | "https://override.us-west-2.amazonaws.com" |

## Support by AWS SDKs and tools
<a name="host-prefix-sdk-compat"></a>

The following SDKs support the features and settings described in this topic. Any partial exceptions are noted. Any JVM system property settings are supported by the AWS SDK for Java and the AWS SDK for Kotlin only.

| SDK | Supported | Notes or more information |
| --- | --- | --- |
| [AWS CLI v2](https://docs.aws.amazon.com/cli/latest/userguide/) | Yes |  |
| [SDK for C\+\+](https://docs.aws.amazon.com/sdk-for-cpp/latest/developer-guide/) | No | Setting not supported, but can be configured in code on the client using: [`enableHostPrefixInjection`](https://sdk.amazonaws.com/cpp/api/LATEST/aws-cpp-sdk-core/html/struct_aws_1_1_client_1_1_client_configuration.html). |
| [SDK for Go V2 (1.x)](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/) | No | Can be disabled [using middleware](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/configure-endpoints.html). |
| [SDK for Go 1.x (V1)](https://docs.aws.amazon.com/sdk-for-go/latest/developer-guide/) | No |  |
| [SDK for Java 2.x](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/) | No | Setting not supported, but can be configured in code on the client using: [`SdkAdvancedClientOption.DISABLE_HOST_PREFIX_INJECTION`](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/core/client/config/SdkAdvancedClientOption.html#DISABLE_HOST_PREFIX_INJECTION). |
| [SDK for Java 1.x](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/) | No | Setting not supported, but can be configured in code on the client using: [`withDisableHostPrefixInjection`](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/ClientConfiguration.html). |
| [SDK for JavaScript 3.x](https://docs.aws.amazon.com/sdk-for-javascript/latest/developer-guide/) | No | Setting not supported, but can be configured in code on the client using: [`disableHostPrefix`](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/s3-control/). |
| [SDK for JavaScript 2.x](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/) | No | Setting not supported, but can be configured in code on the client using: [`hostPrefixEnabled`](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/Config.html). |
| [SDK for Kotlin](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/) | No |  |
| [SDK for .NET 4.x](https://docs.aws.amazon.com/sdk-for-net/latest/developer-guide/) | No | Setting not supported, but can be configured in code on the client using: [`DisableHostPrefixInjection`](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/Runtime/TClientConfig.html). |
| [SDK for .NET 3.x](https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/) | No | Setting not supported, but can be configured in code on the client using: [`DisableHostPrefixInjection`](https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/Runtime/TClientConfig.html). |
| [SDK for PHP 3.x](https://docs.aws.amazon.com/sdk-for-php/latest/developer-guide/) | No | Setting not supported, but can be configured in code on the client using: [`disable_host_prefix_injection`](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-Aws.AwsClient.html). |
| [SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/) | Yes | Can be configured in code on the client using: [`inject_host_prefix`](https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html). |
| [SDK for Ruby 3.x](https://docs.aws.amazon.com/sdk-for-ruby/latest/developer-guide/) | No | Setting not supported, but can be configured in code on the client using: [`disable_host_prefix_injection`](https://github.com/aws/aws-sdk-ruby/blob/version-3/gems/aws-sdk-core/lib/aws-sdk-core/plugins/endpoint_pattern.rb#L8). |
| [SDK for Rust](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/) | No |  |
| [SDK for Swift](https://docs.aws.amazon.com/sdk-for-swift/latest/developer-guide/) | No |  |
| [Tools for PowerShell V5](https://docs.aws.amazon.com/powershell/latest/userguide/) | No | Setting not supported, but can be included in specific cmdlets using parameter -ClientConfig @{DisableHostPrefixInjection = $true}. |
| [Tools for PowerShell V4](https://docs.aws.amazon.com/powershell/v4/userguide/) | No | Setting not supported, but can be included in specific cmdlets using parameter -ClientConfig @{DisableHostPrefixInjection = $true}. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for none. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdkref` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

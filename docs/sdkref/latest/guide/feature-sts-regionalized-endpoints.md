---
source_url: https://docs.aws.amazon.com/sdkref/latest/guide/feature-sts-regionalized-endpoints.html
---

# AWS STS Regional endpoints
<a name="feature-sts-regionalized-endpoints"></a>

**Note**
For help in understanding the layout of settings pages, or in interpreting the **Support by AWS SDKs and tools** table that follows, see [Understanding the settings pages of this guide](settings-reference.md#settingsPages).

 AWS Security Token Service (AWS STS) is available both as a global and Regional service. Some of AWS SDKs and CLIs use the global service endpoint (`https://sts.amazonaws.com`) by default, while some use the Regional service endpoints (`https://sts.{{{region_identifier}}}.{{{partition_domain}}}`). In Regions that are [enabled by default](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html), requests to the AWS STS global endpoint are automatically served in the same Region where the request originates. In opt-in Regions, requests to the AWS STS global endpoint are served by a single AWS Region, US East (N. Virginia). For more information on AWS STS endpoints, see [Endpoints](https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html#sts-endpoints) in the *AWS Security Token Service API Reference* or [Manage AWS STS in an AWS Region](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html) in the *AWS Identity and Access Management User Guide*.

It is an AWS best practice to use Regional endpoints whenever possible and to configure your [AWS Region](feature-region.md). Customers in [partitions](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html?id=docs_gateway#partition) other than commercial must use Regional endpoints. Not all SDKs and tools support this setting, but all have defined behavior around global and Regional endpoints. See the following section for more information.

**Note**
AWS has made changes to the AWS Security Token Service (AWS STS) global endpoint (`https://sts.amazonaws.com`) in Regions [enabled by default](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html) to enhance its resiliency and performance. AWS STS requests to the global endpoint are automatically served in the same AWS Region as your workloads. These changes will not be deployed to opt-in Regions. We recommend that you use the appropriate AWS STS regional endpoints. For more information, see [AWS STS global endpoint changes](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_region-endpoints.html#reference_sts_global_endpoint_changes) in the *AWS Identity and Access Management User Guide*.

For SDKs and tools that support this setting, customers can configure the functionality by using the following:

**`sts_regional_endpoints` - shared AWS `config` file setting`AWS_STS_REGIONAL_ENDPOINTS` - environment variable**
This setting specifies how the SDK or tool determines the AWS service endpoint that it uses to talk to the AWS Security Token Service (AWS STS).
**Default value:** `regional`, see exceptions in the following table.
All new SDK major versions releasing after July 2022 will default to `regional`. New SDK major versions might remove this setting and use `regional` behavior. To reduce future impact regarding this change, we recommend you start using `regional` in your application when possible.
**Valid values:**   *(Recommended value: `regional`)*
+ **`legacy`** – Uses the global AWS STS endpoint, `sts.amazonaws.com`.
+ **`regional`** – The SDK or tool always uses the AWS STS endpoint for the currently configured Region. For example, if the client is configured to use `us-west-2`, all calls to AWS STS are made to the Regional endpoint `sts.us-west-2.amazonaws.com`, instead of the global `sts.amazonaws.com` endpoint. To send a request to the global endpoint while this setting is enabled, you can set the Region to `aws-global`.
Example of setting these values in the `config` file:

```
[default]
sts_regional_endpoints = regional
```
Linux/macOS example of setting environment variables via command line:

```
export AWS_STS_REGIONAL_ENDPOINTS=regional
```
Windows example of setting environment variables via command line:

```
setx AWS_STS_REGIONAL_ENDPOINTS regional
```

## Support by AWS SDKs and tools
<a name="feature-sts-regionalized-endpoints-sdk-compat"></a>

**Note**
It is an AWS best practice to use Regional endpoints whenever possible and to configure your [AWS Region](feature-region.md).

 The table that follows summarizes, for your SDK or tool:
+ **Supports setting**: Whether the shared `config` file variable and environment variable for STS Regional endpoints are supported.
+ **Default setting value**: The default value of the setting if it is supported.
+ **Default service client target STS Endpoint**: What default endpoint is used by the client even if the setting to change it is not available.
+ **Service client fallback behavior**: What the SDK does when it is supposed to use a Regional endpoint but no Region has been configured. This is the behavior regardless of if it is using a Regional endpoint because of a default or because `regional` has been selected by the setting.

The table also uses the following values:
+ **Global endpoint**: `https://sts.amazonaws.com`.
+ **Regional endpoint**: Based on the configured [AWS Region](feature-region.md) used by your application.
+ **`us-east-1` (Regional)**: Uses the `us-east-1` Region endpoint but with longer session tokens than typical global requests.

| SDK |  Supports setting  |  Default setting value  |  Default service client target STS Endpoint  |  Service client fallback behavior  | Notes or more information |
| --- | --- | --- | --- | --- | --- |
| [AWS CLI v2](https://docs.aws.amazon.com/cli/latest/userguide/) | No | N/A | Regional endpoint | Global endpoint |  |
| [AWS CLI v1](https://docs.aws.amazon.com/cli/v1/userguide/cli-chap-welcome.html) | Yes | legacy | Global endpoint | Global endpoint |  |
| [SDK for C\+\+](https://docs.aws.amazon.com/sdk-for-cpp/latest/developer-guide/) | No | N/A | Regional endpoint | us-east-1 (Regional) |  |
| [SDK for Go V2 (1.x)](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/) | No | N/A | Regional endpoint | Request failure |  |
| [SDK for Go 1.x (V1)](https://docs.aws.amazon.com/sdk-for-go/latest/developer-guide/) | Yes | legacy | Global endpoint | Global endpoint | To use shared config file settings, you must turn on loading from the config file; see [Sessions](https://docs.aws.amazon.com/sdk-for-go/api/aws/session/). |
| [SDK for Java 2.x](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/) | No | N/A | Regional endpoint | Request failure | If no Region is configured, the `AssumeRole` and `AssumeRoleWithWebIdentity` will use the global STS endpoint. |
| [SDK for Java 1.x](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/) | Yes | legacy | Global endpoint | Global endpoint |  |
| [SDK for JavaScript 3.x](https://docs.aws.amazon.com/sdk-for-javascript/latest/developer-guide/) | No | N/A | Regional endpoint | us-east-1 (Regional) |  |
| [SDK for JavaScript 2.x](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/) | Yes | legacy | Global endpoint | Global endpoint |  |
| [SDK for Kotlin](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/) | No | N/A | Regional endpoint | Global endpoint |  |
| [SDK for .NET 4.x](https://docs.aws.amazon.com/sdk-for-net/latest/developer-guide/) | No | N/A | Regional endpoint | us-east-1 (Regional) |  |
| [SDK for .NET 3.x](https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/) | Yes | regional | Global endpoint | Global endpoint |  |
| [SDK for PHP 3.x](https://docs.aws.amazon.com/sdk-for-php/latest/developer-guide/) | Yes | regional | Global endpoint | Request failure |  |
| [SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/) | Yes | regional | Global endpoint | Global endpoint |  |
| [SDK for Ruby 3.x](https://docs.aws.amazon.com/sdk-for-ruby/latest/developer-guide/) | Yes | regional | Regional endpoint | Request failure |  |
| [SDK for Rust](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/) | No | N/A | Regional endpoint | Request failure |  |
| [SDK for Swift](https://docs.aws.amazon.com/sdk-for-swift/latest/developer-guide/) | No | N/A | Regional endpoint | Request failure |  |
| [Tools for PowerShell V5](https://docs.aws.amazon.com/powershell/latest/userguide/) | Yes | regional | Global endpoint | Global endpoint |  |
| [Tools for PowerShell V4](https://docs.aws.amazon.com/powershell/v4/userguide/) | Yes | regional | Global endpoint | Global endpoint |  |

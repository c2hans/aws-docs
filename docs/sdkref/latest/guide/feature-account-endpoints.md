---
source_url: https://docs.aws.amazon.com/sdkref/latest/guide/feature-account-endpoints.html
---

# Account-based endpoints

**Note**
For help in understanding the layout of settings pages, or in interpreting the **Support by AWS SDKs and tools** table that follows, see [Understanding the settings pages of this guide](settings-reference.md#settingsPages).

Account-based endpoints help ensure high performance and scalability by using your AWS account ID to route requests for services that support this feature. When you use an AWS SDK and service that support account-based endpoints, the SDK client constructs and uses an account-based endpoint rather than a regional endpoint. If the account ID isn't visible to the SDK client, the client uses the regional endpoint.

Account-based endpoints take the following forms. In the following examples, replace `{{<account-id>}}` with your AWS account ID and `{{<region>}}` with your AWS Region:
+ Amazon DynamoDB – `https://{{<account-id>}}.ddb.{{<region>}}.amazonaws.com`
+ Amazon DynamoDB Streams – `https://{{<account-id>}}.streams-ddb.{{<region>}}.amazonaws.com`

Configure this functionality by using the following:

**`aws_account_id` - shared AWS `config` file setting`AWS_ACCOUNT_ID` - environment variable`aws.accountId` - JVM system property: Java/Kotlin only**
The AWS account ID. Used for account-based endpoint routing. An AWS account ID has a format like 111122223333.
 Account-based endpoint routing provides better request performance for some services.

**`account_id_endpoint_mode` - shared AWS `config` file setting`AWS_ACCOUNT_ID_ENDPOINT_MODE` - environment variable`aws.accountIdEndpointMode` - JVM system property: Java/Kotlin only**
This setting is used to turn off account-based endpoint routing if necessary, and bypass account-based rules.
**Default value:** `preferred`
**Valid values:**
+ **`preferred`** – The endpoint should include account ID if available.
+ **`disabled`** – A resolved endpoint doesn't include account ID.
+ **`required`** – The endpoint must include account ID. If the account ID isn't available, the SDK throws an error.

## Support by AWS SDKs and tools
<a name="account-endpoints-sdk-compat"></a>

The following SDKs support the features and settings described in this topic. Any partial exceptions are noted. Any JVM system property settings are supported by the AWS SDK for Java and the AWS SDK for Kotlin only.

The *Released in SDK version* column shows the first SDK version that supports account-based endpoints for Amazon DynamoDB. For Amazon DynamoDB Streams, see the *Notes or more information* column.

| SDK | Supported | Released in SDK version | Notes or more information |
| --- | --- | --- | --- |
| [AWS CLI v2](https://docs.aws.amazon.com/cli/latest/userguide/) | Yes | 2.25.0 | Amazon DynamoDB Streams support added in 2.40.4. |
| [AWS CLI v1](https://docs.aws.amazon.com/cli/v1/userguide/cli-chap-welcome.html) | Yes | 1.38.0 | Not supported for Amazon DynamoDB Streams. |
| [SDK for C\+\+](https://docs.aws.amazon.com/sdk-for-cpp/latest/developer-guide/) | No |  |  |
| [SDK for Go V2 (1.x)](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/) | Yes | v1.35.0 | Amazon DynamoDB Streams support added in service/dynamodbstreams v1.48.0. |
| [SDK for Go 1.x (V1)](https://docs.aws.amazon.com/sdk-for-go/latest/developer-guide/) | No |  |  |
| [SDK for Java 2.x](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/) | Yes | v2.28.4 | Amazon DynamoDB Streams support added in v2.59.2. |
| [SDK for Java 1.x](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/) | Yes | v1.12.771 | Not supported for Amazon DynamoDB Streams. |
| [SDK for JavaScript 3.x](https://docs.aws.amazon.com/sdk-for-javascript/latest/developer-guide/) | Yes | v3.656.0 | Amazon DynamoDB Streams support added in v3.1170.0. |
| [SDK for JavaScript 2.x](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/) | No |  |  |
| [SDK for Kotlin](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/) | Yes | v1.3.37 | Amazon DynamoDB Streams support added in v1.9.38. |
| [SDK for .NET 4.x](https://docs.aws.amazon.com/sdk-for-net/latest/developer-guide/) | Yes | 4.0.0 | Amazon DynamoDB Streams support added in AWSSDK.DynamoDBStreams 4.1.1. |
| [SDK for .NET 3.x](https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/) | No |  |  |
| [SDK for PHP 3.x](https://docs.aws.amazon.com/sdk-for-php/latest/developer-guide/) | Yes | v3.318.0 | Amazon DynamoDB Streams support added in v3.404.0. |
| [SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/) | Yes | 1.37.0 | Amazon DynamoDB Streams support added in 1.44.4. |
| [SDK for Ruby 3.x](https://docs.aws.amazon.com/sdk-for-ruby/latest/developer-guide/) | Yes | v1.123.0 | Amazon DynamoDB Streams support added in aws-sdk-dynamodbstreams v1.108.0. |
| [SDK for Rust](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/) | Yes | release-2025-04-24 | Amazon DynamoDB Streams support added in release-2026-11-16. |
| [SDK for Swift](https://docs.aws.amazon.com/sdk-for-swift/latest/developer-guide/) | Yes | 1.2.0 | Amazon DynamoDB Streams support added in 1.8.28. |
| [Tools for PowerShell V5](https://docs.aws.amazon.com/powershell/latest/userguide/) | No |  |  |
| [Tools for PowerShell V4](https://docs.aws.amazon.com/powershell/v4/userguide/) | No |  |  |

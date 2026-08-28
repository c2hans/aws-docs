---
source_url: https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/setting-region.html
---

 The [AWS SDK for JavaScript V3 API Reference Guide](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/) describes in detail all the API operations for the AWS SDK for JavaScript version 3 (V3).

# Set the AWS Region
<a name="setting-region"></a>

An AWS Region is a named set of AWS resources in the same geographical area. An example of a Region is `us-east-1`, which is the US East (N. Virginia) Region. You specify a Region when creating a service client in the SDK for JavaScript so that the SDK accesses the service in that Region. Some services are available only in specific Regions.

The SDK for JavaScript doesn't select a Region by default. However, you can set the AWS Region using an environment variable, or a shared configuration `config` file.

## In a client class constructor
<a name="setting-region-constructor"></a>

When you instantiate a service object, you can specify the AWS Region for that resource as part of the client class constructor, as shown here.

```
const s3Client = new S3.S3Client({region: 'us-west-2'});
```

## Use an environment variable
<a name="setting-region-environment-variable"></a>

You can set the Region using the `AWS_REGION` environment variable. If you define this variable, the SDK for JavaScript reads it and uses it.

## Use a shared config file
<a name="setting-region-config-file"></a>

Much like the shared credentials file lets you store credentials for use by the SDK, you can keep your AWS Region and other configuration settings in a shared file named `config` for the SDK to use. If the `AWS_SDK_LOAD_CONFIG` environment variable is set to a truthy value, the SDK for JavaScript automatically searches for a `config` file when it loads. Where you save the `config` file depends on your operating system:
+ Linux, macOS, or Unix users - `~/.aws/config`
+ Windows users - `C:\Users\USER_NAME\.aws\config`

If you don't already have a shared `config` file, you can create one in the designated directory. In the following example, the `config` file sets both the Region and the output format.

```
[default]
   region=us-west-2
   output=json
```

For more information about using shared `config` and `credentials` files, see [Shared config and credentials files](https://docs.aws.amazon.com/sdkref/latest/guide/file-format.html) in the *AWS SDKs and Tools Reference Guide*.

## Order of precedence for setting the Region
<a name="setting-region-order-of-precedence"></a>

The following is the order of precedence for Region setting:

1. If a Region is passed to a client class constructor, that Region is used.

1. If a Region is set in the environment variable, that Region is used.

1. Otherwise, the Region defined in the shared config file is used.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for JavaScript. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-javascript` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

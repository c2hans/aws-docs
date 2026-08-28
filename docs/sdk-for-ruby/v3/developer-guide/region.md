---
source_url: https://docs.aws.amazon.com/sdk-for-ruby/v3/developer-guide/region.html
---

# Setting the AWS Region for the AWS SDK for Ruby
<a name="region"></a>

You can access AWS services that operate in a specific geographic area by using AWS Regions. This can be useful both for redundancy and to keep your data and applications running close to where you and your users access them.

**Important**
Most resources reside in a specific AWS Region and you must supply the correct Region for the resource when using the SDK.

You must set a default AWS Region for the SDK for Ruby to use for AWS requests. This default is used for any SDK service method calls that aren't specified with a Region.

For more information on the `region` setting, see [AWS Region](https://docs.aws.amazon.com/sdkref/latest/guide/feature-region.html) in the *AWS SDKs and Tools Reference Guide*. This also includes examples on how to set the default region through the shared AWS `config` file or environment variables.

## Region search order for resolution
<a name="aws-ruby-sdk-setting-region"></a>

You need to set a Region when using most AWS services. The AWS SDK for Ruby searches for a Region in the following order:

1.  Setting the Region in a client or resource object

1.  Setting the Region by using `Aws.config`

1.  Setting the Region by using environment variables

1.  Setting the Region by using the shared `config` file

## How to set the Region
<a name="WaysToSetRegion"></a>

This section describes different ways to set a Region, starting with the most common approach.

### Setting the Region using the shared `config` file
<a name="aws-ruby-sdk-region-config"></a>

Set the region by setting the `region` variable in the shared AWS `config` file. For more information about the shared `config` file, see [Shared config and credentials files](https://docs.aws.amazon.com/sdkref/latest/guide/file-format.html) in the *AWS SDKs and Tools Reference Guide*.

Example of setting this value in the `config` file:

```
[default]
region = us-west-2
```

The shared `config` file is not checked if the environment variable `AWS_SDK_CONFIG_OPT_OUT` is set.

### Setting the Region using environment variables
<a name="aws-ruby-sdk-region-environment"></a>

Set the Region by setting the `AWS_REGION` environment variable.

Use the `export` command to set this variable on Unix-based systems, such as Linux or macOS. The following example sets the Region to `us-west-2`.

```
export AWS_REGION=us-west-2
```

To set this variable on Windows, use the `set` command. The following example sets the Region to `us-west-2`.

```
set AWS_REGION=us-west-2
```

### Setting the Region with `Aws.config`
<a name="aws-ruby-sdk-region-aws-config"></a>

Set the Region by adding a `region` value to the `Aws.config` hash. The following example updates the `Aws.config` hash to use the `us-west-1` Region.

```
Aws.config.update({region: 'us-west-1'})
```

Any clients or resources that you create later are bound to this Region.

### Setting the Region in a client or resource object
<a name="aws-ruby-sdk-region-client-resource"></a>

Set the Region when you create an AWS client or resource. The following example creates an Amazon S3 resource object in the `us-west-1` Region. Choose the correct Region for your AWS resources. A service client object is immutable, so you must create a new client for each service to which you make requests and for making requests to the same service using a different configuration.

```
s3 = Aws::S3::Resource.new(region: 'us-west-1')
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Ruby. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-ruby` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

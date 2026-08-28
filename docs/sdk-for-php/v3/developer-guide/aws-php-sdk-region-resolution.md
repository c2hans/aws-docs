---
source_url: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/aws-php-sdk-region-resolution.html
---

# Setting the AWS Region for the AWS SDK for PHP Version 3
<a name="aws-php-sdk-region-resolution"></a>

SDK clients connect to an AWS service in a specific AWS Region that you specify when you create the client. This configuration allows your application to interact with AWS resources in that geographical area. When you create a service client without explicitly setting a Region, the SDK uses the default Region from your external configuration.

## Region resolution chain
<a name="region-resolution-chain"></a>

The AWS SDK for PHP Version 3 uses the following order to determine which Region a service client uses:

1. Region provided in code—If you explicitly set the Region in the client constructor options, this takes precedence over all other sources.

   ```
   $s3Client = new Aws\S3\S3Client([
       'region' => 'us-west-2'
   ]);
   ```

1. Environment variables—If no Region is provided in code, the SDK checks for these environment variables in order:
   + `AWS_REGION`
   + `AWS_DEFAULT_REGION`

   ```
   # Example of setting Region through environment variables.
   export AWS_REGION=us-east-1
   ```

1. AWS config files—If no Region environment variables are set, the SDK checks the AWS config files:

   1. The SDK looks in `~/.aws/config` (or the location specified by `AWS_CONFIG_FILE` environment variable)

   1. The SDK examines the region setting within the profile specified by the `AWS_PROFILE` environment variable

   1. If no `AWS_PROFILE` is specified, the SDK uses the "default" profile

   As an example, assume we have the following configuration file settings:

   ```
   # Example ~/.aws/config file.
   [default]
   region = eu-west-1

   [profile production]
   region = eu-central-1
   ```

   If the `AWS_PROFILE` environment variable is set with a value of "production", clients use the `eu-central-1 Region`. If no `AWS_PROFILE` environment variable exists, clients use the `eu-west-1` Region.

1. If the SDK finds no Region value in any of the above sources, it throws an exception since a Region value is a required setting for a service client.

## Best practices
<a name="region-resolution-best-practices"></a>

Consider the following best practices when working with Regions in the AWS SDK for PHP Version 3:

**Explicitly set the Region in production code**
For production applications, we recommend explicitly setting the Region in your code rather than relying on environment variables or the `config`. This makes your code more predictable and less dependent on external configuration.

**Use environment variables for development and testing**
For development and testing environments, using environment variables allows for more flexibility without changing code.

**Use profiles for multiple environments**
If your application needs to work with multiple AWS environments, consider using different profiles in your AWS `config` file and switching between them as needed.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for PHP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-php` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

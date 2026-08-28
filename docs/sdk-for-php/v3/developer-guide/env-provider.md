---
source_url: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/env-provider.html
---

# `env` provider in the SDK for PHP
<a name="env-provider"></a>

Using environment variables to contain your credentials prevents you from accidentally sharing your AWS secret access key. We recommend that you never add your AWS access keys directly to the client in any production files.

To authenticate to Amazon Web Services, the SDK first checks for credentials in your environment variables. The SDK uses the `getenv()` function to look for the `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_SESSION_TOKEN` environment variables. These credentials are referred to as environment credentials. For instructions on how to obtain these values, see [Authenticate using short-term credentials](https://docs.aws.amazon.com/sdkref/latest/guide/access-temp-idc.html) in the *AWS SDKs and Tools Reference Guide*.

If you’re hosting your application on [AWS Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_PHP_eb.html), you can set the `AWS_ACCESS_KEY_ID`, `AWS_SECRET_KEY`, and `AWS_SESSION_TOKEN` environment variables [through the AWS Elastic Beanstalk console](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environments-cfg-softwaresettings.html#environments-cfg-softwaresettings-console) so that the SDK can use those credentials automatically.

For more information on how to set environment variables, see [Environment variables support](https://docs.aws.amazon.com/sdkref/latest/guide/environment-variables.html) in the *AWS SDKs and Tools Reference Guide*. Also, for a list of all environment variables supported by most AWS SDKs, see [Environment variables list](https://docs.aws.amazon.com/sdkref/latest/guide/settings-reference.html#EVarSettings).

You can also set the environment variables in the command line, as shown here.

 **Linux**

```
$ export AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
   # The access key for your AWS account.
$ export AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
   # The secret access key for your AWS account.
$ export AWS_SESSION_TOKEN=AQoDYXdzEJr...<remainder of security token>
   # The temporary session key for your AWS account.
   # The AWS_SECURITY_TOKEN environment variable can also be used, but is only supported for backward compatibility purposes.
   # AWS_SESSION_TOKEN is supported by multiple AWS SDKs other than PHP.
```

 **Windows**

```
C:\> SET  AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
   # The access key for your AWS account.
C:\> SET  AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
   # The secret access key for your AWS account.
C:\> SET AWS_SESSION_TOKEN=AQoDYXdzEJr...<remainder of security token>
   # The temporary session key for your AWS account.
   # The AWS_SECURITY_TOKEN environment variable can also be used, but is only supported for backward compatibility purposes.
   # AWS_SESSION_TOKEN is supported by multiple AWS SDKs besides PHP.
```

 `Aws\Credentials\CredentialProvider::env` attempts to load credentials from environment variables.

```
use Aws\Credentials\CredentialProvider;
use Aws\S3\S3Client;

$client = new S3Client([
    'region'      => 'us-west-2',
    'version'     => '2006-03-01',
    'credentials' => CredentialProvider::env()
]);
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for PHP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-php` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/instanceprofile-provider.html
---

# `instanceProfile` provider in the SDK for PHP
<a name="instanceprofile-provider"></a>

 `Aws\Credentials\CredentialProvider::instanceProfile` attempts to load credentials for an IAM role specified in an Amazon EC2 instance profile.

```
use Aws\Credentials\CredentialProvider;
use Aws\S3\S3Client;

$provider = CredentialProvider::instanceProfile();
// Be sure to memoize the credentials
$memoizedProvider = CredentialProvider::memoize($provider);

$client = new S3Client([
    'region'      => 'us-west-2',
    'version'     => '2006-03-01',
    'credentials' => $memoizedProvider
]);
```

By default, the provider retries fetching credentials up to three times. The number of retries can be set with the `retries` option, and disabled entirely by setting the option to `0` as shown in the following code.

```
use Aws\Credentials\CredentialProvider;

$provider = CredentialProvider::instanceProfile([
    'retries' => 0
]);
$memoizedProvider = CredentialProvider::memoize($provider);
```

If the environment variable `AWS_METADATA_SERVICE_NUM_ATTEMPTS` is available, its value takes precedence over the 'retries' option shown previously.

**Note**
You can disable this attempt to load from Amazon EC2 instance profiles by setting the `AWS_EC2_METADATA_DISABLED` environment variable to `true`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for PHP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-php` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

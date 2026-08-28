---
source_url: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/ini-provider.html
---

# `ini` provider in the SDK for PHP
<a name="ini-provider"></a>

 `Aws\Credentials\CredentialProvider::ini` attempts to load credentials from the shared `config` and `credentials` files. By default, the SDK attempts to load the “default” profile from the shared AWS `credentials` file located at `~/.aws/credentials`. If the SDK finds the `AWS_SDK_LOAD_NONDEFAULT_CONFIG` environment variable, it also checks for a "default" profile in the shared AWS `config` file located at `~/.aws/config`.

```
use Aws\Credentials\CredentialProvider;
use Aws\S3\S3Client;

$provider = CredentialProvider::ini();
// Cache the results in a memoize function to avoid loading and parsing
// the ini file on every API operation
$provider = CredentialProvider::memoize($provider);

$client = new S3Client([
    'region'      => 'us-west-2',
    'version'     => '2006-03-01',
    'credentials' => $provider
]);
```

You can use a custom profile or .ini file location by providing arguments to the function that creates the provider.

```
$profile = 'production';
$path = '/full/path/to/credentials.ini';

$provider = CredentialProvider::ini($profile, $path);
$provider = CredentialProvider::memoize($provider);

$client = new S3Client([
    'region'      => 'us-west-2',
    'version'     => '2006-03-01',
    'credentials' => $provider
]);
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for PHP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-php` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

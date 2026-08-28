---
source_url: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/process-provider.html
---

# `process` provider in the SDK for PHP
<a name="process-provider"></a>

 `Aws\Credentials\CredentialProvider::process` attempts to load credentials by executing `credential_process` value that is specified in a profile in a [shared AWS configuration file](https://docs.aws.amazon.com/sdkref/latest/guide/file-format.html).

By default, the SDK attempts to load the “default” profile first from the shared AWS `credentials` file located at `~/.aws/credentials`. If the "default" profile is not found in the shared `credentials` file, the SDK looks in the shared `config` file for the default profile. The following is an example of configuration for the shared `credentials` file.

```
[default]
credential_process = /path/to/file/credential_returning_executable.sh --custom-command custom_parameter
```

The SDK will call the `credential_process` command exactly as given by using PHP's `shell_exec` function and then read JSON data from stdout. The `credential_process` must write credentials to stdout in the following format:

```
{
    "Version": 1,
    "AccessKeyId": "",
    "SecretAccessKey": "",
    "SessionToken": "",
    "Expiration": ""
}
```

 `SessionToken` and `Expiration` are optional. If present, the credentials will be treated as temporary.

```
use Aws\Credentials\CredentialProvider;
use Aws\S3\S3Client;

$provider = CredentialProvider::process();
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

$provider = CredentialProvider::process($profile, $path);
$provider = CredentialProvider::memoize($provider);

$client = new S3Client([
    'region'      => 'us-west-2',
    'version'     => '2006-03-01',
    'credentials' => $provider
]);
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for PHP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-php` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

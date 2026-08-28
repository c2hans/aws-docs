---
source_url: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/ecscredentials-provider.html
---

# `ecsCredentials` provider in the SDK for PHP
<a name="ecscredentials-provider"></a>

 `Aws\Credentials\CredentialProvider::ecsCredentials` attempts to load credentials by a `GET` request, whose URI is specified by the environment variable `AWS_CONTAINER_CREDENTIALS_RELATIVE_URI` in the container.

```
use Aws\Credentials\CredentialProvider;
use Aws\S3\S3Client;

$provider = CredentialProvider::ecsCredentials();
// Be sure to memoize the credentials
$memoizedProvider = CredentialProvider::memoize($provider);

$client = new S3Client([
    'region'      => 'us-west-2',
    'version'     => '2006-03-01',
    'credentials' => $memoizedProvider
]);
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for PHP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-php` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

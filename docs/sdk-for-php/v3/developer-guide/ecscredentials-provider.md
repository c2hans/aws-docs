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

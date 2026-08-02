---
source_url: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/defaultprovider-provider.html
---

# `defaultProvider` provider in the SDK for PHP
<a name="defaultprovider-provider"></a>

 `Aws\Credentials\CredentialProvider::defaultProvider` is the default credential provider and is also called the [default credential provider chain](guide_credentials_default_chain.md). This provider is used if you omit a `credentials` option when creating a client. For example, if you create an S3Client as shown in the following snippet, the SDK uses the default provider:

```
$client = new S3Client([
    'region' => 'us-west-2'
]);
```

You can also use the defaultProvider in code if you want to supply parameters to specific credential providers in the chain. For example the following example provides custom connection timeout and retry settings if the `ecsCredentials` provider function is used.

```
use Aws\Credentials\CredentialProvider;
use Aws\S3\S3Client;

$provider = CredentialProvider::defaultProvider([
    'timeout' => '1.5',
    'retries' => 5
]);

$client = new S3Client([
    'region' => 'us-west-2',
    'credentials' => $provider
]);
```

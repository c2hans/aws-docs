---
source_url: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/memoizing-credentials.html
---

# Memoizing credentials in the SDK for PHP
<a name="memoizing-credentials"></a>

At times you might need to create a credential provider that remembers the previous return value. This can be useful for performance when loading credentials is an expensive operation or when using the `Aws\Sdk` class to share a credential provider across multiple clients. You can add memoization to a credential provider by wrapping the credential provider function in a `memoize` function.

```
use Aws\Credentials\CredentialProvider;

$provider = CredentialProvider::instanceProfile();
// Wrap the actual provider in a memoize function
$provider = CredentialProvider::memoize($provider);

// Pass the provider into the Sdk class and share the provider
// across multiple clients. Each time a new client is constructed,
// it will use the previously returned credentials as long as
// they haven't yet expired.
$sdk = new Aws\Sdk(['credentials' => $provider]);

$s3 = $sdk->getS3(['region' => 'us-west-2', 'version' => 'latest']);
$ec2 = $sdk->getEc2(['region' => 'us-west-2', 'version' => 'latest']);

assert($s3->getCredentials() === $ec2->getCredentials());
```

When the memoized credentials are expired, the memoize wrapper invokes the wrapped provider in an attempt to refresh the credentials.

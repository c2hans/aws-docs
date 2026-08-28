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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for PHP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-php` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

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

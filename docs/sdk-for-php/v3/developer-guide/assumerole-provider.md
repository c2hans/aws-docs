---
source_url: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/assumerole-provider.html
---

# `assumeRole` provider in the SDK for PHP
<a name="assumerole-provider"></a>

If you use `Aws\Credentials\AssumeRoleCredentialProvider` to create credentials by assuming a role, you need to provide `'client'` information with an `StsClient` object and `'assume_role_params'` details, as shown.

**Note**
To avoid unnecessarily fetching AWS STS credentials on every API operation, you can use the `memoize` function to handle automatically refreshing the credentials when they expire. See the following code for an example.

```
use Aws\Credentials\CredentialProvider;
use Aws\Credentials\InstanceProfileProvider;
use Aws\Credentials\AssumeRoleCredentialProvider;
use Aws\S3\S3Client;
use Aws\Sts\StsClient;

// Passing Aws\Credentials\AssumeRoleCredentialProvider options directly
$profile = new InstanceProfileProvider();
$ARN = "arn:aws:iam::123456789012:role/xaccounts3access";
$sessionName = "s3-access-example";

$assumeRoleCredentials = new AssumeRoleCredentialProvider([
    'client' => new StsClient([
        'region' => 'us-east-2',
        'version' => '2011-06-15',
        'credentials' => $profile
    ]),
    'assume_role_params' => [
        'RoleArn' => $ARN,
        'RoleSessionName' => $sessionName,
    ],
]);

// To avoid unnecessarily fetching STS credentials on every API operation,
// the memoize function handles automatically refreshing the credentials when they expire
$provider = CredentialProvider::memoize($assumeRoleCredentials);

$client = new S3Client([
    'region'      => 'us-east-2',
    'version'     => '2006-03-01',
    'credentials' => $provider
]);
```

For more information regarding `'assume_role_params'`, see [AssumeRole](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-sts-2011-06-15.html#assumerole).

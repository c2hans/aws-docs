---
source_url: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/assume-role-with-web-identity-provider.html
---

# `assumeRoleWithWebIdentityCredentialProvider` provider in the SDK for PHP
<a name="assume-role-with-web-identity-provider"></a>

 `Aws\Credentials\CredentialProvider::assumeRoleWithWebIdentityCredentialProvider` attempts to load credentials by assuming a role. If the environment variables `AWS_ROLE_ARN` and `AWS_WEB_IDENTITY_TOKEN_FILE` are present, the provider will attempt to assume the role specified at `AWS_ROLE_ARN` using the token on disk at the full path specified in `AWS_WEB_IDENTITY_TOKEN_FILE`. If environment variables are used, the provider will attempt to set the session from the `AWS_ROLE_SESSION_NAME` environment variable.

If environment variables are not set, the provider will use the default profile, or the one set as `AWS_PROFILE`. The provider reads profiles from `~/.aws/credentials` and `~/.aws/config` by default, and can read from profiles specified in the `filename` config option. The provider will assume the role in `role_arn` of the profile, reading a token from the full path set in `web_identity_token_file`. `role_session_name` will be used if set on the profile.

The provider is called as part of the default chain and can be called directly.

```
use Aws\Credentials\CredentialProvider;
use Aws\S3\S3Client;

$provider = CredentialProvider::assumeRoleWithWebIdentityCredentialProvider();
// Cache the results in a memoize function to avoid loading and parsing
// the ini file on every API operation
$provider = CredentialProvider::memoize($provider);

$client = new S3Client([
    'region'      => 'us-west-2',
    'version'     => '2006-03-01',
    'credentials' => $provider
]);
```

By default, this credential provider will inherit the configured region which will be used by the StsClient to assume the role. Optionally, a full StsClient can be provided. Credentials should be set as `false` on any provided StsClient.

```
use Aws\Credentials\CredentialProvider;
use Aws\S3\S3Client;
use Aws\Sts\StsClient;

$stsClient = new StsClient([
    'region'      => 'us-west-2',
    'version'     => 'latest',
    'credentials' => false
])

$provider = CredentialProvider::assumeRoleWithWebIdentityCredentialProvider([
    'stsClient' => $stsClient
]);
// Cache the results in a memoize function to avoid loading and parsing
// the ini file on every API operation
$provider = CredentialProvider::memoize($provider);

$client = new S3Client([
    'region'      => 'us-west-2',
    'version'     => '2006-03-01',
    'credentials' => $provider
]);
```

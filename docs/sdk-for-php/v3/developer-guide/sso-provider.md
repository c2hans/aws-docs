---
source_url: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/sso-provider.html
---

# `sso` provider in the SDK for PHP
<a name="sso-provider"></a>

`Aws\Credentials\CredentialProvider::sso` is the single sign-on credential provider. This provider is also known as the AWS IAM Identity Center credential provider.

```
use Aws\Credentials\CredentialProvider;
use Aws\S3\S3Client;

$credentials = CredentialProvider::sso('profile default');

$s3 = new Aws\S3\S3Client([
    'version'     => 'latest',
    'region'      => 'us-west-2',
    'credentials' => $credentials
]);
```

If you use a named profile, substitute the name of your profile for ‘`default`’ in the previous example. To learn more about setting up named profiles, see [Shared `config` and `credentials` files](https://docs.aws.amazon.com/sdkref/latest/guide/file-format.html) in the *AWS SDKs and Tools Reference Guide*. Alternatively, you can use the [https://docs.aws.amazon.com/sdkref/latest/guide/file-format.html#file-format-profile](https://docs.aws.amazon.com/sdkref/latest/guide/file-format.html#file-format-profile) environment variable to specify which profile's settings to use.

To understand more how the IAM Identity Center provider works, see [Understand IAM Identity Center authentication](https://docs.aws.amazon.com/sdkref/latest/guide/understanding-sso.html) in the *AWS SDKs and Tools Reference Guide*.

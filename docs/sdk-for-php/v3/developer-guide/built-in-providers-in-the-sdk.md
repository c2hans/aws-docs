---
source_url: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/built-in-providers-in-the-sdk.html
---

# Built-in credential providers in the AWS SDK for PHP Version 3
<a name="built-in-providers-in-the-sdk"></a>

The SDK provides several built-in credential providers that you can use individually or combine in a [custom credential provider chain](chaining-providers.md).

When you specify a credential provider during service client creation, the SDK attempts to load credentials by using only the specified credential provider. It does not use the [default credential provider chain](guide_credentials_default_chain.md). If you know that you want a service client to use the `instanceProfile` provider, you can short-circuit the default chain by specifying the `instanceProfile` provider in the service client constructor:

```
use Aws\Credentials\CredentialProvider;
use Aws\S3\S3Client;

$provider = CredentialProvider::instanceProfile();
// Be sure to memoize the credentials
$memoizedProvider = CredentialProvider::memoize($provider);

$client = new S3Client([
    'region'      => 'us-west-2',
    'credentials' => $memoizedProvider  // The default credential provider chain is not used.
]);
```

**Important**
Credential providers are invoked every time an API operation is performed. If loading credentials is an expensive task (e.g., loading from disk or a network resource), or if credentials are not cached by your provider, consider wrapping your credential provider in an `Aws\Credentials\CredentialProvider::memoize` function. The default credential provider used by the SDK is automatically memoized.

**Topics**
+ [`login` provider in the SDK for PHP](login-provider.md)
+ [`assumeRole` provider in the SDK for PHP](assumerole-provider.md)
+ [`sso` provider in the SDK for PHP](sso-provider.md)
+ [`defaultProvider` provider in the SDK for PHP](defaultprovider-provider.md)
+ [`ecsCredentials` provider in the SDK for PHP](ecscredentials-provider.md)
+ [`env` provider in the SDK for PHP](env-provider.md)
+ [`assumeRoleWithWebIdentityCredentialProvider` provider in the SDK for PHP](assume-role-with-web-identity-provider.md)
+ [`ini` provider in the SDK for PHP](ini-provider.md)
+ [`process` provider in the SDK for PHP](process-provider.md)
+ [`instanceProfile` provider in the SDK for PHP](instanceprofile-provider.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for PHP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-php` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

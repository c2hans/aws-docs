---
source_url: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/guide_credentials.html
---

# Using AWS SDK for PHP Version 3 credential providers
<a name="guide_credentials"></a>

For reference information on available credentials mechanisms for the AWS SDKs, see [Credentials and access](https://docs.aws.amazon.com/sdkref/latest/guide/access.html) in the *AWS SDKs and Tools Reference Guide*.

**Important**
For security, we *strongly recommend* that you do **not** use the root account for AWS access. Always refer to the [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the *IAM User Guide* for the latest security recommendations.

The role of a credentials provider in the AWS SDK for PHP Version 3 is to source and supply credentials to the SDK's AWS service clients. The SDK uses the credentials it sources to authenticate with the service by cryptographically signing each request. Credentials usually consist of access keys—an access key ID and a secret access key together.

When you use temporary credentials, such as when you [set up IAM Identity Center authentication](credentials.md#use-idc-for-auth) or configure your runtime to [assume an IAM role](assumerole-provider.md), a session token is added to the access keys, providing time-limited access to AWS resources.

## What is a credential provider in the AWS SDK for PHP Version 3?
<a name="cred-provider-defn-php"></a>

A credential provider is a function that returns a `GuzzleHttp\Promise\PromiseInterface` that is fulfilled with an `Aws\Credentials\CredentialsInterface` instance or rejected with an `Aws\Exception\CredentialsException`. The [SDK provides several implementations](built-in-providers-in-the-sdk.md) of credential provider functions or you can [implement your own](creating-a-custom-provider.md) custom logic for creating credentials or to optimize credential loading.

Credential providers are passed into the `credentials` client constructor option. Credential providers are asynchronous, which forces them to be lazily evaluated each time an API operation is invoked. As such, passing in a credential provider function to an SDK client constructor doesn’t immediately validate the credentials. If the credential provider doesn’t return a credentials object, an API operation will be rejected with an `Aws\Exception\CredentialsException`.

```
use Aws\Credentials\CredentialProvider;
use Aws\S3\S3Client;

// Use the ECS credential provider.
$provider = CredentialProvider::ecsCredentials();
// Be sure to memoize the credentials.
$memoizedProvider = CredentialProvider::memoize($provider);

// Pass the provider to the client
$client = new S3Client([
    'region'      => 'us-west-2',
    'version'     => '2006-03-01',
    'credentials' => $memoizedProvider
]);
```

---
source_url: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/creating-a-custom-provider.html
---

# Creating a custom credential provider to use with the SDK for PHP
<a name="creating-a-custom-provider"></a>

Credential providers are simply functions that when invoked return a promise (`GuzzleHttp\Promise\PromiseInterface`) that is fulfilled with an `Aws\Credentials\CredentialsInterface` object or rejected with an `Aws\Exception\CredentialsException`.

A best practice for creating providers is to create a function that is invoked to create the actual credential provider. As an example, here’s the source of the `env` provider (slightly modified for example purposes). Notice that it is a function that returns the actual provider function. This allows you to easily compose credential providers and pass them around as values.

```
use GuzzleHttp\Promise;
use GuzzleHttp\Promise\RejectedPromise;

// This function CREATES a credential provider
public static function env()
{
    // This function IS the credential provider
    return function () {
        // Use credentials from environment variables, if available
        $key = getenv(self::ENV_KEY);
        $secret = getenv(self::ENV_SECRET);
        if ($key && $secret) {
            return Create::promise_for(
                new Credentials($key, $secret, getenv(self::ENV_SESSION))
            );
        }

        $msg = 'Could not find environment variable '
            . 'credentials in ' . self::ENV_KEY . '/' . self::ENV_SECRET;
        return new RejectedPromise(new CredentialsException($msg));
    };
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for PHP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-php` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

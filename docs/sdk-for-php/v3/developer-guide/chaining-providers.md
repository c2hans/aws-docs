---
source_url: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/chaining-providers.html
---

# Chaining credential providers in the SDK for PHP
<a name="chaining-providers"></a>

You can chain credential providers by using the `Aws\Credentials\CredentialProvider::chain()` function. This function accepts a variadic number of arguments, each of which are credential provider functions. This function then returns a new function that’s the composition of the provided functions, such that they are invoked one after the other until one of the providers returns a promise that is fulfilled successfully.

The `defaultProvider` uses this composition to check multiple providers before failing. The source of the `defaultProvider` demonstrates the use of the `chain` function.

```
// This function returns a provider
public static function defaultProvider(array $config = [])
{
    // This function is the provider, which is actually the composition
    // of multiple providers. Notice that we are also memoizing the result by
    // default.
    return self::memoize(
        self::chain(
            self::env(),
            self::ini(),
            self::instanceProfile($config)
        )
    );
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for PHP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-php` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

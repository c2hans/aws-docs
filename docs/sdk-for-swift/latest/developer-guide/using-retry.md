---
source_url: https://docs.aws.amazon.com/sdk-for-swift/latest/developer-guide/using-retry.html
---

# Configuring retry using the AWS SDK for Swift
<a name="using-retry"></a>

Calls to AWS services occasionally encounter problems or unexpected situations. Certain types of errors, such as throttling or transient errors, might be successful if the call is retried.

This page describes how to configure automatic retries with the AWS SDK for Swift.

## Default retry configuration
<a name="retries-default"></a>

By default, every service client is automatically configured with a standard retry strategy. The default configuration tries each action up to three times (the initial attempt plus two retries). The intervening delay between each call is configured with exponential backoff and random jitter to avoid retry storms. This configuration works for the majority of use cases but may be unsuitable in some circumstances, such as high-throughput systems.

The SDK attempts retries only on retryable errors. Examples of retryable errors are socket timeouts, service-side throttling, concurrency or optimistic lock failures, and transient service errors. Missing or invalid parameters, authentication/security errors, and misconfiguration exceptions are not considered retryable.

## Configuring retry
<a name="retries-configure"></a>

You can customize the standard retry strategy by setting the maximum number of attempts and the rate limiting strategy to use. To change the retry configuration, create a structure of type `S3ClientConfiguration` with the properties you wish to customize. For details on how to configure a service client, see [Configuring AWS SDK for Swift service clients in code](config-code.md).

### Maximum number of attempts
<a name="retries-max-attempts"></a>

You can customize the maximum number of attempts by specifying a value for the `S3ClientConfiguration` structure's `maxAttempts` property. The default value is 3.

### Retry mode
<a name="retries-rate-limiting-mode"></a>

The retry mode can be set by changing the `S3ClientConfiguration` structure's `retryMode`. The available values are provided by the `enum` `AWSRetryMode`.

#### Legacy
<a name="retries-rate-limiting-mode-legacy"></a>

The `legacy` retry mode—the default—is the original standard retry mode. In this mode, requests may be sent immediately, and are not delayed for rate limiting when throttling is detected. Requests are only delayed according to the backoff strategy in use, which is exponentially by default.

#### Standard
<a name="retries-rate-limiting-mode-standard"></a>

In the AWS SDK for Swift, the `standard` mode is the same as legacy mode.

#### Adaptive
<a name="retries-rate-limiting-mode-adaptive"></a>

In the `adaptive` retry mode, initial and retry requests may be delayed by an additional amount when throttling is detected. This is intended to reduce congestion when throttling is in effect. This is sometimes called "client-side rate limiting" mode, and is available opt-in. You should only use adaptive mode when advised to do so by an AWS representative.

### Example
<a name="retries-example"></a>

First, import the modules needed to configure retry:

```
import AWSS3
import SmithyRetries
import SmithyRetriesAPI
```

Then create the custom configuration. This example's `S3ClientConfiguration` asks for the client to make up to three attempts for each action, using the `adaptive` retry mode.

```
        let config: S3Client.S3ClientConfiguration

        // Create an Amazon S3 client configuration object that specifies the
        // adaptive retry mode and sets the maximum number of attempts to 3.
        // If that fails, create a default configuration instead.

        do {
            config = try await S3Client.S3ClientConfiguration(
                awsRetryMode: .adaptive,
                maxAttempts: 3
            )
        } catch {
            do {
                config = try await S3Client.S3ClientConfiguration()
            } catch {
                print("Error: Unable to configure Amazon S3.")
                dump(error)
                return
            }
        }

        // Create an Amazon S3 client using the configuration created above.

        let client = S3Client(config: config)
```

It first attempts to create the configuration using the application's preferred settings. If that fails, a default configuration is created instead. If that also fails, the example outputs an error message. A real-world application might instead present an error message and let the user decide what to do.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Swift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-swift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

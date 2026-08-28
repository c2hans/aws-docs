---
source_url: https://docs.aws.amazon.com/sdk-for-ruby/v3/developer-guide/retries.html
---

# Configuring retries in the AWS SDK for Ruby
<a name="retries"></a>

The AWS SDK for Ruby provides a default retry behavior for service requests and customizable configuration options. Calls to AWS services occasionally return unexpected exceptions. Certain types of errors, such as throttling or transient errors, might be successful if the call is retried.

Retry behavior can be configured globally using environment variables or settings in the shared AWS `config` file. For information on this approach, see [Retry behavior](https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html) in the *AWS SDKs and Tools Reference Guide*. It also includes detailed information on retry strategy implementations and how to choose one over another.

Alternatively, these options can also be configured in your code, as shown in the following sections.

## Specifying client retry behavior in code
<a name="clientretry"></a>

By default, the AWS SDK for Ruby performs up to three retries, with 15 seconds between retries, for a total of up to four attempts. Therefore, an operation could take up to 60 seconds to time out.

The following example creates an Amazon S3 client in the region `us-west-2`, and specifies to wait five seconds between two retries on every client operation. Therefore, Amazon S3 client operations could take up to 15 seconds to time out.

```
 s3 = Aws::S3::Client.new(
   region: region,
   retry_limit: 2,
   retry_backoff: lambda { |c| sleep(5) }
)
```

Any explicit setting set in the code or on a service client itself takes precedence over those set in environment variables or the shared `config` file.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Ruby. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-ruby` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

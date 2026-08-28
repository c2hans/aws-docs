---
source_url: https://docs.aws.amazon.com/sdk-for-ruby/v3/developer-guide/service-clients.html
---

# Making AWS service requests using the AWS SDK for Ruby
<a name="service-clients"></a>

 To programmatically access AWS services, SDKs use a client class for each AWS service. For example, if your application needs to access Amazon EC2, your application creates an Amazon EC2 client object to interface with that service. You then use the service client to make requests to that AWS service.

To make a request to an AWS service, you must first create and [configure](configuring.md) a service client. For each AWS service your code uses, it has its own gem and its own dedicated type for interacting with it. The client exposes one method for each API operation exposed by the service.

Each service client requires an AWS Region and a credential provider. The SDK uses these values to send requests to the correct Region for your resources and to sign requests with the correct credentials. You can specify these values programmatically in code or have them automatically loaded from the environment.
+ When instantiating a client class, AWS credentials must be supplied. For the order that the SDK checks for authentication providers, see [Credential provider chain](credential-providers.md#credchain).

+ The SDK has a series of places (or sources) that it checks in order to find a value for configuration settings. For details, see [Precedence of settings](configuring.md#precedence-settings).

The SDK for Ruby includes client classes that provide interfaces to the AWS services. Each client class supports a particular AWS service and follows the convention `Aws::{{<service identifier>}}::Client`. For example, [`Aws::S3::Client`](https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/S3/Client.html) provides an interface to the Amazon Simple Storage Service service, and [`Aws::SQS::Client`](https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/SQS/Client.html) provides an interface to the Amazon Simple Queue Service service.

 All client classes for all AWS services are thread-safe.

You can pass configuration options directly to Client and Resource constructors. These options take precedence over the environment and `Aws.config` defaults.

```
# using a credentials object
ec2 = Aws::EC2::Client.new(region: 'us-west-2', credentials: credentials)
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Ruby. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-ruby` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

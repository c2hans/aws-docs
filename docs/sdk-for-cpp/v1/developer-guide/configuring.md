---
source_url: https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/configuring.html
---

# Configuring service clients in the AWS SDK for C\+\+
<a name="configuring"></a>

 To programmatically access AWS services, the AWS SDK for C\+\+ uses a client class for each AWS service. For example, if your application needs to access Amazon EC2, your application creates an Amazon EC2 client object to interface with that service. You then use the service client to make requests to that AWS service.

To make a request to an AWS service, you must first create a service client. For each AWS service your code uses, it has its own library and its own dedicated type for interacting with it. The client exposes one method for each API operation exposed by the service.

There are many alternative ways to configure SDK behavior, but ultimately everything has to do with the behavior of service clients. Any configuration has no effect until a service client that is created from them is used.

You must establish how your code authenticates with AWS when you develop with AWS services. You must also set the AWS Region you want to use.

The [AWS SDKs and Tools Reference Guide](https://docs.aws.amazon.com/sdkref/latest/guide/) also contains settings, features, and other foundational concepts common among many of the AWS SDKs.

**Topics**
+ [SDK configuration](sdkoptions.md)
+ [Client configuration externally](config-external.md)
+ [Client configuration in code](client-config.md)
+ [AWS Region](region.md)
+ [Credential providers](credproviders.md)
+ [CMake parameters](cmake-params.md)
+ [Logging](logging.md)
+ [HTTP](overriding-http-client.md)
+ [Controlling iostreams used by the `HttpClient` and the `AWSClient`](configuring-iostreams.md)
+ [Using a custom libcrypto](libcrypto.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for C++. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-cpp` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

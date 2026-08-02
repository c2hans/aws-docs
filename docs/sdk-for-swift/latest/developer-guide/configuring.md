---
source_url: https://docs.aws.amazon.com/sdk-for-swift/latest/developer-guide/configuring.html
---

# Configuring service clients in the AWS SDK for Swift
<a name="configuring"></a>

 To programmatically access AWS services, SDKs use a client class/object for each AWS service. For example, if your application needs to access Amazon EC2, your application creates an Amazon EC2 client object to interface with that service. You then use the service client to make requests to that AWS service.

To make a request to an AWS service, you must first create a service client. For each AWS service your code uses, it has its own crate/library/gem/package and its own dedicated type for interacting with it. The client exposes one method for each API operation exposed by the service.

There are many alternative ways to configure SDK behavior, but ultimately everything has to do with the behavior of service clients. Any configuration has no effect until a service client that is created from them is used.

You must establish how your code authenticates with AWS when you develop with AWS services. You must also set the AWS Region you want to use.

The [AWS SDKs and Tools Reference Guide](https://docs.aws.amazon.com/sdkref/latest/guide/) also contains settings, features, and other foundational concepts common among many of the AWS SDKs.

**Topics**
+ [Client configuration externally](config-external.md)
+ [Client configuration in code](config-code.md)
+ [AWS Region](region.md)
+ [Credential providers](credential-providers.md)
+ [Retry](using-retry.md)
+ [HTTP](http.md)

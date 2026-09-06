---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/configuring-service-clients.html
---

# Configuring service clients in the AWS SDK for Java 2.x
<a name="configuring-service-clients"></a>

To programmatically access AWS services, the SDK for Java 2.x uses a client object for each AWS service. For example, if your application needs to access Amazon EC2, you create an Amazon EC2 client object—an instance of the [Ec2Client](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/ec2/Ec2Client.html) class—to interface with that service. You then use the service client to make requests to that AWS service. For most applications, you can use a [singleton instance of a service client](singleton-service-clients.md).

There are many ways to configure SDK behavior, but ultimately everything has to do with the behavior of service clients. Any configuration has no effect until your code creates a service client that uses the configuration.

Examples of the configuration that you provide are:
+ How your code authenticates with AWS when you call a service
+ The AWS Region you want a service client to use
+ Retry and timeout settings for service calls
+ HTTP proxy configuration

Refer to the [AWS SDKs and Tools Reference Guide](https://docs.aws.amazon.com/sdkref/latest/guide/) for settings, features, and other foundational concepts common to many of the AWS SDKs.

**Topics**
+ [Client configuration externally](configuring-service-clients-ext.md)
+ [Client configuration in code](configuring-service-clients-code.md)
+ [Singleton service clients](singleton-service-clients.md)
+ [AWS Region](region-selection.md)
+ [Credentials providers](credentials.md)
+ [Retries](retry-strategy.md)
+ [Timeouts](timeouts.md)
+ [Observability](observability.md)
+ [Endpoints](endpoint-config.md)
+ [Configure HTTP clients](http-configuration.md)
+ [Interceptors](interceptors.md)

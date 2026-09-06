---
source_url: https://docs.aws.amazon.com/sdk-for-ruby/v3/developer-guide/configuring.html
---

# Configuring service clients in the AWS SDK for Ruby
<a name="configuring"></a>

 To programmatically access AWS services, the AWS SDK for Ruby uses a client class for each AWS service. For example, if your application needs to access Amazon EC2, your application creates an Amazon EC2 client object to interface with that service. You then use the service client to make requests to that AWS service.

To make a request to an AWS service, you must first create a service client. For each AWS service your code uses, it has its own gem and its own dedicated type for interacting with it. The client exposes one method for each API operation exposed by the service.

There are many alternative ways to configure SDK behavior, but ultimately everything has to do with the behavior of service clients. Any configuration has no effect until a service client that is created from them is used.

You must establish how your code authenticates with AWS when you develop with AWS services. You must also set the AWS Region you want to use.

The [AWS SDKs and Tools Reference Guide](https://docs.aws.amazon.com/sdkref/latest/guide/) also contains settings, features, and other foundational concepts common among many of the AWS SDKs.

**Topics**
+ [Precedence of settings](#precedence-settings)
+ [Client configuration externally](environment-variables.md)
+ [Client configuration in code](setup-config.md)
+ [AWS Region](region.md)
+ [Credential providers](credential-providers.md)
+ [Retries](retries.md)
+ [Observability](observability.md)
+ [HTTP](http.md)

 The [Shared `config` and `credentials` files](https://docs.aws.amazon.com/sdkref/latest/guide/file-format.html) can be used for configuration settings. For all AWS SDK settings, see the [Settings reference](https://docs.aws.amazon.com/sdkref/latest/guide/settings-reference.html) in the *AWS SDKs and Tools Reference Guide*.

Different profiles can be used to store different configurations. To specify the active profile that the SDK loads, you can use the `AWS_PROFILE` environment variable or the `profile` option of `Aws.config`.

## Precedence of settings
<a name="precedence-settings"></a>

Global settings configure features, credential providers, and other functionality that are supported by most SDKs and have a broad impact across AWS services. All AWS SDKs have a series of places (or sources) that they check in order to find a value for global settings. Not all settings are available in all sources. The following is the setting lookup precedence:

1. Any explicit setting set in the code or on a service client itself takes precedence over anything else.

   1. Any parameters passed directly into a client constructor take highest precedence.

   1. `Aws.config` is checked for global or service-specific settings.

1. The environment variable is checked.

1. The shared AWS `credentials` file is checked.

1. The shared AWS `config` file is checked.

1. Any default value provided by the AWS SDK for Ruby source code itself is used last.

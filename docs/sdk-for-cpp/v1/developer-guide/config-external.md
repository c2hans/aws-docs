---
source_url: https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/config-external.html
---

# Configuring AWS SDK for C\+\+ service clients externally
<a name="config-external"></a>

Many configuration settings can be handled outside of your code. When configuration is handled externally, the configuration is applied across all of your applications. Most configuration settings can be set as either environment variables or in a separate shared AWS `config` file. The shared `config` file can maintain separate sets of settings, called profiles, to provide different configurations for different environments or tests.

Environment variables and shared `config` file settings are standardized and shared across AWS SDKs and tools to support consistent functionality across different programming languages and applications.

See the *AWS SDKs and Tools Reference Guide* to learn about configuring your application through these methods, plus details on each cross-sdk setting. To see all the all settings that the SDK can resolve from the environment variables or configuration files, see the [Settings reference](https://docs.aws.amazon.com/sdkref/latest/guide/settings-reference.html) in the *AWS SDKs and Tools Reference Guide*.

To make a request to an AWS service, you first instantiate a client for that service. You can configure common settings for service clients such as timeouts, the HTTP client, and retry configuration.

Each service client requires an AWS Region and a credential provider. The SDK uses these values to send requests to the correct Region for your resources and to sign requests with the correct credentials. You can specify these values programmatically in code or have them automatically loaded from the environment.

The SDK has a series of places (or sources) that it checks in order to find a value for configuration settings.

1. Any explicit setting set in the code or on a service client itself takes precedence over anything else.

1. Environment variables
   + For details on setting environment variables, see [environment variables](https://docs.aws.amazon.com/sdkref/latest/guide/environment-variables.html) in the *AWS SDKs and Tools Reference Guide*.
   + Note that you can configure environment variables for a shell at different levels of scope: system-wide, user-wide, and for a specific terminal session.

1. Shared `config` and `credentials` files
   + For details on setting up these files, see the [Shared `config` and `credentials` files](https://docs.aws.amazon.com/sdkref/latest/guide/file-format.html) in the *AWS SDKs and Tools Reference Guide*.

1. Any default value provided by the SDK source code itself is used last.
   + Some properties, such as Region, don't have a default. You must specify them either explicitly in code, in an environment setting, or in the shared `config` file. If the SDK can't resolve required configuration, API requests can fail at runtime.

**Note**
 To see all the all settings that the SDK can resolve from the environment variables or configuration files, see the [Settings reference](https://docs.aws.amazon.com/sdkref/latest/guide/settings-reference.html) in the *AWS SDKs and Tools Reference Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for C++. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-cpp` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

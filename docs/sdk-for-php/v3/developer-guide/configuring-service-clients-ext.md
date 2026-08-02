---
source_url: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/configuring-service-clients-ext.html
---

# Configuring service clients for the AWS SDK for PHP Version 3 externally
<a name="configuring-service-clients-ext"></a>

Many configuration settings can be handled outside of your code. Most configuration settings can be set as either environment variables or in a separate shared AWS `config` file. The AWS shared `config` file can maintain separate sets of settings, called profiles, to provide different configurations for different environments or tests. For a complete discussion of the AWS shared `config` and `credentials` files, see the [https://docs.aws.amazon.com/sdkref/latest/guide/file-format.html](https://docs.aws.amazon.com/sdkref/latest/guide/file-format.html).

Most environment variables and shared `config` file settings are standardized and shared across AWS SDKs and tools to support consistent functionality across different programming languages and applications.

To see all the all settings that the SDK can resolve from the environment variables or configuration files, see the [Settings reference](https://docs.aws.amazon.com/sdkref/latest/guide/settings-reference.html) in the *AWS SDKs and Tools Reference Guide*.

## Configuration provider chain for client configuration
<a name="configuration-provider-chain"></a>

The SDK checks several places (or sources) to find configuration values.

1. Any explicit setting set in the code or on a service client itself takes precedence over anything else.

1. Environment variables
   + For details on setting environment variables, see [environment variables](https://docs.aws.amazon.com/sdkref/latest/guide/environment-variables.html) in the *AWS SDKs and Tools Reference Guide*.
   + Note that you can configure environment variables for a shell at different levels of scope: system-wide, user-wide, and for a specific terminal session.

1. Shared `config` and `credentials` files
   + For details on setting up these files, see the [Shared `config` and `credentials` files](https://docs.aws.amazon.com/sdkref/latest/guide/file-format.html) in the *AWS SDKs and Tools Reference Guide*.

1. Any default value provided by the SDK source code itself is used last.
   + Some properties, such as Region, don't have a default. You must specify them either explicitly in code, in an environment setting, or in the shared `config` file. If the SDK can't resolve required configuration, API requests can fail at runtime.

Besides this general configuration chain, the AWS SDK for PHP Version 3 also uses specialized provider chains including the [credentials provider chain](guide_credentials_default_chain.md) and the [AWS Region resolution chain](aws-php-sdk-region-resolution.md#region-resolution-chain). These specialized chains add additional providers that take into account the environment that the SDK is running in. For example, in a container or an EC2 instance.

## Create a service client configured using external settings
<a name="create-client-ext-conf"></a>

You need to create a service client in your application to talk to an AWS service. Service clients are your essential connection to AWS services, handling all the complex communication details so you don't have to worry about them. They take care of important tasks like security, error handling, and retries automatically, letting you focus on building your application rather than dealing with technical complications.

### Construct a service client using a constructor with no parameters
<a name="create-client-ext-builder"></a>

If all configuration settings that you need are coming from external sources, you can create a service client by using an empty constructor:

```
require 'vendor/autoload.php';

use Aws\S3\S3Client;

$s3 = new S3Client([]);
```

The previous code snippet creates an `S3Client` instance. During creation, the SDK looks through the configuration provider chain for settings. Once the SDK finds a setting value, it uses the value.

The default AWS Region provider chain and the default credentials provider chain will also be used in the creation process. Somewhere in the chain, the SDK must resolve the AWS Region to use and find settings that enable it to retrieve credentials for signing requests. If the SDK fails to find those values, the client creation fails.

## AWS SDK for PHP Version 3 environment variables
<a name="java-ext-config"></a>

Beyond the [cross-sdk settings](https://docs.aws.amazon.com/sdkref/latest/guide/settings-reference.html#settingsPages) supported by most AWS SDKs, the AWS SDK for PHP Version 3 works with the following environment variables:

**AWS\_SDK\_LOAD\_NONDEFAULT\_CONFIG**
When set, this environment variable instructs the SDK to load credentials from the AWS `config` file (`~/.aws/config`) in addition to the `credentials` file (`~/.aws/credential`s).

**AWS\_SDK\_UA\_APP\_ID**
Sets a custom application identifier that gets included in the User-Agent header for requests made by the SDK.

**AWS\_SUPPRESS\_PHP\_DEPRECATION\_WARNING**
 When set to true, suppresses PHP deprecation warnings that the SDK might generate.

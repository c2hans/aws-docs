---
source_url: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/configuring-service-clients-code.html
---

# Configuring service clients in code for the AWS SDK for PHP Version 3
<a name="configuring-service-clients-code"></a>

As an alternative to—or in addition to—[configuring service clients externally](configuring-service-clients-ext.md), you can configure them programmatically in code.

By configuring service clients in code, you gain fine-grained control of the many options available to you. Most of the configuration that you can set externally are also available for you to set in code.

## Basic configuration in code
<a name="conf-service-client-code-basic"></a>

You can create and configure a service client in code by passing an associative array of options to a client’s constructor. In the following example, the associative array contains only the "region" option that the client uses:

```
require 'vendor/autoload.php';

use Aws\S3\S3Client;
use Aws\Exception\AwsException;

//Create an S3Client
$s3 = new S3Client([
    'region' => 'eu-south-2'
]);
```

Information about the optional "version" parameter is available in the [configuration options](guide_configuration.md#cfg-version) topic.

Notice that we did **not** explicitly provide credentials to the client. That’s because the SDK uses the [default credential provider chain](guide_credentials_default_chain.md) to look for credential information.

All of the general client configuration options are described in detail in [Client constructor options for the AWS SDK for PHP Version 3](guide_configuration.md). The array of options provided to a client can vary based on which client you’re creating. These custom client configuration options are described in the [API documentation](https://docs.aws.amazon.com/aws-sdk-php/latest/) for each client.

## Using the `Sdk` Class
<a name="sdk-class"></a>

The `Aws\Sdk` class acts as a client factory and is used to manage shared configuration options across multiple clients. Many of the options that can be provided to a specific client constructor can also be supplied to the `Aws\Sdk` class. These options are then applied to each client constructor.

 **Imports**

```
require 'vendor/autoload.php';

use Aws\S3\S3Client;
use Aws\Exception\AwsException;
```

 **Sample Code**

```
// The same options that can be provided to a specific client constructor can also be supplied to the Aws\Sdk class.
// Use the us-west-2 region and latest version of each client.
$sharedConfig = [
    'region' => 'us-west-2'
];
// Create an SDK class used to share configuration across clients.
$sdk = new Aws\Sdk($sharedConfig);
// Create an Amazon S3 client using the shared configuration data.
$client = $sdk->createS3();
```

Options that are shared across all clients are placed in root-level key-value pairs. Service-specific configuration data can be provided in an associative array with a key that is the same as the namespace of a service (e.g., “S3”, “DynamoDb”, etc.).

```
$sdk = new Aws\Sdk([
    'region'   => 'us-west-2',
    'DynamoDb' => [
        'region' => 'eu-central-1'
    ]
]);

// Creating an Amazon DynamoDb client will use the "eu-central-1" AWS Region.
$client = $sdk->createDynamoDb();
```

Service-specific configuration values are a union of the service-specific values and the root-level values (i.e., service-specific values are shallow-merged onto root-level values).

**Note**
We highly recommended that you use the `Sdk` class to create clients if you’re using multiple client instances in your application. The `Sdk` class automatically uses the same HTTP client for each SDK client, allowing SDK clients for different services to perform nonblocking HTTP requests. If the SDK clients don’t use the same HTTP client, then HTTP requests sent by the SDK client might block promise orchestration between services.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for PHP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-php` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

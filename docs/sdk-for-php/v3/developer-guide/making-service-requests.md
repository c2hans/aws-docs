---
source_url: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/making-service-requests.html
---

# Making AWS service requests using the AWS SDK for PHP Version 3
<a name="making-service-requests"></a>

## SDK request workflow overview
<a name="usage-summary"></a>

Working with the AWS SDK for PHP Version 3 follows a consistent pattern across all AWS services. The basic workflow involves three main steps:

1. [**Create a service client**](#creating-a-client)—Instantiate a **Client** object for the AWS service you want to use.

1. [**Execute operations**](#executing-service-operations)—Call methods on the client that correspond to operations in the service's API.

1. [**Process results**](#result-objects)—Work with the array-like **Result** object returned on success, or handle any **Exception** thrown on failure.

The following sections explain each of these steps in detail, starting with how to create and configure service clients.

## Creating a basic service client
<a name="creating-a-client"></a>

You can create a client by passing an associative array of options to a client’s constructor.

 **Imports**

```
require 'vendor/autoload.php';

use Aws\S3\S3Client;
use Aws\Exception\AwsException;
```

 **Sample Code**

```
//Create an S3Client
$s3 = new Aws\S3\S3Client([
    'region' => 'us-east-2'  // Since version 3.277.10 of the SDK,
]);                          // the 'version' parameter defaults to 'latest'.
```

Information about the optional "version" parameter is available in the [configuration options](guide_configuration.md#cfg-version) topic.

Notice that we did **not** explicitly provide credentials to the client. That’s because the SDK uses the [default credential provider chain](guide_credentials_default_chain.md) to look for credential information.

All of the general client configuration options are described in detail in [Client constructor options for the AWS SDK for PHP Version 3](guide_configuration.md). The array of options provided to a client can vary based on which client you’re creating. These custom client configuration options are described in the [API documentation](https://docs.aws.amazon.com/aws-sdk-php/latest/) for each client.

While the example above shows basic client creation, you can customize your service clients to meet specific requirements. For more detailed information about configuring service clients through code, see [Configuring service clients in code for the AWS SDK for PHP Version 3](configuring-service-clients-code.md). If you need to configure service clients using external configuration files or environment variables, refer to [Configuring service clients for the AWS SDK for PHP Version 3 externally](configuring-service-clients-ext.md).

## Making requests
<a name="executing-service-operations"></a>

You can make service requests by calling the method of the same name on a client object. For example, to perform the Amazon S3 [PutObject operation](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTObjectPUT.html), you call the `Aws\S3\S3Client::putObject()` method.

 **Imports**

```
require 'vendor/autoload.php';

use Aws\S3\S3Client;
```

 **Sample Code**

```
// Use the us-east-2 region and latest version of each client.
$sharedConfig = [
    'profile' => 'default',
    'region' => 'us-east-2'
];

// Create an SDK class used to share configuration across clients.
$sdk = new Aws\Sdk($sharedConfig);

// Use an Aws\Sdk class to create the S3Client object.
$s3Client = $sdk->createS3();

// Send a PutObject request and get the result object.
$result = $s3Client->putObject([
    'Bucket' => 'amzn-s3-demo-bucket',
    'Key' => 'my-key',
    'Body' => 'this is the body!'
]);

// Download the contents of the object.
$result = $s3Client->getObject([
    'Bucket' => 'amzn-s3-demo-bucket',
    'Key' => 'my-key'
]);

// Print the body of the result by indexing into the result object.
echo $result['Body'];
```

Operations available to a client and the structure of the input and output are defined at runtime based on a service description file. When creating a client, if you don't provide a `version` parameter (for example., *“2006-03-01”* or *“latest”*) of the service model, the client defaults to the latest version. The SDK finds the corresponding configuration file based on the provided version.

Operation methods like `putObject()` all accept a single argument, an associative array that represents the parameters of the operation. The structure of this array (and the structure of the result object) is defined for each operation in the SDK’s API Documentation (e.g., see the API docs for [putObject operation](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-s3-2006-03-01.html#putobject)).

### HTTP handler options
<a name="http-handler-options"></a>

You can also fine-tune how the underlying HTTP handler executes the request by using the special `@http` parameter. The options you can include in the `@http` parameter are the same as the ones you can set when you instantiate the client with the [“http” client option](guide_configuration.md#config-http).

```
// Send the request through a proxy
$result = $s3Client->putObject([
    'Bucket' => 'amzn-s3-demo-bucket',
    'Key'    => 'my-key',
    'Body'   => 'this is the body!',
    '@http'  => [
        'proxy' => 'http://192.168.16.1:10'
    ]
]);
```

## Working with result objects
<a name="result-objects"></a>

Executing a successful operation returns an `Aws\Result` object. Instead of returning the raw XML or JSON data of a service, the SDK coerces the response data into an associative array structure. It normalizes some aspects of the data based on its knowledge of the specific service and the underlying response structure.

You can access data from the `AWS\Result` object like an associative PHP array.

 **Imports**

```
require 'vendor/autoload.php';
use Aws\S3\S3Client;
use Aws\Exception\AwsException;
```

 **Sample Code**

```
// Use the us-east-2 region and latest version of each client.
$sharedConfig = [
    'profile' => 'default',
    'region' => 'us-east-2',
];

// Create an SDK class used to share configuration across clients.
$sdk = new Aws\Sdk($sharedConfig);

// Use an Aws\Sdk class to create the S3Client object.
$s3 = $sdk->createS3();
$result = $s3->listBuckets();
foreach ($result['Buckets'] as $bucket) {
    echo $bucket['Name'] . "\n";
}

// Convert the result object to a PHP array
$array = $result->toArray();
```

The contents of the result object depend on the operation that was executed and the version of a service. The result structure of each API operation is documented in the API docs for each operation.

The SDK is integrated with [JMESPath](http://jmespath.org/), a [DSL](http://en.wikipedia.org/wiki/Domain-specific_language) used to search and manipulate JSON data or, in our case, PHP arrays. The result object contains a `search()` method you can use to more declaratively extract data from the result.

 **Sample Code**

```
$s3 = $sdk->createS3();
$result = $s3->listBuckets();
```

```
$names = $result->search('Buckets[].Name');
```

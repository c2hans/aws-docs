---
source_url: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/s3-examples-configuring-a-bucket.html
---

# Configuring Amazon S3 buckets with the AWS SDK for PHP Version 3
<a name="s3-examples-configuring-a-bucket"></a>

Cross-origin resource sharing (CORS) defines a way for client web applications that are loaded in one domain to interact with resources in a different domain. With CORS support in Amazon S3, you can build rich client-side web applications with Amazon S3 and selectively allow cross-origin access to your Amazon S3 resources.

For more information about using CORS configuration with an Amazon S3 bucket, see [Cross-Origin Resource Sharing (CORS)](https://docs.aws.amazon.com/AmazonS3/latest/dev/cors.html).

The following examples show how to:
+ Get the CORS configuration for a bucket using [GetBucketCors](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-s3-2006-03-01.html#getbucketcors).
+ Set the CORS configuration for a bucket using [PutBucketCors](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-s3-2006-03-01.html#putbucketcors).

All the example code for the AWS SDK for PHP is available [here on GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/php/example_code).

## Credentials
<a name="examplecredentials"></a>

Before running the example code, configure your AWS credentials, as described in [Authenticating with AWS using AWS SDK for PHP Version 3](credentials.md). Then import the AWS SDK for PHP, as described in [Installing the AWS SDK for PHP Version 3](getting-started_installation.md).

## Get the CORS configuration
<a name="get-the-cors-configuration"></a>

Create a PHP file with the following code. First create an AWS.S3 client service, then call the `getBucketCors` method and specify the bucket whose CORS configuration you want.

The only parameter required is the name of the selected bucket. If the bucket currently has a CORS configuration, that configuration is returned by Amazon S3 as a [CORSRules object](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-s3-2006-03-01.html#shape-corsrule).

 **Imports**

```
require 'vendor/autoload.php';

use Aws\Exception\AwsException;
use Aws\S3\S3Client;
```

 **Sample Code**

```
$client = new S3Client([
    'profile' => 'default',
    'region' => 'us-west-2',
    'version' => '2006-03-01'
]);

try {
    $result = $client->getBucketCors([
        'Bucket' => $bucketName, // REQUIRED
    ]);
    var_dump($result);
} catch (AwsException $e) {
    // output error message if fails
    error_log($e->getMessage());
}
```

## Set the CORS configuration
<a name="set-the-cors-configuration"></a>

Create a PHP file with the following code. First create an AWS.S3 client service. Then call the `putBucketCors` method and specify the bucket whose CORS configuration to set, and the CORSConfiguration as a [CORSRules JSON object](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-s3-2006-03-01.html#shape-corsrule).

 **Imports**

```
require 'vendor/autoload.php';

use Aws\Exception\AwsException;
use Aws\S3\S3Client;
```

 **Sample Code**

```
$client = new S3Client([
    'profile' => 'default',
    'region' => 'us-west-2',
    'version' => '2006-03-01'
]);

try {
    $result = $client->putBucketCors([
        'Bucket' => $bucketName, // REQUIRED
        'CORSConfiguration' => [ // REQUIRED
            'CORSRules' => [ // REQUIRED
                [
                    'AllowedHeaders' => ['Authorization'],
                    'AllowedMethods' => ['POST', 'GET', 'PUT'], // REQUIRED
                    'AllowedOrigins' => ['*'], // REQUIRED
                    'ExposeHeaders' => [],
                    'MaxAgeSeconds' => 3000
                ],
            ],
        ]
    ]);
    var_dump($result);
} catch (AwsException $e) {
    // output error message if fails
    error_log($e->getMessage());
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for PHP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-php` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

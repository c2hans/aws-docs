---
source_url: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/s3-examples-bucket-policies.html
---

# Working with Amazon S3 bucket policies with the AWS SDK for PHP Version 3
<a name="s3-examples-bucket-policies"></a>

You can use a bucket policy to grant permission to your Amazon S3 resources. To learn more, see [Using Bucket Policies and User Policies](https://docs.aws.amazon.com/AmazonS3/latest/dev/using-iam-policies.html).

The following example shows how to:
+ Return the policy for a specified bucket using [GetBucketPolicy](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-s3-2006-03-01.html#getbucketpolicy).
+ Replace a policy on a bucket using [PutBucketPolicy](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-s3-2006-03-01.html#putbucketpolicy).
+ Delete a policy from a bucket using [DeleteBucketPolicy](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-s3-2006-03-01.html#deletebucketpolicy).

All the example code for the AWS SDK for PHP is available [here on GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/php/example_code).

## Credentials
<a name="examplecredentials"></a>

Before running the example code, configure your AWS credentials, as described in [Authenticating with AWS using AWS SDK for PHP Version 3](credentials.md). Then import the AWS SDK for PHP, as described in [Installing the AWS SDK for PHP Version 3](getting-started_installation.md).

## Get, delete, and replace a policy on a bucket
<a name="get-delete-and-replace-a-policy-on-a-bucket"></a>

 **Imports**

```
require "vendor/autoload.php";

use Aws\Exception\AwsException;
use Aws\S3\S3Client;
```

 **Sample Code**

```
$s3Client = new S3Client([
    'profile' => 'default',
    'region' => 'us-west-2',
    'version' => '2006-03-01'
]);

$bucket = 'amzn-s3-demo-bucket';

// Get the policy of a specific bucket
try {
    $resp = $s3Client->getBucketPolicy([
        'Bucket' => $bucket
    ]);
    echo "Succeed in receiving bucket policy:\n";
    echo $resp->get('Policy');
    echo "\n";
} catch (AwsException $e) {
    // Display error message
    echo $e->getMessage();
    echo "\n";
}

// Deletes the policy from the bucket
try {
    $resp = $s3Client->deleteBucketPolicy([
        'Bucket' => $bucket
    ]);
    echo "Succeed in deleting policy of bucket: " . $bucket . "\n";
} catch (AwsException $e) {
    // Display error message
    echo $e->getMessage();
    echo "\n";
}

// Replaces a policy on the bucket
try {
    $resp = $s3Client->putBucketPolicy([
        'Bucket' => $bucket,
        'Policy' => 'foo policy',
    ]);
    echo "Succeed in put a policy on bucket: " . $bucket . "\n";
} catch (AwsException $e) {
    // Display error message
    echo $e->getMessage();
    echo "\n";
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for PHP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-php` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
